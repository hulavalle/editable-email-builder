"""Regenerates the sample images of the library (eeb/library/img): abstract placeholders, free of any rights.
Run from the repo root: python3 tools/make-example-images.py  (needs Pillow and Playwright)."""

import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter

SRC, IMG = os.path.join("tools", "example-src"), os.path.join("eeb", "library", "img")


def scene(path, size, sky, sea, sun, sun_at=(0.62, 0.18)):
    w, h = size
    img = Image.new("RGB", size, sky[0])
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        draw.line([(0, y), (w, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(sky[0], sky[1])))
    x, y = sun_at
    draw.ellipse([w * x, h * y, w * x + h * 0.22, h * (y + 0.22)], fill=sun)
    draw.rectangle([0, h * 0.62, w, h], fill=sea)
    draw.polygon([(0, h * 0.62), (w * 0.35, h * 0.48), (w * 0.7, h * 0.62)], fill=tuple(c - 25 for c in sea))
    img.filter(ImageFilter.GaussianBlur(1)).save(path)


def main():
    os.makedirs(IMG, exist_ok=True)
    tmp = os.path.join(SRC, "tmp.png")
    jobs = [
        ("hero-photo.jpg", (1200, 760), ((242, 214, 186), (214, 160, 128)), (46, 98, 112), (255, 236, 200), "1200"),
        ("offer-photo.jpg", (1012, 606), ((226, 232, 236), (190, 204, 214)), (120, 150, 160), (250, 250, 245), "1012"),
        ("product-one.jpg", (320, 370), ((186, 214, 232), (120, 170, 200)), (40, 90, 110), (255, 245, 220), "320"),
        ("product-two.jpg", (320, 370), ((240, 220, 200), (210, 170, 140)), (150, 110, 90), (255, 240, 210), "320"),
        ("product-three.jpg", (320, 370), ((210, 226, 214), (160, 190, 170)), (70, 110, 90), (250, 250, 230), "320"),
        ("product-four.jpg", (560, 560), ((236, 226, 214), (214, 196, 176)), (120, 96, 80), (250, 244, 232), "560"),
        ("product-wide.jpg", (1200, 800), ((228, 236, 238), (196, 214, 220)), (40, 90, 110), (255, 250, 236), "1200"),
        ("story-one.jpg", (520, 520), ((246, 226, 206), (226, 186, 150)), (150, 90, 70), (255, 240, 220), "520"),
        ("story-two.jpg", (520, 520), ((214, 228, 240), (170, 196, 220)), (60, 100, 140), (250, 250, 255), "520"),
        ("event-photo.jpg", (1200, 700), ((44, 62, 80), (90, 110, 130)), (20, 40, 56), (255, 214, 140), "1200"),
        ("portrait.jpg", (200, 200), ((230, 214, 196), (200, 170, 140)), (110, 80, 60), (250, 236, 220), "200"),
    ]
    for name, size, sky, sea, sun, width in jobs:
        scene(tmp, size, sky, sea, sun)
        run("image", tmp, os.path.join(IMG, name), "--width", width)
    # A dark photo for white text on top: the sun sets behind the sea, away from the title.
    scene(tmp, (1200, 1400), ((24, 38, 54), (58, 78, 98)), (16, 30, 42), (236, 196, 140), sun_at=(0.70, 0.56))
    run("image", tmp, os.path.join(IMG, "hero-dark.jpg"), "--width", "1200")
    os.remove(tmp)
    run("image", os.path.join(SRC, "logo.svg"), os.path.join(IMG, "logo.png"), "--width", "336")
    run("image", os.path.join(SRC, "logo-dark.svg"), os.path.join(IMG, "logo-dark.png"), "--width", "336")
    for name in sorted(os.listdir(os.path.join(SRC, "svg"))):
        run("image", os.path.join(SRC, "svg", name), os.path.join(IMG, name.replace(".svg", ".png")), "--width", "128")
    run("image", os.path.join(SRC, "wave-sand-ink.svg"), os.path.join(IMG, "wave-sand-ink.png"), "--width", "1200")
    run("image", os.path.join(SRC, "wave-ink-white.svg"), os.path.join(IMG, "wave-ink-white.png"), "--width", "1200")


def run(*args):
    subprocess.run([sys.executable, "-m", "eeb", *args], check=True)


if __name__ == "__main__":
    main()
