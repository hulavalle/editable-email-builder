"""Email platform adapters. An adapter owns everything one platform needs and nothing else:

- TOKENS: the platform's merge tag for each {{esp.*}} token the blocks use;
- translate(): neutral annotations (data-edit, data-repeat, data-hide, /* @group */, /* @editable */)
  into the platform's own syntax;
- RULES and check(): what the platform requires of the HTML it receives;
- package(): the file the platform imports.

To add a platform, copy mailchimp.py, fill those four parts and register it below.
docs/adding-an-adapter.md lists what to find out about the platform first.
"""

from . import mailchimp

ADAPTERS = {"mailchimp": mailchimp}

# Every {{esp.*}} token a block or a template may use. Each adapter maps all of them.
TOKENS = (
    "subject", "preview", "unsubscribe_url", "preferences_url", "archive_url",
    "address", "permission_reminder", "company", "year",
)


def get(name):
    if name not in ADAPTERS:
        from ..compose import BuildError
        raise BuildError(f"unknown platform `{name}`. Available: {', '.join(sorted(ADAPTERS))}", 2)
    adapter = ADAPTERS[name]
    missing = set(TOKENS) - set(adapter.TOKENS)
    if missing:
        from ..compose import BuildError
        raise BuildError(f"the {name} adapter does not map {', '.join(sorted(missing))}", 1)
    return adapter
