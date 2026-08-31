#!/usr/bin/env python3
"""Square card thumbnails for the booking-page procedure selector.

The selector renders each photograph at roughly 170 CSS px, so the 600w
procedure-page derivatives were about double what any screen could use and made
/book the heaviest page on the site. This centre-crops each source to 1:1 — the
shape the card already displays via object-fit — and writes 340w and 510w WebP,
which is 1x and 1.5x-to-2x for that box.

Sources are the graded 4:5 derivatives in img/procedures/. Idempotent: re-running
overwrites. Run after any change to the procedure photography set.
"""
import os, glob
from PIL import Image

SRC = "src/public/img/procedures"
SLUGS = ["tummy-tuck", "bbl", "skinny-bbl", "hd-liposuction", "breast-augmentation",
         "breast-lift", "breast-lift-aug", "facelift", "rhinoplasty", "eyelid-surgery",
         "scarless-eyelid"]
WIDTHS = [340, 510]

total_before = total_after = 0
for slug in SLUGS:
    src = os.path.join(SRC, f"{slug}-600.jpg")
    if not os.path.isfile(src):
        raise SystemExit(f"missing source: {src}")
    total_before += os.path.getsize(src)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    side = min(w, h)
    # centre horizontally; bias the vertical crop upward, since these are torso and
    # face photographs where the subject sits above centre
    left = (w - side) // 2
    top = max(0, int((h - side) * 0.38))
    sq = im.crop((left, top, left + side, top + side))
    for out_w in WIDTHS:
        out = os.path.join(SRC, f"{slug}-card-{out_w}.webp")
        sq.resize((out_w, out_w), Image.LANCZOS).save(out, "WEBP", quality=78, method=6)
        total_after += os.path.getsize(out)

print(f"11 sources {total_before/1024:.0f}kb  ->  {len(WIDTHS)*11} thumbs {total_after/1024:.0f}kb")
