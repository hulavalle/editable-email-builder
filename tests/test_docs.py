"""The docs stay true: counts, links and block descriptions are checked against the code."""

import os
import re
import unittest

from eeb import adapters, lint
from eeb.compose import LIBRARY, read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = ["README.md", "AGENTS.md"] + [os.path.join("docs", f) for f in os.listdir(os.path.join(ROOT, "docs"))]


class Docs(unittest.TestCase):
    def test_every_block_says_what_it_is_for(self):
        for name in os.listdir(os.path.join(LIBRARY, "blocks")):
            with self.subTest(block=name):
                self.assertRegex(read(os.path.join(LIBRARY, "blocks", name)), r"^\s*<!--")

    def test_every_library_template_says_what_it_is_for(self):
        for name in os.listdir(os.path.join(LIBRARY, "templates")):
            with self.subTest(template=name):
                self.assertRegex(read(os.path.join(LIBRARY, "templates", name, "template.toml")), r"^# \w")

    def test_the_rule_count_in_the_readme_is_true(self):
        total = len(lint.RULES) + sum(len(a.RULES) for a in adapters.ADAPTERS.values())
        self.assertIn(f"{total} rules", read(os.path.join(ROOT, "README.md")))

    def test_the_library_counts_in_the_readme_are_true(self):
        readme = read(os.path.join(ROOT, "README.md"))
        blocks = len([b for b in os.listdir(os.path.join(LIBRARY, "blocks")) if b.endswith(".html")])
        templates = len(os.listdir(os.path.join(LIBRARY, "templates")))
        self.assertIn(f"{blocks} blocks", readme)
        self.assertIn(f"{templates} starting templates", readme)

    def test_relative_links_point_to_files(self):
        for doc in DOCS:
            folder = os.path.dirname(os.path.join(ROOT, doc))
            for target in re.findall(r"\]\(([^)#:]+)(?:#[^)]*)?\)", read(os.path.join(ROOT, doc))):
                with self.subTest(doc=doc, target=target):
                    self.assertTrue(os.path.exists(os.path.join(folder, target)))

    def test_every_adapter_maps_every_token(self):
        for name in adapters.ADAPTERS:
            with self.subTest(adapter=name):
                adapters.get(name)


if __name__ == "__main__":
    unittest.main()
