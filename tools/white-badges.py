#!/usr/bin/env python3
"""Derive white ("reverse") versions of the credential marks for the dark hero.

Alpha is taken from how DARK each pixel is, so the internal shapes of each mark
survive instead of collapsing into a silhouette. Colour is discarded entirely —
these read as one ink, which is the point on a film frame.
"""
from PIL import Image
import pathlib, sys

SRC = pathlib.Path("src/public/img/badges")
GAMMA = {"abps": 0.60, "asps": 0.48, "acs": 0.68}   # <1 lifts; the ASPS ring is a
                                                    # mid-tone teal and washes out otherwise
FLOOR = {"abps": 0.06, "asps": 0.06, "acs": 0.14}   # ignore near-white paper

for slug in ("abps", "asps", "acs"):
    for tag in ("", "@2x"):
        p = SRC / f"{slug}{tag}.png"
        if not p.exists():
            sys.exit(f"missing {p}")
        im = Image.open(p).convert("RGBA")
        w, h = im.size
        px = im.load()
        out = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        op = out.load()
        g, floor = GAMMA[slug], FLOOR[slug]
        for y in range(h):
            for x in range(w):
                r, gg, b, a = px[x, y]
                if a == 0:
                    continue
                lum = (0.2126 * r + 0.7152 * gg + 0.0722 * b) / 255.0
                v = 1.0 - lum                     # dark ink -> opaque white
                if v < floor:
                    continue
                v = ((v - floor) / (1.0 - floor)) ** g
                op[x, y] = (255, 255, 255, int(round(min(1.0, v) * (a / 255.0) * 255)))
        out.save(SRC / f"{slug}-w{tag}.png", optimize=True)
    print(f"{slug}-w.png written")
