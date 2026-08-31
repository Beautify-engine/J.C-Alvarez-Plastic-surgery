#!/usr/bin/env python3
"""Crop the credential badges to their content box and export web sizes.

The source PNGs are 1080x1350 with the mark floating in a sea of white or
transparency. Nothing is recoloured: ABPS and ASPS both publish usage terms
that forbid altering their certification marks.
"""
from PIL import Image
import pathlib

SRC = pathlib.Path("assets/Badges")
OUT = pathlib.Path("src/public/img/badges"); OUT.mkdir(parents=True, exist_ok=True)
NAMES = {"17.png": "abps", "16.png": "asps", "Untitled design (1).png": "acs"}
HEIGHTS = (72, 144)          # 1x and 2x for a ~72px display height

def content_box(im, tol=248):
    """Bounding box of pixels that are neither transparent nor near-white."""
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    x0, y0, x1, y1 = w, h, -1, -1
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 16:                       # transparent
                continue
            if r >= tol and g >= tol and b >= tol:   # near-white
                continue
            if x < x0: x0 = x
            if y < y0: y0 = y
            if x > x1: x1 = x
            if y > y1: y1 = y
    return (x0, y0, x1 + 1, y1 + 1) if x1 >= 0 else None

for fn, slug in NAMES.items():
    p = SRC / fn
    if not p.exists():
        print(f"missing {p}"); continue
    im = Image.open(p).convert("RGBA")
    box = content_box(im)
    if not box:
        print(f"{fn}: no content found"); continue
    # 3% breathing room so the mark is not flush to its own edge
    pad = int(max(box[2] - box[0], box[3] - box[1]) * 0.03)
    box = (max(0, box[0] - pad), max(0, box[1] - pad),
           min(im.width, box[2] + pad), min(im.height, box[3] + pad))
    cropped = im.crop(box)
    for hgt in HEIGHTS:
        wid = round(cropped.width * hgt / cropped.height)
        tag = "" if hgt == HEIGHTS[0] else "@2x"
        out = OUT / f"{slug}{tag}.png"
        cropped.resize((wid, hgt), Image.LANCZOS).save(out, optimize=True)
    print(f"{slug:5s} {im.size} -> crop {cropped.size}  ratio {cropped.width/cropped.height:.2f}")
