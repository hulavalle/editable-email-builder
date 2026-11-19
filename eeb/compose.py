"""Compose a template into one neutral HTML document.

The project root holds brand.toml, base.html and blocks/. A template is a folder with a
template.toml that lists blocks in order, each with its content. The result is still neutral:
editable regions are data-* attributes and ESP merge tags are {{esp.*}} tokens. An adapter
turns that into what one email platform expects.
"""

import os
import re
import tomllib

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".gif")
LOOP = re.compile(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", re.S)
TOKEN = re.compile(r"\{\{([\w.]+)\}\}")


class BuildError(Exception):
    def __init__(self, message, code=1):
        super().__init__(message)
        self.code = code


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_toml(path):
    try:
        with open(path, "rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        raise BuildError(f"{path} does not exist")
    except tomllib.TOMLDecodeError as e:
        raise BuildError(f"{path} is not valid TOML: {e}")


def lookup(context, key):
    value = context
    for part in key.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def render(text, context, used, where):
    """{{#list}}...{{/list}} repeats per item with {{n}} counting from 1. {{key}} inserts a value.
    {{esp.*}} tokens stay as they are: the adapter fills them."""

    def repeat(m):
        name, body = m.group(1), m.group(2)
        items = context.get(name)
        if not isinstance(items, list) or not items:
            raise BuildError(f"{where}: missing list `{name}`")
        used.add(name)
        parts = []
        for i, item in enumerate(items, 1):
            inner = set()
            parts.append(render(body, {**context, **item, "n": str(i)}, inner, f"{where}, {name}[{i}]"))
            used.update(inner - set(item))
            unused = set(item) - inner
            if unused:
                raise BuildError(f"{where}, {name}[{i}]: the block does not use {', '.join(sorted(unused))}")
        return "".join(parts)

    text = LOOP.sub(repeat, text)

    def put(m):
        key = m.group(1)
        if key.startswith("esp."):
            return m.group(0)
        value = lookup(context, key)
        if value is None or isinstance(value, (dict, list)):
            raise BuildError(f"{where}: missing `{key}`")
        used.add(key.split(".")[0])
        return str(value)

    return TOKEN.sub(put, text)


def resolve_images(values, base_dir, copies):
    """A local image path is copied next to the HTML and replaced by its file name."""
    if isinstance(values, list):
        return [resolve_images(v, base_dir, copies) for v in values]
    if isinstance(values, dict):
        return {k: resolve_images(v, base_dir, copies) for k, v in values.items()}
    if isinstance(values, str) and values.lower().endswith(IMAGE_EXT) and not re.match(r"^https?://", values):
        path = os.path.normpath(os.path.join(base_dir, values))
        if not os.path.isfile(path):
            raise BuildError(f"image {path} does not exist")
        name = os.path.basename(path)
        if copies.get(name, path) != path:
            raise BuildError(f"two different images are named {name}: they all end up in one folder")
        copies[name] = path
        return name
    return values


def split_block(text):
    """A block file: an optional leading comment, an optional <style>, then markup."""
    text = re.sub(r"^\s*<!--.*?-->\s*", "", text, count=1, flags=re.S)
    m = re.match(r"\s*<style>(.*?)</style>\s*", text, flags=re.S)
    if not m:
        return "", text
    return m.group(1).strip("\n"), text[m.end():]


def compose(root, template_dir):
    """Returns (neutral html, {image file name: source path}, the template's manifest)."""
    manifest = load_toml(os.path.join(template_dir, "template.toml"))
    brand = load_toml(os.path.join(root, "brand.toml"))
    copies, styles, body, seen = {}, [], [], set()

    for i, block in enumerate(manifest.get("block", []), 1):
        kind = block.get("type")
        where = f"template.toml, block {i} ({kind})"
        path = os.path.join(root, "blocks", f"{kind}.html")
        if not kind or not os.path.isfile(path):
            raise BuildError(f"{where}: there is no blocks/{kind}.html")
        if kind in seen:
            raise BuildError(f"{where}: this block is already in the template. Its editable names would repeat. "
                             "Repetition belongs to the ESP: mark the block repeatable instead")
        seen.add(kind)
        values = resolve_images({k: v for k, v in block.items() if k != "type"}, template_dir, copies)
        css, markup = split_block(read(path))
        used = set()
        context = {**values, "brand": brand}
        if css:
            styles.append(render(css, context, used, where))
        body.append(render(markup, context, used, where).strip("\n"))
        unused = set(values) - used
        if unused:
            raise BuildError(f"{where}: the block does not use {', '.join(sorted(unused))}")

    if not body:
        raise BuildError("template.toml has no [[block]]")
    base = read(os.path.join(root, "base.html"))
    context = {"brand": brand, "lang": manifest.get("lang", ""), "styles": "\n\n".join(styles), "blocks": "\n".join(body)}
    return render(base, context, set(), "base.html"), copies, manifest
