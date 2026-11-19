# Mailchimp

The Mailchimp adapter (`eeb/adapters/mailchimp.py`) targets the classic email builder through Mailchimp's template language. Its rules start with `MC`: `python3 -m eeb rules` lists them. This page holds what no rule can check.

Sources: the Mailchimp help articles on the template language, on creating editable content areas, and on importing a custom HTML template.

## Import a template

1. Build the template: `python3 -m eeb build <template>`.
2. In Mailchimp, create a template with **Import HTML** and upload `dist/mailchimp/<template>.zip`.
3. Create campaigns with the classic email builder. In the new builder, a custom template is a closed block of code.

Custom code templates need the Standard plan or higher.

## How the template language behaves

- Each `mc:edit` name is a stored field. When a campaign switches templates, the text of matching names stays and the rest is lost. Never rename or remove an editable name in a template that is already in use: add a new one instead.
- Hide and remove buttons (`mc:hideable`, `mc:repeatable`) work in the campaign builder, not in the template editor. A removed block looks faded and is not sent. Use **Preview** and **Enter preview mode** to see what goes out.
- Changes made inside the variants of a repeatable block are lost when a campaign is replicated or saved as a template.
- The **Design** tab is built from the `@tab`, `@section` and `/*@editable*/` comments in the `<style>` of the `<head>`.
- Mailchimp inlines the CSS when it sends, according to its help. Check it in a test send.

## Import limits

- The zip holds one HTML file, weighs under 1 MB and has no folders. Image names use lowercase letters, digits and hyphens.
- On import, Mailchimp uploads the zip's images to Content Studio and rewrites `<img src>`. It does not rewrite a `url()` in the `<style>`: a background photo must be uploaded to Content Studio first, and its URL goes in the template (rule MC10).

## Email clients

- Outlook on Windows shows no CSS background images. The `hero_background` block shows its color and a short header there.
- Gmail and Outlook do not load web fonts. They show the end of each font stack in `brand.toml`.
