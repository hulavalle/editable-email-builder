# Blocks

A block is one section of an email: a file with an optional leading comment, an optional `<style>` and the markup. The library's blocks live in `eeb/library/blocks/`. A project can add its own in `blocks/`, and a project block with the same name as a library block replaces it.

The reference is generated from the block files, so it cannot drift:

```sh
python3 -m eeb blocks
```

For each block it prints what the block is for, the fields `template.toml` must give it, the list fields (such as `[[block.cards]]`), its editable names, and whether the editor can repeat or hide it.

## Brand roles

Blocks never name a color or a font. They use the roles of `brand.toml`: `{{brand.colors.primary}}`, `accent`, `ink`, `sand`, `mist`, `line`, `white` and `black`, and `{{brand.fonts.headings}}` and `body`. [Set up a client repo](client-repo.md) says what each role paints.

## Using a block twice

A block's editable names are fixed, so a template can use it once. To use it again, give every use an `id`:

```toml
[[block]]
type = "image_text"
id = "one"

[[block]]
type = "image_text"
id = "two"
```

The id is added to every editable name (`image_text_photo_one`) and to its label. Keep the ids once a template is in a platform: the platform stores content by name.

A block that puts template values in its CSS, such as `hero_background`, can appear only once.

## Conventions for a new block

- Start with a comment that says what the block is for and what the person editing can do with it. `eeb blocks` prints it, and a test fails without it.
- Wrap the block in `<tr>…</tr>`. `base.html` places blocks inside a 600 px table.
- Mark each text, button and photo with `data-edit` and a `data-label`. Use the block name as a prefix: `offer_photo`, `offer_button`.
- Style editable content with a class on its container, in the block's `<style>`. Put `/* @group Tab / Section */` before each rule and `/* @editable */` before each property the style panel may change.
- Keep fixed layout inline: paddings, borders, widths.
- Give a fixed-width button table the class `button-table`, and a padded cell the class `mobile-pad`: both shrink on a phone.
- Take every color and font from a brand role.
- Use `{{#list}}…{{/list}}` for a repeated part, with `{{n}}` as the position from 1.
- Add the media queries under `@media only screen and (max-width:{{brand.mobile}}px)`.
- Use the block in at least one library template, or a test fails: a block no template uses has never been built.
