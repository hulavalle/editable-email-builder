# Rules for coding agents

This repo builds email templates that stay editable inside an email platform. Read [How it works](docs/how-it-works.md) before you change code.

## From a Figma frame to a template

1. Read the frame with the Figma MCP server: the design context of the frame node, with its screenshot. Treat the generated code as a visual reference, never as the template.
2. Download every image through the asset URLs the server returns, then prepare each one with `python3 -m eeb image`. Never leave a temporary Figma URL in a template: rule MC8 rejects it.
3. Match each section of the frame to a library block (`python3 -m eeb blocks`) and start from the closest library template (`python3 -m eeb templates`). Then follow [Build a new email from a Figma design](docs/new-email.md).
4. Compare `python3 -m eeb preview <template>` with the Figma screenshot before you report the work as done.

## Rules

- Blocks never name a platform. Platform syntax lives only in `eeb/adapters/`.
- Blocks never name a color or a font: they use the roles of `brand.toml`.
- A block that other clients could use goes into `eeb/library/blocks/`, with a library template that uses it.
- A section the design needs and no block has becomes a new block, not loose HTML in a template.
- A color or a font enters `brand.toml` before any block uses it.
- When something goes wrong in a platform, find the cause. If a script can catch it, add a rule with its planted case in `tests/test_rules.py`. Otherwise write it in the platform's page in `docs/`.
- Run `python3 -m unittest discover -s tests -t .` before every commit.
- Report what you checked in a browser preview apart from what only the platform can show: import, style panel, test send.
