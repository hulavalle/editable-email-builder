"""SVG sources of the library's neutral icons: feature icons and social placeholders."""

INK, WHITE = "#13293d", "#ffffff"

def svg(body, size=64, bg="none"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 64 64"><rect width="64" height="64" fill="{bg}"/>{body}</svg>'

FEATURES = {
    "icon-truck": '<path d="M8 20h30v22H8zM38 28h10l8 8v6H38z" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/><circle cx="18" cy="46" r="5" fill="#fff" stroke="#1d4e5f" stroke-width="3"/><circle cx="46" cy="46" r="5" fill="#fff" stroke="#1d4e5f" stroke-width="3"/>',
    "icon-leaf": '<path d="M14 50C14 26 30 14 52 12c-2 22-14 38-38 38z" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/><path d="M14 50L36 28" stroke="#1d4e5f" stroke-width="3" stroke-linecap="round"/>',
    "icon-shield": '<path d="M32 8l20 8v14c0 13-9 22-20 26-11-4-20-13-20-26V16z" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/><path d="M23 32l6 6 12-13" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "icon-gift": '<rect x="12" y="26" width="40" height="26" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/><rect x="9" y="18" width="46" height="9" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/><path d="M32 18v34" stroke="#1d4e5f" stroke-width="3"/><path d="M32 18c-4-8-14-10-14-4s10 4 14 4zM32 18c4-8 14-10 14-4s-10 4-14 4z" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/>',
    "icon-heart": '<path d="M32 52S10 38 10 24a11 11 0 0 1 22-3 11 11 0 0 1 22 3c0 14-22 28-22 28z" fill="none" stroke="#1d4e5f" stroke-width="3" stroke-linejoin="round"/>',
}

SOCIAL = {
    "social-one": '<circle cx="32" cy="32" r="30" fill="#13293d"/><rect x="20" y="20" width="24" height="24" rx="7" fill="none" stroke="#fff" stroke-width="3"/><circle cx="32" cy="32" r="6" fill="none" stroke="#fff" stroke-width="3"/>',
    "social-two": '<circle cx="32" cy="32" r="30" fill="#13293d"/><path d="M35 50V34h6l1-7h-7v-4c0-2 1-3 3-3h4v-6h-6c-6 0-8 4-8 9v4h-5v7h5v16z" fill="#fff"/>',
    "social-three": '<circle cx="32" cy="32" r="30" fill="#13293d"/><path d="M21 21l22 22M43 21L21 43" stroke="#fff" stroke-width="4" stroke-linecap="round"/>',
    "social-four": '<circle cx="32" cy="32" r="30" fill="#13293d"/><rect x="17" y="22" width="30" height="20" rx="6" fill="#fff"/><path d="M29 27v10l9-5z" fill="#13293d"/>',
}
