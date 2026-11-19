# Add an email platform

An adapter owns everything one platform needs. Blocks, templates and the core lint stay the same.

## Find out first

Answer these from the platform's documentation before you write code:

1. How does it mark an editable region, a label, a repeatable block, a variant and a hideable block? Which of these does it lack?
2. Can its style panel edit CSS from the template? With which syntax?
3. What is the merge tag for each token in `eeb/adapters/__init__.py`: subject, preview text, unsubscribe link, preferences link, browser view link, postal address, permission reminder, company and year?
4. How does it import a template: pasted HTML, a zip, an API? Which limits apply to size, file names and folders?
5. Which images does the import upload, and which must already be hosted?

## Steps

1. Copy `eeb/adapters/mailchimp.py` to `eeb/adapters/<name>.py`.
2. Fill `TOKENS` with the platform's merge tags. `eeb/adapters/__init__.py` refuses an adapter that leaves a token out.
3. Write `translate()`: neutral annotations to the platform's syntax. When the platform has no equivalent, remove the annotation and say so in the adapter's docstring.
4. Write `RULES` and `check()` for what the platform requires of the HTML it receives. Give each rule an id with the platform's prefix.
5. Write `package()`: the file the platform imports.
6. Register the module in `ADAPTERS` in `eeb/adapters/__init__.py`.
7. Add a planted case for each new rule in `tests/test_rules.py`, and a check that the example template builds clean with `--esp <name>`.
8. Write `docs/<name>.md` with what no rule can check.
