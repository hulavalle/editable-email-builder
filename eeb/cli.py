"""eeb: build email templates that stay editable inside the email platform.

Usage: python3 -m eeb <command> [args]

  templates                       list the library templates, starting points for a new email
  new <name> --from <template>    copy a library template to templates/<name> to start a new email
  init                            copy the library brand.toml here, to map your design system onto it
  build <template> [--esp NAME]   compose templates/<template> (yours first, then the library's),
                                  lint it, translate it for the platform. An example template
                                  gets no zip: it is for preview only
                                  (default: mailchimp), lint the result and write
                                  dist/<esp>/<template>/index.html and dist/<esp>/<template>.zip.
                                  No zip is written when a rule fails
  rules [--esp NAME]              list the rules and why each one exists
  preview <template> [--esp NAME] build, then screenshot the HTML at 700 and 375 px (needs Playwright)
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
from .compose import LIBRARY, BuildError, compose, fields, find, read

ROOT = os.environ.get("EEB_ROOT") or os.getcwd()


def build(template, esp, root=None, out=None):
    """Returns (folder, zip path or None, [(layer, rule, line, message)])."""
    root = root or ROOT
    adapter = adapters.get(esp)
    template_dir = template_path(root, template)
    neutral, images, manifest = compose(root, template_dir)
    example = manifest.get("example") is True
    findings = [("core", *f) for f in lint.check(neutral, root, example=example)]
    samples = sorted(n for n, src in images.items() if os.path.dirname(src) == os.path.join(LIBRARY, "img"))
    if samples and not example:
        findings.append(("core", "C10", 0, f"library sample images still in use: {', '.join(samples)}"))

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
    if findings or example:
        os.remove(zip_path)
        zip_path = None
    return folder, zip_path, findings


def template_path(root, name):
    for base in (os.path.join(root, "templates"), os.path.join(LIBRARY, "templates")):
        if os.path.isfile(os.path.join(base, name, "template.toml")):
            return os.path.join(base, name)
    raise BuildError(f"there is no template `{name}` in templates/ or in the library: python3 -m eeb templates", 2)


def describe(path):
    """The first comment paragraph of a file, in one line."""
    lines = []
    for line in read(path).splitlines():
        if not line.startswith("#"):
            break
        lines.append(line.lstrip("# ").strip())
    return " ".join(lines).split("  ")[0]


def templates():
    folder = os.path.join(LIBRARY, "templates")
    out = []
    for name in sorted(os.listdir(folder)):
        toml = os.path.join(folder, name, "template.toml")
        if os.path.isfile(toml):
            first = re.split(r"(?<=\.)\s", describe(toml), 1)[0]
            out.append(f"{name:<22} {first}")
    return "\n".join(out)


def new(name, source, root=None):
    root = root or ROOT
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        raise BuildError("the name uses lowercase letters, digits and hyphens", 2)
    src = os.path.join(LIBRARY, "templates", source)
    dest = os.path.join(root, "templates", name)
    if not os.path.isfile(os.path.join(src, "template.toml")):
        raise BuildError(f"there is no library template `{source}`: python3 -m eeb templates", 2)
    if os.path.exists(dest):
        raise BuildError(f"templates/{name} already exists", 4)
    shutil.copytree(src, dest)
    toml = os.path.join(dest, "template.toml")
    text = re.sub(r"(?m)^example = true\n", "", read(toml))
    with open(toml, "w", encoding="utf-8") as f:
        f.write(text)
    return dest


def init(root=None):
    root = root or ROOT
    dest = os.path.join(root, "brand.toml")
    if os.path.exists(dest):
        raise BuildError("brand.toml already exists here", 4)
    shutil.copyfile(os.path.join(LIBRARY, "brand.toml"), dest)
    return dest


def report(findings, esp):
    rules = {**lint.RULES, **adapters.get(esp).RULES}
    for layer, rule, line, message in sorted(findings, key=lambda f: (f[1], f[2])):
        where = f"line {line}" if line else "document"
        html = "neutral HTML" if layer == "core" else f"{layer} HTML"
        print(f"{rule:<5} {html}, {where}: {message}")
    for rule in sorted({f[1] for f in findings}):
        print(f"      {rule}: {rules[rule]}")


def preview(template, esp):
    """Builds first, so a screenshot never shows an older build."""
    folder, _, findings = build(template, esp)
    if findings:
        report(findings, esp)
        raise BuildError(f"{template} does not build clean: fix it before looking at it", 1)
    page = os.path.join(folder, "index.html")
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
    names = set()
    for folder in (os.path.join(ROOT, "blocks"), os.path.join(LIBRARY, "blocks")):
        if os.path.isdir(folder):
            names |= {f[:-5] for f in os.listdir(folder) if f.endswith(".html")}
    lines = []
    for name in sorted(names):
        path = find(ROOT, "blocks", name + ".html")
        text = read(path)
        purpose = re.match(r"\s*<!--(.*?)-->", text, re.S)
        required, optional, lists = fields(text)
        lines.append(name + ("" if path.startswith(LIBRARY) else "  (this project)"))
        if purpose:
            lines.append("  " + " ".join(purpose.group(1).split()))
        lines.append("  fields: " + ", ".join(required + [f"[[{k}]] with {', '.join(v)}" for k, v in lists.items()]))
        if optional:
            lines.append("  optional: " + ", ".join(f"{k} = {d}" if d else k for k, d in sorted(optional.items())))
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
        if command == "templates":
            print(templates())
            return 0
        if command == "init":
            print(f"created {os.path.relpath(init())}: map your colors and fonts onto its roles")
            return 0
        if command == "new":
            source = _option(args, "--from", None)
            if len(args) != 1 or not source:
                raise BuildError("usage: new <name> --from <library template>", 2)
            dest = new(args[0], source)
            print(f"created {os.path.relpath(dest)}. Replace its texts, links and library: images, then build it")
            return 0
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
            if zip_path is None:
                print(f"built {os.path.relpath(folder)}/index.html, no zip: an example template is for preview only. "
                      f"Start a real email with: python3 -m eeb new <name> --from {args[0]}")
            else:
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
