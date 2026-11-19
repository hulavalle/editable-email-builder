# Blocks

A block is one section of an email: a file in `blocks/` with an optional leading comment, an optional `<style>` and the markup. The block fixes its editable names, so every template that uses it shares them.

The reference is generated from the block files, so it cannot drift:

```sh
python3 -m eeb blocks
```

For each block it prints what the block is for, the fields `template.toml` must give it, the list fields (`[[block.cards]]`), its editable names, and whether the editor can repeat or hide it.

## Conventions for a new block

- Start with a comment that says what the block is for and what the person editing can do with it. `eeb blocks` prints it, and a test fails without it.
- Wrap the block in `<tr>…</tr>`. `base.html` places blocks inside a 600 px table.
- Mark each text, button and photo with `data-edit` and a `data-label`. Use the block name as a prefix: `offer_photo`, `offer_button`.
- Style editable content with a class on its container, in the block's `<style>`. Put `/* @group Tab / Section */` before each rule and `/* @editable */` before each property the style panel may change.
- Keep fixed layout inline: paddings, borders, widths.
- Take every color and font from `{{brand.*}}`.
- Use `{{#list}}…{{/list}}` for a repeated part, with `{{n}}` as the position from 1.
- Add the media queries under `@media only screen and (max-width:{{brand.mobile}}px)`.
