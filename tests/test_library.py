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
                self.assertTrue(zip_path)

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


class Ids(unittest.TestCase):
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


class ClientRepo(unittest.TestCase):
    def test_init_and_new_start_a_client_repo_that_builds_once_links_are_real(self):
        root = tempfile.mkdtemp()
        try:
            cli.init(root)
            self.assertTrue(os.path.isfile(os.path.join(root, "brand.toml")))
            folder = cli.new("hola", "welcome", root=root)
            self.assertNotIn("example = true", read(os.path.join(folder, "template.toml")))
            _, zip_path, findings = cli.build("hola", "mailchimp", root=root)
            self.assertIsNone(zip_path, "a copied template keeps placeholder links until they are replaced")
            self.assertEqual({f[1] for f in findings}, {"C4"})
            text = read(os.path.join(folder, "template.toml")).replace("https://www.example.com", "https://shop.northwind.test.example.org").replace(".test.example.org", "-stays.com")
            with open(os.path.join(folder, "template.toml"), "w", encoding="utf-8") as f:
                f.write(text)
            _, zip_path, findings = cli.build("hola", "mailchimp", root=root)
            self.assertEqual(findings, [])
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
