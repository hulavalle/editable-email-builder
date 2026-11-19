"""Rules that hold for every email platform. They run on the neutral HTML, before an adapter
translates it. Each rule says why it exists: the message is the documentation."""

import os
import re

from .html import Document, editable_properties

EDITABLE = r"/\*\s*@editable\s*\*/"
HTML_MAX = 90_000     # Gmail clips a message over 102 KB, and the ESP adds tracking on top
STYLE_MAX = 16_000    # Gmail drops a <style> block over 16 KB
ESP_TOKEN = re.compile(r"\{\{esp\.\w+\}\}")

RULES = {
    "E1": "Every visible text sits inside a data-edit region. Text outside one cannot be changed in the "
          "email platform, which is exactly what makes a template generic instead of editable.",
    "E2": "Inside a data-edit region there is no style attribute and no <font>: the look comes from classes "
          "in the <head>. Otherwise retyping a text in the editor loses its style, and the platform's style "
          "panel cannot change it.",
    "E3": "Each data-edit name is unique, uses lowercase letters, digits and underscores, and has a "
          "data-label. Platforms store content by that name: a repeated name mixes content, a renamed one "
          "loses it, and the label is what the person editing the campaign sees.",
    "E4": "A data-edit region is never inside another one, and an editable image is never inside an "
          "editable text region. Editors cannot open nested regions.",
    "E5": "Every CSS rule with /* @editable */ properties is preceded by a /* @group Tab / Section */ "
          "comment, which names it in the platform's style panel.",
    "E6": "A property that is editable in the <head> is not also set inline (style or bgcolor) on an element "
          "with that class. Inline wins, and the change made in the style panel would not show.",
    "L1": "The email has an unsubscribe link ({{esp.unsubscribe_url}}) and the sender's postal address "
          "({{esp.address}}). Anti-spam law and every platform require both.",
    "L2": "The email has a preview text slot ({{esp.preview}}), so each campaign sets its own preview text "
          "instead of the inbox showing the first words of the body.",
    "D1": "The document declares <!doctype html>, charset utf-8 and a lang attribute.",
    "C1": "No script, form, input, button, iframe, svg, video, audio, object or embed: email clients strip "
          "them or flag the message.",
    "C2": "No position, float, flex or grid. Outlook on Windows ignores them and the layout breaks.",
    "C3": "A background image only goes in a <head> rule with /* @editable */ and a background-color "
          "fallback. Never in a background= attribute or inline: it could not be changed in the platform, "
          "and Outlook on Windows shows only the color.",
    "C4": "Every link goes to https, mailto:, tel: or an {{esp.*}} merge tag, opens in a new tab, and never "
          "points to #, nothing or a reserved placeholder domain (example.com, .org, .net, .invalid, .test). "
          "Only a template marked `example = true` may keep placeholder domains.",
    "C5": f"The HTML weighs under {HTML_MAX // 1000} KB, so Gmail does not clip it, and the <style> under "
          f"{STYLE_MAX // 1000} KB, so Gmail does not drop it.",
    "C6": "Every table has role=\"presentation\" and cellpadding, cellspacing and border set to 0.",
    "C7": "Every image has an alt attribute (empty when decorative) and a width attribute.",
    "C8": "No {{...}} placeholder is left unfilled, apart from {{esp.*}} merge tags written without spaces. "
          "A token with spaces inside the braces, such as {{ esp.first_name }}, is not filled and would ship as text.",
    "C9": "A table with border-radius, or holding a rounded cell, has border-collapse:separate inline. The "
          "border-collapse:collapse of the reset removes rounded corners.",
    "C10": "Only a template marked `example = true` uses the library's sample images (`library:`). A client "
           "email replaces them with its own photos and logo, or it would ship another company's.",
    "A1": "Text reaches WCAG AA contrast on its background: 4.5:1, or 3:1 for large text (24 px, or 19 px bold). "
          "The background is the nearest one set by a class, an inline style or bgcolor.",
    "B1": "Every color comes from brand.toml.",
    "B2": "Every font-family is a stack from brand.toml, and fonts only load from Google Fonts.",
}


PLACEHOLDER = re.compile(r"^https://([\w-]+\.)*(example\.(com|org|net)|[\w-]+\.(invalid|test))(/|$)")


def check(source, root, example=False):
    """Returns [(rule, line, message)] for the neutral HTML of one template."""
    brand = _brand(root)
    colors = {c.lower() for c in brand["colors"].values()}
    stacks = {re.sub(r"\s+", " ", f.strip()) for k, f in brand["fonts"].items() if k != "google"}
    doc = Document(source)
    found = []

    def bad(rule, line, message):
        found.append((rule, line, message))

    editables = [n for n in doc.nodes if "data-edit" in n.attrs]

    def inside_edit(node):
        return any("data-edit" in a.attrs for a in node.ancestors())

    # E1, E2
    for t in doc.texts():
        clean = re.sub(r"[\s ​‌‍﻿]+", "", t.text)
        chain = [t.parent] + list(t.parent.ancestors())
        if not clean or clean == "{{esp.preview}}" or any(a.tag in ("head", "style", "title") for a in chain):
            continue
        if not any("data-edit" in a.attrs for a in chain):
            bad("E1", t.line, f'text outside a data-edit region: "{t.text.strip()[:40]}"')
    for n in editables:
        for d in n.descendants():
            if "style" in d.attrs or d.tag == "font":
                bad("E2", d.line, f'<{d.tag}> with its own style inside data-edit="{n.attrs["data-edit"]}"')

    # E3, E4
    seen = {}
    for n in editables:
        name = n.attrs["data-edit"] or ""
        if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
            bad("E3", n.line, f'data-edit="{name}" is not a valid name')
        if name in seen:
            bad("E3", n.line, f'data-edit="{name}" is already used on line {seen[name]}')
        seen.setdefault(name, n.line)
        if not n.attrs.get("data-label"):
            bad("E3", n.line, f'data-edit="{name}" has no data-label')
        if inside_edit(n):
            bad("E4", n.line, f'data-edit="{name}" is inside another data-edit region')

    # E5, E6
    for comments, selector, body in doc.rules:
        props = editable_properties(body, EDITABLE)
        if props and not re.search(r"@group\s+[^/*]+/", comments):
            bad("E5", 0, f"`{selector}` has editable properties and no /* @group Tab / Section */ before it")
        m = re.fullmatch(r"\.([\w-]+)(?:\s+([a-z0-9]+))?", selector)
        if not props or not m:
            continue
        cls, tag = m.group(1), m.group(2)
        for n in doc.nodes:
            if cls not in n.classes():
                continue
            targets = [n] if not tag else [d for d in n.descendants() if d.tag == tag]
            for target in targets:
                clash = props & set(target.style())
                if "background-color" in props and "bgcolor" in target.attrs:
                    clash.add("bgcolor")
                if clash:
                    bad("E6", target.line, f"`{selector}` is editable but <{target.tag}> sets {', '.join(sorted(clash))} inline")

    # L1, L2, D1
    for token in ("{{esp.unsubscribe_url}}", "{{esp.address}}"):
        if token not in source:
            bad("L1", 0, f"missing {token}")
    if "{{esp.preview}}" not in source:
        bad("L2", 0, "missing {{esp.preview}}")
    if not doc.doctype:
        bad("D1", 1, "missing <!doctype html>")
    if not any(n.tag == "meta" and (n.attrs.get("charset") or "").lower() == "utf-8" for n in doc.nodes):
        bad("D1", 0, 'missing <meta charset="utf-8">')
    if not any(n.tag == "html" and n.attrs.get("lang") for n in doc.nodes):
        bad("D1", 0, "missing lang on <html>")

    # C1 to C9
    for n in doc.nodes:
        if n.tag in ("script", "form", "input", "button", "iframe", "svg", "video", "audio", "object", "embed"):
            bad("C1", n.line, f"<{n.tag}>")
    declarations = doc.declarations()
    for line, key, value in declarations:
        if key in ("position", "float") or (key == "display" and re.search(r"\b(flex|grid|inline-flex)\b", value)):
            bad("C2", line, f"{key}:{value}")
    for n in doc.nodes:
        if "background" in n.attrs:
            bad("C3", n.line, f'background="{n.attrs["background"]}" on <{n.tag}>')
        for key in n.style():
            if key in ("background-image", "background"):
                bad("C3", n.line, f"inline {key} on <{n.tag}>")
    for _, selector, body in doc.rules:
        if "url(" in body:
            if not re.search(EDITABLE + r"\s*background-image\s*:", body):
                bad("C3", 0, f"`{selector}` has a background image that is not editable")
            if "background-color" not in body:
                bad("C3", 0, f"`{selector}` has a background image and no background-color fallback")
    for n in doc.nodes:
        if n.tag != "a":
            continue
        href = (n.attrs.get("href") or "").strip()
        if not re.match(r"^(https://|mailto:|tel:|\{\{esp\.\w+\}\}$)", href) or (PLACEHOLDER.match(href) and not example):
            bad("C4", n.line, f'href="{href}"')
        if n.attrs.get("target") != "_blank":
            bad("C4", n.line, f'<a href="{href[:40]}"> has no target="_blank"')
    if len(source.encode("utf-8")) > HTML_MAX:
        bad("C5", 0, f"the HTML weighs {len(source.encode('utf-8')) // 1000} KB")
    if len(doc.css.encode("utf-8")) > STYLE_MAX:
        bad("C5", 0, f"the <style> weighs {len(doc.css.encode('utf-8')) // 1000} KB")
    for n in doc.nodes:
        if n.tag == "table":
            missing = [a for a, v in (("role", "presentation"), ("cellpadding", "0"), ("cellspacing", "0"), ("border", "0"))
                       if n.attrs.get(a) != v]
            if missing:
                bad("C6", n.line, f"<table> without {', '.join(missing)}")
        if n.tag == "img":
            if "alt" not in n.attrs:
                bad("C7", n.line, f'<img src="{n.attrs.get("src")}"> has no alt')
            if not n.attrs.get("width"):
                bad("C7", n.line, f'<img src="{n.attrs.get("src")}"> has no width')
    for i, line in enumerate(source.splitlines(), 1):
        for m in re.finditer(r"\{\{\s*[#/]?[\w.]+\s*\}\}", line):
            if not ESP_TOKEN.fullmatch(m.group(0)):
                bad("C8", i, m.group(0))
    rounded = set()
    for _, selector, body in doc.rules:
        m = re.fullmatch(r"\.([\w-]+)", selector)
        if m and re.search(r"border-radius\s*:", body):
            rounded.add(m.group(1))
    for n in doc.nodes:
        if n.tag not in ("table", "td") or ("border-radius" not in n.style() and not rounded & set(n.classes())):
            continue
        table = n if n.tag == "table" else next((a for a in n.ancestors() if a.tag == "table"), None)
        if table is not None and table.style().get("border-collapse") != "separate":
            bad("C9", table.line, f"<table> with rounded corners on <{n.tag}> and no border-collapse:separate")

    # A1
    found += contrast_findings(doc)

    # B1, B2
    plain = re.sub(r"<!--.*?-->", "", source, flags=re.S)
    plain = re.sub(r"/\*.*?\*/", "", plain, flags=re.S)
    for m in re.finditer(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\(", plain):
        if m.group(0).lower() not in colors:
            bad("B1", plain.count("\n", 0, m.start()) + 1, f"{m.group(0).lower()} is not a color in brand.toml")
    for line, key, value in declarations:
        if key == "font-family" and re.sub(r"\s+", " ", value.replace("!important", "").strip()) not in stacks:
            bad("B2", line, f"font-family:{value}")
    if "@font-face" in doc.css or "@import" in doc.css:
        bad("B2", 0, "@font-face or @import in the <style>")
    for n in doc.nodes:
        if n.tag == "link" and not (n.attrs.get("href") or "").startswith("https://fonts.googleapis.com/"):
            bad("B2", n.line, f'<link href="{n.attrs.get("href")}">')
    return found


HEX = re.compile(r"#[0-9a-fA-F]{6}\b")


def _hex(value):
    m = HEX.search(value or "")
    return m.group(0).lower() if m else None


def _luminance(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    x, y = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


def contrast_findings(doc):
    """A1: text colors set by class rules, measured against the nearest background."""
    backgrounds, texts = {}, []
    for _, selectors, body in doc.rules:
        props = dict((k.lower(), v.strip()) for k, v in re.findall(r"([\w-]+)\s*:\s*([^;]+)", re.sub(r"/\*.*?\*/", "", body, flags=re.S)))
        for selector in selectors.split(","):
            m = re.fullmatch(r"\s*\.([\w-]+)(?:\s+([a-z0-9]+))?\s*", selector)
            if not m:
                continue
            cls, tag = m.group(1), m.group(2)
            if not tag and _hex(props.get("background-color")):
                backgrounds[cls] = _hex(props["background-color"])
            if _hex(props.get("color")):
                size = re.match(r"(\d+)", props.get("font-size", "16"))
                bold = props.get("font-weight", "400") in ("700", "bold")
                texts.append((cls, tag, _hex(props["color"]), int(size.group(1)) if size else 16, bold, selector.strip()))
    page = backgrounds.get("page", "#ffffff")

    def background(node):
        for n in [node] + list(node.ancestors()):
            if not hasattr(n, "attrs"):
                continue
            inline = _hex(n.style().get("background-color")) or _hex(n.attrs.get("bgcolor"))
            if inline:
                return inline
            for cls in n.classes():
                if cls in backgrounds:
                    return backgrounds[cls]
        return page

    found, seen = [], set()
    for cls, tag, color, size, bold, selector in texts:
        need = 3.0 if size >= 24 or (size >= 19 and bold) else 4.5
        for n in doc.nodes:
            if cls not in n.classes():
                continue
            for target in ([n] if not tag else [d for d in n.descendants() if d.tag == tag]):
                text = "".join(t.text for t in doc.texts(target)).strip()
                if not text:
                    continue
                bg = background(target)
                ratio = contrast(color, bg)
                key = (selector, bg)
                if ratio < need and key not in seen:
                    seen.add(key)
                    found.append(("A1", target.line, f"`{selector}` {color} on {bg} is {ratio:.1f}:1, needs {need:.1f}:1"))
    return found


def _brand(root):
    from .compose import find, load_toml
    return load_toml(find(root, "brand.toml"))
