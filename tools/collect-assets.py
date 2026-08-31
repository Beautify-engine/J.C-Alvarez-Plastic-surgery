#!/usr/bin/env python3
"""Copy every asset the GHL export references into one uploadable folder.

Independently re-scans the built blobs rather than trusting ASSETS.txt, so a path
the exporter failed to record shows up here as a discrepancy instead of as a 404
three weeks later.
"""
import pathlib, re, shutil, sys

SRC = pathlib.Path('src/public')
GHL = pathlib.Path('dist/ghl')
OUT = pathlib.Path('dist/ghl-assets')

# independent scan of the exported blobs
found = set()
for f in GHL.rglob('*.html'):
    t = f.read_text()
    for m in re.finditer(r'ASSET_BASE_URL(/(?:img|video|fonts)/[^\s"\',)]+)', t):
        found.add(m.group(1))

listed = {l.strip() for l in (GHL / 'ASSETS.txt').read_text().splitlines() if l.strip()}
if found - listed:
    print('! in the pages but missing from ASSETS.txt:', sorted(found - listed), file=sys.stderr)
if listed - found:
    print('! listed but not referenced by any page:', sorted(listed - found)[:5], file=sys.stderr)

paths = sorted(found | listed)
if OUT.exists():
    shutil.rmtree(OUT)

copied, missing, total = 0, [], 0
for rel in paths:
    src = SRC / rel.lstrip('/')
    if not src.exists():
        missing.append(rel)
        continue
    dst = OUT / rel.lstrip('/')
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    copied += 1
    total += dst.stat().st_size

print(f'copied {copied} files -> {OUT}/  ({total/1024/1024:.1f} MB)')
if missing:
    print(f'\n!! {len(missing)} referenced files DO NOT EXIST on disk:', file=sys.stderr)
    for m in missing:
        print('   ', m, file=sys.stderr)
    sys.exit(1)

by = {}
for f in OUT.rglob('*'):
    if f.is_file():
        k = f.relative_to(OUT).parts[0] + '/' + (f.relative_to(OUT).parts[1] if len(f.relative_to(OUT).parts) > 2 else '')
        by[k] = by.get(k, [0, 0])
        by[k][0] += 1
        by[k][1] += f.stat().st_size
print()
for k in sorted(by):
    n, sz = by[k]
    print(f'  {k:24s} {n:4d} files  {sz/1024/1024:6.2f} MB')
