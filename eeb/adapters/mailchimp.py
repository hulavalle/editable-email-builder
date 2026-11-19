"""Mailchimp, classic email builder, through its template language.

Sources: Mailchimp help on the template language (mc:edit, mc:repeatable, mc:variant,
mc:hideable, mc:label), on editable styles (@tab, @section, @editable) and on importing a
custom HTML template (zip under 1 MB, one HTML file, images at the root). The template
language does not work in Mailchimp's new builder. docs/mailchimp.md has the details that no
rule can check.
"""

import os
import re
import zipfile

from ..html import Document

NAME = "mailchimp"
ZIP_MAX = 1_000_000
IMAGE_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.(jpg|jpeg|png|gif)$")
IMAGE_EXT = (".jpg", ".jpeg", ".png", ".gif")

PREVIEW = (
    "<!--*|IF:MC_PREVIEW_TEXT|*-->\n"
    '<!--[if !gte mso 9]><!----><span class="mcnPreviewText" style="display:none; font-size:0px; '
    "line-height:0px; max-height:0px; max-width:0px; opacity:0; overflow:hidden; visibility:hidden; "
    'mso-hide:all;">*|MC_PREVIEW_TEXT|*</span><!--<![endif]-->\n'
    "<!--*|END:IF|*-->"
)

TOKENS = {
    "subject": "*|MC:SUBJECT|*",
    "preview": PREVIEW,
    "unsubscribe_url": "*|UNSUB|*",
    "preferences_url": "*|UPDATE_PROFILE|*",
    "archive_url": "*|ARCHIVE|*",
    "address": "*|HTML:LIST_ADDRESS_HTML|*",
    "permission_reminder": "*|LIST:DESCRIPTION|*",
    "company": "*|LIST:COMPANY|*",
    "year": "*|CURRENT_YEAR|*",
    "first_name": "*|FNAME|*",
}

RULES = {
    "MC1": "An mc:repeatable is never inside an mc:edit (it stops repeating) and holds at least one mc:edit.",
    "MC2": "mc:variant only goes with a named mc:repeatable, and the variants of one repeatable are adjacent "
           "siblings.",
    "MC3": "mc:hideable never sits on the same element as mc:repeatable.",
    "MC4": "No id attribute inside an mc:repeatable: repeating the block would duplicate it.",
    "MC5": "mc:edit goes on td, div or img, the containers the editor can open.",
    "MC6": "An editable image has width (Outlook shows it at its natural size without one), max-width in its "
           "style and no height: Mailchimp strips the height and a replaced photo would stretch.",
    "MC7": "The preview text span holds only *|MC_PREVIEW_TEXT|*. Fixed text next to it would ship in every "
           "campaign.",
    "MC8": "Every <img> is a file at the root of the zip, named with lowercase letters, digits and hyphens, "
           ".jpg, .png or .gif, or an https URL. No subfolders, no SVG, no temporary Figma URLs.",
    "MC9": "The zip weighs under 1 MB and holds one HTML file and no folders. That is Mailchimp's import limit.",
    "MC10": "An image inside url() in the <style>, such as a background photo, is an absolute https URL, for "
            "example from Mailchimp's Content Studio. On import Mailchimp uploads and rewrites only <img src>: "
            "a url() with a file name stays broken and the photo does not show.",
    "MC11": "Every {{esp.*}} token became a Mailchimp merge tag, and *|UNSUB|* is present.",
}


def translate(source):
    """Neutral annotations to Mailchimp's template language."""
    out = re.sub(r"(\s)data-edit=", r"\1mc:edit=", source)
    out = re.sub(r"(\s)data-label=", r"\1mc:label=", out)
    out = re.sub(r"(\s)data-repeat=", r"\1mc:repeatable=", out)
    out = re.sub(r"(\s)data-variant=", r"\1mc:variant=", out)
    out = re.sub(r"(\s)data-hide(?=[\s>/])", r"\1mc:hideable", out)
    out = re.sub(r"/\*\s*@group\s+([^/*]+?)\s*/\s*([^*]+?)\s*\*/", r"/*\n@tab \1\n@section \2\n*/", out)
    out = re.sub(r"/\*\s*@editable\s*\*/\s*", "/*@editable*/", out)
    for key, tag in TOKENS.items():
        out = out.replace("{{esp.%s}}" % key, tag)
    return out


def check(source, folder=None, zip_path=None):
    """Returns [(rule, line, message)] for the translated HTML."""
    doc = Document(source)
    found = []

    def bad(rule, line, message):
        found.append((rule, line, message))

    def inside_edit(node):
        return any("mc:edit" in a.attrs for a in node.ancestors())

    for n in doc.nodes:
        if "mc:repeatable" in n.attrs:
            if inside_edit(n):
                bad("MC1", n.line, "mc:repeatable inside an mc:edit")
            if not any("mc:edit" in d.attrs for d in n.descendants()):
                bad("MC1", n.line, "mc:repeatable with no mc:edit inside")
            if "mc:hideable" in n.attrs:
                bad("MC3", n.line, "mc:hideable and mc:repeatable on the same element")
            for d in n.descendants():
                if "id" in d.attrs:
                    bad("MC4", d.line, f'id="{d.attrs["id"]}" inside an mc:repeatable')
        if "mc:variant" in n.attrs and not n.attrs.get("mc:repeatable"):
            bad("MC2", n.line, "mc:variant without a named mc:repeatable")
        if "mc:edit" in n.attrs:
            name = n.attrs["mc:edit"]
            if n.tag not in ("td", "div", "img"):
                bad("MC5", n.line, f'mc:edit="{name}" is on <{n.tag}>')
            if n.tag == "img":
                if not n.attrs.get("width"):
                    bad("MC6", n.line, f'editable image "{name}" has no width')
                if "height" in n.attrs:
                    bad("MC6", n.line, f'editable image "{name}" has a height')
                if "max-width" not in n.style():
                    bad("MC6", n.line, f'editable image "{name}" has no max-width in its style')
    groups = {}
    for n in doc.nodes:
        if "mc:variant" in n.attrs and n.attrs.get("mc:repeatable"):
            groups.setdefault(n.attrs["mc:repeatable"], []).append(n)
    for name, variants in groups.items():
        siblings = [c for c in variants[0].parent.children if hasattr(c, "tag")]
        positions = sorted(siblings.index(v) for v in variants if v in siblings)
        if len({id(v.parent) for v in variants}) > 1 or positions != list(range(positions[0], positions[0] + len(variants))):
            bad("MC2", variants[0].line, f'the variants of mc:repeatable="{name}" are not adjacent siblings')

    previews = [n for n in doc.nodes if "mcnPreviewText" in n.classes()]
    for n in previews:
        content = "".join(t.text for t in doc.texts(n)).strip()
        if content != "*|MC_PREVIEW_TEXT|*":
            bad("MC7", n.line, f'the preview text is not only *|MC_PREVIEW_TEXT|*: "{content[:40]}"')

    for n in doc.nodes:
        if n.tag != "img":
            continue
        src = n.attrs.get("src") or ""
        if src.startswith("https://"):
            if "figma.com" in src or "example.com" in src:
                bad("MC8", n.line, f"{src[:60]} is a temporary or example URL")
            elif not src.lower().split("?")[0].endswith(IMAGE_EXT):
                bad("MC8", n.line, f"{src[:60]} is not .jpg, .png or .gif")
        elif not IMAGE_NAME.match(src):
            bad("MC8", n.line, f'"{src}" is neither a valid file name at the root of the zip nor an https URL')
        elif folder and not os.path.isfile(os.path.join(folder, src)):
            bad("MC8", n.line, f'"{src}" is not next to the HTML')
    for url in re.findall(r"url\(\s*['\"]?([^'\")]+)", doc.css):
        if not url.startswith("https://"):
            bad("MC10", 0, f'url("{url[:60]}") is not an https URL: upload the image to Content Studio and use its URL')
        elif not url.lower().split("?")[0].endswith(IMAGE_EXT) or "figma.com" in url or "example.com" in url:
            bad("MC10", 0, f'url("{url[:60]}") is not a usable .jpg, .png or .gif')

    if zip_path and os.path.isfile(zip_path):
        if os.path.getsize(zip_path) >= ZIP_MAX:
            bad("MC9", 0, f"the zip weighs {os.path.getsize(zip_path) // 1000} KB")
        with zipfile.ZipFile(zip_path) as z:
            htmls = [x for x in z.namelist() if x.lower().endswith((".html", ".htm"))]
            if len(htmls) != 1:
                bad("MC9", 0, f"the zip holds {len(htmls)} HTML files")
            if any("/" in x for x in z.namelist()):
                bad("MC9", 0, "the zip has folders")

    for m in re.finditer(r"\{\{\s*esp\.(\w+)\s*\}\}", source):
        bad("MC11", source.count("\n", 0, m.start()) + 1, f"{m.group(0)} did not become a Mailchimp merge tag")
    if "*|UNSUB|*" not in source:
        bad("MC11", 0, "missing *|UNSUB|*")
    return found


def package(folder, images, zip_path):
    """The zip Mailchimp imports: index.html and every image at the root."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(folder, "index.html"), "index.html")
        for name in sorted(images):
            z.write(os.path.join(folder, name), name)
    return zip_path

