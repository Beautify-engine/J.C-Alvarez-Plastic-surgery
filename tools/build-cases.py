#!/usr/bin/env python3
"""Export whole before/after slides as single square case images.

Supersedes split-cases.py. That tool cut each slide into a left/right pair, but the
halves were letterboxed independently and stopped being comparable — different scale,
different framing, black gaps. The slides were composed as a unit by whoever made them,
with matching scale and their own Before/After labels, so they are used whole.
"""
import json, os, subprocess
SRC, OUT = 'assets/_raw/cases', 'src/public/img/cases'
m = json.load(open('content/case-map.json'))
os.makedirs(OUT, exist_ok=True)
for old in os.listdir(OUT):
    if old.endswith(('-a.jpg', '-b.jpg')):
        os.remove(os.path.join(OUT, old))
n = 0
for slug, files in m.items():
    for i, fn in enumerate(sorted(files, key=lambda f: int(''.join(c for c in f if c.isdigit()))), 1):
        src = os.path.join(SRC, fn)
        for w, q, suffix in ((1000, '4', ''), (300, '5', '-t')):
            subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vf',
                            f'scale={w}:{w}:flags=lanczos', '-q:v', q,
                            f'{OUT}/{slug}-{i:02d}{suffix}.jpg', '-y'], check=True)
        n += 1
print('cases exported:', n)
