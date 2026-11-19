"""The library works as a whole: every template builds clean, every block is used, blocks can
repeat with an id, a client repo can start from it, and every button is readable."""

import os
import re
import shutil
import tempfile
import tomllib
import unittest

from eeb import cli
from eeb.compose import LIBRARY, BuildError, compose, read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = sorted(os.listdir(os.path.join(LIBRARY, "templates")))


def contrast(a, b):
    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


class Library(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = tempfile.mkdtemp()
        cls.results = {t: cli.build(t, "mailchimp", root=ROOT, out=cls.out) for t in TEMPLATES}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.out, ignore_errors=True)

    def test_every_template_builds_clean(self):
        for name, (_, zip_path, findings) in self.results.items():
            with self.subTest(template=name):
                self.assertEqual(findings, [])
                self.assertIsNone(zip_path, "library templates are examples: preview only")

    def test_every_block_is_used_by_a_template(self):
        used = set()
        manifests = [os.path.join(LIBRARY, "templates", n, "template.toml") for n in TEMPLATES]
        fixtures = os.path.join(ROOT, "tests", "fixtures")
        manifests += [os.path.join(fixtures, n, "template.toml") for n in os.listdir(fixtures)]
        for manifest in manifests:
            used |= set(re.findall(r'^type = "(\w+)"', read(manifest), re.M))
        blocks = {b[:-5] for b in os.listdir(os.path.join(LIBRARY, "blocks"))}
        self.assertEqual(blocks - used, set(), "a block no template uses has never been built or linted")

    def test_every_button_is_readable(self):
        brand = tomllib.loads(read(os.path.join(LIBRARY, "brand.toml")))["colors"]
        base = read(os.path.join(LIBRARY, "base.html"))
        for cls in re.findall(r"^\.(button-[\w-]+) \{", base, re.M):
            bg = re.search(r"\." + cls + r" \{[^}]*background-color:\{\{brand\.colors\.(\w+)\}\}", base).group(1)
            fg = re.search(r"\." + cls + r" a \{[^}]*color:\{\{brand\.colors\.(\w+)\}\}", base).group(1)
            with self.subTest(button=cls):
                self.assertGreaterEqual(contrast(brand[bg], brand[fg]), 4.5, f"{fg} on {bg}")


class TemplateCase(unittest.TestCase):
    """A throwaway project root that composes one template.toml written by the test."""

    def setUp(self):
        self.root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root)

    def template(self, text):
        folder = os.path.join(self.root, "templates", "t")
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "template.toml"), "w", encoding="utf-8") as f:
            f.write(text)
        return folder


class Ids(TemplateCase):
    def test_a_block_with_ids_repeats_with_distinct_names(self):
        html, _, _ = compose(self.root, self.template(
            '[[block]]\ntype = "heading_text"\nid = "intro"\ntext = "<p>a</p>"\n\n'
            '[[block]]\ntype = "heading_text"\nid = "outro"\ntext = "<p>b</p>"\n'))
        self.assertIn('data-edit="text_intro"', html)
        self.assertIn('data-edit="text_outro"', html)

    def test_a_repeated_block_without_id_is_refused(self):
        with self.assertRaises(BuildError):
            compose(self.root, self.template(
                '[[block]]\ntype = "divider"\n\n[[block]]\ntype = "divider"\n'))


class Bands(TemplateCase):
    """Each use of a block sits on the band its template names, and dark bands turn its text light."""

    def test_two_uses_of_a_block_sit_on_two_bands(self):
        html, _, _ = compose(self.root, self.template(
            '[[block]]\ntype = "heading_text"\nid = "light"\ntext = "<p>a</p>"\n\n'
            '[[block]]\ntype = "heading_text"\nid = "dark"\nband = "ink"\ntext = "<p>b</p>"\n'))
        self.assertIn('class="copy band-white', html)
        self.assertIn('class="copy band-ink', html)
        self.assertIn("/* @group Bands / Ink band text */", html)
        self.assertNotIn("/* @group Bands / White band text */", html, "a light band keeps the block's own colors")

    def test_a_band_that_is_not_a_brand_color_is_refused(self):
        with self.assertRaises(BuildError):
            compose(self.root, self.template('[[block]]\ntype = "heading_text"\nband = "teal"\ntext = "<p>a</p>"\n'))

    def test_text_on_a_band_is_checked_with_the_color_that_wins(self):
        from eeb import lint
        dark = '[[block]]\ntype = "heading_text"\nband = "{}"\ntext = "<p>a</p>"\n'
        html, _, _ = compose(self.root, self.template(dark.format("ink")))
        self.assertEqual([f for f in lint.check(html, self.root) if f[0] == "A1"], [])
        html, _, _ = compose(self.root, self.template(dark.format("accent")))
        self.assertEqual([f for f in lint.check(html, self.root) if f[0] == "A1"], [],
                         "the block's own ink text reads on the accent band")


class Sections(unittest.TestCase):
    """The markup of a block: lists share a width among their items, optional parts show once and
    inverted parts show when a field is missing."""

    def test_share_divides_a_width_among_the_items(self):
        from eeb.compose import render
        body = '{{#items}}<td width="{{share:540}}"><img width="{{share:540-10}}"></td>{{/items}}'
        two = render(body, {"items": [{}, {}]}, set(), "t")
        three = render(body, {"items": [{}, {}, {}]}, set(), "t")
        self.assertEqual(two.count('width="270"'), 2)
        self.assertEqual(two.count('width="260"'), 2)
        self.assertEqual(three.count('width="180"'), 3)
        self.assertEqual(three.count('width="170"'), 3)
        with self.assertRaises(BuildError):
            render("{{share:540}}", {}, set(), "t")

    def test_an_optional_list_shows_its_part_once_and_an_inverted_part_fills_in(self):
        from eeb.compose import render
        body = "{{#totals?}}<table>{{#totals}}<tr>{{label}}</tr>{{/totals}}</table>{{/totals}}"
        self.assertEqual(render(body, {"totals": [{"label": "a"}, {"label": "b"}]}, set(), "t"),
                         "<table><tr>a</tr><tr>b</tr></table>")
        self.assertEqual(render(body, {}, set(), "t"), "")
        item = "{{#items}}{{#icon?}}<img src={{icon}}>{{/icon}}{{^icon}}<p>{{n}}</p>{{/icon}}{{/items}}"
        self.assertEqual(render(item, {"items": [{"icon": "x.png"}, {}]}, set(), "t"), "<img src=x.png><p>2</p>")

    def test_fields_list_optional_items_and_optional_lists(self):
        from eeb.compose import fields
        _, optional, lists = fields(read(os.path.join(LIBRARY, "blocks", "steps.html")))
        self.assertEqual(lists["items"], ["text", "icon (optional)"])
        _, optional, lists = fields(read(os.path.join(LIBRARY, "blocks", "order_summary.html")))
        self.assertNotIn("totals", lists)
        self.assertIn("[[totals]] with amount, label", optional)


class ClientRepo(unittest.TestCase):
    def test_init_and_new_start_a_client_repo_that_builds_once_links_are_real(self):
        root = tempfile.mkdtemp()
        try:
            cli.init(root)
            self.assertTrue(os.path.isfile(os.path.join(root, "brand.toml")))
            folder = cli.new("hola", "welcome", root=root)
            self.assertNotIn("example = true", read(os.path.join(folder, "template.toml")))
            _, zip_path, findings = cli.build("hola", "mailchimp", root=root)
            self.assertIsNone(zip_path, "a copied template keeps placeholder links and sample images until they are replaced")
            self.assertEqual({f[1] for f in findings}, {"C4", "C10"})
            text = read(os.path.join(folder, "template.toml")).replace("https://www.example.com", "https://www.northwind-stays.com")
            os.makedirs(os.path.join(folder, "img"))
            for name in set(re.findall(r'"library:([\w.-]+)"', text)):
                shutil.copyfile(os.path.join(LIBRARY, "img", name), os.path.join(folder, "img", "own-" + name))
            text = re.sub(r'"library:([\w.-]+)"', r'"img/own-\1"', text)
            with open(os.path.join(folder, "template.toml"), "w", encoding="utf-8") as f:
                f.write(text)
            _, zip_path, findings = cli.build("hola", "mailchimp", root=root)
            self.assertEqual(findings, [])
            self.assertTrue(zip_path)
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
