"""Every rule fires on a planted violation, and the example template is clean.

Each case is the real shape of a mistake: a string of the built HTML and what it becomes. A new
rule without a case here fails test_every_rule_has_a_case."""

import os
import shutil
import tempfile
import unittest
import zipfile

from eeb import cli, lint
from eeb.adapters import mailchimp
from eeb.compose import compose, read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLE = os.path.join(ROOT, "eeb", "library", "templates", "example")
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "hero-background")

# Core rules run on the neutral HTML.
CORE = {
    "E1": [('<tr>\n<td class="footer"', '<tr><td style="padding:10px;">Fixed text nobody can change</td></tr>\n<tr>\n<td class="footer"')],
    "E2": [("<p>30% OFF ALL STAYS", '<p style="font-size:22px;">30% OFF ALL STAYS')],
    "E3": [('data-edit="offer_band"', 'data-edit="offer_text"'), ('data-edit="promo_text"', 'data-edit="Promo Text"'),
           (' data-label="Offer: band"', "")],
    "E4": [("<p>Save 30%", '<div data-edit="inner" data-label="x"><p>Save 30%</div>')],
    "E5": [("/* @group Footer / Background */", "/* Footer background */")],
    "E6": [('<td class="footer" data-edit="footer" data-label="Legal footer" align="center" style="',
            '<td class="footer" data-edit="footer" data-label="Legal footer" align="center" style="background-color:#13293d; ')],
    "L1": [("{{esp.unsubscribe_url}}", "https://www.northwind-stays.com/"), ("<p>{{esp.address}}</p>", "")],
    "L2": [("{{esp.preview}}", "")],
    "D1": [('<meta charset="utf-8">', "")],
    "C1": [("</body>", "<script>alert(1)</script></body>")],
    "C2": [('style="padding:14px 20px;', 'style="float:left; padding:14px 20px;')],
    "C3": [('<td class="hero" align="center"', '<td class="hero" background="hero-photo.jpg" align="center"')],
    "C4": [('<a href="https://www.example.com/contact/" target="_blank">', '<a href="#" target="_blank">'),
           ('<a href="https://www.example.com/contact/" target="_blank">', '<a href="https://www.northwind-stays.com/contact/">')],
    "C5": [("</body>", "<!--" + "x" * lint.HTML_MAX + "--></body>")],
    "C6": [('<table role="presentation" class="offer-card"', '<table class="offer-card"')],
    "C7": [('alt="" style="display:block; width:100%; max-width:600px;', 'style="display:block; width:100%; max-width:600px;')],
    "C8": [("BOOK NOW</a>", "{{button}}</a>")],
    "C9": [('style="border-collapse:separate; width:506px;', 'style="width:506px;')],
    "B1": [(".footer {\n  /* @editable */ background-color:#13293d;", ".footer {\n  /* @editable */ background-color:#123456;")],
    "B2": [("</style>\n<!--[if mso]>", ".odd { font-family:Comic Sans MS, cursive; }\n</style>\n<!--[if mso]>")],
}

# Mailchimp rules run on the translated HTML. MC9 checks the zip and has its own test.
MAILCHIMP = {
    "MC1": [('<table role="presentation" mc:repeatable="offer"',
             '<table role="presentation" mc:repeatable="empty" cellpadding="0" cellspacing="0" border="0"><tr><td></td></tr></table>'
             '<table role="presentation" mc:repeatable="offer"')],
    "MC2": [('mc:repeatable="products"', 'mc:variant="three"')],
    "MC3": [('mc:repeatable="products"', 'mc:repeatable="products" mc:hideable')],
    "MC4": [('class="product-name"', 'id="name" class="product-name"')],
    "MC5": [('<a href="https://www.example.com/contact/" target="_blank">',
             '<a mc:edit="link" mc:label="x" href="https://www.example.com/contact/" target="_blank">')],
    "MC6": [('src="offer-photo.jpg" width="506"', 'src="offer-photo.jpg" width="506" height="303"')],
    "MC7": [(">*|MC_PREVIEW_TEXT|*<", ">*|MC_PREVIEW_TEXT|* Save 30% this spring<")],
    "MC8": [('src="product-one.jpg"', 'src="img/product-one.jpg"'),
            ('src="product-two.jpg"', 'src="https://www.figma.com/api/mcp/asset/abc.png"'),
            ('src="product-three.jpg"', 'src="product-three.svg"')],
    "MC10": [(".hero {\n", '.hero {\n  background-image:url("hero-photo.jpg");\n')],
    "MC11": [("*|UNSUB|*", "{{esp.unsubscribe}}")],
}


class Rules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = tempfile.mkdtemp()
        cls.folder, cls.zip_path, cls.findings = cli.build("example", "mailchimp", root=ROOT, out=cls.out)
        cls.neutral = compose(ROOT, EXAMPLE)[0]
        cls.final = read(os.path.join(cls.folder, "index.html"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.out, ignore_errors=True)

    def test_example_is_clean(self):
        self.assertEqual(self.findings, [])
        self.assertTrue(os.path.isfile(self.zip_path))

    def test_every_rule_has_a_case(self):
        self.assertEqual(set(lint.RULES) - set(CORE), set())
        self.assertEqual(set(mailchimp.RULES) - set(MAILCHIMP) - {"MC9"}, set())

    def test_core_rules_fire(self):
        for rule, cases in CORE.items():
            for old, new in cases:
                with self.subTest(rule=rule, new=new[:50]):
                    self.assertIn(old, self.neutral, "the case no longer matches the built HTML")
                    fired = {f[0] for f in lint.check(self.neutral.replace(old, new, 1), ROOT)}
                    self.assertIn(rule, fired)

    def test_mailchimp_rules_fire(self):
        for rule, cases in MAILCHIMP.items():
            for old, new in cases:
                with self.subTest(rule=rule, new=new[:50]):
                    self.assertIn(old, self.final, "the case no longer matches the built HTML")
                    fired = {f[0] for f in mailchimp.check(self.final.replace(old, new, 1), self.folder)}
                    self.assertIn(rule, fired)

    def test_mc9_zip_limits(self):
        bad = os.path.join(self.out, "bad.zip")
        with zipfile.ZipFile(bad, "w") as z:
            z.writestr("index.html", self.final)
            z.writestr("other.html", self.final)
            z.writestr("img/photo.jpg", b"x")
        self.assertIn("MC9", {f[0] for f in mailchimp.check(self.final, self.folder, bad)})

    def test_placeholder_links_only_in_examples(self):
        self.assertNotIn("C4", {f[0] for f in lint.check(self.neutral, ROOT, example=True)})
        self.assertIn("C4", {f[0] for f in lint.check(self.neutral, ROOT, example=False)})


class HeroBackground(unittest.TestCase):
    def test_https_background_builds_clean(self):
        neutral, images, _ = compose(ROOT, FIXTURE)
        self.assertEqual(lint.check(neutral, ROOT), [])
        out = tempfile.mkdtemp()
        try:
            final = mailchimp.translate(neutral)
            with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
                f.write(final)
            for name, src in images.items():
                shutil.copyfile(src, os.path.join(out, name))
            self.assertEqual(mailchimp.check(final, out), [])
            broken = final.replace("https://images.example.net/hero.jpg", "hero.jpg")
            self.assertIn("MC10", {f[0] for f in mailchimp.check(broken, out)})
        finally:
            shutil.rmtree(out)


class Build(unittest.TestCase):
    def test_a_failing_build_leaves_no_zip(self):
        root = tempfile.mkdtemp()
        try:
            shutil.copytree(EXAMPLE, os.path.join(root, "templates", "example"))
            manifest = os.path.join(root, "templates", "example", "template.toml")
            text = read(manifest).replace("{{esp.unsubscribe_url}}", "https://www.example.com/")
            with open(manifest, "w", encoding="utf-8") as f:
                f.write(text)
            _, zip_path, findings = cli.build("example", "mailchimp", root=root)
            self.assertIsNone(zip_path)
            self.assertIn("L1", {f[1] for f in findings})
            self.assertFalse(os.path.exists(os.path.join(root, "dist", "mailchimp", "example.zip")))
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
