"""Regenerates the images of templates/example: abstract placeholders, free of any rights.
Run from the repo root: python3 tools/make-example-images.py  (needs Pillow and Playwright)."""

import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.join("templates", "example")
SRC, IMG = os.path.join(HERE, "src"), os.path.join(HERE, "img")


def scene(path, size, sky, sea, sun):
    w, h = size
    img = Image.new("RGB", size, sky[0])
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        draw.line([(0, y), (w, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(sky[0], sky[1])))
    draw.ellipse([w * 0.62, h * 0.18, w * 0.62 + h * 0.22, h * 0.40], fill=sun)
    draw.rectangle([0, h * 0.62, w, h], fill=sea)
    draw.polygon([(0, h * 0.62), (w * 0.35, h * 0.48), (w * 0.7, h * 0.62)], fill=tuple(c - 25 for c in sea))
    img.filter(ImageFilter.GaussianBlur(1)).save(path)


def main():
    os.makedirs(IMG, exist_ok=True)
    tmp = os.path.join(HERE, "src", "tmp.png")
    jobs = [
        ("hero-photo.jpg", (1200, 760), ((242, 214, 186), (214, 160, 128)), (46, 98, 112), (255, 236, 200), "1200"),
        ("offer-photo.jpg", (1012, 606), ((226, 232, 236), (190, 204, 214)), (120, 150, 160), (250, 250, 245), "1012"),
        ("product-one.jpg", (320, 370), ((186, 214, 232), (120, 170, 200)), (40, 90, 110), (255, 245, 220), "320"),
        ("product-two.jpg", (320, 370), ((240, 220, 200), (210, 170, 140)), (150, 110, 90), (255, 240, 210), "320"),
        ("product-three.jpg", (320, 370), ((210, 226, 214), (160, 190, 170)), (70, 110, 90), (250, 250, 230), "320"),
    ]
    for name, size, sky, sea, sun, width in jobs:
        scene(tmp, size, sky, sea, sun)
        run("image", tmp, os.path.join(IMG, name), "--width", width)
    os.remove(tmp)
    run("image", os.path.join(SRC, "logo.svg"), os.path.join(IMG, "logo.png"), "--width", "336")
    run("image", os.path.join(SRC, "wave-sand-ink.svg"), os.path.join(IMG, "wave-sand-ink.png"), "--width", "1200")
    run("image", os.path.join(SRC, "wave-ink-white.svg"), os.path.join(IMG, "wave-ink-white.png"), "--width", "1200")


def run(*args):
    subprocess.run([sys.executable, "-m", "eeb", *args], check=True)


if __name__ == "__main__":
    main()
