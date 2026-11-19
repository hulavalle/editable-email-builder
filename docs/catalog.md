# Figma kit catalog

This page maps a licensed Figma kit of email templates onto the library. Each row is one laid-out template of the kit, with its node id in the kit's Figma file, the library template built from it, its purpose and its sections from top to bottom. Each section names the library block that draws it. A library template built from the kit says `# Kit frame <id>.` in its opening comment, and a test keeps that comment and this table in step.

The library takes the structure and the design of each template: the order of the sections, the composition, the type hierarchy, the spacing and the kind of each module. It takes none of the brands that appear in the kit. Texts are rewritten for the sample brand, Example Co., and every image is a sample made with `tools/make-example-images.py` or drawn in SVG. No asset of the kit enters the repo.

## How to read a section

- `heading_text` is an existing block that draws the section with its content changed.
- `heading_text` (align = left) is an existing block that needs one more field or option. The field in parentheses is the proposal. The block work decides the final field.
- **new** `logo_bar` is a block the library does not have yet.

## Templates not imported

The kit has 80 laid-out templates. Two repeat another template, so 78 are imported:

- `1:1656` (Abandoned Cart) is the same frame as `1:936`.
- `1:3731` (Blog #2) is the same design as `1:1777` (Blog No. 2).

## New blocks

Five sections of the kit have no block. Sections that are the same module with another look are grouped under one block:

- `logo_bar`: the logo on the left and a small editable area on the right, such as links, a short message, a button or social icons, on one band. It stacks on a phone. It covers logo-and-menu headers, account bars and footer rows. 12 sections in 9 templates.
- `link_stack`: links stacked one per row, between thin rules or as outlined pills, in one editable area. For categories and help pages above the footer. 10 sections in 10 templates.
- `callout`: an inset panel with its own color, border and rounded corners, holding a heading, a text, an optional photo and an optional button. For referral boxes, survey cards, gift panels and an access card. 8 sections in 6 templates.
- `text_columns`: two text columns side by side, such as billing and shipping addresses or two groups of links. It stacks on a phone. 4 sections in 3 templates.
- `image_mosaic`: one tall photo beside two stacked photos, each with a button under it. It stacks on a phone. 2 sections in 2 templates.

Other modules of the kit look new but fit an existing block once the block takes a field:

- Rows with an icon beside a title and a text use `steps`, with an icon in place of the number.
- Guarantee rows with an icon beside one line use `features`, with thin rules between the columns.
- App store badges use `social`, with a title line and a larger icon.
- Article cards, myth cards and stories with a photo above the text use `image`, inset, then `heading_text`, aligned left.
- Timelines, shop-the-look rows and reading lists use `image_text`. Rows alternate the photo side, and some rows take a button or a narrow photo.

## Fields the existing blocks need

These proposals come from the sections marked with a field in the table. The number is how many sections ask for it. The first group exists now. `python3 -m eeb blocks` lists each block's optional fields.

- `band` on every block that draws a background: 48 sections across 31 templates put a block on another brand color, often dark with white text.
- `align = left`: 22 sections of `heading_text`, and some of `logo_header`, `section_title`, `social`, `footer`, `promo`, `prefooter`, `button` and `hero_background`.
- Optional logo and button in the hero blocks: 25 sections of `hero_background`, 3 of `hero_image` and 2 of `hero_text`. `hero_background` also takes `gap`, the photo above the title.
- `image` with `width`, `space` and `radius`: 21 sections.
- `footer` with a logo: 5 sections.
- `image_text` with a button: 7 sections.
- `button` with `width` and `style`: 4 sections at full width, and light buttons on dark bands.
- `heading_text` with `padding`, for text close under a photo.
- `features` with one column per item, two to five, icons optional per item, and `rules` between the columns: 14 sections.
- `steps` with an `icon` per item in place of the number: 8 sections.
- `image_pair` and `products_two` with one column per item, so three photos or three cards make three columns, and `products_two` with the button optional per card: 7 sections.
- `order_summary` without `totals`: 4 sections.
- `social` with a `title` line above the icons.
- `hero_image` with a paragraph under its title.

Still to build:

- About 20 other options appear once or twice each, such as `faq` questions in boxes or a ring style for `countdown`. The design adapts to the existing block for those, unless the block work finds the field cheap.

## Gaps outside the blocks

- Five templates set their sections inside an inset card or an outlined frame on a page color: Post-Purchase Follow-Up, Limited-Time Discounts, Affiliate Program Promotion, Product Features and Flash Sale. `base.html` has no option for that frame.
- At least 18 templates have no unsubscribe link or no postal address, and 3 have no footer at all. Rule L1 requires both, so every imported template ends with the `footer` block.
- Most designs ask for at least one thing the lint forbids. [Adaptations](#adaptations) lists each one with the change that replaces it.

## Templates

| Kit template | Figma | Library template | Purpose | Sections, top to bottom |
|---|---|---|---|---|
| Teaser | `1:5227` |  | A product teaser: it builds anticipation with a headline over a photo, says something exciting is coming, gives the release date with a reminder button, invites a first purchase, then offers quick links, social icons and the footer. | Open In Browser: `view_in_browser`<br>Hero Banner: `hero_background` (logo and button optional)<br>Heading + Text: `heading_text`<br>Line: `divider`<br>Product Release Date: **new** `callout` (on a band, not on a photo)<br>Line: `divider`<br>Heading + Text: `heading_text`<br>Button: `button`<br>Line: `divider`<br>Menu: `features` (columns = 2)<br>Line: `divider`<br>Menu: `social`<br>Line: `divider`<br>Text + Menu: `footer` |
| Flash Sale | `1:5295` |  | A 48-hour flash sale: a hero with large sale lettering, the main offer, its code and a button, then three product offers each with a code and a button, then a footer with social icons, subscription line, contact rows and address. | Open In Browser: `logo_header`<br>Open In Browser: `promo`<br>Open In Browser (lettering + photo): `image`<br>Open In Browser (offer copy): `hero_text`<br>Products: `product_feature` (heading region above the photo)<br>Text: **new** `logo_bar`<br>Menu: `steps` (an icon per item)<br>Text + Text: `footer` (align = left) |
| Sale Email | `1:5377` |  | A holiday sale announcement: the sale name, offer and button, a large oval photo, a second short message with a pill-shaped photo and button, then a brand footer with logo, address, social icons and unsubscribe. | Logo: `logo_header`<br>Heading: `hero_text`<br>Frame 115: `image`<br>Heading: `heading_text`<br>Frame 115 (photo): `image`<br>Frame 115 (button): `button`<br>Line: `divider`<br>Text: `logo_header`<br>Menu: `social`<br>Text + Text: `footer` |
| Trending Products | `1:5419` |  | A what's-new email: a hero with an oval photo, short intro and button, a checkerboard of labeled photos, a framed feature photo with a link, a code strip, a grid of six trending products, VIP perks, a pay-later strip, and the footer. | Hero Banner (logo): `logo_header`<br>Hero Banner (photo): `image` (inset = true)<br>Hero Banner (copy): `heading_text`<br>Hero Banner (button): `button`<br>Image Breaker: `image_text` (bleed = true)<br>Frame 116 (photo): `image` (inset = true)<br>Frame 116 (link): `heading_text`<br>Heading: `promo`<br>Text: `heading_text`<br>Text + Text: `image_pair` (columns = 3, captions optional)<br>Frame 138 (title): `heading_text`<br>Frame 138 (perks): `features` (columns = 4)<br>Frame 118: `features`<br>Frame 139: `promo`<br>Menu: `social`<br>Text: `footer` |
| Social Proof | `1:5742` |  | A press roundup: the logo, a 'press knows best' title, four rows that pair a photo with a press outlet's logo and a short quote, then a brand footer with links and the legal line. | Logo: `logo_header` (align = left)<br>Header Text: `heading_text`<br>Image Breakers: `image_text` (bleed = true)<br>Pre-Footer + All rights reserved text: **new** `logo_bar`<br>Blank space: `spacer`<br>Footer: `footer` |
| Welcome Email | `1:5666` |  | A welcome email: a discount strip, a header with logo and categories, a big photo, a welcome title with the discount line and a button, a short intro, a second photo with a titled link, four product picks, and a footer with account, store, category and social links. | Promo strip: `promo` (align = left)<br>Header Strip: **new** `logo_bar`<br>Hero Banner Image: `image`<br>Header Text + rule: `section_title`<br>Sub Heading + CTA button: `cta`<br>Body Text: `heading_text`<br>Image Breaker Image: `image` (inset = true)<br>Header Text: `heading_text`<br>Product Block (title): `heading_text`<br>Product Block (grid): `image_pair`<br>All rights reserved text: **new** `logo_bar`<br>Pre-Footer: **new** `logo_bar`<br>Divider: `divider`<br>Footer: `footer` (align = left) |
| Product Features | `1:5580` |  | A product launch: logo, menu and a shipping strip, a big left-aligned title and button over a photo, a 'get the look' intro, a shoppable photo with four numbered products, more picks, and a footer. | Logo: `logo_header`<br>Header Strip: `menu`<br>Header Strip: `promo`<br>Hero banner: `hero_background` (align = left; logo optional)<br>Header Text: `heading_text` (align = left)<br>Image Breaker Image (photo): `image` (inset = true)<br>Image Breaker Image (products): `products_two` (name optional, button as a full-width bar)<br>Product Block (title): `heading_text`<br>Product Block (grid): `image_pair`<br>Pre-Footer: `prefooter`<br>Footer: `footer` |
| Gift Card | `1:5525` | `gift_card` | A gift card push: a browser link, a header with logo and menu, a short headline over a big photo, a paragraph with a gift card button, five service perks, then a footer with social icons, policy links, legal lines and a decorative shape. | Promo Strip: `view_in_browser`<br>Header Strip: `logo_header` (align = left) and `menu`<br>Hero banner: `hero_background` (no logo, no button)<br>Body Text (paragraph): `heading_text`<br>Body Text (button): `button`<br>Body Text (perks): `features` (five items)<br>Footer (social): `social` (title)<br>Footer (links): `prefooter`<br>Footer (legal): `footer` |
| Customer Spotlight | `1:5798` |  | A customer before-and-after story: the logo, a title with one accented word and a short intro, two photos side by side, and the customer's quote. | Hero Logo: `logo_header`<br>Mask group (title): `heading_text`<br>Mask group (photos): `image_pair` (captions optional)<br>Mask group (quote): `testimonial` (photo optional) |
| Behind The Scenes Content | `1:5819` |  | A behind-the-brand video episode: a shipping strip and browser link, two logos and a menu, a photo, the episode title and teaser with a watch button, then social links, a site link, a category list, a review score and the footer. | Header Strip: `promo`<br>Link: `view_in_browser`<br>Transition: `divider`<br>Frame 12134 + Frame 12135: `logo_header`<br>Menu: `menu`<br>Hero Image: `image` (inset = true)<br>Header + Header + Body + Body: `heading_text`<br>CTA: `button`<br>Social Media: `menu`<br>Link: `heading_text`<br>Footer (category list): **new** `link_stack`<br>Footer (review score): `image`<br>Footer (legal): `footer` |
| Company Updates | `1:5911` |  | A quarterly newsletter: an issue label and logo, an intro, two new-release articles, two 2×2 galleries with captions, a link line, a tips article, three more articles, and a stay-tuned close. | Header: `view_in_browser`<br>Logo: `logo_header`<br>Body: `heading_text`<br>Header: `heading_text`<br>Image + Body: `product_feature` (link instead of button)<br>Image + Body: `product_feature` (link instead of button)<br>Transition: `divider` (ornament)<br>Header: `heading_text`<br>Image breaker 1 + Image Breaker 2: `image_pair`<br>Transition: `divider` (ornament)<br>Header: `heading_text`<br>Image Breaker 1 + Image Breaker 2: `image_pair`<br>Transition: `heading_text`<br>Body: `heading_text`<br>Image: `image` (inset = true)<br>Body: `heading_text`<br>Image Breaker: `product_feature` (link instead of button)<br>Body: `product_feature` (link instead of button)<br>Body: `product_feature` (link instead of button)<br>Body Header: `heading_text`<br>Footer: `footer` |
| Brand Storytelling | `1:6018` |  | A founder's brand story: the logo and a photo over a decorative shape, the story title on a dark band, a personal letter, four brand values, the founder's sign-off with a button and a P.S. code, four best-sellers, two value strips, and the footer. | Frame 12161 (logo): `logo_header`<br>Frame 12161 (photo): `image`<br>Frame 12161 (title band): `heading_text`<br>Transition: `wave`<br>Body: `heading_text` (align = left)<br>Image Breaker: `features` (columns = 2)<br>Body: `signature` (photo optional)<br>CTA: `button`<br>Body: `heading_text`<br>Product Block (title): `heading_text`<br>Product Block (cards): `products_two`<br>Pre-Footer (claims): `promo`<br>Pre-Footer (values): `features` (columns = 4)<br>Footer (logo): `logo_header`<br>Footer (social): `social`<br>Footer (legal): `footer` |
| Holiday Greetings | `1:6121` | `holiday_greeting` | A holiday greeting: a logo band, a festive headline with a button over a photo, a warm message, a best-seller title with a photo and a button, two service promises, social icons and a contact footer. | Logo Header: `logo_header` (band = primary)<br>Hero Image: `hero_background` (button, no logo)<br>Body: `heading_text` (band = dark)<br>Body Headline: `heading_text`<br>Image Breaker: `image` (inset)<br>CTA: `button`<br>Footer (promises): `steps` (an icon per item), between two `divider`<br>Footer (social): `social`<br>Footer (contact): `footer` (band = sand) |
| Discount Reminder | `1:6163` |  | A last-chance discount reminder: logo, a checkered border and a category menu, a bold headline over a large photo, the code reminder with a button, a friendly sign-off strip, and footer links. | Logo Header: `logo_header`<br>Transition: `wave`<br>Menu: `menu`<br>Hero Image (headline): `heading_text`<br>Hero Image (photo): `image` (inset = true)<br>Hero Image (code line): `heading_text`<br>Hero Image (button): `button`<br>Footer (sign-off): `promo`<br>Footer (border): `wave`<br>Footer (links): `steps` (an icon per item)<br>Footer (legal): `footer` |
| Countdown Timer Emails | `1:6271` | `early_bird_countdown` | An early-bird deal with a deadline: logo and menu, the offer headline, a countdown, the offer details and a button, a photo with a second button and terms, four service promises, a VIP club banner, and the footer. | Logo Header: `logo_header`<br>Menu: `menu`<br>Body: `hero_text` (no button)<br>Countdown: `countdown`<br>Body: `heading_text` (band = primary)<br>CTA: `button` (band = primary, style = accent)<br>Image Breaker (photo): `image`<br>Image Breaker (button): `button` (style = accent)<br>Image Breaker (terms): `heading_text`<br>Pre-Footer: `features` (four items)<br>Pre-footer: `image_text` (band = primary)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = white) |
| Benefits Emails | `1:6372` |  | A product benefits email: logo and a large title, an annotated product photo, three benefits with short explanations, a button, an ingredients title with photo and text, a two-column 'free from' list, a second button, and the footer. | Hero Banner (logo): `logo_header`<br>Hero Banner (title): `heading_text`<br>Hero Banner (photo): `image`<br>Body: `faq`<br>CTA: `button`<br>Image Breaker (title): `heading_text`<br>Image Breaker (photo): `image` (inset = true)<br>Image Breaker (text): `heading_text`<br>Image Breaker: `steps` (an icon per item)<br>CTA: `button`<br>Footer (logo): `logo_header`<br>Footer (social): `social`<br>Footer (disclaimer): `coupon` (border = solid, plain text)<br>Footer (legal): `footer` |
| Testimonials | `1:3831` |  | Social proof email: a quote-themed header with a shop button, a 'five-star reviews' heading, three customer review cards with stars, a shop button, then a lifestyle photo with a last button before the footer. | Hero Banner (logo): `logo_header`<br>Hero Banner (title): `hero_text` (band = light)<br>Headline: `heading_text`<br>Image Breaker (3 review cards): `testimonial` (stars)<br>Button: `button`<br>Transition: `spacer`<br>Pre-Footer (photo): `image`<br>Pre-Footer (button): `button`<br>Footer: `footer` |
| FAQ | `1:3922` |  | Answers common customer questions: a promo strip and playful header, then three question-and-answer pairs each followed by a recommended product with a button, a pro tip card, a sign-off, a six-item feature grid, a label band and the footer. | Promo Strip: `promo` (band = light)<br>Hero Banner: `hero_image`<br>Image Breaker 1 (Q&A): `faq` (style = bubbles)<br>Image Breaker 1 (recommended product): `image_text` (button)<br>Image Breaker 2 (Q&A): `faq` (style = bubbles)<br>Image Breaker 2 (recommended product): `image_text` (button)<br>Image Breaker 3 (Q&A): `faq` (style = bubbles)<br>Image Breaker 3 (recommended product): `image_text` (button)<br>Image Breaker 4 (pro tip): `offer`<br>Ending Signature: `heading_text` (band = dark)<br>Icon and Features: `features`<br>Featured Text: `promo`<br>Footer (social): `social` (band = dark)<br>Footer (legal): `footer` |
| General Promotions | `1:4102` |  | General sale email: promo strip, a collage header with logo and title, a short pitch with a button, a dark band of six product cards, a closing heading with text and button, then social icons and the footer. | Promo Strip: `promo` (band = light)<br>Hero Banner: `hero_image` (button optional)<br>Text: `heading_text`<br>Button: `button`<br>Transition + Product Block + Transition: `products`<br>Headline + Text: `heading_text`<br>Button: `button`<br>Footer (social): `social`<br>Footer (legal): `footer` (band = light) |
| Event Invitation | `1:4213` |  | Invites readers to a free in-person event: a photo header with a big event name, a card with the invitation, date and place, an RSVP button, and a social footer. | Hero Banner (photo header): `hero_background` (button optional)<br>Hero Banner (invitation card + button): `event_details` (card)<br>Footer (social): `social` (labels)<br>Footer (legal): `footer` |
| Thank You Email | `1:4425` |  | Seasonal thank-you that doubles as a promo: code strip, a 'we're thankful for you' photo header, a gift card visual with a discount message and button, a dark referral band (give a discount, get a reward) with a photo and button, a referral link line, three category tiles, a brand block with social icons, links and an app badge, and the footer. | Promo Strip: `promo`<br>Hero Banner: `hero_background` (logo and button optional)<br>IMAGE BREAKER (gift card): `image`<br>Body Section (text): `heading_text`<br>Body Section (button): `button`<br>Transition: `wave`<br>Sub-heading + IMAGE BREAKER + Body Section: `product_feature` (band = dark)<br>Body Section (referral link + label): `heading_text`<br>Category: `image_pair` (columns = 3)<br>Body Section (logo): `logo_header`<br>Body Section (social): `social`<br>Body Section (links): `prefooter`<br>Body Section (company line): `heading_text`<br>Body Section (app badge): `social` (title, badge size)<br>Footer: `footer` (band = light) |
| Referral Program Promotion | `1:4254` |  | Asks customers to refer friends for a free product: logo and menu, a 'refer a friend' photo header with a button, two short lists explaining how it works, a high-five call to action with fine print, a guarantees bar and a dark footer. | Header: `logo_header`<br>Promo Strip: `menu`<br>Spacer: `spacer`<br>Hero Banner: `hero_background` (logo optional)<br>Body Section 1: `heading_text`<br>Body Section 2: `heading_text`<br>Body Section + CTA + Body Section: `cta` (note)<br>Footer (guarantees): `features` (separators)<br>Footer (social): `social` (band = dark)<br>Footer (legal): `footer` (logo) |
| Reward/Points Program | `1:4319` |  | Tells members they have loyalty points to redeem: inline logo and menu, a big 'you've got points' headline, a short text with a redeem button, a photo-beside-text block announcing new rewards, and a footer over a photo with help contact and social icons. | Header: **new** `logo_bar`<br>Spacer: `spacer`<br>Hero Banner: `hero_text` (button optional)<br>Body Section: `heading_text`<br>CTA: `button`<br>Frame 12055: `image_text`<br>Footer (legal, with logo): `footer` (logo)<br>Footer (social): `social` (band = dark) |
| Newsletter Recap | `1:4373` |  | Welcome issue of a content newsletter: a type masthead with tagline, three photos, a long left-aligned letter on what each issue contains plus housekeeping, a wide photo, social icons and a light footer. | Hero Banner (masthead): `logo_header`<br>Hero Banner (photos): `image_pair` (columns = 3)<br>Frame 12076: `heading_text` (align = left)<br>Hero Banner (wide photo): `image`<br>Promo Strip: `social` (band = dark)<br>Footer: `footer` (band = light) |
| Mythbuster | `1:4509` | `myth_busting` | Debunks three common myths about a product category: logo, a headline with a short line and a button, three cards each with a photo, the myth, a 'truth' tag and the answer, a closing call to action and a dark footer with social icons. | Hero Banner Logo: `logo_header`<br>Hero Banner: `hero_text` (band = light)<br>Image Breaker (3 myth cards): `image` (inset; then heading_text)<br>Body Header + CTA: `cta`<br>Footer (social): `social` (band = dark)<br>Footer (legal): `footer` |
| Did You Know Content | `1:4567` |  | Educational 'did you know' email: a photo header with the logo, an intro heading and text, a numbered 'here's how' list with closing text and a button, a product photo with heading, text and button, a full-width photo, and a dark footer with stacked link buttons. | Hero Image (logo): `logo_header`<br>Hero Image (photo): `image`<br>Body: `heading_text`<br>Body (title): `heading_text`<br>Body (numbered list): `steps` (style = numeral)<br>Body (closing text): `heading_text`<br>CTA: `button`<br>Image Breaker: `image`<br>Body: `heading_text`<br>CTA: `button`<br>Prefooter: `image`<br>Footer (brand + links): **new** `link_stack`<br>Footer (legal): `footer` (logo) |
| Product Comparison | `1:4632` |  | Compares the product with a generic competitor: a colored header with title, text, button and photo, a feature comparison table with a button, a big closing headline with a button and a product photo, and a dark footer with stacked buttons and social icons. | Hero Banner (Frame 12392 + Hero Image): `hero_image`<br>Image Breaker (comparison): `comparison`<br>CTA: `button`<br>Transition: `wave`<br>Body Header + CTA: `cta`<br>Image: `image`<br>Footer (stacked buttons): **new** `link_stack`<br>Footer (social): `social` (band = dark)<br>Footer (legal): `footer` |
| Product Launch Countdown | `1:4744` |  | Pre-launch story email: a shipping strip and logo, two photo-led editorial blocks (heading, subheading, paragraphs, button: a behind-the-scenes link, then a pre-order), guarantees with social icons and a light footer; despite the title, the frame has no countdown. | Hero Banner strips: `promo`<br>Hero Banner Logo: `logo_header`<br>Image Breaker 1: `product_feature`<br>Image Breaker 2: `product_feature`<br>Footer (guarantees): `features` (separators)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = light) |
| Cart Abandonment Reminder | `1:4807` |  | Reminds a shopper of the item left in the cart, on an all-black design: logo, a ruled 'we're worried about you' title with text, the item photo with its name and a checkout button, a ruled title over two more product suggestions, and a footer with social icons, stacked links and legal lines. | Hero Banner Logo: `logo_header`<br>Body (ruled title): `section_title` (style = ruled)<br>Body (text): `heading_text` (align = left)<br>Image Breaker + CTA: `product_feature`<br>Body (ruled title 2): `section_title` (style = ruled)<br>Product Block: `image_pair`<br>Footer (social): `social`<br>Footer (links): **new** `link_stack`<br>Footer (legal): `footer` |
| Contest Invitation | `1:4865` |  | Invites readers to enter a co-branded giveaway: two logos, a photo, an eyebrow and title with an enter button and text, the prizes as two photo cards, a photo fading into a second headline with text and a guide button, an 'explore the brand' photo mosaic with shop buttons, the contest fine print and the footer. | Hero Banner Logo: `logo_header` (logo_two)<br>Hero Image: `image`<br>Body + CTA: `hero_text`<br>Body: `heading_text`<br>Image Breaker (prizes): `image_pair`<br>Image Breaker (photo fade): `image`<br>Image Breaker (headline + text): `heading_text`<br>CTA: `button`<br>Transition: `divider` (style = double)<br>Body: `section_title`<br>Image Breaker (mosaic): **new** `image_mosaic`<br>Body (fine print): `heading_text` (size = small)<br>Footer (legal, with logo): `footer` (logo)<br>Footer (social): `social` |
| Bundle Offers | `1:4952` |  | Promotes build-your-own bundles through five customer picks: an offer strip, a photo header with title, five repeated bundle cards (who the person is, what is in their bundle, a product photo with a savings badge, a build button), and a help block with the footer. | Hero Strip: `promo`<br>Hero Banner: `hero_background` (button optional)<br>Image Breaker (5 bundle cards): **new** `text_columns` (then image and button)<br>Transition: `wave`<br>Footer (help): `heading_text` (band = dark)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = light) |
| Blog Content Highlight (A) | `1:5104` |  | Holiday editorial digest: a rewards strip, a photo header with a left-aligned title and a read button, an intro line, alternating photo-and-text story blocks with shop links, a row of three product photos, a shop button, two photo tiles, a stack of links, a gift guide band and the footer. | Hero Strip: `promo` (band = light)<br>Hero Banner: `hero_background` (align = left)<br>Body: `heading_text`<br>Image Breaker 1: `image_text`<br>Product Block: `image_pair` (columns = 3)<br>Image Breaker 2: `image_text`<br>Image Breaker 3: `image_text`<br>Image Breaker 4: `image_text`<br>Image Breaker 5: `image_text`<br>CTA Button: `button`<br>Pre-footer (photo tiles): `image_pair`<br>Pre-footer (heading): `heading_text`<br>Pre-footer (links): **new** `link_stack`<br>Pre-footer (gift guide band): `promo`<br>Footer (social): `social`<br>Footer (legal): `footer` (band = light) |
| Abandoned Cart | `1:936` | `cart_checkout_nudge` | Reminds a shopper they left an item in the cart: a headline over a product photo, a short nudge, the cart item with quantity and total, a checkout button, then a help image and a 'Questions?' note before links, socials and the legal footer. | Logo Section: `logo_header`<br>Hero Banner (title): `heading_text`<br>Hero Banner (photo): `image` (inset)<br>Text Content: `heading_text`<br>Abandoned Cart: `order_summary` (no totals)<br>CTA Button: `button`<br>Image Breaker: `image` (inset)<br>Text Content: `heading_text`<br>Divider: `divider`<br>Pre Footer (links): `prefooter`<br>Pre Footer (socials): `social`<br>Divider: `divider`<br>Footer: `footer` (band = white) |
| Order Confirmation | `1:981` |  | Confirms an order: greeting, order number and date, the items ordered with prices, the totals, the payment method, billing and shipping addresses and a help line, then nav links, a social and address strip and the website link. | Logo: `logo_header`<br>Headline + Body: `heading_text`<br>Order No.: `heading_text`<br>Body + Divider (items ordered): `section_title` (align = left)<br>Product Details x2 + Other Details: `order_summary` (item_style = rule)<br>Body (payment info): `section_title` (align = left)<br>Payment Info: `order_summary` (totals optional)<br>Body + Other Details (addresses): **new** `text_columns`<br>Divider: `divider`<br>Body (help): `heading_text`<br>Body (nav links): `prefooter`<br>Footer: **new** `text_columns`<br>Credit Footer: `footer` |
| Shipping Confirmation | `1:1081` |  | Tells the customer their package has shipped: headline, a note with the order number, a track-package button, the items in the shipment, a refer-a-friend panel, a 'See you soon' photo, then a footer logo, social icons and the address. | Logo: `logo_header`<br>Menu Bar: `menu`<br>Headline + Body: `heading_text`<br>CTA Button: `button`<br>Divider: `divider` (ornament)<br>Body: `heading_text`<br>Products: `order_summary` (item_style = box)<br>Body Text: **new** `callout`<br>Divider: `divider` (ornament)<br>Header: `heading_text`<br>Pre-footer: `image`<br>Footer-Logo: `logo_header`<br>Footer (follow us): `social` (text)<br>Footer (legal): `footer` |
| Post-Purchase Follow-Up | `1:1146` |  | Thanks a customer for a first purchase and asks for a review, then pitches a subscription in a tinted panel and invites them to follow on social, all in rounded white cards on a grey page, ending with a footer card. | Logo: `logo_header`<br>Hero Banner: `image` (inset = true)<br>Headline + Body: `heading_text` (align = left)<br>CTA Button: `button`<br>Transition + Body + Transition: **new** `callout`<br>Image Breaker + Body + Transition: `product_feature`<br>Transition + Body (footer logo): `logo_header`<br>Socials: `social`<br>Text + Transition: `footer` |
| Replenishment Reminder | `1:1219` |  | Reminds a customer that a prescribed product is about to run out: sender line, logo, a personal headline, the product to reorder with a full-width button and a phone line, more products to refill with a button, four reasons to order through the service on dark bands, a last button and the footer. | Header + Divider: `section_title` (align = left)<br>Logo: `logo_header` (align = left)<br>Headline + Body: `heading_text` (align = left)<br>Product Details: `order_summary` (totals optional)<br>CTA Button: `button` (width = full)<br>Body: `heading_text`<br>Transition: `spacer`<br>Product Details (heading): `heading_text` (align = left)<br>Product Details (item): `order_summary` (totals optional)<br>CTA Button: `button` (width = full)<br>Transition: `spacer`<br>Image Breaker x4: `steps` (an icon per item)<br>Transition: `spacer`<br>CTA Button: `button` (width = full)<br>Text + Logo + Text: `footer` (logo) |
| Customer Feedback Request | `1:1308` |  | Invites customers to join a product feedback panel: logo, a title over a full-bleed photo, a question headline with text and a form button, a large photo with a founder quote, three perks in columns on a grey band, and a black footer with social links and legal lines. | Logo Header: `logo_header`<br>Hero Banner: `hero_background` (logo and button optional)<br>Header & Body text: `heading_text`<br>CTA: `button` (width = full)<br>Testimonial/Image Breaker + Body text: `testimonial` (photo_size = large)<br>Pre Footer: `features` (icon_width)<br>Footer (social links): `prefooter`<br>Footer (legal): `footer` |
| Survey Invitation | `1:1351` |  | Asks the reader to take a short survey in exchange for a discount code: logo, a bordered card with a greeting and two text-and-button pairs, then a footer with logo, tagline, social icons and legal lines between dashed rules. | Hero Banner / Logo Here: `logo_header`<br>Image Breaker / Text 1: **new** `callout`<br>Image Breaker / Text 2: **new** `callout`<br>Footer / Vector 1: `divider`<br>Footer / Logo Here: `logo_header`<br>Footer / tagline: `heading_text`<br>Footer / Vector 2: `divider`<br>Footer / Social Icons: `social`<br>Footer / Vector 3: `divider`<br>Footer Details: `footer` |
| Birthday Emails | `1:1402` |  | Celebrates the brand's birthday with a giveaway: logo, a huge 'Happy Birthday' headline, a paragraph and an enter button, a full-width photo, then a black footer with logo, stacked links, social icons and legal lines. | Logo Header + Hero Banner: `hero_image` (text)<br>Footer (logo): `logo_header`<br>Footer (links): `prefooter`<br>Footer (icons): `social`<br>Footer (text): `footer` |
| Special Offers | `1:376` | `bestseller_discount` | Offers a discount on bestsellers: logo, a type-only hero with eyebrow, title, condition and code button on a sand band, a full-width photo, a two-by-three grid of bestsellers, three category tiles, a row of service promises, and a sand footer with logo, slogan, links, socials and the legal line. | Header: `logo_header`<br>Hero Banner: `hero_text` (band = sand)<br>Image Breaker: `image`<br>Product (title): `heading_text`<br>Product (grid): `products_two` three times<br>Category: `image_pair` (three photos)<br>Menu: `features` (labels only)<br>Footer (logo): `logo_header` (band = sand)<br>Footer (slogan + contact): `heading_text` (band = sand)<br>Footer (menu): `prefooter`<br>Footer (icons): `social` (band = sand)<br>Footer (copyrights + unsubscribe): `footer` (band = white) |
| Back in Stock | `1:492` | `back_in_stock_hero` | Announces that a favorite item is back in stock: a full-bleed photo with the logo between thin rules and a two-weight headline, a short text, a shop button, a left-aligned thank-you note, then links with a small image and the legal line. | Hero Banner: `hero_background` (logo and button optional)<br>Body: `heading_text`<br>CTA: `button`<br>Body: `heading_text` (align = left)<br>Divider: `divider`<br>Pre-Footer: `prefooter` (align = left)<br>Footer: `footer` |
| Low Inventory Alerts | `1:525` |  | Warns that a product is almost sold out: one full-bleed photo carrying the logo, a two-weight headline and a rounded panel with text and a shop button, then a black footer with logo, three outlined link buttons, socials and the legal line. | Hero Banner and Body Text: `hero_background` (text)<br>Footer (logo): `logo_header`<br>Footer (CTA links): `prefooter` (style = pills)<br>Footer (socials): `social`<br>Footer (body): `footer` |
| New Product Launch | `1:566` |  | Launches a new product: a red hero with the logo between rules, stacked 'Introducing' type around the product photo with a badge, a bold claim and a button, a photo with bold justified copy over it, a benefit timeline with icons, an emotional text block with a button, a thank-you note, links with a small image and the legal line. | Hero Banner (logo): `logo_header` (rules)<br>Hero Banner (art): `image`<br>Body: `heading_text`<br>CTA: `button`<br>Hero Banner: `hero_background` (logo and button optional)<br>IB: `steps` (an icon per item)<br>Body: `heading_text` (align = left)<br>CTA: `button`<br>Body: `heading_text` (align = left)<br>Divider: `divider`<br>Pre-Footer: `prefooter` (image)<br>Footer: `footer` |
| Seasonal Collection Highlight | `1:669` |  | Presents a seasonal collection: a photo hero with logo and slanted title, an intro with two shop buttons, three photo moments each with a short caption (one a staggered pair), two more shop buttons, a gift link, a curved tagline, socials and the legal footer. | HERO: `hero_background` (logo and button optional)<br>Body: `heading_text`<br>CTA: `button`<br>CTA: `button`<br>Image Breaker: `image` (inset = true)<br>Body: `heading_text`<br>Image Breaker: `image_pair` (stagger)<br>Body: `heading_text`<br>Image Breaker: `image` (inset = true)<br>Body: `heading_text`<br>CTA: `button`<br>CTA: `button`<br>Body: `prefooter`<br>FOOTER (tagline): `image`<br>FOOTER (icons): `social`<br>FOOTER (legal): `footer` |
| ICYMI | `1:756` |  | Reminds readers of a product they may have missed: logo, a giant headline overlapped by a cut-out product on a diagonal two-tone background, short text and a button on grey, then the legal footer and social icons. | Hero Banner: `hero_image` (button optional)<br>Body: `heading_text`<br>CTA: `button`<br>Footer: `footer`<br>Socials: `social` |
| Limited-Time Discounts | `1:830` |  | Pushes a last-hour sitewide sale: inside a bordered card, a photo with logo and a 'last hour' badge, the discount title, a code pill and a button, then a countdown, a free-gift panel, three category rows with code and button, a claims panel, then a small logo, two link columns and a long legal footer. | Frame 12068: `hero_background` (logo and button optional)<br>Frame 12061 (title): `heading_text`<br>Frame 12061 (code): `coupon`<br>Frame 12061 (button): `button`<br>Frame 12065: `countdown`<br>Frame 12062 (gift panel): **new** `callout`<br>Frame 12062 (title): `heading_text`<br>Frame 12066, 12067, 12063: `image_text` (button)<br>Frame 12069: **new** `callout`<br>Frame 12070: `logo_header` (align = left)<br>Frame 12072 + 12071: **new** `text_columns`<br>Frame 12073: `divider`<br>Footer: `footer` |
| Holiday Promotions | `1:780` |  | Promotes holiday gifts: a photo hero with logo and title, a sale heading with text and a button, a second heading over two stacked photos with a button and a line, a rule, an extended-returns note with a gift icon, four trust badges on grey and a spare slot; it has no legal footer. | Hero: `hero_background` (logo and button optional)<br>Body: `heading_text`<br>CTA: `button`<br>IB (heading): `heading_text`<br>IB (photos): `image` (inset = true)<br>IB (button): `button`<br>IB (text): `heading_text`<br>Transition: `divider`<br>Pre footer: `heading_text` (icon)<br>iCON: `features` (columns = 4)<br>Additional: `heading_text` |
| Anniversary Emails (A) | `1:1429` |  | A brand anniversary sale: a strip announces a returning product, a photo hero repeats the number of years with a shop button, a paragraph and button push the anniversary sale, a titled timeline walks through the brand's milestones year by year, then a dark thank-you band with a sale button and the legal footer. | Logo Header: `logo_header`<br>Header & Body text: `promo`<br>Hero Banner: `hero_background` (logo optional)<br>Body text: `heading_text`<br>CTA: `button`<br>Header & Body text: `heading_text`<br>Image Breaker: `image_text` (alternating direction, no connecting line)<br>Body text: `hero_text`<br>Footer: `footer` (band = light) |
| Blog Content Highlight (B) | `1:1532` |  | A holiday digest from a home-goods brand: a rewards strip, a photo hero titled as the digest with a read-now button, a short intro, five story cards that alternate photo and text with a shop link, a row of three product links, a shop-all button, two photo tiles, a stacked list of store links ending on a gift-guide band, and the footer. | Frame 47: `promo`<br>Hero Banner: `hero_background` (align = left)<br>Body: `heading_text`<br>Product Block 1: `image_text`<br>Product: `products_two` (columns = 3)<br>Product Block 2: `image_text`<br>Product Block 3: `image_text`<br>Product Block 4: `image_text`<br>Product Block 5: `image_text`<br>Frame 12117: `button`<br>Frame 12119: `image_pair`<br>Frame 12125: **new** `link_stack`<br>Footer (icons): `social`<br>Footer (legal): `footer` (band = light) |
| Exclusive Access Email | `1:1703` |  | A Black Friday early-access announcement: the logo on a striped band, then one dark rounded card with an eyebrow, a big 'starts now' title, a product photo, a teaser line, a short paragraph and a shop button, then a light legal footer. | Stripes Background + Logo Section: `logo_header`<br>Hero Banner Contents: **new** `callout` (with a photo)<br>Footer: `footer` (band = light) |
| Price Drop Alert | `1:1742` | `price_drop` | A price-drop alert: a promo strip, then on a dark band the logo, a title, a short paragraph and a shop button above a product photo that fades into the band, then social icons and a light legal footer. | Promo Strip: `promo` (band = light)<br>Logo Section + Hero Banner Content: `hero_image` (band = black, paragraph under the title)<br>Pre Footer: `social` (band = light)<br>Footer: `footer` (band = light) |
| Blog No. 2 | `1:1777` | `blog_digest` | A wellness blog digest: a photo hero with a flush-left title and intro, four article rows that alternate photo side (tag, question title, paragraph, button), a titled list of three suggested reads with a button each, social icons, a wide logo with four category links, and a dark legal footer. | Hero Banner: `hero_background` (align = left)<br>Image Breaker: `image_text` (band = dark)<br>Header: `heading_text` (align = left)<br>Product Block: `image_text` (photo_width = 140)<br>Pre Footer: `social` (align = left)<br>Logo (artwork): `image`<br>Logo (links): `menu`<br>Footer: `footer` |
| Pre-Sale Announcement (A) | `1:1887` |  | A pre-sale teaser for a seasonal product: on a dark band the logo and a hand-lettered 'coming' title over a strip of three product photos, a short paragraph, a full-width button, social icons and a light footer. | Hero Image: `hero_image` (button optional)<br>Body: `heading_text` (band = dark)<br>CTA: `button` (band = dark)<br>Frame 42: `social`<br>FOOTER: `footer` (band = light) |
| Pre-Sale Announcement (B) | `1:1946` |  | A founder's pre-launch letter: the logo on a pattern, then cream ticket-shaped cards, each a big flush-left heading with paragraphs (welcome, when it launches, share it or keep it secret with a share button), a centered thank-you signed by the owner with a framed photo, then a footer with a contact line, email-frequency choices and legal links. | Header Logo: `logo_header`<br>Body header + Body Text: `heading_text` (align = left)<br>TRANSITION: `wave`<br>Body Header 2 + Body Text 2: `heading_text` (align = left)<br>TRANSITION: `wave`<br>Body Header 3 + Body Text 3: `heading_text` (align = left)<br>CTA: `button` (align = left)<br>TRANSITION: `wave`<br>Body Header 4 + Body Text 4: `heading_text`<br>Image: `image` (width)<br>TRANSITION: `wave`<br>Footer (contact): `heading_text`<br>Footer (rule): `divider`<br>Footer (frequency): `prefooter` (pills)<br>Footer (legal): `footer` (band = light) |
| Order Tracking Emails | `1:2002` |  | A shipping notification: a label strip, the logo, a photo hero saying the order is on its way, a short paragraph with a track-package button, the ordered items and the totals, then category links, pill links to help pages, a brand-story teaser with a round photo, social icons and the unsubscribe line. | banner: `promo`<br>Logo Header: `logo_header`<br>Hero Banner: `hero_background` (align = left)<br>Body: `heading_text` (align = left)<br>CTA: `button`<br>Product Block (title): `heading_text`<br>Product Block + Total: `order_summary` (photo_width = 230)<br>Menu: `prefooter`<br>Footer (pills): `prefooter` (pills)<br>Footer (story): `image_text`<br>Footer (icons): `social` (align = left)<br>Footer (legal): `footer` (band = light) |
| Brand Advocacy/Story | `1:2091` | `gratitude_letter` | A first-anniversary thank-you letter: logo and a 'note of gratitude' title framed by sun rays, a long letter with a pull quote and a sign-off, three team signatures with names and roles, and a dark footer with social icons and legal links, then a disclaimer. | Hero Banner (logo): `logo_header`<br>Hero Banner (title): `heading_text`<br>Body: `heading_text` (align = left) three times, the pull quote in the middle<br>Signature: `features` (rules = true)<br>Footer (icons): `social` (band = dark)<br>Footer (legal): `footer`<br>Footer (disclaimer): `footer` (band = white) |
| Review Request 1 | `1:2177` |  | A review request with a referral push: a full-width photo with the logo, a peach band with five stars, a playful title, a line of text and a leave-a-review button, a referral offer card (photo, give/get band, title, text, button), and a footer with the logo, a did-you-know box, links and legal lines. | Hero Banner: `image`<br>Body + CTA: `cta`<br>Divider: `divider`<br>Image reaker: `offer`<br>Divider: `divider`<br>Footer (logo): `logo_header`<br>Footer (did you know): `coupon` (solid border)<br>Footer (links): `prefooter`<br>Footer (legal): `footer` (band = light) |
| Review Request 2 | `1:2241` |  | A post-purchase review request: a photo hero asking whether the customer loves the product, a short paragraph, the purchased product with its name link, a leave-a-review button, social icons, then a footer with the logo, a product tagline between dashed rules, social icons again and the legal lines. | Hero Banner: `hero_background` (button optional)<br>Body: `heading_text`<br>Dynamic Block: `product_feature` (button optional)<br>CTA: `button`<br>Social Media: `social`<br>Footer (rule): `divider`<br>Footer (logo): `logo_header`<br>Footer (tagline): `heading_text`<br>Footer (icons): `social`<br>Footer (legal): `footer` (band = light) |
| Customer Milestone Emails | `1:2298` | `customer_milestone` | A loyalty milestone email: a photo hero welcoming the customer into a club, then on black two short sections, each a two-tone heading, a paragraph and a button (look back, share it), and a dark footer with social icons and legal links. | Hero Banner: `hero_background` (button optional)<br>Body + Body: `heading_text` (band = dark)<br>CTA: `button` (band = dark)<br>Body + Body: `heading_text` (band = dark)<br>CTA: `button` (band = dark)<br>Social Media: `social` (band = dark)<br>Footer: `footer` |
| Renewal Offers | `1:2353` |  | A membership renewal reminder: a photo fading into black with the logo, a heading saying the membership is almost up, a line of text, a turn-on-renewal button, the monthly price, and legal links on black. | Hero Banner (photo): `image`<br>Hero Banner (logo): `logo_header` (band = dark)<br>Body + CTA: `hero_text`<br>Body: `heading_text` (band = dark)<br>Footer: `footer` |
| Year-in-Review | `1:2384` |  | A year-in-review recap: a photo hero titled 'a year in review', a short intro, numbered chapters (new products and best sellers as alternating photo-and-quote rows, then team growth, a project, a collaboration, big wins and press mentions as photo cards with text or lists), a closing paragraph with a button, a follow-along heading with social icons, and a footer with links. | Hero Banner: `hero_background` (button optional)<br>Body: `heading_text` (align = left)<br>Image Breaker (chapter titles): `heading_text` (align = left)<br>Image Breaker (rows): `image_text`<br>Image Breaker: `image` (inset; then heading_text, align = left)<br>Image Breaker: `image` (inset; then heading_text, align = left)<br>Image Breaker: `image` (inset; then heading_text, align = left)<br>Body: `heading_text` (align = left)<br>CTA: `button`<br>Body: `heading_text`<br>Social Media: `social`<br>Footer (links): `prefooter`<br>Footer (legal): `footer` (band = light) |
| Special Day Promotions | `1:2482` |  | A holiday sale (a Mother's Day example): an arched photo with the logo and a round discount badge on a brand-colored band, a big serif sale title, a short line and a shop button, two small featured items with captions, and a light footer with social icons. | Hero Banner (photo): `image`<br>Hero Banner (text) + CTA: `hero_text`<br>Image Breaker: `image_pair` (separators)<br>Footer (legal): `footer` (band = light)<br>Footer (icons): `social` |
| Anniversary Emails (B) | `1:2529` |  | Marks a subscriber's anniversary with the service: a personal greeting and message, a four-step reminder of how the service works, a button to manage deliveries, then a help contact, social links, a brand tagline, a review score and app download links before the legal lines. | Header: `hero_background` (title and button optional)<br>Body Headline + Body Text: `heading_text`<br>Transition: `wave`<br>Image Breaker Headline: `heading_text`<br>Image breaker 1-4: `image_text`<br>CTA: `button`<br>Prefooter / Transition 2: `wave`<br>Prefooter / Frame 38: `heading_text` (band = primary)<br>Prefooter / Frame 42: `social`<br>Prefooter / Frame 39: `heading_text` (band = primary)<br>Footer / Frame 43: `heading_text` (stars as text)<br>Footer / Frame 44: `divider`<br>Footer / Frame 45: `social` (title, badge size)<br>Footer / Frame 5: `footer` |
| Early Bird Access | `1:2693` |  | Gives subscribers early access to a sale: a hero announcing early-bird access, the discount and its code, a photo collage and a wide photo with a shop button, three featured products each with a shop button, then a closing line, four selling points and four trust badges. | Hero Banner: `hero_background` (button optional)<br>Image Breaker / Text: `heading_text`<br>Image Breaker / Code: `coupon`<br>Image Breaker / Shape: `image`<br>Image Breaker / Put Image Here: `image`<br>Image Breaker / CTA Button: `button`<br>Header / zigzag: `wave`<br>Header / title: `heading_text`<br>Product 1-3: `product_feature` (text_first = true)<br>Frame 12864: `heading_text`<br>Frame 12865: `menu`<br>iCON: `features` (columns = 4) |
| Giveaway Announcement | `1:2761` |  | Announces a giveaway run with a partner brand: both logos, a photo with the giveaway title and an enter button, how it works, the prizes it includes, a guide to read, products to explore, then a closing paragraph, icons and the legal lines. | Logo: **new** `logo_bar`<br>Hero Banner / photo: `image`<br>Hero Banner / text: `hero_text`<br>Body: `heading_text`<br>Body: `heading_text`<br>Image Breaker: `image_pair`<br>Body: `heading_text`<br>Pre-Footer / photo: `image`<br>Pre-Footer / text: `heading_text`<br>Pre-Footer / CTA BUTTON: `button`<br>Frame 12863 / title: `heading_text`<br>Frame 12863 / grid: **new** `image_mosaic`<br>Body: `heading_text`<br>Logo: `logo_header`<br>Frame 12116: `features` (columns = 4)<br>Additional: `footer` |
| How To Guides | `1:2847` |  | Introduces a beginner's guide: a hero asking if the reader is new to the subject with a get-started button, two guide items with a recommended-products button, a subscribe prompt, then logo, menu links, icons and the legal lines. | Logo: `logo_header`<br>Hero Banner: `hero_background` (logo optional)<br>Image Breaker / title: `heading_text`<br>Image Breaker / Title 1-2: `image_text`<br>Image Breaker / Frame 12116: `cta`<br>Pre-Footer: `cta`<br>Footer / LOGO: `logo_header`<br>Footer / Frame 12115: **new** `link_stack`<br>Frame 12116: `features` (columns = 4)<br>Additional: `footer` |
| Subscription Upsell | `1:2918` |  | Invites a customer to join a paid membership: a hero with the promise, what the membership is, four benefits and a join button, then a lighter alternative (book a single service) and a footer with links, app download, a tagline and the legal lines. | Hero Banner: `hero_background` (button optional)<br>Hero Banner / wave: `wave`<br>Body: `heading_text` (band = primary)<br>Image Breaker: `steps` (icon per item)<br>CTA: `button`<br>Transition: `wave`<br>Image Breaker: `image_text` (button)<br>Footer / icons: `social`<br>Footer / links: **new** `link_stack`<br>Footer / app: `social` (title, badge size)<br>Footer / tagline: `heading_text`<br>Footer / legal: `footer` |
| Site Abandoned | `1:3018` |  | Brings back a visitor who browsed without buying: a playful compliment on their taste, a short message and a shop button, four products with prices and shop buttons, a second shop button, then links and the legal lines. | Logo Header: `logo_header`<br>Menu: `menu`<br>Hero Banner: `image`<br>Body / Header + Divider: `section_title`<br>Body / Body: `heading_text`<br>CTA: `button`<br>Product Block: `products_two`<br>CTA: `button`<br>Footer / Transition: `wave`<br>Footer / links: `prefooter`<br>Footer / legal: `footer` |
| Product Education Emails | `1:3093` | `product_education` | Teaches about a product line: a hero photo, an eyebrow, heading and paragraph with a shop button, a full-width content image, a personal thank-you with three recommended products and a more button, then link rows, logo and the legal lines. | Logo Header: `logo_header`<br>Hero Image: `image`<br>Body: `heading_text` (align = left, band = sand)<br>CTA: `button` (band = sand)<br>Divider: `divider` (band = sand)<br>Content: `image`<br>Product Block / Frame 12245: `heading_text` (band = sand)<br>Product Block / Product Block: `products_two` (three cards, no buttons)<br>Product Block / CTA: `button` (band = sand)<br>Footer / links: `prefooter`<br>Footer / Logo: `logo_header` (band = sand)<br>Footer / legal: `footer` twice, copyright on sand and legal lines on white |
| Problem Acknowledgment/Resolution | `1:3152` |  | Answers a customer worry head-on with a two-line 'X? No problem.' headline, explains it with a shop button, then makes it right with a discount code card over a photo, and closes with a dark branded footer. | Logo Header: `logo_header`<br>Hero banner / Frame 12249: `hero_text`<br>Hero banner / Image: `image`<br>Hero banner / Promo: `coupon`<br>Hero banner / Promo button: `button`<br>Footer / Logo Header: `logo_header`<br>Footer / Frame 12250: `heading_text` (band = ink)<br>Footer / Frame 42: `social`<br>Footer / Frame 12251-12253: **new** `link_stack`<br>Footer / Frame 12254: `footer` |
| Post-Holiday Clearance Sales | `1:3264` |  | Clears post-holiday stock: a teaser line, a logo bar with a free-shipping promise, an extra-off clearance banner with an access button, four rows pairing a styled photo with a discounted product, category tiles and links, then terms, social links, legal links and the logo. | Body: `view_in_browser`<br>Frame 12323: **new** `logo_bar`<br>Hero Banner: `hero_text`<br>Product Block / PB1-PB4: `image_text` (button)<br>Frame 12327: `features` (columns = 3, no icon)<br>Frame 12232: **new** `link_stack`<br>Frame 12328: `footer`<br>Frame 12329: `social` (title)<br>Frame 12289: `footer`<br>Frame 12331: `logo_header` |
| Urgent Flash Sales | `1:3383` |  | Announces a short flash sale: logo, a free-shipping strip, a hero with the discount, two shop buttons (men, women), terms and the end time, then six discounted products and a dark footer. | Hero Logo: `logo_header`<br>Hero Strip: `promo`<br>Hero  Banner: `hero_background` (buttons list)<br>Product Block x3: `products_two` (button optional)<br>Footer / Frame 12338: `logo_header`<br>Footer / links + address: `footer` |
| Exit Intent Discounts | `1:3439` |  | Catches a visitor who left with a big first-order discount: a logo bar with a get-started link, a playful 50%-off headline, a short pitch, the code inline, a button, a brand tagline and a footer. | Hero Logo + Divider: **new** `logo_bar`<br>Hero Image: `image`<br>Body: `heading_text` (band = mist)<br>Body: `coupon` (inline = true)<br>CTA: `button`<br>Pre-footer: `heading_text`<br>Footer / Frame 12329: **new** `logo_bar`<br>Footer / Frame 12348: `footer` |
| Newsletter Sign-Up Welcome Emails | `1:3495` |  | Welcomes a new subscriber: a welcome title and photo, a tagline with a first-order discount button and its code, the brand story, three brand values each with a button, and a quiz invitation before the footer. | Hero Banner Logo: `logo_header`<br>Hero Banner Header: `heading_text`<br>Hero Banner: `image` (inset = true)<br>Body Header + CTA: `cta`<br>Code: `heading_text`<br>Body: `offer` (photo and band optional)<br>Transition: `wave`<br>Image Breaker Header: `heading_text`<br>Image Breaker x3: `offer` (photo and band optional)<br>Body Header + CTA: `cta`<br>Footer / Frame 12329: `social`<br>Footer / legal: `footer` |
| Social Media Highlight | `1:3583` |  | Asks subscribers to follow the brand on social media: a logo bar with a shop button, a photo with the follow-us headline, a short pitch, one button per network and a footer. | Hero Headline: **new** `logo_bar`<br>Hero banner: `hero_background` (align = left, logo and button optional, inset)<br>Body: `heading_text` (align = left)<br>CTA x2: `button`<br>Footer / Frame 12342: `divider`<br>Footer / Frame 12329 logo: `logo_header`<br>Footer / Frame 12329 icons: `social`<br>Footer / legal: `footer` |
| Referral Reminder Emails | `1:3623` |  | Reminds customers to refer a friend: a bold question with a refer button on color above a lifestyle photo, three short paragraphs and the button again, a brand tagline band and the footer. | Hero Banner: `hero_image`<br>Body / text: `heading_text`<br>Body / button: `button`<br>Image Breaker / curve: `wave`<br>Image Breaker / tagline: `heading_text`<br>Footer / logo: `logo_header`<br>Footer / icons: `social`<br>Footer / legal: `footer` |
| Affiliate Program Promotion | `1:3664` |  | Recruits affiliates: a headline inviting readers to join the program, an image collage, why it is worth it, a sign-up button, a checklist of benefits, a quote from an affiliate, social links and the brand sign-off. | Logo: `logo_header`<br>Hero Banner Headline: `heading_text`<br>Hero Banner: `image`<br>Body: `heading_text` (align = left)<br>CTA Button: `button`<br>Image Breaker: `steps` (icon per item)<br>Testimony: `testimonial` (layout = card)<br>Footer / follow: `social` (title)<br>Footer / sign-off + unsubscribe: `footer` |

## Adaptations

Each item is a section whose design asks for something a rule rejects, with the rule and the change that replaces it. The rules never relax for a template. Under a template the library has built, the items marked **Built** say what differs from the frame.

Every library template paints with the library brand. Its fonts, type sizes, button shapes and colors come from `brand.toml` and `base.html`, so the type is smaller than the kit's 22 px body text and the buttons are not pills. The kit's grey placeholder photos become sample images, and a photo with text on it is the dark sample `hero-dark.jpg`.

### Teaser

- Hero Banner: text on photo: hosted background URL with a color fallback (C3); the inset rounded card becomes square in Outlook
- Product Release Date: text on photo (C3), and `hero_background` can appear once per email: the card becomes a `callout` on a band color

### Flash Sale

- Open In Browser: gradient strip: use one solid brand color (C3, B1)
- Open In Browser (lettering + photo): rotated outlined display type and overlap (C2, B2): bake the lettering and the photo into one image
- Open In Browser (offer copy): the right-column offset only exists because of the overlapping lettering: center the copy under the image

### Sale Email

- Frame 115: oval mask and outline: bake the shape and stroke into the image on the band color
- Frame 115 (photo): pill mask and outline: bake them into the image

### Trending Products

- Hero Banner (photo): oval mask and outline: bake them into the image
- Frame 118: white text on light tan fails contrast (A1): darken the tile color or use dark text

### Product Features

- Hero banner: text on photo: hosted background URL with a color fallback (C3)
- Image Breaker Image (photo): markers positioned over the photo (C2): bake them into the image
- Image Breaker Image (products): number badges over the photos: bake them into the images

### Gift Card

- **Built.** The header strip, logo beside the menu, becomes the logo flush left with the menu under it: `logo_bar` does not exist yet.
- **Built.** The headline sits over the dark sample photo in white, since the light checkerboard of the frame has no text color that passes A1.
- **Built.** The decorative shapes under the footer are dropped: no sample wave joins white to white.
- **Built.** The five perks use the library's line icons, with a new gift icon.
- Hero banner: text on photo: hosted background URL with a color fallback (C3)

### Customer Spotlight

- Mask group (title): script accent word (B2): set it in the heading font's italic; gradient background (C3): use a solid brand color
- Mask group (quote): white text on the light part of the gradient fails contrast (A1)

### Brand Storytelling

- Frame 12161 (logo): gradient background (C3): use one solid brand color
- Frame 12161 (photo): photo overlapping a decorative shape (C2): bake the shape, photo and background into one image
- Pre-Footer (values): gradient background (C3): use one solid brand color

### Holiday Greetings

- **Built.** The logo band is `primary` and the message band `ink`: the brand roles closest to the frame's dark green and grey green.
- **Built.** The two promises are `steps` with an icon each, between two `divider`. The frame's rule between the two promises and the one under the social icons are dropped.
- **Built.** The one-line promise sits level with the top of its icon, not centered on it.
- Hero Image: text on photo: hosted background URL with a color fallback (C3)

### Discount Reminder

- Menu: display font (B2): use the heading stack; white on mustard fails contrast (A1)
- Hero Image (headline): outlined type with shadow (B2) and overlap with the photo (C2): set it above the photo in the heading font, or bake headline and photo into one image

### Countdown Timer Emails

- **Built.** The light blue band becomes `primary`, so white text passes A1, and the orange buttons become the accent button with ink text.
- **Built.** The countdown keeps the library's boxed numbers, not rings.
- **Built.** The four promises use the library's line icons. The members' banner is `image_text` with a sample photo in place of the phone illustration, kept inside the band.
- **Built.** The second button sits under the photo instead of overlapping it (C2).
- Body: white on light blue fails contrast (A1): darken the band
- Countdown: static numbers: for a ticking timer, put a timer service's GIF in an image block
- Body: white on light blue (A1)
- CTA: white on orange fails contrast (A1)
- Image Breaker (button): overlap (C2): place the button under the photo
- Pre-footer: the illustration breaks out of the band at the top and right (C2): crop it to the band; direction = rtl

### Benefits Emails

- Hero Banner (photo): labels and leader lines over the photo (C2): bake them into the image, or list the labels under it

### Testimonials

- Hero Banner (title): quote glyphs overlap the arc and the button (C2): drop them or bake arc and glyphs into a wave image above; the offset shadow becomes a plain border
- Image Breaker (3 review cards): quote glyphs overlap the card corners (C2): drop them or put one glyph inside the card above the stars
- Button: offset shadow: use a plain border
- Transition: gradient background: use a solid color
- Pre-Footer (photo): the kit puts the button over the photo's lower third: place it under the photo (next section) or use hero_background with a hosted URL

### FAQ

- Hero Banner: outlined sticker type is decorative (text stroke): set a plain bold heading or bake it into an image; the straddling button and the tilted sticker over the photo need positioning (C2): keep the button on the band, bake the sticker into the photo
- Image Breaker 1 (Q&A): Q:/A: stickers overlap the boxes and the boxes are offset (C2): write 'Q:' and 'A:' inline, keep the boxes full width
- Image Breaker 1 (recommended product): sticker overlaps the photo corner (C2): bake it into the photo or write it as an eyebrow above the name
- Image Breaker 4 (pro tip): card, photo, sticker and button overlap (C2): stack them as the offer card does (photo, 'Pro tip' band, text, button)

### General Promotions

- Hero Banner: thumbnails are scattered with absolute positions (C2) and the title sits on a pattern: put logo and title on a solid band, bake collage, captions and the bottom wave into one image
- Text: gradient background: use a solid color
- Headline + Text: gradient background: use a solid color

### Event Invitation

- Hero Banner (photo header): text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook; tilted stickers overlap the title (C2): drop them or bake into the photo; display serif must be the headings stack (B2)
- Hero Banner (invitation card + button): card overlaps the photo edge (C2): start it below the photo

### Thank You Email

- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook; bake the bottom arc into the photo or follow with a wave
- IMAGE BREAKER (gift card): rotation and shadow must be in the image itself
- Category: label over the tile image: put it as a caption under the tile, or bake it into the image

### Referral Program Promotion

- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook

### Reward/Points Program

- Frame 12055: the fade into white must be in the photo; the block pads the photo, so the edge bleed is lost
- Footer (legal, with logo): text over a background photo (C3): use a solid dark band, or a hosted background with a color fallback

### Newsletter Recap

- Frame 12076: box shadow does not render in most clients: drop it or use a thin border

### Mythbuster

- **Built.** The "Truth" pill becomes a bold label on its own line.
- **Built.** The closing button is the full-width call-to-action button of `cta`.
- Footer (legal): about 8 px text and a blue link on black: raise to 12 px and use a role that passes contrast (A1)

### Did You Know Content

- Hero Image (logo): the kit puts the logo over the photo: place it on a band above (or hero_background with title and button optional and a hosted URL)
- Hero Image (photo): bake the accent rule into the photo or add a divider in the accent role
- Image Breaker: the photo crosses two band colors: bake both colors into the image

### Product Comparison

- Hero Banner (Frame 12392 + Hero Image): bake the white curve into the photo or follow with a wave
- Image Breaker (comparison): the heading above the table goes in a heading_text (the block has no title); pill heads and stems need images or a class, not inline style

### Product Launch Countdown

- Image Breaker 1: the kit's photo is 520 px wide; the block caps it at 400

### Cart Abandonment Reminder

- Footer (legal): text around 8 px: raise to 12 px

### Contest Invitation

- Image Breaker (prizes): rotated cards need transforms: set them straight, or bake the tilted pair into one image; the two labels go in heading_text blocks above and below
- Image Breaker (photo fade): the title starts over the fade: keep the fade in the photo and start the text below it
- Transition: the notch is a vector shape: drop it, or ship the ornament as a wave image
- Image Breaker (mosaic): buttons sit over the photos (C2): place each button under its photo, or bake it into the image and link the image

### Bundle Offers

- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook
- Image Breaker (5 bundle cards): portrait and badge overlap the photo (C2): move the portrait beside the bio, bake the badge into the photo; gradient background behind all five: use solid bands

### Blog Content Highlight (A)

- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook
- Image Breaker 1: the card overlaps the photo (C2): place them side by side, direction rtl
- Image Breaker 2: overlap (C2): side by side, direction ltr
- Image Breaker 3: overlap (C2): side by side
- Image Breaker 4: overlap (C2): side by side
- Image Breaker 5: overlap (C2): side by side
- Pre-footer (photo tiles): text over photos: move title and line into the captions under each photo

### Abandoned Cart

- **Built.** The cart item keeps the `order_summary` layout: an 80 px thumbnail and the total on the right, not a large photo beside the name.
- **Built.** The rules above and below the links are the library's solid `divider`, not dashed.
- Pre Footer (socials): icons drawn as vectors: export PNG icons

### Order Confirmation

- Body (payment info): light grey label on white: check contrast
- Body (nav links): light grey links on white: check contrast
- Footer: very light grey text: contrast
- Credit Footer: no unsubscribe link anywhere and the address sits in the column strip: rule L1 needs both in the footer, so add them here

### Shipping Confirmation

- Divider: ornament is a vector: export a PNG
- Footer (follow us): icons drawn as vectors: export PNG icons
- Footer (legal): no unsubscribe link: rule L1 needs one; tiny light grey text: contrast

### Customer Feedback Request

- Hero Banner: text on photo: hosted background URL and a color fallback (hero_background); sans caps eyebrow plus serif display plus serif body: keep to the two brand stacks

### Survey Invitation

- Image Breaker / Text 1: decorative PNG stickers overlap the card edges (1:1373, 1:1376, 1:1379): drop them or place them in the flow; the checkered offset shadow under the buttons needs overlap: use a plain outlined button; serif, monospace and sans faces: keep to two stacks
- Footer / Social Icons: icons drawn as vectors: export PNG icons

### Birthday Emails

- Logo Header + Hero Banner: condensed display headline, geometric body and a third face on the button: keep to the two brand stacks
- Footer (icons): icons drawn as vectors: export PNG icons

### Special Offers

- **Built.** The two-by-three grid is three `products_two` rows with ids. The button is the primary button.
- **Built.** The category tiles carry their label under the photo, in the caption.
- **Built.** The row of promises is `features` with labels only, no icons, instead of `menu`.
- **Built.** The slogan and contact lines sit in a `heading_text` on sand, and the copyright lines go in the white `footer`.
- Hero Banner: soft glow (text shadow) behind the type: drop it
- Category: label over photo: put the label under each tile or bake it into the image
- Footer (icons): icons drawn as vectors: export PNG icons

### Back in Stock

- **Built.** The thin rules beside the logo are dropped.
- **Built.** The title is white on the dark sample photo, where the kit has black text on a light photo.
- **Built.** The small square image in the pre-footer is dropped. Its links stack flush left.
- Hero Banner: text on photo: hosted background URL and a color fallback (hero_background)

### Low Inventory Alerts

- Hero Banner and Body Text: text on photo: hosted background URL and a color fallback (hero_background); the panel looks translucent: give it a solid color

### New Product Launch

- Hero Banner (art): overlapping type, photo and a rotated badge: bake them into one image and carry the words in the alt text
- Hero Banner: text on photo: hosted background URL and a color fallback (hero_background); justified text: set it flush left
- IB: the connecting line runs across rows: bake each segment into its icon image

### Seasonal Collection Highlight

- HERO: text on photo: hosted background URL and a color fallback (hero_background); rotated title: set it straight or bake it into the photo
- FOOTER (tagline): text on a curve: bake it into an image

### ICYMI

- Hero Banner: photo overlaps the headline and the diagonal is a vector: put the headline above and bake the diagonal into the photo

### Limited-Time Discounts

- Frame 12068: text on photo: hosted background URL and a color fallback (hero_background)
- Frame 12065: for a live timer, a timer service image in an image block

### Holiday Promotions

- Hero: text on photo: hosted background URL and a color fallback (hero_background)
- Pre footer: icon is a vector: export a PNG

### Anniversary Emails (A)

- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)
- Image Breaker: connector line and dots are absolute vectors crossing the bands: draw them as a bordered narrow column with a dot image per row, or drop them

### Blog Content Highlight (B)

- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)
- Product Block 1: the card overlaps the photo by about 40 px: set them side by side (direction rtl), the card as the text cell
- Product Block 2: card overlaps the photo: side by side, direction ltr, with an id
- Product Block 3: card overlaps the photo: side by side, with an id
- Product Block 4: card overlaps the photo: side by side, with an id
- Product Block 5: card overlaps the photo: side by side, with an id
- Frame 12119: text over the photos: move title and line into the captions under each photo

### Exclusive Access Email

- Stripes Background + Logo Section: the stripes are a layer under both the logo and the card: a hosted CSS background with a color fallback on a wrapper of both, or a flat color
- Hero Banner Contents: sparkle images overlap the title (absolute): drop them or bake them into the photo; grey button with white text is low contrast

### Price Drop Alert

- **Built.** The product photo is the sample photo without the fade into the band.
- **Built.** The button is the primary button, not a light pill.
- Logo Section + Hero Banner Content: the photo carries a gradient cover: bake the fade into the image

### Blog No. 2

- **Built.** The logo sits flush left with the header text, and the intro sits under the title instead of at the foot of the photo.
- **Built.** The suggested reads use the 260 px photo of `image_text`, where the kit has 140 px thumbnails.
- **Built.** The wide logo artwork is the sample logo in `logo_header`.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)
- Product Block: grey byline on black is low contrast

### Pre-Sale Announcement (A)

- Hero Image: decorative display type and a brush stroke overlapping the title: set the title in the headings stack, drop the stroke or bake it into the photo; make the three photos one 600 px image
- FOOTER: three families (display, monospace, serif): keep two stacks, headings and body

### Pre-Sale Announcement (B)

- Header Logo: image behind the logo: flatten logo and pattern into one image, or use a flat band color
- CTA: white on orange is borderline contrast

### Order Tracking Emails

- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); or move the title under the photo as heading_text
- Footer (story): round photo: bake the circle into the image (Outlook ignores border-radius)

### Brand Advocacy/Story

- **Built.** The sun rays behind the title are dropped, and the title is set in the heading font in ink.
- **Built.** The pull quote is an italic `h2` in its own `heading_text` between two parts of the letter.
- **Built.** The three signatures are `features` with `rules = true`: each signature image becomes a 48 px portrait above the name and role.
- Hero Banner (logo): thin sun-ray lines fan out behind logo and title (vector mask): bake them into a hosted background image or drop them

### Review Request 1

- Hero Banner: logo over the photo: put a logo_header above the photo, or bake the logo in
- Body + CTA: stars are decoration: set them as star characters in the title

### Review Request 2

- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); decorative display face: use the headings stack
- Footer (tagline): decorative display face: use the headings stack

### Customer Milestone Emails

- **Built.** Each heading's second line, in an accent color in the kit, takes the band's text color like the first line.
- **Built.** The social icons are the light sample icons, so they read on the dark band.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)

### Renewal Offers

- Hero Banner (photo): fade is a gradient cover: bake it into the photo
- Hero Banner (logo): logo overlaps the photo: place it in its own black band under the photo

### Year-in-Review

- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); tan display type on a light photo is low contrast
- CTA: white on copper is low contrast
- Body: copper on light grey is low contrast

### Special Day Promotions

- Hero Banner (photo): arch mask, logo and badge overlap the photo: bake the arch and badge into the image, or move the logo to a logo_header above and the offer into the title

### Anniversary Emails (B)

- Header: text on photo: hero_background with a hosted https URL and a color fallback; or logo_header above an image
- Image breaker 1-4: number badge overlaps the photo: bake the number into the photo or open the text with the number; bake the blob mask into each image
- Prefooter / Frame 39: photo corners around the band are overlap: drop them or make the band one image (wave) above the tagline

### Early Bird Access

- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback; the scalloped edge needs a wave image under the hero
- Image Breaker / Shape: shape mask: bake the arches into one image with background-colored corners
- Product 1-3: shape masks: bake each shape into the product photo

### Giveaway Announcement

- Image Breaker: rotation and overlap: set the two cards straight, side by side; the polaroid frame becomes the caption band
- Pre-Footer / photo: the title overlaps the fade: bake the fade into the photo and start the title below it
- Frame 12863 / grid: buttons over photos: place each button under its photo

### How To Guides

- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback
- Image Breaker / Title 1-2: blob-shaped card: needs an image background; use a plain tinted band instead
- Pre-Footer: blob-shaped card: plain tinted band instead

### Subscription Upsell

- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback

### Site Abandoned

- Hero Banner: script and decorative display type: export the lettering as an image with alt text, or set it in hero_text with the heading font

### Product Education Emails

- **Built.** The thick rule under the button is the library's thin `divider` on sand.
- **Built.** The three products are `products_two` with three cards and no buttons. Their names keep the card's heading style, not small capitals.
- **Built.** The two link rows become one `prefooter` row, and the copyright sits in a `footer` on sand above the white legal lines.

### Problem Acknowledgment/Resolution

- Hero banner / Image: the promo card sits on the photo: place it below the photo
- Footer / Frame 12251-12253: brush-stroke underline is an image: use a plain rule or bake it into each link image

### Post-Holiday Clearance Sales

- Hero Banner: CSS gradient fails in Outlook: a solid brand color, or a hosted gradient image with a color fallback
- Product Block / PB1-PB4: staggered offset is positioning: top-align both columns

### Urgent Flash Sales

- Hero  Banner: text on photo: hero_background with a hosted https URL and a color fallback
- Product Block x3: monospace price face is outside the two font stacks: use the body font

### Exit Intent Discounts

- Hero Image: rotated, absolutely placed letters: export the lettering as an image with alt text, or set a straight title in hero_text

### Newsletter Sign-Up Welcome Emails

- Image Breaker x3: circle notch and photo overlap the card edge: drop the notch (or put an icon inside the card) and stack the photo above

### Social Media Highlight

- Hero banner: text on photo: hero_background with a hosted https URL and a color fallback

### Affiliate Program Promotion

- Hero Banner: overlap and gradients: flatten the collage into one image
