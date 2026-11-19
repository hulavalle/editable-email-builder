"""eeb: build email templates that stay editable inside the email platform.

Usage: python3 -m eeb <command> [args]

  build <template> [--esp NAME]   compose templates/<template>, lint it, translate it for the platform
                                  (default: mailchimp), lint the result and write
                                  dist/<esp>/<template>/index.html and dist/<esp>/<template>.zip.
                                  No zip is written when a rule fails
  rules [--esp NAME]              list the rules and why each one exists
  preview <template> [--esp NAME] screenshots of the built HTML at 700 and 375 px (needs Playwright)
  image <src> <dest> --width N [--height N] [--focus X,Y] [--darken TOP,BOTTOM,UNTIL] [--background #hex]
                                  crop, scale, darken the top and compress an image for an email.
                                  Export at twice the display width. An .svg is rasterized with
                                  Playwright. Needs Pillow
  blocks                          list every block: what it is for, its fields and its editable names
  esps                            list the email platforms with an adapter

Exit codes: 0 done, 1 a rule or a precondition failed, 2 usage error, 5 a tool is missing.
"""

import io
import os
import re
import shutil
import sys

from . import adapters, lint
from .compose import BuildError, compose, read

ROOT = os.environ.get("EEB_ROOT") or os.getcwd()


def build(template, esp, root=None, out=None):
    """Returns (folder, zip path or None, [(layer, rule, line, message)])."""
    root = root or ROOT
    adapter = adapters.get(esp)
    template_dir = os.path.join(root, "templates", template)
    if not os.path.isfile(os.path.join(template_dir, "template.toml")):
        raise BuildError(f"there is no templates/{template}/template.toml", 2)
    neutral, images, manifest = compose(root, template_dir)
    findings = [("core", *f) for f in lint.check(neutral, root, example=manifest.get("example") is True)]

    out = out or os.path.join(root, "dist", esp)
    folder = os.path.join(out, template)
    shutil.rmtree(folder, ignore_errors=True)
    os.makedirs(folder)
    final = adapter.translate(neutral)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(final)
    for name, src in images.items():
        shutil.copyfile(src, os.path.join(folder, name))
    zip_path = os.path.join(out, f"{template}.zip")
    adapter.package(folder, images, zip_path)
    findings += [(esp, *f) for f in adapter.check(final, folder, zip_path)]
    if findings:
        os.remove(zip_path)
        zip_path = None
    return folder, zip_path, findings


def report(findings, esp):
    rules = {**lint.RULES, **adapters.get(esp).RULES}
    for layer, rule, line, message in sorted(findings, key=lambda f: (f[1], f[2])):
        where = f"line {line}" if line else "document"
        html = "neutral HTML" if layer == "core" else f"{layer} HTML"
        print(f"{rule:<5} {html}, {where}: {message}")
    for rule in sorted({f[1] for f in findings}):
        print(f"      {rule}: {rules[rule]}")


def preview(template, esp):
    folder = os.path.join(ROOT, "dist", esp, template)
    page = os.path.join(folder, "index.html")
    if not os.path.isfile(page):
        raise BuildError(f"not built yet: python3 -m eeb build {template} --esp {esp}")
    shots = []
    with _playwright()() as p:
        browser = p.chromium.launch()
        try:
            for width in (700, 375):
                tab = browser.new_page(viewport={"width": width, "height": 800})
                tab.goto("file://" + page)
                tab.wait_for_load_state("networkidle")
                path = os.path.join(folder, f"preview-{width}.png")
                tab.screenshot(path=path, full_page=True)
                shots.append(path)
        finally:
            browser.close()
    return shots


def image(args):
    try:
        from PIL import Image
    except ImportError:
        raise BuildError("Pillow is missing: pip install pillow", 5)
    if len(args) < 2:
        raise BuildError("usage: image <src> <dest> --width N [--height N] [--focus X,Y] "
                         "[--darken TOP,BOTTOM,UNTIL] [--background #hex]", 2)
    src, dest, rest = args[0], args[1], args[2:]
    opts = dict(zip(rest[::2], rest[1::2]))
    if "--width" not in opts:
        raise BuildError("missing --width: the width in pixels, twice what the image takes in the email", 2)
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*\.(jpg|jpeg|png|gif)$", os.path.basename(dest)):
        raise BuildError(f"{os.path.basename(dest)}: use lowercase letters, digits and hyphens, and .jpg, .png or .gif", 2)
    width = int(opts["--width"])
    if src.lower().endswith(".svg"):
        with _playwright()() as p:
            browser = p.chromium.launch()
            try:
                tab = browser.new_page(viewport={"width": width, "height": 10})
                svg = read(src)
                tab.set_content(f'<html><body style="margin:0;background:transparent"><div id="s" style="width:{width}px">{svg}</div></body></html>')
                tab.eval_on_selector("#s svg", f"e => {{ e.style.width='{width}px'; e.style.height='auto'; }}")
                data = tab.locator("#s svg").screenshot(omit_background=True)
            finally:
                browser.close()
        picture = Image.open(io.BytesIO(data)).convert("RGBA")
    else:
        picture = Image.open(src).convert("RGBA")
    if "--height" in opts:
        height = int(opts["--height"])
        fx, fy = (float(x) for x in opts.get("--focus", "0.5,0.5").split(","))
        scale = max(width / picture.width, height / picture.height)
        picture = picture.resize((round(picture.width * scale), round(picture.height * scale)), Image.LANCZOS)
        x = min(max(round(picture.width * fx - width / 2), 0), picture.width - width)
        y = min(max(round(picture.height * fy - height / 2), 0), picture.height - height)
        picture = picture.crop((x, y, x + width, y + height))
    elif picture.width != width:
        picture = picture.resize((width, round(picture.height * width / picture.width)), Image.LANCZOS)
    if "--darken" in opts:
        top, bottom, until = (float(x) for x in opts["--darken"].split(","))
        layer = Image.new("RGBA", picture.size)
        stop = max(1, round(picture.height * until))
        for y in range(picture.height):
            t = min(y / stop, 1)
            layer.paste((0, 0, 0, round(255 * (top + (bottom - top) * t))), (0, y, picture.width, y + 1))
        picture = Image.alpha_composite(picture, layer)
    if dest.lower().endswith((".jpg", ".jpeg")) or "--background" in opts:
        color = opts.get("--background", "#ffffff").lstrip("#")
        canvas = Image.new("RGBA", picture.size, tuple(int(color[i:i + 2], 16) for i in (0, 2, 4)) + (255,))
        picture = Image.alpha_composite(canvas, picture)
    if dest.lower().endswith((".jpg", ".jpeg")):
        picture = picture.convert("RGB")
        for quality in (82, 76, 70, 64, 58, 52):
            picture.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)
            if os.path.getsize(dest) <= 180_000:
                break
    else:
        picture.save(dest, optimize=True)
    print(f"{dest}: {picture.width}x{picture.height}, {os.path.getsize(dest) // 1000} KB")


def blocks():
    """Every block, read from blocks/: purpose, fields, list fields and editable names."""
    folder = os.path.join(ROOT, "blocks")
    lines = []
    for name in sorted(f[:-5] for f in os.listdir(folder) if f.endswith(".html")):
        text = read(os.path.join(folder, name + ".html"))
        purpose = re.match(r"\s*<!--(.*?)-->", text, re.S)
        lists = {m.group(1): sorted(set(re.findall(r"\{\{(\w+)\}\}", m.group(2))) - {"n"})
                 for m in re.finditer(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", text, re.S)}
        outside = re.sub(r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}", "", text, flags=re.S)
        fields = sorted(set(re.findall(r"\{\{(\w+)\}\}", outside)))
        lines.append(name)
        if purpose:
            lines.append("  " + " ".join(purpose.group(1).split()))
        lines.append("  fields: " + ", ".join(fields + [f"[[{k}]] with {', '.join(v)}" for k, v in lists.items()]))
        lines.append("  editable: " + ", ".join(re.findall(r'data-edit="([^"]+)"', text)))
        marks = re.findall(r'data-repeat="([^"]+)"', text)
        if marks:
            lines.append("  repeatable: " + ", ".join(marks))
        if re.search(r"\sdata-hide[\s>]", text):
            lines.append("  hideable")
        lines.append("")
    return "\n".join(lines).rstrip()


def _playwright():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        raise BuildError("Playwright is missing: pip install playwright && playwright install chromium", 5)


def _option(args, name, default):
    if name in args:
        i = args.index(name)
        if i + 1 >= len(args):
            raise BuildError(f"{name} needs a value", 2)
        value = args[i + 1]
        del args[i:i + 2]
        return value
    return default


def main(argv):
    if not argv or argv[0] in ("help", "-h", "--help"):
        print(__doc__.strip())
        return 0 if argv else 2
    command, args = argv[0], list(argv[1:])
    try:
        esp = _option(args, "--esp", "mailchimp")
        if command == "blocks":
            print(blocks())
            return 0
        if command == "esps":
            print("\n".join(sorted(adapters.ADAPTERS)))
            return 0
        if command == "rules":
            for rule, text in {**lint.RULES, **adapters.get(esp).RULES}.items():
                print(f"{rule:<5} {text}")
            return 0
        if command == "image":
            image(args)
            return 0
        if len(args) != 1:
            raise BuildError(f"usage: {command} <template>", 2)
        if command == "build":
            folder, zip_path, findings = build(args[0], esp)
            if findings:
                report(findings, esp)
                print(f"no zip: {len(findings)} findings. A zip with these would import broken.", file=sys.stderr)
                return 1
            print(f"built {os.path.relpath(folder)}/index.html and {os.path.relpath(zip_path)}")
            return 0
        if command == "preview":
            for shot in preview(args[0], esp):
                print(os.path.relpath(shot))
            return 0
        raise BuildError(f"unknown command: {command}", 2)
    except BuildError as e:
        print(f"eeb: {e}", file=sys.stderr)
        return e.code


def run():
    """Entry point for the `eeb` command installed by pip."""
    sys.exit(main(sys.argv[1:]))
