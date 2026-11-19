# Set up a client repo

A client repo holds only what belongs to the client: its brand, its emails and any block the library does not have. Everything else comes from the library inside `eeb/`.

## Before you start

- Gather the client's design system: brand colors, the dark text color, the page background, the fonts.
- Decide the email platform. Today only Mailchimp has an adapter.

## Steps

1. Create the repo and copy the engine into it. Pin the commit you copied, so an update is a decision:

	```sh
	mkdir client-emails && cd client-emails && git init
	git -C ~/editable-email-builder archive HEAD eeb | tar -x
	```

2. Copy the example brand and open it:

	```sh
	python3 -m eeb init
	```

3. Map the client's design system onto the roles in `brand.toml`. Keep the role names: every block uses them.

	| Role | What it paints |
	|---|---|
	| `primary` | Strips, bands, primary buttons, headings on light backgrounds |
	| `accent` | Thin rules, the accent button, the numbers in `stats`, the stars in `rating` |
	| `ink` | Body text, dark bands, the footer |
	| `sand` | The page background and soft sections |
	| `mist` | Light buttons on dark bands |
	| `line` | Dividers and table rules |
	| `white` | Cards and text on dark colors |
	| `black` | Fine card borders |

	Put a color the client does not have on the closest one it has. Check that white on `primary` and `ink` on `accent` reach 4.5:1: the test `test_every_button_is_readable` shows how.

4. Start each email from a library template:

	```sh
	python3 -m eeb templates
	python3 -m eeb new spring-sale --from promotion
	```

	The copy keeps the library's sample images (`library:hero-photo.jpg`) so it builds right away. Replace them with the client's images, prepared with `python3 -m eeb image`.

5. Replace the texts and the links. A copied template does not build until its links point at the client's site: rule C4 rejects the placeholder domain.

6. Build and look at it:

	```sh
	python3 -m eeb preview spring-sale
	```

## When the library is not enough

- **A section the library does not have.** Write a block in the client's `blocks/` folder. Follow [Blocks](blocks.md). If other clients would use it, add it to the library instead.
- **A library block that needs a change for this client.** Copy it to the client's `blocks/` with the same name. The client's copy wins. Keep the editable names, or campaigns already in the platform lose their content.
- **A fix to the engine or a library block.** Make it in `editable-email-builder`, then copy `eeb/` into each client repo again.
