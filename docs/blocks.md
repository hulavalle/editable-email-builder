# Blocks

A block is one section of an email: a file with an optional leading comment, an optional `<style>` and the markup. The library's blocks live in `eeb/library/blocks/`. A project can add its own in `blocks/`, and a project block with the same name as a library block replaces it.

The reference is generated from the block files, so it cannot drift:

```sh
python3 -m eeb blocks
```

For each block it prints what the block is for, the fields `template.toml` must give it, the list fields (such as `[[block.cards]]`), its editable names, and whether the editor can repeat or hide it.

## Brand roles

Blocks never name a color or a font. They use the roles of `brand.toml`: `{{brand.colors.primary}}`, `accent`, `ink`, `sand`, `mist`, `line`, `white` and `black`, and `{{brand.fonts.headings}}` and `body`. [Set up a client repo](client-repo.md) says what each role paints.

## Bands

Every block that draws its own background sits on a band: one color role, chosen per use with the `band` field. Without `band`, the block keeps its usual color, such as white for `heading_text` or ink for `footer`.

```toml
[[block]]
type = "heading_text"
id = "dark"
band = "ink"
text = "<h2>Made to last</h2>"
```

compose adds the CSS of each band the template uses, after the blocks' own CSS. In the style panel each band is one section, **Bands / Ink band**, so every block on that band changes color together. Blocks color their text for light bands. On a band that `brand.toml` lists under `[bands]`, the headings, paragraphs, list items and links of every block take the color given there. Rule A1 checks the color that wins, so text that does not read on its band still fails the build.

These blocks have no band, because a band would break their design: `countdown`, `stats`, `offer`, `products`, `hero_background`, `wave` and `view_in_browser`.

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
- Put the block on a band: add `band-{{band|white}}` to the class of its outer cell, with its usual color role as the default, and give the block no background rule of its own. Color its text for a light band.
- Keep fixed layout inline: paddings, borders, widths.
- Give a fixed-width button table the class `button-table`, and a padded cell the class `mobile-pad`: both shrink on a phone.
- Take every color and font from a brand role.
- Use `{{#list}}…{{/list}}` for a repeated part, with `{{n}}` as the position from 1 and `{{count}}` as the number of items. For columns, let the items set the count: `{{share:540}}` is 540 px shared among the items, rounded down, and `{{share:540-10}}` the same less 10 px of padding, so two items get 270 and 260, three get 180 and 170.
- Give an optional field a default with `{{field|default}}`. Wrap an optional part in `{{#field?}}…{{/field}}`: it shows once when the template gives the field a value, a list with items included, and disappears when the field is missing or empty. `{{^field}}…{{/field}}` is its opposite, for what shows in its place. Inside a list, both work on the item's own fields, such as an icon that replaces a number.
- Add the media queries under `@media only screen and (max-width:{{brand.mobile}}px)`.
- Use the block in at least one library template, or a test fails: a block no template uses has never been built.
