# Figma kit catalog

This page maps a licensed Figma kit of email templates onto the library. Each row is one laid-out template of the kit, with its node id in the kit's Figma file, the library template built from it, its purpose and its sections from top to bottom. Each section names the library block that draws it. A library template built from the kit says `# Kit frame <id>.` in its opening comment, and a test keeps that comment and this table in step.

The library takes the structure and the design of each template: the order of the sections, the composition, the type hierarchy, the spacing and the kind of each module. It takes none of the brands that appear in the kit. Texts are rewritten for the sample brand, Example Co., and every image is a sample made with `tools/make-example-images.py` or drawn in SVG. No asset of the kit enters the repo.

## How to read a section

- `heading_text` is an existing block that draws the section with its content changed.
- `heading_text` (align = left) is an existing block that needs one more field or option. The field in parentheses is the proposal. The block work decides the final field.
- `logo_bar`, `link_stack`, `callout`, `text_columns` and `image_mosaic` were added to the library for the kit. [New blocks](#new-blocks) lists them.

## Templates not imported

The kit has 80 laid-out templates. Two repeat another template, so 78 are imported:

- `1:1656` (Abandoned Cart) is the same frame as `1:936`.
- `1:3731` (Blog #2) is the same design as `1:1777` (Blog No. 2).

## New blocks

Five sections of the kit had no block, so the library now has five more. Sections that are the same module with another look share one block. `python3 -m eeb blocks` lists their fields.

- `logo_bar`: the logo on the left and, on the right, a small text area for links or a short message, and an optional button in the accent style. It stacks and centers on a phone. It covers logo-and-menu headers, account bars and footer rows. 12 sections in 9 templates.
- `link_stack`: links stacked one per row in one editable area, with `style = "rules"` (thin lines between the rows) or `style = "pills"` (each link an outlined pill in the color of its text). For categories and help pages above the footer. 10 sections in 10 templates.
- `callout`: an inset rounded panel on the block's band, with its own color chosen with `panel`, holding a heading and text, an optional photo and an optional full-width button. A dark panel turns its text white. For referral boxes, survey cards, gift panels and an access card. 8 sections in 6 templates.
- `text_columns`: two text areas side by side, such as billing and shipping addresses or who a bundle is for beside what is inside it. It stacks on a phone. 4 sections in 3 templates.
- `image_mosaic`: one tall photo beside two stacked photos, each with a button under it. It stacks on a phone. 2 sections in 2 templates.

Options that no built template needs yet are left out until one does: a thin rule under `logo_bar` (the `divider` block draws one), left alignment for `link_stack`, and a rule between the columns or a flush-right column for `text_columns`.

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
- The library's sample icons are drawn in the primary color, so the templates keep icon rows on light bands where the kit has dark ones.
- The sample images have no app store badges, review site badges, partner logos or waves beyond ink to white and sand to ink. The templates replace them with text or drop them, as their **Built** notes say.

## Templates

| Kit template | Figma | Library template | Purpose | Sections, top to bottom |
|---|---|---|---|---|
| Teaser | `1:5227` | `product_teaser` | A product teaser: it builds anticipation with a headline over a photo, says something exciting is coming, gives the release date with a reminder button, invites a first purchase, then offers quick links, social icons and the footer. | Open In Browser: `view_in_browser`<br>Hero Banner: `hero_background` (logo, no button)<br>Heading + Text: `heading_text`<br>Line: `divider`<br>Product Release Date: `callout` (align = left, on a band, not on a photo)<br>Line: `divider`<br>Heading + Text: `heading_text`<br>Button: `button`<br>Line: `divider`<br>Menu: `features` (two items with icons)<br>Line: `divider`<br>Menu: `social`<br>Line: `divider`<br>Text + Menu: `footer` (band = white) |
| Flash Sale | `1:5295` | `flash_sale_codes` | A 48-hour flash sale: a hero with large sale lettering, the main offer, its code and a button, then three product offers each with a code and a button, then a footer with social icons, subscription line, contact rows and address. | Open In Browser: `logo_header` (band = black)<br>Open In Browser: `promo` (band = accent)<br>Open In Browser (lettering + photo): `image` (band = black, width, radius)<br>Open In Browser (offer copy): `hero_text` (band = black)<br>Open In Browser (fine print): `heading_text` (band = black)<br>Products: `product_feature` (band = mist, three uses between white spacers)<br>Text: `logo_bar`<br>Text (subscription line): `heading_text` (align = left)<br>Menu: `steps` (an icon per item)<br>Text + Text: `footer` (align = left) |
| Sale Email | `1:5377` | `holiday_sale` | A holiday sale announcement: the sale name, offer and button, a large oval photo, a second short message with a pill-shaped photo and button, then a brand footer with logo, address, social icons and unsubscribe. | Logo: `logo_header` (band = primary)<br>Heading: `hero_text` (band = primary)<br>Frame 115: `image` (band = primary, width, radius)<br>Heading: `heading_text` (band = primary)<br>Frame 115 (photo): `image` (band = primary, width, radius)<br>Frame 115 (button): `button` (band = primary, style = light)<br>Line: `divider` (band = primary)<br>Text: `logo_header` (band = primary)<br>Menu: `social` (band = primary, light icons)<br>Text + Text: `footer` (band = primary, address first) |
| Trending Products | `1:5419` | `whats_new_trending` | A what's-new email: a hero with an oval photo, short intro and button, a checkerboard of labeled photos, a framed feature photo with a link, a code strip, a grid of six trending products, VIP perks, a pay-later strip, and the footer. | Hero Banner (logo): `logo_header` (band = sand)<br>Hero Banner (photo): `image` (band = sand, width, radius)<br>Hero Banner (copy): `heading_text` (band = sand)<br>Hero Banner (button): `button` (band = sand)<br>Image Breaker: `image_text` (band = line, three uses, alternating)<br>Frame 116 (photo): `image` (band = sand, width, space)<br>Frame 116 (link): `heading_text` (band = sand)<br>Heading: `promo` (band = primary)<br>Text: `heading_text`<br>Text + Text: `image_pair` (three photos, two uses)<br>Frame 138 (title): `heading_text` (band = line)<br>Frame 138 (perks): `features` (band = line, four items with icons)<br>Frame 118: `features` (band = line, three items with icons)<br>Frame 139: `promo` (band = line)<br>Menu: `social`<br>Text: `footer` (band = white) |
| Social Proof | `1:5742` | `press_roundup` | A press roundup: the logo, a 'press knows best' title, four rows that pair a photo with a press outlet's logo and a short quote, then a brand footer with links and the legal line. | Logo: `logo_header` (align = left)<br>Header Text: `heading_text`<br>Image Breakers: `image_text` (four uses, alternating, band = mist on the first and third)<br>Pre-Footer: `logo_bar` (band = mist)<br>Blank space: `spacer`<br>Footer + All rights reserved text: `footer` (band = mist) |
| Welcome Email | `1:5666` | `welcome_discount` | A welcome email: a discount strip, a header with logo and categories, a big photo, a welcome title with the discount line and a button, a short intro, a second photo with a titled link, four product picks, and a footer with account, store, category and social links. | Promo strip: `promo` (band = mist, align = left)<br>Header Strip: `logo_bar`<br>Hero Banner Image: `image`<br>Header Text + rule: `section_title`<br>Sub Heading: `heading_text`<br>CTA button: `button` (style = light, width)<br>Body Text: `heading_text`<br>Image Breaker Image: `image` (width, space)<br>Header Text: `heading_text`<br>Product Block (title): `heading_text`<br>Product Block (grid): `image_pair` (two uses)<br>All rights reserved text: `logo_bar` (band = black)<br>Pre-Footer: `prefooter` (align = left) and `social` (align = left)<br>Divider: `divider`<br>Footer: `footer` (align = left) |
| Product Features | `1:5580` | `shop_the_look` | A product launch: logo, menu and a shipping strip, a big left-aligned title and button over a photo, a 'get the look' intro, a shoppable photo with four numbered products, more picks, and a footer. | Logo: `logo_header`<br>Header Strip: `menu` (band = white)<br>Header Strip: `promo` (band = line)<br>Hero banner: `hero_background` (align = left, button, no logo)<br>Header Text: `heading_text` (align = left)<br>Image Breaker Image (photo): `image` (width, radius)<br>Image Breaker Image (products): `products_two` (band = white, two uses)<br>Product Block (title): `heading_text`<br>Product Block (grid): `image_pair` (two uses)<br>Pre-Footer: `prefooter` (band = white)<br>Footer: `footer` (band = white) |
| Gift Card | `1:5525` | `gift_card` | A gift card push: a browser link, a header with logo and menu, a short headline over a big photo, a paragraph with a gift card button, five service perks, then a footer with social icons, policy links, legal lines and a decorative shape. | Promo Strip: `view_in_browser`<br>Header Strip: `logo_bar`<br>Hero banner: `hero_background` (no logo, no button)<br>Body Text (paragraph): `heading_text`<br>Body Text (button): `button`<br>Body Text (perks): `features` (five items)<br>Footer (social): `social` (title)<br>Footer (links): `prefooter`<br>Footer (legal): `footer` |
| Customer Spotlight | `1:5798` | `customer_transformation` | A customer before-and-after story: the logo, a title with one accented word and a short intro, two photos side by side, and the customer's quote. | Hero Logo: `logo_header`<br>Mask group (title): `heading_text` (band = line)<br>Mask group (photos): `image_pair` (band = line, captions Before and After)<br>Mask group (quote): `testimonial` (band = line, with a portrait)<br>Footer: `footer` (band = white) |
| Behind The Scenes Content | `1:5819` | `behind_the_brand` | A behind-the-brand video episode: a shipping strip and browser link, two logos and a menu, a photo, the episode title and teaser with a watch button, then social links, a site link, a category list, a review score and the footer. | Header Strip: `promo` (band = mist)<br>Link: `view_in_browser`<br>Transition: `divider`<br>Frame 12134 + Frame 12135: `logo_header`<br>Menu: `menu` (band = white)<br>Hero Image: `image` (width, space)<br>Header + Header + Body + Body: `heading_text` (band = mist)<br>CTA: `button` (width)<br>Social Media: `menu` (band = white)<br>Link: `heading_text`<br>Footer (category list): `link_stack`<br>Footer (review score): `heading_text`<br>Footer (legal): `footer` (band = white) |
| Company Updates | `1:5911` | `quarterly_newsletter` | A quarterly newsletter: an issue label and logo, an intro, two new-release articles, two 2×2 galleries with captions, a link line, a tips article, three more articles, and a stay-tuned close. | Header: `view_in_browser`<br>Logo: `logo_header` (band = black)<br>Body: `heading_text` (band = black)<br>Header: `heading_text` (band = black)<br>Image + Body: `image` (band = black, width, radius) and `heading_text` with a link<br>Image + Body: `image` (band = black, width, radius) and `heading_text` with a link<br>Transition: `divider` (band = black)<br>Header: `heading_text` (band = black)<br>Image breaker 1 + Image Breaker 2: `image_pair` (band = black, two uses)<br>Transition: `divider` (band = black)<br>Header: `heading_text` (band = black)<br>Image Breaker 1 + Image Breaker 2: `image_pair` (band = black, two uses)<br>Transition: `heading_text` (band = black)<br>Body: `heading_text` (band = black)<br>Image: `image` (band = black, width, radius)<br>Body: `heading_text` (band = black)<br>Image Breaker + Body: `image` and `heading_text` (band = black, three pairs)<br>Body Header: `heading_text` (band = black)<br>Footer: `footer` (band = black) |
| Brand Storytelling | `1:6018` | `brand_story_letter` | A founder's brand story: the logo and a photo over a decorative shape, the story title on a dark band, a personal letter, four brand values, the founder's sign-off with a button and a P.S. code, four best-sellers, two value strips, and the footer. | Frame 12161 (logo): `logo_header` (band = sand)<br>Frame 12161 (photo): `image` (band = sand, width = 320)<br>Frame 12161 (title band): `heading_text` (band = ink)<br>Transition: `wave`<br>Body: `heading_text` (align = left)<br>Image Breaker: `features` (two items, twice)<br>Body (sign-off): `heading_text` (align = left)<br>CTA: `button`<br>Body: `heading_text`<br>Product Block (title): `heading_text`<br>Product Block (cards): `products_two` (two cards, twice)<br>Pre-Footer (claims): `promo` (band = ink)<br>Pre-Footer (values): `features` (four items, band = sand)<br>Footer (logo): `logo_header` (band = mist)<br>Footer (social): `social` (band = mist)<br>Footer (legal): `footer` (band = mist) |
| Holiday Greetings | `1:6121` | `holiday_greeting` | A holiday greeting: a logo band, a festive headline with a button over a photo, a warm message, a best-seller title with a photo and a button, two service promises, social icons and a contact footer. | Logo Header: `logo_header` (band = primary)<br>Hero Image: `hero_background` (button, no logo)<br>Body: `heading_text` (band = ink)<br>Body Headline: `heading_text`<br>Image Breaker: `image` (inset)<br>CTA: `button`<br>Footer (promises): `steps` (an icon per item), between two `divider`<br>Footer (social): `social`<br>Footer (contact): `footer` (band = sand) |
| Discount Reminder | `1:6163` | `discount_reminder` | A last-chance discount reminder: logo, a checkered border and a category menu, a bold headline over a large photo, the code reminder with a button, a friendly sign-off strip, and footer links. | Logo Header: `logo_header` (band = sand)<br>Transition: `spacer` (band = ink)<br>Menu: `menu` (band = accent)<br>Hero Image (headline): `heading_text` (band = sand)<br>Hero Image (photo): `image` (width = 460)<br>Hero Image (code line): `heading_text`<br>Hero Image (button): `button` (style = accent)<br>Footer (sign-off): `promo` (band = accent)<br>Footer (border): `spacer` (band = ink)<br>Footer (links): `steps` (an icon per item)<br>Footer (legal): `footer` (band = accent) |
| Countdown Timer Emails | `1:6271` | `early_bird_countdown` | An early-bird deal with a deadline: logo and menu, the offer headline, a countdown, the offer details and a button, a photo with a second button and terms, four service promises, a VIP club banner, and the footer. | Logo Header: `logo_header`<br>Menu: `menu`<br>Body: `hero_text` (no button)<br>Countdown: `countdown`<br>Body: `heading_text` (band = primary)<br>CTA: `button` (band = primary, style = accent)<br>Image Breaker (photo): `image`<br>Image Breaker (button): `button` (style = accent)<br>Image Breaker (terms): `heading_text`<br>Pre-Footer: `features` (four items)<br>Pre-footer: `image_text` (band = primary)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = white) |
| Benefits Emails | `1:6372` | `product_benefits` | A product benefits email: logo and a large title, an annotated product photo, three benefits with short explanations, a button, an ingredients title with photo and text, a two-column 'free from' list, a second button, and the footer. | Hero Banner (logo): `logo_header`<br>Hero Banner (title): `heading_text`<br>Hero Banner (photo): `image`<br>Body: `faq`<br>CTA: `button` (width = 540)<br>Image Breaker (title): `heading_text`<br>Image Breaker (photo): `image` (width = 540, radius = 8)<br>Image Breaker (text): `heading_text`<br>Image Breaker: `text_columns`<br>CTA: `button` (width = 540)<br>Footer (logo): `logo_header`<br>Footer (social): `social`<br>Footer (disclaimer): `coupon`<br>Footer (legal): `footer` (band = white) |
| Testimonials | `1:3831` | `customer_reviews` | Social proof email: a quote-themed header with a shop button, a 'five-star reviews' heading, three customer review cards with stars, a shop button, then a lifestyle photo with a last button before the footer. | Hero Banner (logo): `logo_header` (band = mist)<br>Hero Banner (title): `hero_text` (band = mist)<br>Headline: `heading_text` (band = sand)<br>Image Breaker (3 review cards): `callout` (panel = white, three times)<br>Button: `button` (width = 440)<br>Transition: `spacer`<br>Pre-Footer (photo): `image` (width = 360)<br>Pre-Footer (button): `button` (width = 440)<br>Footer: `footer` |
| FAQ | `1:3922` | `customer_questions` | Answers common customer questions: a promo strip and playful header, then three question-and-answer pairs each followed by a recommended product with a button, a pro tip card, a sign-off, a six-item feature grid, a label band and the footer. | Promo Strip: `promo` (band = mist)<br>Hero Banner: `hero_image` (band = mist)<br>Image Breaker 1 (Q&A): `faq` (band = sand)<br>Image Breaker 1 (recommended product): `image_text` (button)<br>Image Breaker 2 (Q&A): `faq` (band = sand)<br>Image Breaker 2 (recommended product): `image_text` (button)<br>Image Breaker 3 (Q&A): `faq` (band = sand)<br>Image Breaker 3 (recommended product): `image_text` (button)<br>Image Breaker 4 (pro tip): `offer`<br>Ending Signature: `heading_text` (band = ink)<br>Icon and Features: `features` (three items, twice)<br>Featured Text: `promo` (band = ink)<br>Footer (social): `social` (band = black)<br>Footer (legal): `footer` (band = black) |
| General Promotions | `1:4102` | `general_sale` | General sale email: promo strip, a collage header with logo and title, a short pitch with a button, a dark band of six product cards, a closing heading with text and button, then social icons and the footer. | Promo Strip: `promo` (band = white)<br>Hero Banner: `hero_image` (band = mist, no button)<br>Text: `heading_text` (band = sand)<br>Button: `button` (width = 200)<br>Transition + Product Block + Transition: `products`<br>Headline + Text: `heading_text`<br>Button: `button` (width = 200)<br>Footer (social): `social` (band = mist)<br>Footer (legal): `footer` (band = mist) |
| Event Invitation | `1:4213` | `open_studio_invitation` | Invites readers to a free in-person event: a photo header with a big event name, a card with the invitation, date and place, an RSVP button, and a social footer. | Hero Banner (photo header): `hero_background` (logo, no button)<br>Hero Banner (invitation card): `callout` (band = mist, align = left)<br>Hero Banner (button): `button` (band = mist, width = 340)<br>Footer (social): `social` (band = ink, title)<br>Footer (legal): `footer` |
| Thank You Email | `1:4425` | `thank_you_referral` | Seasonal thank-you that doubles as a promo: code strip, a 'we're thankful for you' photo header, a gift card visual with a discount message and button, a dark referral band (give a discount, get a reward) with a photo and button, a referral link line, three category tiles, a brand block with social icons, links and an app badge, and the footer. | Promo Strip: `promo` (band = ink)<br>Hero Banner: `hero_background` (no logo, no button)<br>IMAGE BREAKER (gift card): `image` (band = sand, width = 280)<br>Body Section (text): `heading_text` (band = sand)<br>Body Section (button): `button` (band = sand)<br>Transition: `wave`<br>Sub-heading: `heading_text` (band = ink)<br>IMAGE BREAKER: `image` (band = ink)<br>Body Section: `heading_text` (band = ink)<br>Body Section (button): `button` (band = ink, style = light)<br>Body Section (referral link + label): `heading_text`<br>Category: `image_pair` (three photos)<br>Body Section (logo): `logo_header`<br>Body Section (social): `social`<br>Body Section (links): `prefooter` (band = white)<br>Body Section (company line): `heading_text`<br>Footer: `footer` (band = white) |
| Referral Program Promotion | `1:4254` | `referral_program` | Asks customers to refer friends for a free product: logo and menu, a 'refer a friend' photo header with a button, two short lists explaining how it works, a high-five call to action with fine print, a guarantees bar and a dark footer. | Header: `logo_header`<br>Promo Strip: `menu` (band = mist)<br>Spacer: `spacer`<br>Hero Banner: `hero_background` (no logo, button)<br>Body Section 1: `heading_text`<br>Body Section 2: `heading_text`<br>Body Section + CTA: `cta`<br>Body Section (fine print): `heading_text`<br>Footer (guarantees): `features` (rules, band = mist)<br>Footer (logo): `logo_header` (band = ink)<br>Footer (links): `prefooter` (band = ink)<br>Footer (social): `social` (band = ink)<br>Footer (legal): `footer` |
| Reward/Points Program | `1:4319` | `loyalty_points` | Tells members they have loyalty points to redeem: inline logo and menu, a big 'you've got points' headline, a short text with a redeem button, a photo-beside-text block announcing new rewards, and a footer over a photo with help contact and social icons. | Header: `logo_bar`<br>Hero Banner: `hero_text` (band = ink, no button)<br>Body Section: `heading_text`<br>CTA: `button`<br>Frame 12055: `image_text`<br>Footer (help): `heading_text` (band = ink)<br>Footer (logo): `logo_header` (band = ink)<br>Footer (social): `social` (band = ink)<br>Footer (legal): `footer` |
| Newsletter Recap | `1:4373` | `newsletter_welcome_issue` | Welcome issue of a content newsletter: a type masthead with tagline, three photos, a long left-aligned letter on what each issue contains plus housekeeping, a wide photo, social icons and a light footer. | Hero Banner (masthead): `heading_text`<br>Hero Banner (photos): `image_pair` (three photos, no captions)<br>Frame 12076: `heading_text` (align = left)<br>Hero Banner (wide photo): `image` (width = 550)<br>Promo Strip: `social` (band = black)<br>Footer: `footer` (band = white) |
| Mythbuster | `1:4509` | `myth_busting` | Debunks three common myths about a product category: logo, a headline with a short line and a button, three cards each with a photo, the myth, a 'truth' tag and the answer, a closing call to action and a dark footer with social icons. | Hero Banner Logo: `logo_header`<br>Hero Banner: `hero_text` (band = mist)<br>Image Breaker (3 myth cards): `image` (inset; then heading_text)<br>Body Header + CTA: `cta`<br>Footer (social): `social` (band = black)<br>Footer (legal): `footer` |
| Did You Know Content | `1:4567` | `did_you_know` | Educational 'did you know' email: a photo header with the logo, an intro heading and text, a numbered 'here's how' list with closing text and a button, a product photo with heading, text and button, a full-width photo, and a dark footer with stacked link buttons. | Hero Image (logo): `logo_header`<br>Hero Image (photo): `image`<br>Hero Image (accent rule): `spacer` (band = accent)<br>Body: `heading_text` (band = mist)<br>Body (title): `heading_text`<br>Body (numbered list): `steps`<br>Body (closing text): `heading_text`<br>CTA: `button`<br>Image Breaker: `image` (width, space, band = mist)<br>Body: `heading_text` (band = mist)<br>CTA: `button` (band = mist)<br>Prefooter: `image`<br>Prefooter (accent rule): `spacer` (band = accent)<br>Footer (logo): `logo_header` (band = black)<br>Footer (tagline): `heading_text` (band = black)<br>Footer (links): `link_stack` (style = pills)<br>Footer (legal): `footer` (band = black) |
| Product Comparison | `1:4632` | `versus_comparison` | Compares the product with a generic competitor: a colored header with title, text, button and photo, a feature comparison table with a button, a big closing headline with a button and a product photo, and a dark footer with stacked buttons and social icons. | Hero Banner (Frame 12392 + Hero Image): `hero_image` (band = sand)<br>Image Breaker (title): `heading_text`<br>Image Breaker (comparison): `comparison`<br>CTA: `button`<br>Body Header + CTA: `cta` (band = sand)<br>Image: `image` (width = 400)<br>Footer (stacked buttons): `link_stack` (style = pills)<br>Footer (social): `social` (band = ink)<br>Footer (legal): `footer` |
| Product Launch Countdown | `1:4744` | `launch_story` | Pre-launch story email: a shipping strip and logo, two photo-led editorial blocks (heading, subheading, paragraphs, button: a behind-the-scenes link, then a pre-order), guarantees with social icons and a light footer; despite the title, the frame has no countdown. | Hero Banner strips: `promo` (band = ink)<br>Hero Banner Logo: `logo_header` (band = mist)<br>Image Breaker 1: `product_feature` (band = sand)<br>Image Breaker 2: `product_feature`<br>Footer (guarantees): `features` (two items, band = mist)<br>Footer (social): `social` (band = mist)<br>Footer (legal): `footer` (band = white) |
| Cart Abandonment Reminder | `1:4807` | `cart_reminder` | Reminds a shopper of the item left in the cart, on an all-black design: logo, a ruled 'we're worried about you' title with text, the item photo with its name and a checkout button, a ruled title over two more product suggestions, and a footer with social icons, stacked links and legal lines. | Hero Banner Logo: `logo_header` (band = black)<br>Body (rule above): `divider` (band = black)<br>Body (ruled title): `section_title` (align = left, band = black)<br>Body (text): `heading_text` (align = left, band = black)<br>Image Breaker: `image` (width = 440)<br>Image Breaker (caption): `heading_text`<br>CTA: `button` (style = accent)<br>Body (rule above): `divider`<br>Body (ruled title 2): `section_title` (align = left)<br>Product Block: `image_pair`<br>Footer (social): `social` between two `divider`<br>Footer (links): `link_stack`<br>Divider: `divider`<br>Footer (legal): `footer` (align = left, band = black) |
| Contest Invitation | `1:4865` | `contest_invitation` | Invites readers to enter a co-branded giveaway: two logos, a photo, an eyebrow and title with an enter button and text, the prizes as two photo cards, a photo fading into a second headline with text and a guide button, an 'explore the brand' photo mosaic with shop buttons, the contest fine print and the footer. | Hero Banner Logo: `logo_bar`<br>Hero Image: `image`<br>Body + CTA: `hero_text` (band = black)<br>Body: `heading_text`<br>Image Breaker (prizes): `image_pair`<br>Image Breaker (photo fade): `image`<br>Image Breaker (headline + text): `heading_text`<br>CTA: `button`<br>Transition: `divider`<br>Body: `section_title`<br>Image Breaker (mosaic): `image_mosaic`<br>Footer (logo): `logo_header`<br>Footer (social): `social`<br>Footer (legal, with the fine print): `footer` |
| Bundle Offers | `1:4952` | `bundle_picks` | Promotes build-your-own bundles through five customer picks: an offer strip, a photo header with title, five repeated bundle cards (who the person is, what is in their bundle, a product photo with a savings badge, a build button), and a help block with the footer. | Hero Strip: `promo`<br>Hero Banner: `hero_background` (logo, no button)<br>Image Breaker (5 bundle cards): `text_columns`, `image` and `button`, five times<br>Transition: `wave`<br>Footer (help): `heading_text` (band = ink)<br>Footer (logo): `logo_header` (band = ink)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = white) |
| Blog Content Highlight (A) | `1:5104` | `seasonal_digest` | Holiday editorial digest: a rewards strip, a photo header with a left-aligned title and a read button, an intro line, alternating photo-and-text story blocks with shop links, a row of three product photos, a shop button, two photo tiles, a stack of links, a gift guide band and the footer. | Hero Strip: `promo` (band = white)<br>Hero Banner: `hero_background` (align = left)<br>Body: `heading_text` (band = sand)<br>Image Breaker 1: `image_text` (direction = rtl)<br>Product Block: `image_pair` (three images)<br>Image Breaker 2: `image_text`<br>Image Breaker 3: `image_text`<br>Image Breaker 4: `image_text`<br>Image Breaker 5: `image_text`<br>CTA Button: `button` (style = light, width = 540)<br>Pre-footer (photo tiles): `image_pair`<br>Pre-footer (heading): `heading_text`<br>Pre-footer (links): `link_stack`<br>Pre-footer (gift guide band): `promo` (band = primary)<br>Footer (social): `social`<br>Footer (legal): `footer` (band = white) |
| Abandoned Cart | `1:936` | `cart_checkout_nudge` | Reminds a shopper they left an item in the cart: a headline over a product photo, a short nudge, the cart item with quantity and total, a checkout button, then a help image and a 'Questions?' note before links, socials and the legal footer. | Logo Section: `logo_header`<br>Hero Banner (title): `heading_text`<br>Hero Banner (photo): `image` (inset)<br>Text Content: `heading_text`<br>Abandoned Cart: `order_summary` (no totals)<br>CTA Button: `button`<br>Image Breaker: `image` (inset)<br>Text Content: `heading_text`<br>Divider: `divider`<br>Pre Footer (links): `prefooter`<br>Pre Footer (socials): `social`<br>Divider: `divider`<br>Footer: `footer` (band = white) |
| Order Confirmation | `1:981` | `order_confirmation_detailed` | Confirms an order: greeting, order number and date, the items ordered with prices, the totals, the payment method, billing and shipping addresses and a help line, then nav links, a social and address strip and the website link. | Logo: `logo_header`<br>Headline + Body: `heading_text`<br>Order No.: `heading_text`<br>Body + Divider (items ordered): `heading_text` (align = left) and `divider`<br>Product Details x2 + Other Details: `order_summary`<br>Body + Payment Info: `heading_text` (align = left)<br>Body + Other Details (addresses): `text_columns`<br>Divider: `divider`<br>Body (help): `heading_text`<br>Body (nav links): `prefooter` (band = white)<br>Footer: `text_columns`<br>Credit Footer: `footer` (band = white) |
| Shipping Confirmation | `1:1081` | `shipping_confirmation` | Tells the customer their package has shipped: headline, a note with the order number, a track-package button, the items in the shipment, a refer-a-friend panel, a 'See you soon' photo, then a footer logo, social icons and the address. | Logo: `logo_header`<br>Menu Bar: `menu` (band = mist)<br>Headline + Body: `heading_text`<br>CTA Button: `button` (width = 220)<br>Divider: `divider`<br>Body: `heading_text`<br>Products: `order_summary`<br>Body Text: `callout`<br>Divider: `divider`<br>Header: `heading_text`<br>Pre-footer: `image`<br>Footer-Logo: `logo_header` (band = mist)<br>Footer (follow us): `social` (title, band = mist)<br>Footer (legal): `footer` (band = mist) |
| Post-Purchase Follow-Up | `1:1146` | `post_purchase_followup` | Thanks a customer for a first purchase and asks for a review, then pitches a subscription in a tinted panel and invites them to follow on social, all in rounded white cards on a grey page, ending with a footer card. | Logo: `logo_header` (band = mist)<br>Hero Banner: `image` (width = 520, radius)<br>Headline: `heading_text`<br>Body: `heading_text` (align = left)<br>CTA Button: `button`<br>Transition + Body + Transition: `callout` (panel = mist)<br>Transition: `spacer` (band = mist)<br>Image Breaker + Body: `product_feature`<br>Transition: `spacer` (band = mist)<br>Body (footer logo): `logo_header` (band = line)<br>Socials: `social` (band = line)<br>Text: `footer` (band = line) |
| Replenishment Reminder | `1:1219` | `replenishment_reminder` | Reminds a customer that a prescribed product is about to run out: sender line, logo, a personal headline, the product to reorder with a full-width button and a phone line, more products to refill with a button, four reasons to order through the service on dark bands, a last button and the footer. | Header + Divider: `heading_text` (align = left) and `divider`<br>Logo: `logo_header` (align = left)<br>Headline + Body: `heading_text` (align = left)<br>Product Details: `order_summary` (no totals)<br>CTA Button: `button` (width = 540)<br>Body: `heading_text`<br>Transition: `spacer` (band = mist)<br>Product Details (heading): `heading_text` (align = left)<br>Product Details (item): `order_summary` (no totals)<br>CTA Button: `button` (width = 540)<br>Transition: `spacer` (band = mist)<br>Image Breaker x4 (title): `heading_text` (align = left, band = sand)<br>Image Breaker x4: `steps` (an icon per item, band = sand)<br>Transition: `spacer` (band = mist)<br>CTA Button: `button` (width = 540, band = mist)<br>Text + Logo + Text: `footer` (logo, band = mist) |
| Customer Feedback Request | `1:1308` | `feedback_panel` | Invites customers to join a product feedback panel: logo, a title over a full-bleed photo, a question headline with text and a form button, a large photo with a founder quote, three perks in columns on a grey band, and a black footer with social links and legal lines. | Logo Header: `logo_header`<br>Hero Banner: `hero_background` (no logo or button, gap)<br>Header & Body text: `heading_text`<br>CTA: `button` (width = 480)<br>Image Breaker: `image` (width = 470)<br>Testimonial + Body text: `testimonial` (band = white)<br>Pre Footer: `features` (band = mist)<br>Footer (social links): `prefooter` (band = black)<br>Footer (legal): `footer` (band = black) |
| Survey Invitation | `1:1351` | `survey_invitation` | Asks the reader to take a short survey in exchange for a discount code: logo, a bordered card with a greeting and two text-and-button pairs, then a footer with logo, tagline, social icons and legal lines between dashed rules. | Hero Banner / Logo Here: `logo_header`<br>Image Breaker / Text 1: `callout` (align = left)<br>Image Breaker / Text 2: `callout` (align = left)<br>Footer / Vector 1: `divider`<br>Footer / Logo Here: `logo_header`<br>Footer / tagline: `heading_text`<br>Footer / Vector 2: `divider`<br>Footer / Social Icons: `social`<br>Footer / Vector 3: `divider`<br>Footer Details: `footer` |
| Birthday Emails | `1:1402` | `brand_birthday` | Celebrates the brand's birthday with a giveaway: logo, a huge 'Happy Birthday' headline, a paragraph and an enter button, a full-width photo, then a black footer with logo, stacked links, social icons and legal lines. | Logo Header + Hero Banner: `hero_image` (text, band = white)<br>Footer (logo): `logo_header` (band = black)<br>Footer (links): `prefooter` (band = black)<br>Footer (icons): `social` (band = black)<br>Footer (text): `footer` (band = black) |
| Special Offers | `1:376` | `bestseller_discount` | Offers a discount on bestsellers: logo, a type-only hero with eyebrow, title, condition and code button on a sand band, a full-width photo, a two-by-three grid of bestsellers, three category tiles, a row of service promises, and a sand footer with logo, slogan, links, socials and the legal line. | Header: `logo_header`<br>Hero Banner: `hero_text` (band = sand)<br>Image Breaker: `image`<br>Product (title): `heading_text`<br>Product (grid): `products_two` three times<br>Category: `image_pair` (three photos)<br>Menu: `features` (labels only)<br>Footer (logo): `logo_header` (band = sand)<br>Footer (slogan + contact): `heading_text` (band = sand)<br>Footer (menu): `prefooter`<br>Footer (icons): `social` (band = sand)<br>Footer (copyrights + unsubscribe): `footer` (band = white) |
| Back in Stock | `1:492` | `back_in_stock_hero` | Announces that a favorite item is back in stock: a full-bleed photo with the logo between thin rules and a two-weight headline, a short text, a shop button, a left-aligned thank-you note, then links with a small image and the legal line. | Hero Banner: `hero_background` (logo and button optional)<br>Body: `heading_text`<br>CTA: `button`<br>Body: `heading_text` (align = left)<br>Divider: `divider`<br>Pre-Footer: `prefooter` (align = left)<br>Footer: `footer` |
| Low Inventory Alerts | `1:525` | `low_stock_alert` | Warns that a product is almost sold out: one full-bleed photo carrying the logo, a two-weight headline and a rounded panel with text and a shop button, then a black footer with logo, three outlined link buttons, socials and the legal line. | Hero Banner and Body Text: `hero_background` (logo, gap, text and button in the title area)<br>Footer (logo): `logo_header` (band = black)<br>Footer (CTA links): `link_stack` (style = pills, band = black)<br>Footer (socials): `social` (band = black)<br>Footer (body): `footer` (band = black) |
| New Product Launch | `1:566` | `product_introduction` | Launches a new product: a red hero with the logo between rules, stacked 'Introducing' type around the product photo with a badge, a bold claim and a button, a photo with bold justified copy over it, a benefit timeline with icons, an emotional text block with a button, a thank-you note, links with a small image and the legal line. | Hero Banner (logo): `logo_header` (band = primary)<br>Hero Banner (art): `heading_text` (band = primary, 'Introducing') and `image` (band = primary, width = 300)<br>Body: `heading_text` (band = primary)<br>CTA: `button` (band = primary, style = light)<br>Hero Banner: `hero_background` (align = left, no logo or button)<br>IB: `steps` (an icon per item, band = sand)<br>Body: `heading_text` (align = left, band = ink)<br>CTA: `button` (band = ink, style = light)<br>Body: `heading_text` (align = left)<br>Divider: `divider`<br>Pre-Footer: `prefooter` (align = left)<br>Footer: `footer` (band = white) |
| Seasonal Collection Highlight | `1:669` | `seasonal_collection` | Presents a seasonal collection: a photo hero with logo and slanted title, an intro with two shop buttons, three photo moments each with a short caption (one a staggered pair), two more shop buttons, a gift link, a curved tagline, socials and the legal footer. | HERO: `hero_background` (logo, gap)<br>Body: `heading_text` (band = sand)<br>CTA: `button` (band = sand)<br>CTA: `button` (band = sand)<br>Image Breaker: `image` (width = 320, space)<br>Body: `heading_text` (band = sand, padding)<br>Image Breaker: `image_pair` (band = sand)<br>Body: `heading_text` (band = sand, padding)<br>Image Breaker: `image` (width = 320, space)<br>Body: `heading_text` (band = sand, padding)<br>CTA: `button` (band = sand)<br>CTA: `button` (band = sand)<br>Body: `prefooter` (band = white)<br>FOOTER (tagline): `heading_text`<br>FOOTER (icons): `social`<br>FOOTER (legal): `footer` (band = white) |
| ICYMI | `1:756` | `missed_it_reminder` | Reminds readers of a product they may have missed: logo, a giant headline overlapped by a cut-out product on a diagonal two-tone background, short text and a button on grey, then the legal footer and social icons. | Hero Banner: `hero_image` (band = white, no button)<br>Body: `heading_text` (band = mist)<br>CTA: `button` (band = mist)<br>Socials: `social`<br>Footer: `footer` (band = white) |
| Limited-Time Discounts | `1:830` | `last_hour_sale` | Pushes a last-hour sitewide sale: inside a bordered card, a photo with logo and a 'last hour' badge, the discount title, a code pill and a button, then a countdown, a free-gift panel, three category rows with code and button, a claims panel, then a small logo, two link columns and a long legal footer. | Frame 12068: `hero_background` (logo, 'last hour' line as the title)<br>Frame 12061 (title): `heading_text` (padding)<br>Frame 12061 (code): `coupon`<br>Frame 12061 (button): `button` (width = 480)<br>Frame 12065: `countdown`<br>Frame 12062 (gift panel): `callout` (panel = mist)<br>Frame 12062 (title): `heading_text` (padding)<br>Frame 12066, 12067, 12063: `image_text` (button)<br>Frame 12069: `callout` (panel = primary)<br>Frame 12070: `logo_header` (align = left)<br>Frame 12072 + 12071: `text_columns`<br>Frame 12073: `divider`<br>Footer: `footer` (band = white) |
| Holiday Promotions | `1:780` | `holiday_gift_promotion` | Promotes holiday gifts: a photo hero with logo and title, a sale heading with text and a button, a second heading over two stacked photos with a button and a line, a rule, an extended-returns note with a gift icon, four trust badges on grey and a spare slot; it has no legal footer. | Hero: `hero_background` (logo, gap)<br>Body: `heading_text` (padding)<br>CTA: `button` (style = light)<br>IB (heading): `heading_text` (padding)<br>IB (photos): `image` (width = 400, space)<br>IB (button): `button` (style = light)<br>IB (text): `heading_text` (padding)<br>Transition: `divider`<br>Pre footer (icon): `image` (width = 64)<br>Pre footer (text): `heading_text`<br>iCON: `features` (four items, band = line)<br>Additional: `heading_text`<br>Footer: `footer` (band = white) |
| Anniversary Emails (A) | `1:1429` | `brand_anniversary` | A brand anniversary sale: a strip announces a returning product, a photo hero repeats the number of years with a shop button, a paragraph and button push the anniversary sale, a titled timeline walks through the brand's milestones year by year, then a dark thank-you band with a sale button and the legal footer. | Logo Header: `logo_header`<br>Header & Body text: `promo` (band = black)<br>Hero Banner: `hero_background` (gap, button, no logo)<br>Body text: `heading_text` (padding)<br>CTA: `button`<br>Header & Body text: `heading_text` (band = mist)<br>Image Breaker (first year): `heading_text` (band = black)<br>Image Breaker: `image_text` (six rows, alternating direction, bands black and white, no connecting line)<br>Body text: `hero_text` (band = black)<br>Footer: `footer` (band = white) |
| Blog Content Highlight (B) | `1:1532` | `holiday_digest` | A holiday digest from a home-goods brand: a rewards strip, a photo hero titled as the digest with a read-now button, a short intro, five story cards that alternate photo and text with a shop link, a row of three product links, a shop-all button, two photo tiles, a stacked list of store links ending on a gift-guide band, and the footer. | Frame 47: `promo` (band = mist)<br>Hero Banner: `hero_background` (align = left, logo, button)<br>Body: `heading_text` (band = sand)<br>Product Block 1: `image_text` (band = sand)<br>Product: `products_two` (three cards, no button)<br>Product Block 2: `image_text` (band = sand)<br>Product Block 3: `image_text` (band = sand)<br>Product Block 4: `image_text` (band = sand)<br>Product Block 5: `image_text` (band = sand)<br>Frame 12117: `button` (style = light, width = 540)<br>Frame 12119: `image_pair`<br>Frame 12125 (title): `heading_text`<br>Frame 12125: `link_stack`<br>Frame 12125 (gift guide): `heading_text` (band = primary)<br>Footer (icons): `social`<br>Footer (legal): `footer` (band = white) |
| Exclusive Access Email | `1:1703` | `exclusive_access` | A Black Friday early-access announcement: the logo on a striped band, then one dark rounded card with an eyebrow, a big 'starts now' title, a product photo, a teaser line, a short paragraph and a shop button, then a light legal footer. | Stripes Background + Logo Section: `logo_header` (band = line)<br>Hero Banner Contents: `callout` (panel = black, with a photo)<br>Footer: `footer` (band = white) |
| Price Drop Alert | `1:1742` | `price_drop` | A price-drop alert: a promo strip, then on a dark band the logo, a title, a short paragraph and a shop button above a product photo that fades into the band, then social icons and a light legal footer. | Promo Strip: `promo` (band = mist)<br>Logo Section + Hero Banner Content: `hero_image` (band = black, paragraph under the title)<br>Pre Footer: `social` (band = mist)<br>Footer: `footer` (band = mist) |
| Blog No. 2 | `1:1777` | `blog_digest` | A wellness blog digest: a photo hero with a flush-left title and intro, four article rows that alternate photo side (tag, question title, paragraph, button), a titled list of three suggested reads with a button each, social icons, a wide logo with four category links, and a dark legal footer. | Hero Banner: `hero_background` (align = left)<br>Image Breaker: `image_text` (band = black, button)<br>Header: `heading_text` (align = left)<br>Product Block: `image_text` (band = black, button)<br>Pre Footer: `social` (align = left)<br>Logo (artwork): `logo_header`<br>Logo (links): `menu`<br>Footer: `footer` |
| Pre-Sale Announcement (A) | `1:1887` | `presale_teaser` | A pre-sale teaser for a seasonal product: on a dark band the logo and a hand-lettered 'coming' title over a strip of three product photos, a short paragraph, a full-width button, social icons and a light footer. | Hero Image: `hero_image` (band = black, no button)<br>Body: `heading_text` (band = black)<br>CTA: `button` (band = black, style = light, width = 470)<br>Frame 42: `social`<br>FOOTER: `footer` (band = white) |
| Pre-Sale Announcement (B) | `1:1946` | `prelaunch_letter` | A founder's pre-launch letter: the logo on a pattern, then cream ticket-shaped cards, each a big flush-left heading with paragraphs (welcome, when it launches, share it or keep it secret with a share button), a centered thank-you signed by the owner with a framed photo, then a footer with a contact line, email-frequency choices and legal links. | Header Logo: `logo_header` (band = line)<br>Body header + Body Text: `heading_text` (align = left, band = sand)<br>TRANSITION: `spacer` (height = 8)<br>Body Header 2 + Body Text 2: `heading_text` (align = left, band = sand)<br>TRANSITION: `spacer` (height = 8)<br>Body Header 3 + Body Text 3: `heading_text` (align = left, band = sand)<br>CTA: `button` (align = left, style = accent, band = sand)<br>TRANSITION: `spacer` (height = 8)<br>Body Header 4 + Body Text 4: `heading_text` (band = sand)<br>Image: `image` (width = 340, band = sand)<br>Footer (contact): `heading_text`<br>Footer (rule): `divider`<br>Footer (frequency): `prefooter` (band = white)<br>Footer (legal): `footer` (band = white) |
| Order Tracking Emails | `1:2002` | `order_tracking` | A shipping notification: a label strip, the logo, a photo hero saying the order is on its way, a short paragraph with a track-package button, the ordered items and the totals, then category links, pill links to help pages, a brand-story teaser with a round photo, social icons and the unsubscribe line. | banner: `promo` (band = ink)<br>Logo Header: `logo_header` (band = mist)<br>Hero Banner: `hero_background` (align = left, gap)<br>Body: `heading_text` (align = left)<br>CTA: `button` (width = 520)<br>Product Block (title): `heading_text`<br>Product Block + Total: `order_summary`<br>Menu: `prefooter` (band = white)<br>Footer (pills): `link_stack` (style = pills)<br>Footer (story): `image_text` (band = line, direction = rtl)<br>Footer (icons): `social` (align = left, band = mist)<br>Footer (legal): `footer` (band = mist, align = left) |
| Brand Advocacy/Story | `1:2091` | `gratitude_letter` | A first-anniversary thank-you letter: logo and a 'note of gratitude' title framed by sun rays, a long letter with a pull quote and a sign-off, three team signatures with names and roles, and a dark footer with social icons and legal links, then a disclaimer. | Hero Banner (logo): `logo_header`<br>Hero Banner (title): `heading_text`<br>Body: `heading_text` (align = left) three times, the pull quote in the middle<br>Signature: `features` (rules = true)<br>Footer (icons): `social` (band = ink)<br>Footer (legal): `footer`<br>Footer (disclaimer): `footer` (band = white) |
| Review Request 1 | `1:2177` | `review_referral` | A review request with a referral push: a full-width photo with the logo, a peach band with five stars, a playful title, a line of text and a leave-a-review button, a referral offer card (photo, give/get band, title, text, button), and a footer with the logo, a did-you-know box, links and legal lines. | Hero Banner (logo): `logo_header`<br>Hero Banner: `image`<br>Body + CTA: `heading_text` (band = sand) then `button` (band = sand, width = 520)<br>Divider: `divider`<br>Image reaker: `offer`<br>Divider: `divider`<br>Footer (logo): `logo_header`<br>Footer (did you know): `callout`<br>Footer (links): `prefooter` (band = white)<br>Divider: `divider`<br>Footer (legal): `footer` (band = white, align = left) |
| Review Request 2 | `1:2241` | `review_loved_product` | A post-purchase review request: a photo hero asking whether the customer loves the product, a short paragraph, the purchased product with its name link, a leave-a-review button, social icons, then a footer with the logo, a product tagline between dashed rules, social icons again and the legal lines. | Hero Banner: `hero_background` (logo, gap, no button)<br>Body: `heading_text` (band = sand)<br>Dynamic Block: `image` (width = 240) then `heading_text` with the name link<br>CTA: `button` (style = accent, width = 230)<br>Social Media: `social` (band = sand)<br>Footer (rule): `divider`<br>Footer (logo): `logo_header`<br>Footer (tagline): `heading_text`<br>Footer (rule): `divider`<br>Footer (icons): `social`<br>Footer (rule): `divider`<br>Footer (legal): `footer` (band = sand) |
| Customer Milestone Emails | `1:2298` | `customer_milestone` | A loyalty milestone email: a photo hero welcoming the customer into a club, then on black two short sections, each a two-tone heading, a paragraph and a button (look back, share it), and a dark footer with social icons and legal links. | Hero Banner: `hero_background` (button optional)<br>Body + Body: `heading_text` (band = black)<br>CTA: `button` (band = black, style = light)<br>Body + Body: `heading_text` (band = black)<br>CTA: `button` (band = black, style = light)<br>Social Media: `social` (band = ink)<br>Footer: `footer` |
| Renewal Offers | `1:2353` | `membership_renewal` | A membership renewal reminder: a photo fading into black with the logo, a heading saying the membership is almost up, a line of text, a turn-on-renewal button, the monthly price, and legal links on black. | Hero Banner (photo): `image` (the dark sample)<br>Hero Banner (logo): `logo_header` (band = black)<br>Body + CTA: `heading_text` (band = black) then `button` (band = black, style = accent, width = 420)<br>Body: `heading_text` (band = black)<br>Footer: `footer` (band = black) |
| Year-in-Review | `1:2384` | `year_in_chapters` | A year-in-review recap: a photo hero titled 'a year in review', a short intro, numbered chapters (new products and best sellers as alternating photo-and-quote rows, then team growth, a project, a collaboration, big wins and press mentions as photo cards with text or lists), a closing paragraph with a button, a follow-along heading with social icons, and a footer with links. | Hero Banner: `hero_background` (logo, gap)<br>Body: `heading_text` (align = left, band = sand)<br>Image Breaker (chapter titles): `heading_text` (align = left)<br>Image Breaker (rows): `image_text` ×5 (band = sand, alternating direction)<br>Image Breaker: `image` (width = 552), then `heading_text` (align = left)<br>Image Breaker: `image` (width = 552), then `heading_text` (align = left)<br>Image Breaker: `image` (width = 552), then `heading_text` with both lists (align = left)<br>Body: `heading_text` (align = left)<br>CTA: `button` (width = 400)<br>Body: `heading_text`<br>Social Media: `social` (band = sand)<br>Footer (links): `prefooter`<br>Footer (legal): `footer` (band = sand) |
| Special Day Promotions | `1:2482` | `special_day_sale` | A holiday sale (a Mother's Day example): an arched photo with the logo and a round discount badge on a brand-colored band, a big serif sale title, a short line and a shop button, two small featured items with captions, and a light footer with social icons. | Hero Banner (logo): `logo_header` (band = primary)<br>Hero Banner (photo): `image` (band = primary, width = 520)<br>Hero Banner (text) + CTA: `hero_text`<br>Image Breaker: `image_pair` (band = sand)<br>Footer (icons): `social`<br>Footer (legal): `footer` (band = white) |
| Anniversary Emails (B) | `1:2529` | `subscription_anniversary` | Marks a subscriber's anniversary with the service: a personal greeting and message, a four-step reminder of how the service works, a button to manage deliveries, then a help contact, social links, a brand tagline, a review score and app download links before the legal lines. | Header: `hero_background` (logo, gap, title)<br>Body Headline + Body Text: `heading_text` (band = sand)<br>Image Breaker Headline: `heading_text`<br>Image breaker 1-4: `image_text` ×4 (alternating direction)<br>CTA: `button`<br>Prefooter / Frame 38: `heading_text` (band = primary)<br>Prefooter / Frame 42: `social` (band = sand)<br>Prefooter / Frame 39: `heading_text` (band = primary)<br>Footer / Frame 43: `heading_text` (stars as text, band = sand)<br>Footer / Frame 44: `divider` (band = sand)<br>Footer / Frame 45: `heading_text` (app links as text, band = sand)<br>Footer / Frame 5: `footer` (band = sand) |
| Early Bird Access | `1:2693` | `early_bird_access` | Gives subscribers early access to a sale: a hero announcing early-bird access, the discount and its code, a photo collage and a wide photo with a shop button, three featured products each with a shop button, then a closing line, four selling points and four trust badges. | Hero Banner: `hero_background` (logo, eyebrow and subline in the title, no button)<br>Image Breaker / Text: `heading_text`<br>Image Breaker / Code: `coupon`<br>Image Breaker / Shape: `image` (width = 480, radius = 24)<br>Image Breaker / Put Image Here: `image`<br>Image Breaker / CTA Button: `button`<br>Header / title: `heading_text` (band = line)<br>Product 1-3: `product_feature` ×3 (band = line)<br>Frame 12864: `heading_text` (band = line)<br>Frame 12865: `menu` (band = line)<br>iCON: `features` (band = sand)<br>Footer: `footer` (band = sand) |
| Giveaway Announcement | `1:2761` | `partner_giveaway` | Announces a giveaway run with a partner brand: both logos, a photo with the giveaway title and an enter button, how it works, the prizes it includes, a guide to read, products to explore, then a closing paragraph, icons and the legal lines. | Logo: `logo_bar` (partner name as text)<br>Hero Banner / photo: `image`<br>Hero Banner / text: `hero_text` (band = white)<br>Body: `heading_text`<br>Image Breaker: `image_pair`<br>Body: `heading_text`<br>Pre-Footer / photo: `image`<br>Pre-Footer / text: `heading_text`<br>Pre-Footer / CTA BUTTON: `button`<br>Frame 12863 / title: `heading_text`<br>Frame 12863 / grid: `image_mosaic`<br>Body: `heading_text`<br>Logo: `logo_header`<br>Frame 12116: `features`<br>Additional: `footer` (band = white) |
| How To Guides | `1:2847` | `beginner_guide` | Introduces a beginner's guide: a hero asking if the reader is new to the subject with a get-started button, two guide items with a recommended-products button, a subscribe prompt, then logo, menu links, icons and the legal lines. | Logo: `logo_header` (band = line)<br>Hero Banner: `hero_background` (title with paragraph, button)<br>Image Breaker / title: `heading_text` (band = line)<br>Image Breaker / Title 1-2: `image_text` (band = mist)<br>Image Breaker / Frame 12116: `cta` (band = mist)<br>Pre-Footer: `callout` (band = line, panel = mist)<br>Footer / LOGO: `logo_header` (band = mist)<br>Footer / Frame 12115: `link_stack` (style = pills)<br>Frame 12116: `features` (four items with icons)<br>Additional: `footer` (band = white) |
| Subscription Upsell | `1:2918` | `membership_upsell` | Invites a customer to join a paid membership: a hero with the promise, what the membership is, four benefits and a join button, then a lighter alternative (book a single service) and a footer with links, app download, a tagline and the legal lines. | Hero Banner: `hero_background` (logo, gap, no button)<br>Hero Banner / wave: dropped<br>Body: `heading_text` (band = accent)<br>Image Breaker: `steps` (band = accent, icon per item)<br>CTA: `button` (band = accent)<br>Transition: dropped<br>Image Breaker: `image_text` (band = primary, button, button_style = light)<br>Footer / icons: `social`<br>Footer / links: `link_stack`<br>Footer / app: `cta` (band = mist)<br>Footer / tagline: `heading_text`<br>Footer / legal: `footer` (band = white) |
| Site Abandoned | `1:3018` | `browse_abandonment` | Brings back a visitor who browsed without buying: a playful compliment on their taste, a short message and a shop button, four products with prices and shop buttons, a second shop button, then links and the legal lines. | Logo Header: `logo_header` (band = sand)<br>Menu: `menu` (band = accent)<br>Hero Banner: `hero_text` (band = sand, no button)<br>Body / Header + Divider: `section_title` (band = line)<br>Body / Body: `heading_text` (band = line)<br>CTA: `button` (style = accent)<br>Product Block: `products_two` x2 (band = line, two cards with buttons)<br>CTA: `button` (style = accent)<br>Footer / Transition: `divider` (band = accent)<br>Footer / links: `prefooter` (band = accent)<br>Footer / legal: `footer` (band = sand) |
| Product Education Emails | `1:3093` | `product_education` | Teaches about a product line: a hero photo, an eyebrow, heading and paragraph with a shop button, a full-width content image, a personal thank-you with three recommended products and a more button, then link rows, logo and the legal lines. | Logo Header: `logo_header`<br>Hero Image: `image`<br>Body: `heading_text` (align = left, band = sand)<br>CTA: `button` (band = sand)<br>Divider: `divider` (band = sand)<br>Content: `image`<br>Product Block / Frame 12245: `heading_text` (band = sand)<br>Product Block / Product Block: `products_two` (three cards, no buttons)<br>Product Block / CTA: `button` (band = sand)<br>Footer / links: `prefooter`<br>Footer / Logo: `logo_header` (band = sand)<br>Footer / legal: `footer` twice, copyright on sand and legal lines on white |
| Problem Acknowledgment/Resolution | `1:3152` | `concern_resolution` | Answers a customer worry head-on with a two-line 'X? No problem.' headline, explains it with a shop button, then makes it right with a discount code card over a photo, and closes with a dark branded footer. | Logo Header: `logo_header` (band = sand)<br>Hero banner / Frame 12249: `hero_text` (band = sand)<br>Hero banner / Image: `image`<br>Hero banner / Promo: `coupon`<br>Hero banner / Promo button: `button`<br>Footer / Logo Header: `logo_header` (band = ink)<br>Footer / Frame 12250: `heading_text` (band = ink)<br>Footer / Frame 42: `social`<br>Footer / Frame 12251-12253: `link_stack`<br>Footer / Frame 12254: `footer` |
| Post-Holiday Clearance Sales | `1:3264` | `clearance_sale` | Clears post-holiday stock: a teaser line, a logo bar with a free-shipping promise, an extra-off clearance banner with an access button, four rows pairing a styled photo with a discounted product, category tiles and links, then terms, social links, legal links and the logo. | Body: `view_in_browser`<br>Frame 12323: `logo_bar` (text)<br>Hero Banner: `hero_text` (button)<br>Product Block / PB1-PB4: `image_text` x4 (button, direction alternates)<br>Frame 12327: `features` (band = mist, three items, no icon)<br>Frame 12232: `link_stack`<br>Frame 12328: `heading_text` (align = left)<br>Frame 12329: `social` (title)<br>Frame 12289 + Frame 12331: `footer` (band = white, logo) |
| Urgent Flash Sales | `1:3383` | `flash_sale_grid` | Announces a short flash sale: logo, a free-shipping strip, a hero with the discount, two shop buttons (men, women), terms and the end time, then six discounted products and a dark footer. | Hero Logo: `logo_header`<br>Hero Strip: `promo` (band = mist)<br>Hero  Banner: `hero_background` (title with eyebrow and line, gap, one button)<br>Hero Banner / second button: `button` (on white)<br>Hero Banner / terms: `heading_text`<br>Product Block x3: `products_two` x3 (band = mist, no buttons)<br>Footer / Frame 12338 + links + address: `footer` (band = black, logo) |
| Exit Intent Discounts | `1:3439` | `exit_intent_offer` | Catches a visitor who left with a big first-order discount: a logo bar with a get-started link, a playful 50%-off headline, a short pitch, the code inline, a button, a brand tagline and a footer. | Hero Logo + Divider: `logo_bar` (band = mist, text link) and `divider` (band = mist)<br>Hero Image: `hero_text` (band = mist, no button)<br>Body: `heading_text` (band = mist)<br>Body: `coupon` (band = mist)<br>CTA: `button` (band = mist, width = 400)<br>Pre-footer: `heading_text`<br>Footer / Frame 12329: `logo_bar` (band = accent) and `social` (band = accent, align = left)<br>Footer / Frame 12348: `footer` (band = accent, align = left) |
| Newsletter Sign-Up Welcome Emails | `1:3495` | `subscriber_welcome` | Welcomes a new subscriber: a welcome title and photo, a tagline with a first-order discount button and its code, the brand story, three brand values each with a button, and a quiz invitation before the footer. | Hero Banner Logo: `logo_header`<br>Hero Banner Header: `heading_text`<br>Hero Banner: `image` (width = 540)<br>Body Header + CTA: `cta`<br>Code: `heading_text`<br>Body: `callout` (panel = sand)<br>Transition: dropped<br>Image Breaker Header: `heading_text` (band = sand)<br>Image Breaker / photo: `image` (band = sand, width = 420, radius = 12)<br>Image Breaker x3: `callout` x3 (band = sand, panel = white)<br>Body Header + CTA: `heading_text` and `button` (band = sand)<br>Footer / Frame 12329: `social` (band = primary) and `divider`<br>Footer / legal: `footer` (band = primary) |
| Social Media Highlight | `1:3583` | `social_follow` | Asks subscribers to follow the brand on social media: a logo bar with a shop button, a photo with the follow-us headline, a short pitch, one button per network and a footer. | Hero Headline: `logo_bar` (button)<br>Hero banner: `hero_background` (align = left, gap)<br>Body: `heading_text` (align = left)<br>CTA x2: `button` (style = accent)<br>Footer / Frame 12342: `divider`<br>Footer / Frame 12329 logo: `logo_header`<br>Footer / Frame 12329 icons: `social`<br>Footer / legal: `footer` |
| Referral Reminder Emails | `1:3623` | `referral_reminder` | Reminds customers to refer a friend: a bold question with a refer button on color above a lifestyle photo, three short paragraphs and the button again, a brand tagline band and the footer. | Hero Banner: `hero_image` (band = line, button)<br>Body / text: `heading_text` (band = mist)<br>Body / button: `button` (band = mist)<br>Image Breaker / curve: dropped<br>Image Breaker / tagline: `heading_text` (band = accent)<br>Footer / logo: `logo_header` (band = sand)<br>Footer / icons: `social` (band = sand)<br>Footer / legal: `footer` (band = sand) |
| Affiliate Program Promotion | `1:3664` | `affiliate_invitation` | Recruits affiliates: a headline inviting readers to join the program, an image collage, why it is worth it, a sign-up button, a checklist of benefits, a quote from an affiliate, social links and the brand sign-off. | Logo: `logo_header`<br>Hero Banner Headline: `heading_text`<br>Hero Banner: `image` (width = 520)<br>Body: `heading_text` (align = left)<br>CTA Button: `button`<br>Image Breaker: `steps` (icon per item)<br>Testimony: `testimonial`<br>Footer / follow: `divider`, `social` (title) and `divider`<br>Footer / sign-off + unsubscribe: `footer` (band = white) |

## Adaptations

Each item is a section whose design asks for something a rule rejects, with the rule and the change that replaces it. The rules never relax for a template. Under a template the library has built, the items marked **Built** say what differs from the frame.

Every library template paints with the library brand. Its fonts, type sizes, button shapes and colors come from `brand.toml` and `base.html`, so the type is smaller than the kit's 22 px body text and the buttons are not pills. The kit's grey placeholder photos become sample images, and a photo with text on it is the dark sample `hero-dark.jpg`.

### Teaser

- **Built.** The hero is the dark sample photo with the title in white, and the inset rounded card around it is a full-width band.
- **Built.** The release date card is a light `callout` panel with no photo behind it, since `hero_background` can appear once.
- **Built.** The two quick links are `features` items with the library's gift and heart icons and a title; `features` has no link field, so the person editing links the titles in the editor.
- **Built.** The five social placeholders become four library icons.
- Hero Banner: text on photo: hosted background URL with a color fallback (C3); the inset rounded card becomes square in Outlook
- Product Release Date: text on photo (C3), and `hero_background` can appear once per email: the card becomes a `callout` on a band color

### Flash Sale

- **Built.** The gradient strip is one solid accent band and the outlined, rotated sale lettering is dropped: the photo stands alone, rounded, centered above the offer.
- **Built.** The offer copy is centered under the photo and its button is the accent pill of `hero_text`; the fine print under the button moves to its own line below.
- **Built.** Each product card shows its photo first, then the name, saving, code and description, and the button last: `product_feature` has no heading above the photo.
- **Built.** The product buttons are the primary button, not orange.
- **Built.** The social icons in the footer row are text links on the right of `logo_bar`.
- **Built.** The phone and email rows use the library's truck and shield icons, as delivery and help rows.
- Open In Browser: gradient strip: use one solid brand color (C3, B1)
- Open In Browser (lettering + photo): rotated outlined display type and overlap (C2, B2): bake the lettering and the photo into one image
- Open In Browser (offer copy): the right-column offset only exists because of the overlapping lettering: center the copy under the image

### Sale Email

- **Built.** The oval photo is a rounded rectangle with a large radius, and the gold outlines around the photos and logos are dropped.
- **Built.** The first button is the accent pill of `hero_text` and the second a light button, not outlined pills.
- **Built.** The rule above the footer is the line color, not gold.
- **Built.** The address moves from above the social icons into the footer text, so the footer holds it (rule L1).
- Frame 115: oval mask and outline: bake the shape and stroke into the image on the band color
- Frame 115 (photo): pill mask and outline: bake them into the image

### Trending Products

- **Built.** The checkerboard is three `image_text` rows on the line band: each label sits beside an inset photo with a link under it, not on a full-bleed tile.
- **Built.** The tan tiles are the line band, since links in the primary color fail contrast on the accent color (A1).
- **Built.** The hero button is the primary button, since a white pill does not show on the sand band.
- **Built.** The thin frame around the feature photo and the product tiles is dropped, and the trending grid has short captions.
- **Built.** The four perk tiles and three service tiles are columns on one band, not separate rounded tiles.
- Hero Banner (photo): oval mask and outline: bake them into the image
- Frame 118: white text on light tan fails contrast (A1): darken the tile color or use dark text

### Social Proof

- **Built.** Each press row names the outlet in a heading instead of showing its logo, and the photo is inset with rounded corners, not full bleed.
- **Built.** The grey shade sits on the whole row, not only on the text half.
- **Built.** The tagline and the rights line move from the pre-footer panel into the footer text, since `logo_bar` has one text area.

### Welcome Email

- **Built.** The discount line and button are `heading_text` and `button`, since `cta` styles only a heading.
- **Built.** The strip text is larger than in the frame: `promo` sets its size in the style panel.
- **Built.** The black account bar carries the logo on the left, since `logo_bar` needs one; the pin icon before the store link is dropped.
- **Built.** The category links and the social icons sit in two rows, not side by side.
- **Built.** The hero is the dark sample photo, which keeps the frame's near-square shape.

### Product Features

- **Built.** The numbered markers on the photo are dropped and the four products carry the numbers in their names.
- **Built.** The product buttons are primary buttons under each card, not grey bars joined in an outlined frame.
- **Built.** The hero title is in the heading font over the dark sample photo, and its button is the hero's primary pill.
- Hero banner: text on photo: hosted background URL with a color fallback (C3)
- Image Breaker Image (photo): markers positioned over the photo (C2): bake them into the image
- Image Breaker Image (products): number badges over the photos: bake them into the images

### Gift Card

- **Built.** The header strip is a `logo_bar`: the logo on the left, the menu on the right.
- **Built.** The headline sits over the dark sample photo in white, since the light checkerboard of the frame has no text color that passes A1.
- **Built.** The decorative shapes under the footer are dropped: no sample wave joins white to white.
- **Built.** The five perks use the library's line icons, with a new gift icon.
- Hero banner: text on photo: hosted background URL with a color fallback (C3)

### Customer Spotlight

- **Built.** The gradient is one solid line band, and the quote is dark text, since white fails contrast on a light band (A1).
- **Built.** The script accent word is the heading font's italic.
- **Built.** The quote has a small portrait and the customer's name, since `testimonial` needs a photo.
- **Built.** The frame has no footer; a light legal footer closes the email (rule L1).
- Mask group (title): script accent word (B2): set it in the heading font's italic; gradient background (C3): use a solid brand color
- Mask group (quote): white text on the light part of the gradient fails contrast (A1)

### Behind The Scenes Content

- **Built.** The two stacked logos are one logo.
- **Built.** The review score is a heading and a line of text, since the library has no rating badge image.
- **Built.** The strip text is larger than in the frame, and the browser link sits on the page color, since `view_in_browser` has no band.

### Company Updates

- **Built.** Each article is an `image` above a `heading_text` with a link, since `product_feature` always draws a button.
- **Built.** The issue label sits in `view_in_browser` on the page color above the black email, since that block has no band.
- **Built.** The emoji ornaments are dropped: the two ornament transitions are thin rules and the link line is plain text.
- **Built.** Headings use the heading font's italic for the kit's display serif.

### Brand Storytelling

- **Built.** The gradient header is the sand band and the photo sits on it without the decorative shape behind it.
- **Built.** The header photo is a shorter sample than the frame's tall portrait.
- **Built.** The 2x2 values grid is two `features` rows of two items.
- **Built.** The founder's sign-off is a left-aligned `heading_text`, because the frame has no portrait for `signature`.
- **Built.** The wave runs from the ink title band into a white letter, not into the frame's pale lavender body.
- **Built.** The gradient values strip is one solid sand band.
- Frame 12161 (logo): gradient background (C3): use one solid brand color
- Frame 12161 (photo): photo overlapping a decorative shape (C2): bake the shape, photo and background into one image
- Pre-Footer (values): gradient background (C3): use one solid brand color

### Holiday Greetings

- **Built.** The logo band is `primary` and the message band `ink`: the brand roles closest to the frame's dark green and grey green.
- **Built.** The two promises are `steps` with an icon each, between two `divider`. The frame's rule between the two promises and the one under the social icons are dropped.
- **Built.** The one-line promise sits level with the top of its icon, not centered on it.
- Hero Image: text on photo: hosted background URL with a color fallback (C3)

### Discount Reminder

- **Built.** The two checkered borders are thin ink strips (`spacer`), since the library has no checkered image.
- **Built.** The menu and strips set ink text on the accent band in place of white on mustard, for contrast.
- **Built.** The outlined display headline is a plain heading above the photo, not over it.
- **Built.** The three help rows are plain titles beside their icons, aligned left: `steps` has no link style, so the links are left to the editor.
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

- **Built.** The photo labels and leader lines are dropped; the sample photo stands alone.
- **Built.** The two-column 'free from' list is `text_columns` with a check mark on each line, without the rules between rows.
- **Built.** The disclaimer box is the coupon's dashed box on sand, not a thin solid outline.
- **Built.** The title is the library's heading size, smaller than the frame's.
- Hero Banner (photo): labels and leader lines over the photo (C2): bake them into the image, or list the labels under it

### Testimonials

- **Built.** The quote glyphs and the arc behind the title are dropped.
- **Built.** The review cards are `callout` panels with the stars as a heading, because `testimonial` needs a portrait and draws no card.
- **Built.** The buttons are the primary style without the offset shadow, and the hero button is the accent style of `hero_text`.
- **Built.** The last button sits under the photo, not over it.
- Hero Banner (title): quote glyphs overlap the arc and the button (C2): drop them or bake arc and glyphs into a wave image above; the offset shadow becomes a plain border
- Image Breaker (3 review cards): quote glyphs overlap the card corners (C2): drop them or put one glyph inside the card above the stars
- Button: offset shadow: use a plain border
- Transition: gradient background: use a solid color
- Pre-Footer (photo): the kit puts the button over the photo's lower third: place it under the photo (next section) or use hero_background with a hosted URL

### FAQ

- **Built.** The Q: and A: stickers are written inline, and each pair is a plain question and answer between thin rules, not two offset bubbles.
- **Built.** The 'our pick' sticker is an eyebrow above the product name, and the hero sticker is dropped.
- **Built.** The pro tip card is the offer card stacked as photo, 'Pro tip' band, text and button.
- **Built.** The outlined sticker title is a plain bold heading.
- **Built.** The six-feature grid is two `features` rows of three.
- Hero Banner: outlined sticker type is decorative (text stroke): set a plain bold heading or bake it into an image; the straddling button and the tilted sticker over the photo need positioning (C2): keep the button on the band, bake the sticker into the photo
- Image Breaker 1 (Q&A): Q:/A: stickers overlap the boxes and the boxes are offset (C2): write 'Q:' and 'A:' inline, keep the boxes full width
- Image Breaker 1 (recommended product): sticker overlaps the photo corner (C2): bake it into the photo or write it as an eyebrow above the name
- Image Breaker 4 (pro tip): card, photo, sticker and button overlap (C2): stack them as the offer card does (photo, 'Pro tip' band, text, button)

### General Promotions

- **Built.** The scattered thumbnail collage is one sample photo under the logo and title.
- **Built.** The product block shows one row of three cards; the editor repeats the row for the second.
- **Built.** The gradient bands are solid: sand for the pitch, white for the closing heading.
- Hero Banner: thumbnails are scattered with absolute positions (C2) and the title sits on a pattern: put logo and title on a solid band, bake collage, captions and the bottom wave into one image
- Text: gradient background: use a solid color
- Headline + Text: gradient background: use a solid color

### Event Invitation

- **Built.** The photo header uses the dark sample with white type, and the tilted stickers are dropped.
- **Built.** The invitation card starts below the photo instead of overlapping its edge, and is a `callout` panel because `event_details` draws no card.
- **Built.** The social icons have no text labels under them.
- Hero Banner (photo header): text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook; tilted stickers overlap the title (C2): drop them or bake into the photo; display serif must be the headings stack (B2)
- Hero Banner (invitation card + button): card overlaps the photo edge (C2): start it below the photo

### Thank You Email

- **Built.** The gift card section sits on sand so the sand-to-ink wave joins it to the dark referral band; the frame has white there.
- **Built.** The referral band is heading, photo, text and button blocks on ink, keeping the frame's order, not one `product_feature`.
- **Built.** The category labels are captions under the tiles, not over them.
- **Built.** The app store badge is dropped: the library has no badge image.
- **Built.** The arc at the bottom of the photo header is dropped.
- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook; bake the bottom arc into the photo or follow with a wave
- IMAGE BREAKER (gift card): rotation and shadow must be in the image itself
- Category: label over the tile image: put it as a caption under the tile, or bake it into the image

### Referral Program Promotion

- **Built.** The photo header runs full width instead of inset with a margin.
- **Built.** The guarantee icons sit above their lines, not beside them.
- **Built.** The dark footer is logo, links, social icons and the legal lines as four blocks, and the white strip below it is folded into the footer.
- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook

### Reward/Points Program

- **Built.** The grey hero band is ink, and its title is the library's serif instead of the kit's heavy sans, so "POINTS!" is smaller.
- **Built.** The photo beside "Big news!" is a square sample with rounded corners, inside the block's padding, so the fade into white is lost.
- **Built.** The footer over a photo is a solid ink band: the help line, the logo, the social icons and the legal lines are four blocks on it.
- **Built.** The kit's spacer under the header is dropped: the hero band follows the header directly in the frame.
- Frame 12055: the fade into white must be in the photo; the block pads the photo, so the edge bleed is lost
- Footer (legal, with logo): text over a background photo (C3): use a solid dark band, or a hosted background with a color fallback

### Newsletter Recap

- **Built.** The type masthead is a `heading_text` heading and tagline, not a logo image, so it stays editable text.
- **Built.** The letter's card with its shadow is dropped; the letter sits on the white band.
- **Built.** The bulleted lists are paragraphs starting with a bullet, because `heading_text` has no list style.
- **Built.** The three photos have empty captions.
- Frame 12076: box shadow does not render in most clients: drop it or use a thin border

### Mythbuster

- **Built.** The "Truth" pill becomes a bold label on its own line.
- **Built.** The closing button is the full-width call-to-action button of `cta`.
- Footer (legal): about 8 px text and a blue link on black: raise to 12 px and use a role that passes contrast (A1)

### Did You Know Content

- **Built.** The logo sits on a white band above the photo instead of in a box over it.
- **Built.** The thick accent rules under the two photos are 6 px spacers on the accent band.
- **Built.** The four points use the steps block's numbered circles instead of bare accent numerals.
- **Built.** The product photo sits inside the soft band instead of straddling the white and grey bands.
- **Built.** The footer logo is a separate band and the stacked links are full-width pills instead of outlined boxes.
- Hero Image (logo): the kit puts the logo over the photo: place it on a band above (or hero_background with title and button optional and a hosted URL)
- Hero Image (photo): bake the accent rule into the photo or add a divider in the accent role
- Image Breaker: the photo crosses two band colors: bake both colors into the image

### Product Comparison

- **Built.** The comparison title is a `heading_text` above the table, and the table uses the `comparison` block's square cells: no pill heads, stems or thumb icons, ticks and crosses as text.
- **Built.** The cloud-shaped transition is dropped: no sample wave joins white to sand.
- **Built.** The stacked footer buttons are outlined `link_stack` pills, not filled lime pills.
- **Built.** The light blue bands are sand.
- Hero Banner (Frame 12392 + Hero Image): bake the white curve into the photo or follow with a wave
- Image Breaker (comparison): the heading above the table goes in a heading_text (the block has no title); pill heads and stems need images or a class, not inline style

### Product Launch Countdown

- **Built.** The strip has no icon and its text uses the promo block's larger type.
- **Built.** The editorial photos are 400 px wide, the product_feature cap, instead of 520 px.
- **Built.** The subheadings use the product_feature price style, and paragraphs inside one chapter are split with line breaks.
- **Built.** The two guarantees sit side by side with their icons above them instead of stacked with a small icon beside each line.
- Image Breaker 1: the kit's photo is 520 px wide; the block caps it at 400

### Cart Abandonment Reminder

- **Built.** Each ruled title is a divider above a section title, whose short accent rule replaces the full-width rule under it.
- **Built.** The item is an image, a caption and an accent button instead of product_feature, so the photo is 440 px wide and the button gold as in the frame.
- **Built.** The stacked links are centered with thin rules between them instead of flush left.
- **Built.** The legal lines use the footer's 12 px type instead of about 8 px, and carry an unsubscribe link.
- Footer (legal): text around 8 px: raise to 12 px

### Contest Invitation

- **Built.** The second logo becomes a short line in the `logo_bar`, "with Field Kitchen": a text area cannot hold a library sample image.
- **Built.** The prize cards stand straight, as an `image_pair` with captions; "and more" is dropped.
- **Built.** The photo fades into black only in the photo: the headline starts below it, as a `heading_text`.
- **Built.** The notched double rule is a plain `divider`.
- **Built.** The mosaic buttons sit under each photo, in the accent style. The tall sample `photo-tall.jpg` is sized so the bottoms line up.
- **Built.** The long fine print is the first paragraph of the `footer`, at its 12 px size.
- Image Breaker (prizes): rotated cards need transforms: set them straight, or bake the tilted pair into one image; the two labels go in heading_text blocks above and below
- Image Breaker (photo fade): the title starts over the fade: keep the fade in the photo and start the text below it
- Transition: the notch is a vector shape: drop it, or ship the ornament as a wave image
- Image Breaker (mosaic): buttons sit over the photos (C2): place each button under its photo, or bake it into the image and link the image

### Bundle Offers

- **Built.** All five bundle cards are kept: the `<style>` stays at 7 KB and the HTML at 20 KB, well under C5.
- **Built.** Each card is a `text_columns` (who the person is, what is in the bundle), then an `image` and a `button`. The round portrait is dropped and the savings badge becomes a line of text under the list.
- **Built.** The gradient behind the cards is the sand band.
- **Built.** The footer's website and support links, view-in-browser link and address are lines of the `footer`.
- Hero Banner: text on photo: hero_background needs a hosted https URL (MC10) and a color fallback for Outlook
- Image Breaker (5 bundle cards): portrait and badge overlap the photo (C2): move the portrait beside the bio, bake the badge into the photo; gradient background behind all five: use solid bands

### Blog Content Highlight (A)

- **Built.** The header has the logo image instead of a spaced wordmark with a rule, and the empty photo sits under the button instead of between the title and the button.
- **Built.** The read button is the hero's rounded brand button instead of an outlined full-width box.
- **Built.** The story cards sit beside their photos instead of overlapping them, and have no white card behind the text.
- **Built.** The two photo tiles carry their title and line in captions under the photos instead of over them.
- **Built.** The shop button is a light full-width button instead of an outlined one.
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

- **Built.** The items have no hairlines between them, and the discount and totals sit on the order summary's soft panel.
- **Built.** The payment line is a label and one line of text, with no card icon.
- **Built.** The shipping address column is flush left like the billing one instead of flush right.
- **Built.** The footer strip has social links as text instead of icons and no rule between its columns.
- **Built.** The address and an unsubscribe link move to the legal footer under the website link, as rule L1 asks.
- Body (payment info): light grey label on white: check contrast
- Body (nav links): light grey links on white: check contrast
- Footer: very light grey text: contrast
- Credit Footer: no unsubscribe link anywhere and the address sits in the column strip: rule L1 needs both in the footer, so add them here

### Shipping Confirmation

- **Built.** The dividers are plain rules instead of a small sprig ornament.
- **Built.** The shipped items are rows with a price instead of bordered boxes without one.
- **Built.** The refer-a-friend panel has one rounded border instead of a double inset border, and a full-width button.
- **Built.** The legal lines add an unsubscribe link, as rule L1 asks.
- Divider: ornament is a vector: export a PNG
- Footer (follow us): icons drawn as vectors: export PNG icons
- Footer (legal): no unsubscribe link: rule L1 needs one; tiny light grey text: contrast

### Post-Purchase Follow-Up

- **Built.** The rounded white cards on a grey page become full-width white sections split by grey spacers, and the footer card a full-width tinted band.
- **Built.** The hero photo is inset with all four corners rounded instead of filling the top of the card.
- **Built.** The subscription panel is a rounded callout inside the white section instead of the foot of the card, with a full-width button.
- **Built.** The second card's photo is 400 px wide, the product_feature cap.

### Replenishment Reminder

- **Built.** The product rows show a price, and the full-width buttons span 540 px.
- **Built.** The four reasons sit on one soft band with each icon beside its text, instead of four darkening slate bands with the icon above: the sample icons are in the brand color and do not read on a dark band.
- **Built.** The footer logo sits above all the legal lines instead of between the unsubscribe line and the links.
- **Built.** The logo keeps the block's 20 px inset, so it sits a little left of the text column.

### Customer Feedback Request

- **Built.** The large photo is its own image block, and the quote under it is a testimonial with a small round portrait.
- **Built.** The three perks use 48 px icons instead of 150 px photos.
- **Built.** The question headline uses the heading font instead of a bold sans.
- Hero Banner: text on photo: hosted background URL and a color fallback (hero_background); sans caps eyebrow plus serif display plus serif body: keep to the two brand stacks

### Survey Invitation

- **Built.** The one tall card becomes two `callout` panels, one per text and button: a callout holds one text area and one button.
- **Built.** The decorative stickers are dropped and the buttons are plain primary buttons without the checkered shadow.
- **Built.** The dashed rules are the solid `divider` line.
- Image Breaker / Text 1: decorative PNG stickers overlap the card edges (1:1373, 1:1376, 1:1379): drop them or place them in the flow; the checkered offset shadow under the buttons needs overlap: use a plain outlined button; serif, monospace and sans faces: keep to two stacks
- Footer / Social Icons: icons drawn as vectors: export PNG icons

### Birthday Emails

- **Built.** The headline uses the heading font instead of a condensed display face, and the button is the brand button instead of a black pill.
- **Built.** The photo is the 600 by 380 sample instead of a near-square photo.
- **Built.** The stacked footer links sit closer together than in the frame, and the logo has no white box.
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

- **Built.** The translucent rounded panel is gone: its text and button sit straight on the dark sample photo, under the title.
- **Built.** The pill links run the width of the link_stack block, where the kit's pills are about 270 px wide.
- **Built.** The title is the hero's 60 px heading font, so it takes two lines where the kit has three.
- Hero Banner and Body Text: text on photo: hosted background URL and a color fallback (hero_background); the panel looks translucent: give it a solid color

### New Product Launch

- **Built.** The stacked 'Introducing' type around the product with its rotated badge is one heading above a tall sample photo, since no sample image bakes the type in.
- **Built.** The rules either side of the logo are dropped: logo_header has no rule option.
- **Built.** The benefit timeline sits on a sand band without its connecting line, because the sample icons are painted in the primary color and would vanish on a primary band.
- **Built.** The second red band is the ink band, and both black buttons are the light button of base.html.
- **Built.** The small product image beside the footer links is dropped: prefooter holds links only.
- Hero Banner (art): overlapping type, photo and a rotated badge: bake them into one image and carry the words in the alt text
- Hero Banner: text on photo: hosted background URL and a color fallback (hero_background); justified text: set it flush left
- IB: the connecting line runs across rows: bake each segment into its icon image

### Seasonal Collection Highlight

- **Built.** The pale blue page is the sand band.
- **Built.** The staggered pair of photos is an even image_pair with a short caption under each photo.
- **Built.** The slanted title is set straight, and the curved tagline is a straight italic heading.
- **Built.** The stacked buttons sit further apart than the kit's, with the button block's own padding.
- HERO: text on photo: hosted background URL and a color fallback (hero_background); rotated title: set it straight or bake it into the photo
- FOOTER (tagline): text on a curve: bake it into an image

### ICYMI

- **Built.** The headline sits above the photo instead of under the cut-out product, and the diagonal two-tone background is a full-width sample photo.
- **Built.** The social icons come before the legal footer, so the template ends with the footer like the rest of the library.
- Hero Banner: photo overlaps the headline and the diagonal is a vector: put the headline above and bake the diagonal into the photo

### Limited-Time Discounts

- **Built.** The bordered card around the sections is dropped: base.html has no frame option.
- **Built.** The 'last hour' badge is a bold line under the logo, not a yellow pill.
- **Built.** The code pill is the dashed coupon box, and the countdown sits on the brand band in boxes.
- **Built.** The category buttons are the primary button without the arrow.
- Frame 12068: text on photo: hosted background URL and a color fallback (hero_background)
- Frame 12065: for a live timer, a timer service image in an image block

### Holiday Promotions

- **Built.** The gift icon is its own narrow image above the returns note, since heading_text has no icon.
- **Built.** The trust badges are four features with the sample icons and a short label, on the line band.
- **Built.** A legal footer is added at the end, which the kit frame lacks (rule L1).
- **Built.** The hero title is the 60 px heading, larger than the kit's.
- Hero: text on photo: hosted background URL and a color fallback (hero_background)
- Pre footer: icon is a vector: export a PNG

### Anniversary Emails (A)

- **Built.** The connecting line and dots of the timeline are dropped.
- **Built.** The year rows with a photo above or below the text (2020 and 2024 in the kit) are side-by-side image_text rows like the others.
- **Built.** The years are 24 px headings, smaller and lighter than the kit's bold years.
- **Built.** The thank-you button is the accent button of hero_text, not a grey pill.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)
- Image Breaker: connector line and dots are absolute vectors crossing the bands: draw them as a bordered narrow column with a dot image per row, or drop them

### Blog Content Highlight (B)

- **Built.** The story cards sit beside their photos instead of overlapping them.
- **Built.** The title and line over the two photo tiles moved into the captions under each photo.
- **Built.** The gift-guide band is a heading_text on the primary band with one link, under the link stack.
- **Built.** The outlined shop-all button is the light button, and the rewards strip text is larger than the kit's.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)
- Product Block 1: the card overlaps the photo by about 40 px: set them side by side (direction rtl), the card as the text cell
- Product Block 2: card overlaps the photo: side by side, direction ltr, with an id
- Product Block 3: card overlaps the photo: side by side, with an id
- Product Block 4: card overlaps the photo: side by side, with an id
- Product Block 5: card overlaps the photo: side by side, with an id
- Frame 12119: text over the photos: move title and line into the captions under each photo

### Exclusive Access Email

- **Built.** The stripes behind the logo and the card are a flat `line` band.
- **Built.** The product photo sits under the teaser and the paragraph, before the button: the card holds its heading and text in one editable area, so the photo cannot split them.
- **Built.** The card's title is 32 px, smaller than the kit's, and the button is the light button of base.html instead of grey with white text.
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

- **Built.** The strip of three product photos is one wide sample photo.
- **Built.** The hand-lettered title with its brush stroke is the headings font, and the monospace body is the body font.
- **Built.** The cream pill button is the light button of base.html.
- Hero Image: decorative display type and a brush stroke overlapping the title: set the title in the headings stack, drop the stroke or bake it into the photo; make the three photos one 600 px image
- FOOTER: three families (display, monospace, serif): keep two stacks, headings and body

### Pre-Sale Announcement (B)

- **Built.** The pattern behind the logo is the flat line band.
- **Built.** The ticket notches between the cards are an 8 px white spacer: no sample wave image joins sand to sand.
- **Built.** The headings are the 30 px heading style, much smaller than the kit's display headings, and the giant 'Thank you' is the same size as the others.
- **Built.** The three frequency choices are links in one prefooter line, not grey pills.
- **Built.** The framed photo has no white frame, and the small image under the legal links is dropped.
- Header Logo: image behind the logo: flatten logo and pattern into one image, or use a flat band color
- CTA: white on orange is borderline contrast

### Order Tracking Emails

- **Built.** The hero title is white in the heading font on the dark sample photo, not dark sans type on a light photo.
- **Built.** The ordered items keep the order_summary thumbnail size, smaller than the kit's 230 px photos, and each row shows its price.
- **Built.** The three help pills are `link_stack` pills stacked one per row, not side by side.
- **Built.** The round story photo is a square sample photo with the block's rounded corners: Outlook ignores border-radius, and no round sample exists.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); or move the title under the photo as heading_text
- Footer (story): round photo: bake the circle into the image (Outlook ignores border-radius)

### Brand Advocacy/Story

- **Built.** The sun rays behind the title are dropped, and the title is set in the heading font in ink.
- **Built.** The pull quote is an italic `h2` in its own `heading_text` between two parts of the letter.
- **Built.** The three signatures are `features` with `rules = true`: each signature image becomes a 48 px portrait above the name and role.
- Hero Banner (logo): thin sun-ray lines fan out behind logo and title (vector mask): bake them into a hosted background image or drop them

### Review Request 1

- **Built.** The logo sits on white above the photo instead of over it.
- **Built.** The five stars are star characters above the title, in the text color.
- **Built.** The body and button are `heading_text` and `button` on sand rather than `cta`, which has no paragraph style.
- **Built.** The referral card keeps the `offer` block's sand background around the card instead of white, and its give-and-get strip is the primary color.
- **Built.** The did-you-know box is a `callout` on a sand panel, not a `coupon`, so its corners are rounded and its border is the line color.
- **Built.** The photo is the wide sample, shorter than the kit's square photo.
- Hero Banner: logo over the photo: put a logo_header above the photo, or bake the logo in
- Body + CTA: stars are decoration: set them as star characters in the title

### Review Request 2

- **Built.** The decorative display face of the title and tagline is the headings stack, and the hero title is white on the dark sample.
- **Built.** The purchased piece is an inset `image` with its name link in a `heading_text`, since `product_feature` requires a button under its own photo.
- **Built.** The dashed rules are the library's solid thin `divider`.
- **Built.** The product photo is a portrait sample, not square.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); decorative display face: use the headings stack
- Footer (tagline): decorative display face: use the headings stack

### Customer Milestone Emails

- **Built.** Each heading's second line, in an accent color in the kit, takes the band's text color like the first line.
- **Built.** The social icons are the light sample icons, so they read on the dark band.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color)

### Renewal Offers

- **Built.** The photo fading into black is the dark sample photo, with no gradient.
- **Built.** The logo sits in its own black band under the photo instead of overlapping it.
- **Built.** The small uppercase heading is a `heading_text` h2 in the heading font, larger than the kit's 18 px caps.
- **Built.** The renewal button is the accent button of base.html.
- Hero Banner (photo): fade is a gradient cover: bake it into the photo
- Hero Banner (logo): logo overlaps the photo: place it in its own black band under the photo

### Year-in-Review

- **Built.** The hero title is white in the heading font on the dark sample, not tan display type on a light photo.
- **Built.** The grey page is the sand band, and the copper button, links and follow title take the primary color.
- **Built.** The row titles keep the image_text heading style, without the underline and short rule under them.
- **Built.** The two lists are bullet characters with line breaks in one paragraph, since heading_text styles no list items.
- **Built.** The row photos are near-square samples, not the kit's tall portraits.
- Hero Banner: text on photo: hosted URL and color fallback (Outlook shows the color); tan display type on a light photo is low contrast
- CTA: white on copper is low contrast
- Body: copper on light grey is low contrast

### Special Day Promotions

- **Built.** The arched photo is a square inset photo, with the logo above it instead of over it.
- **Built.** The round 20% off badge becomes the eyebrow over the sale title.
- **Built.** The two featured pieces have no vertical rule between them and use the image_pair photo size, larger than the kit's small thumbnails; the three dots are dropped.
- **Built.** The social icons sit above the legal footer, since every template ends with the footer.
- Hero Banner (photo): arch mask, logo and badge overlap the photo: bake the arch and badge into the image, or move the logo to a logo_header above and the offer into the title

### Anniversary Emails (B)

- **Built.** The header photo carries a short title, since hero_background needs one.
- **Built.** The two wave transitions are dropped: the library has no white-to-color wave, so the bands meet on a straight edge.
- **Built.** The step numbers open each row title instead of sitting in a circle over a blob-shaped photo, and the photos are square samples.
- **Built.** The tagline band has no photo corners around it.
- **Built.** The review score is text with star characters, with no review-site logo, and the app badges are two text links.
- Header: text on photo: hero_background with a hosted https URL and a color fallback; or logo_header above an image
- Image breaker 1-4: number badge overlaps the photo: bake the number into the photo or open the text with the number; bake the blob mask into each image
- Prefooter / Frame 39: photo corners around the band are overlap: drop them or make the band one image (wave) above the tagline

### Early Bird Access

- **Built.** The scalloped edge under the hero and the zigzag edge above the products are dropped: no matching wave image exists.
- **Built.** The three arched photos and the product shapes are plain photos with rounded corners.
- **Built.** Each product name sits under its photo, as product_feature places it, and shows a price.
- **Built.** The code box is the library coupon, wide with smaller type than the kit's large code.
- **Built.** The trust badges are the library's service icons with captions on sand, and a legal footer closes the email, which the kit frame lacks.
- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback; the scalloped edge needs a wave image under the hero
- Image Breaker / Shape: shape mask: bake the arches into one image with background-colored corners
- Product 1-3: shape masks: bake each shape into the product photo

### Giveaway Announcement

- **Built.** The partner logo is the partner's name as text on the right of the logo bar, with no rule between them.
- **Built.** The title is in title case in the heading font, so it fits a 320 px screen, and the enter button is the accent button.
- **Built.** The two prize cards stand straight side by side with captions under them, not rotated polaroids.
- **Built.** The guide photo has no fade, and the title starts under it.
- **Built.** The mosaic buttons sit under their photos instead of over them.
- Image Breaker: rotation and overlap: set the two cards straight, side by side; the polaroid frame becomes the caption band
- Pre-Footer / photo: the title overlaps the fade: bake the fade into the photo and start the title below it
- Frame 12863 / grid: buttons over photos: place each button under its photo

### How To Guides

- **Built.** The grey bands become the brand's soft roles: the header and the band around the guide and the subscribe panel are `line`, the guide card and the footer area are `mist`.
- **Built.** The blob-shaped guide card is a full-width `mist` band of two `image_text` rows and a `cta`, not an inset card; the subscribe card is a `callout` with straight rounded corners.
- **Built.** The hero is the dark sample photo with the title, a paragraph and the button in white.
- **Built.** The four placeholder icons are the library's line icons, each with a short label.
- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback
- Image Breaker / Title 1-2: blob-shaped card: needs an image background; use a plain tinted band instead
- Pre-Footer: blob-shaped card: plain tinted band instead

### Subscription Upsell

- **Built.** The two wavy transitions are dropped: the library has no sample wave from a photo to the accent band or from the accent band to the brand color.
- **Built.** The orange membership band is `accent`, so the primary-colored line icons and ink text read on it; the darker alternative band is `primary` with a light button.
- **Built.** The outlined rounded box around the four benefits is dropped: `steps` sits straight on the band.
- **Built.** The app store badge is a `cta` with a title and a full-width button: the library has no badge image.
- Hero Banner: text on photo: hero_background with a hosted https URL and a color fallback

### Site Abandoned

- **Built.** The script and outlined display lettering is a two-line `hero_text` title in the heading font, the first line in italic.
- **Built.** The olive body band is `line`, the closest light brand role.
- **Built.** The dripping wave into the footer is dropped: no sample wave joins `line` to `accent`. A thin `divider` opens the footer band instead.
- **Built.** The four cards are two `products_two` rows; their buttons are full-width primary buttons, not small yellow pills.
- Hero Banner: script and decorative display type: export the lettering as an image with alt text, or set it in hero_text with the heading font

### Product Education Emails

- **Built.** The thick rule under the button is the library's thin `divider` on sand.
- **Built.** The three products are `products_two` with three cards and no buttons. Their names keep the card's heading style, not small capitals.
- **Built.** The two link rows become one `prefooter` row, and the copyright sits in a `footer` on sand above the white legal lines.

### Problem Acknowledgment/Resolution

- **Built.** The discount card sits below the photo on white instead of over it, then the second button follows.
- **Built.** The brush-stroke underlines under the three footer links become `link_stack` rules: thin lines between the rows.
- **Built.** The pale grey header band is sand; the dark footer is ink.
- Hero banner / Image: the promo card sits on the photo: place it below the photo
- Footer / Frame 12251-12253: brush-stroke underline is an image: use a plain rule or bake it into each link image

### Post-Holiday Clearance Sales

- **Built.** The gradient banner is the solid `primary` band of `hero_text`, full width rather than inset, with the accent button.
- **Built.** Each staggered pair of a styled photo and a product card is one `image_text` row: the photo beside the product name, the sale price with the old price struck through and a shop button. The @handle captions and the second, smaller product photo are dropped.
- **Built.** The three grey category tiles are `features` labels on a `mist` band, not separate boxes.
- **Built.** The terms are a small flush-left `heading_text`, and the closing logo sits above the legal links inside `footer`, which must end the email.
- Hero Banner: CSS gradient fails in Outlook: a solid brand color, or a hosted gradient image with a color fallback
- Product Block / PB1-PB4: staggered offset is positioning: top-align both columns

### Urgent Flash Sales

- **Built.** `hero_background` holds one button, so the second shop button and the terms sit under the photo on white instead of on it.
- **Built.** The prices use the body font instead of the kit's monospace face, and the product names keep the card's heading style.
- **Built.** The footer logo is the `footer` block's own logo on the black band.
- Hero  Banner: text on photo: hero_background with a hosted https URL and a color fallback
- Product Block x3: monospace price face is outside the two font stacks: use the body font

### Exit Intent Discounts

- **Built.** The rotated, scattered "50% OFF!" letters are a straight `hero_text` title, much smaller than the lettering, with "Here's" as its eyebrow.
- **Built.** The light blue band is `mist` and the yellow footer is `accent`.
- **Built.** The inline code in a white box is the `coupon` block's dashed box on its own lines.
- **Built.** The footer social icons sit on their own row under the logo, not beside it: `logo_bar` takes text on its right, not images.
- Hero Image: rotated, absolutely placed letters: export the lettering as an image with alt text, or set a straight title in hero_text

### Newsletter Sign-Up Welcome Emails

- **Built.** The story card and the three value cards are `callout` panels, each with its own full-width button.
- **Built.** The green wave into the values band is dropped: no sample wave joins white to sand.
- **Built.** The circle notches on the value cards are dropped, and the photo sits above the first card on the band instead of tucked behind it.
- **Built.** The footer's two thin rules become one `divider` between the icons and the legal lines.
- Image Breaker x3: circle notch and photo overlap the card edge: drop the notch (or put an icon inside the card) and stack the photo above

### Social Media Highlight

- **Built.** The "shop now" pill on the right of the logo bar is the accent button of base.html.
- **Built.** The inset photo with the headline is a full-width `hero_background` on the dark sample, so the title is white and in the serif face, not the kit's two-tone outline type.
- **Built.** The whole email sits on the primary band; the kit's lime buttons are the accent buttons.
- Hero banner: text on photo: hero_background with a hosted https URL and a color fallback

### Referral Reminder Emails

- **Built.** The teal header is `line`, so the primary button and title read on it; the light cyan body is `mist` and the mint footer is `sand`.
- **Built.** The curved edge into the yellow tagline band is dropped: no sample wave joins `mist` to `accent`.
- **Built.** The heavy rounded sans titles are the brand's serif heading font, and the pill buttons are the library's square-cornered primary buttons.

### Affiliate Program Promotion

- **Built.** The outlined frame around the whole email is dropped: `base.html` has no inset frame.
- **Built.** The three-panel collage is one wide sample photo.
- **Built.** The checklist uses the library's line icons in place of check marks, without the rules between the rows.
- **Built.** The quote is the `testimonial` block on its sand band, with the portrait above a short quote, not an outlined box with the portrait beside the name.
- Hero Banner: overlap and gradients: flatten the collage into one image
