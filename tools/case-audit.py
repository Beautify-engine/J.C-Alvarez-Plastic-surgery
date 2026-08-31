#!/usr/bin/env python3
"""Contact sheet of every before/after pair, for a human angle-match check.

split-cases.py extracted the left and right halves of his presentation slides.
Where a slide carried two different views, that produces a pair whose before and
after are shot from different angles — which is misleading in a medical
before/after, regardless of intent. This cannot be reliably auto-detected, so it
gets eyeballed.
"""
import os, re, collections, pathlib
from PIL import Image, ImageDraw

D = pathlib.Path('src/public/img/cases')
OUT = pathlib.Path('design/case-audit')
OUT.mkdir(parents=True, exist_ok=True)

found = collections.defaultdict(set)
for f in os.listdir(D):
    m = re.match(r'(.+)-(\d+)-([ab])\.jpg$', f)
    if m: found[m.group(1)].add(m.group(2))

pairs = [(s, n) for s in sorted(found) for n in sorted(found[s])]
CW, CH, LBL, COLS = 132, 165, 18, 5
rows = (len(pairs) + COLS - 1) // COLS
W, H = CW * 2 * COLS, (CH + LBL) * rows
sheet = Image.new('RGB', (W, H), (16, 16, 16))
d = ImageDraw.Draw(sheet)

for i, (slug, n) in enumerate(pairs):
    cx, cy = (i % COLS) * CW * 2, (i // COLS) * (CH + LBL)
    for j, side in enumerate(('b', 'a')):
        im = Image.open(D / f'{slug}-{n}-{side}.jpg').convert('RGB').resize((CW, CH))
        sheet.paste(im, (cx + j * CW, cy))
    d.rectangle([cx + CW - 1, cy, cx + CW, cy + CH], fill=(230, 120, 60))
    d.text((cx + 3, cy + CH + 3), f'{slug}-{n}', fill=(200, 200, 200))

sheet.save(OUT / 'all-pairs.jpg', quality=90)
print(f'{len(pairs)} pairs -> design/case-audit/all-pairs.jpg  {sheet.size}')
