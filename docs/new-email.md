# Build a new email from a Figma design

This guide takes a Figma email frame to a template you import into your email platform.

## Before you start

- The frame is 600 px wide, or the `width` in `brand.toml`.
- Every color and font in the frame is in `brand.toml`. If one is missing, add it there first. Rules B1 and B2 reject anything else.
- You can read the frame: export by hand from Figma, or use a coding agent with the Figma MCP server. [AGENTS.md](../AGENTS.md) has the steps for agents.

## Steps

1. Split the frame into sections from top to bottom. Match each section to a block in [Blocks](blocks.md).
2. If a section matches no block, write a new block in `blocks/`. Copy the closest block and keep its conventions: `data-edit` regions, `data-label`s, `/* @group */` and `/* @editable */` for styles.
3. Export each photo at twice its display width. Then prepare it:

	```sh
	python3 -m eeb image export.png templates/my-email/img/offer-photo.jpg --width 1012
	```

	Add `--height` to crop, `--focus 0.5,0.4` to choose the crop center, and `--darken 0.6,0.1,0.35` to darken the top for white text. An `.svg`, such as a logo or a wave, is rasterized.
4. If a block takes a background photo, such as `hero_background`, upload that photo to your platform's file manager. Copy its https URL for the template.
5. Copy `templates/example` to `templates/my-email`. Edit `template.toml`: one `[[block]]` per section, in order, with the texts, links and images from the frame. Remove `example = true`.
6. Follow every `<br>` in a text with a line break. Some blocks hide line breaks on mobile, and the words would join.
7. Build and look at the result:

	```sh
	python3 -m eeb build my-email
	python3 -m eeb preview my-email
	```

	If the build fails, each finding names the rule and why it exists. Fix the template or the block, then build again.
8. Compare the 700 px preview with the Figma frame, and check the 375 px preview.
9. Import the zip into the platform. For Mailchimp, see [Mailchimp](mailchimp.md).
10. Send a test to Gmail, Apple Mail and Outlook.

## When the platform shows something wrong

Look for the cause before you change the template. If a script can catch the mistake, add a rule to `eeb/lint.py` or to the adapter, with its planted case in `tests/test_rules.py`. If no script can catch it, write it in the platform's page in `docs/`.
