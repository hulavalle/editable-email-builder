"""Compose a template into one neutral HTML document.

The project root holds brand.toml and, optionally, its own base.html and blocks/. Anything the
project does not have comes from the library in eeb/library: a project block with the same name
wins over the library block. A template is a folder with a template.toml that lists blocks in
order, each with its content. The result is still neutral:
editable regions are data-* attributes and ESP merge tags are {{esp.*}} tokens. An adapter
turns that into what one email platform expects.
"""

import os
import re
import tomllib

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".gif")
LIBRARY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library")
NAME = re.compile(r"[a-z][a-z0-9_]*")
LOOP = re.compile(r"\{\{#(\w+)(\??)\}\}(.*?)\{\{/\1\}\}", re.S)
TOKEN = re.compile(r"\{\{([\w.]+)(?:\|([^{}]*))?\}\}")
BAND = re.compile(r'class="[^"]*\bband-([a-z]+)\b')


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
    """{{#list}}...{{/list}} repeats per item with {{n}} counting from 1. {{#key?}}...{{/key}} is
    optional: it repeats over a list, shows once for any other value and disappears when the key
    is missing or empty. {{key}} inserts a value, {{key|default}} falls back to the default.
    {{esp.*}} tokens stay as they are: the adapter fills them."""

    def repeat(m):
        name, optional, body = m.group(1), m.group(2), m.group(3)
        items = context.get(name)
        if optional:
            used.add(name)
            if not items:
                return ""
            if not isinstance(items, list):
                return render(body, context, used, where)
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
        key, default = m.group(1), m.group(2)
        if key.startswith("esp."):
            return m.group(0)
        value = lookup(context, key)
        if value is None and default is not None:
            return default
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
        if values.startswith("library:"):
            path = os.path.join(LIBRARY, "img", values[len("library:"):])
        else:
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


def styled_classes(css):
    """The first class of every top-level selector in a block's CSS, outside media queries."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"@media[^{]*\{(?:[^{}]*\{[^}]*\})*[^}]*\}", "", css)
    classes = set()
    for selectors in re.findall(r"([^{}]+)\{", css):
        for selector in selectors.split(","):
            m = re.match(r"\s*\.([\w-]+)", selector)
            if m:
                classes.add(m.group(1))
    return classes


def band_styles(root, brand, bands):
    """The CSS of each band the blocks use, in order of first use. On a band that brand.toml lists
    under [bands], text takes that color instead of the block's own."""
    css = split_block(read(find(root, "band.html")))[0]
    out = []
    for name in bands:
        text = brand.get("bands", {}).get(name)
        if text is not None and text not in brand["colors"]:
            raise BuildError(f"brand.toml: [bands] {name} = `{text}` is not a color")
        context = {"name": name, "label": name.capitalize(), "color": brand["colors"][name],
                   "text": brand["colors"][text] if text else ""}
        out.append(render(css, context, set(), "band.html").strip("\n"))
    return "\n\n".join(out)


def fields(text):
    """A block's fields: required ones, optional ones with their default, and list fields."""
    optional, lists = {}, {}
    for m in LOOP.finditer(text):
        inner = sorted({t.group(1) for t in TOKEN.finditer(m.group(3))} - {"n"})
        if m.group(2):
            optional.update({k: "" for k in [m.group(1)] + inner})
        else:
            lists[m.group(1)] = inner
    names = set()
    for t in TOKEN.finditer(LOOP.sub("", text)):
        if t.group(2) is not None:
            optional[t.group(1)] = t.group(2)
        elif not t.group(1).startswith(("brand.", "esp.")):
            names.add(t.group(1))
    return sorted(names - set(optional)), optional, lists


def find(root, *parts):
    """The project's file if it has one, otherwise the library's."""
    own = os.path.join(root, *parts)
    return own if os.path.isfile(own) else os.path.join(LIBRARY, *parts)


def suffix_names(markup, uid):
    """A block used more than once gets its instance id on every editable and repeatable name."""
    markup = re.sub(r'(\sdata-(?:edit|repeat))="([^"]+)"', lambda m: f'{m.group(1)}="{m.group(2)}_{uid}"', markup)
    return re.sub(r'(\sdata-label)="([^"]+)"', lambda m: f'{m.group(1)}="{m.group(2)} ({uid})"', markup)


def compose(root, template_dir):
    """Returns (neutral html, {image file name: source path}, the template's manifest)."""
    manifest = load_toml(os.path.join(template_dir, "template.toml"))
    brand = load_toml(find(root, "brand.toml"))
    copies, styles, body, seen, css_by_kind, class_owner, bands = {}, [], [], set(), {}, {}, {}

    for i, block in enumerate(manifest.get("block", []), 1):
        kind, uid = block.get("type"), block.get("id")
        where = f"template.toml, block {i} ({kind})"
        path = find(root, "blocks", f"{kind}.html") if kind else ""
        if not kind or not os.path.isfile(path):
            raise BuildError(f"{where}: there is no block `{kind}` in blocks/ or in the library")
        if uid is not None and not NAME.fullmatch(str(uid)):
            raise BuildError(f"{where}: id `{uid}` must use lowercase letters, digits and underscores")
        if (kind, uid) in seen:
            raise BuildError(f"{where}: this block is already in the template"
                             + (" with this id" if uid else ". Give each use an `id`, so its editable names differ"))
        if uid is None and any(k == kind for k, _ in seen) or uid is not None and (kind, None) in seen:
            raise BuildError(f"{where}: a block used more than once needs an `id` on every use")
        seen.add((kind, uid))
        values = resolve_images({k: v for k, v in block.items() if k not in ("type", "id")}, template_dir, copies)
        css, markup = split_block(read(path))
        used = set()
        context = {**values, "brand": brand}
        if css:
            rendered = render(css, context, used, where)
            if kind not in css_by_kind:
                for cls in styled_classes(rendered):
                    owner = class_owner.setdefault(cls, kind)
                    if owner != kind:
                        raise BuildError(f"{where}: the class `.{cls}` is also styled by the block `{owner}`. Two blocks "
                                         "styling one class override each other and split it across two style-panel "
                                         "sections: rename the class in one of them")
                css_by_kind[kind] = rendered
                styles.append(rendered)
            elif css_by_kind[kind] != rendered:
                raise BuildError(f"{where}: this block puts template values in its CSS, so it can only appear once")
        markup = render(markup, context, used, where).strip("\n")
        for band in BAND.findall(markup):
            if band not in brand["colors"]:
                raise BuildError(f"{where}: band `{band}` is not a color of brand.toml")
            bands.setdefault(band)
        body.append(suffix_names(markup, uid) if uid else markup)
        unused = set(values) - used
        if unused:
            raise BuildError(f"{where}: the block does not use {', '.join(sorted(unused))}")

    if not body:
        raise BuildError("template.toml has no [[block]]")
    base = read(find(root, "base.html"))
    context = {"brand": brand, "lang": manifest.get("lang", ""), "styles": "\n\n".join(styles),
               "bands": band_styles(root, brand, bands), "blocks": "\n".join(body)}
    return render(base, context, set(), "base.html"), copies, manifest
