"""A small HTML tree and CSS reader, enough for the lint. Standard library only."""

import html.parser
import re

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs, parent, line):
        self.tag, self.attrs, self.parent, self.line = tag, attrs, parent, line
        self.children = []

    def ancestors(self):
        node = self.parent
        while node is not None:
            yield node
            node = node.parent

    def descendants(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.descendants()

    def classes(self):
        return (self.attrs.get("class") or "").split()

    def style(self):
        props = {}
        for decl in (self.attrs.get("style") or "").split(";"):
            if ":" in decl:
                key, value = decl.split(":", 1)
                props[key.strip().lower()] = value.strip()
        return props


class Text:
    def __init__(self, text, parent, line):
        self.text, self.parent, self.line = text, parent, line


class Document:
    """The parsed tree plus the CSS of every <style> outside conditional comments."""

    def __init__(self, source):
        reader = _Reader()
        reader.feed(source)
        reader.close()
        self.source = source
        self.root = reader.root
        self.doctype = reader.doctype
        self.nodes = list(self.root.descendants())
        self.css = "\n".join(
            "".join(c.text for c in n.children if isinstance(c, Text)) for n in self.nodes if n.tag == "style"
        )
        self.rules, self.media = css_rules(self.css)

    def texts(self, node=None):
        for child in (node or self.root).children:
            if isinstance(child, Text):
                yield child
            else:
                yield from self.texts(child)

    def declarations(self):
        """(line, property, value) for every inline style and every rule in <style>, media queries included."""
        found = [(n.line, k, v) for n in self.nodes for k, v in n.style().items()]
        for body in [body for _, _, body in self.rules] + self.media:
            for m in re.finditer(r"([\w-]+)\s*:\s*([^;{}]+)", strip_css_comments(body)):
                found.append((0, m.group(1).lower(), m.group(2).strip()))
        return found


class _Reader(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#document", {}, None, 0)
        self.current = self.root
        self.doctype = False

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype html"):
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.current, self.getpos()[0])
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_startendtag(self, tag, attrs):
        self.current.children.append(Node(tag, dict(attrs), self.current, self.getpos()[0]))

    def handle_endtag(self, tag):
        node = self.current
        while node is not None and node.tag != tag:
            node = node.parent
        if node is not None and node.parent is not None:
            self.current = node.parent

    def handle_data(self, data):
        self.current.children.append(Text(data, self.current, self.getpos()[0]))


def strip_css_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def css_rules(css):
    """Top-level rules as (leading comments, selector, body), and the bodies of @media blocks apart."""
    rules, media = [], []
    pattern = re.compile(r"((?:\s*/\*.*?\*/)*)\s*([^{}]+?)\s*\{", re.S)
    i = 0
    while True:
        m = pattern.search(css, i)
        if not m:
            break
        selector = m.group(2).strip()
        if selector.startswith("@media"):
            depth, j = 1, m.end()
            while depth and j < len(css):
                depth += {"{": 1, "}": -1}.get(css[j], 0)
                j += 1
            media.append(css[m.end():j - 1])
            i = j
            continue
        end = css.find("}", m.end())
        rules.append((m.group(1), selector, css[m.end():end]))
        i = end + 1
    return rules, media


def editable_properties(body, marker):
    """Properties preceded by an editable marker such as /* @editable */ or /*@editable*/."""
    return {m.group(1).lower() for m in re.finditer(marker + r"\s*([\w-]+)\s*:", body)}
