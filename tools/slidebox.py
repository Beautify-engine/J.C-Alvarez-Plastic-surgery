#!/usr/bin/env python3
"""Find each slide's content bounding box: the slides are letterboxed on black with a
title band and baked-in labels, and the layout differs between face and body cases,
so a single fixed crop cannot work across all 68."""
import subprocess, sys
W=H=200
def box(p, thr=26, pad=2):
    raw=subprocess.run(["ffmpeg","-v","error","-i",p,"-vf",f"scale={W}:{H}",
                        "-f","rawvideo","-pix_fmt","gray","-"],capture_output=True).stdout
    if not raw: return None
    rows=[raw[y*W:(y+1)*W] for y in range(H)]
    ys=[y for y,r in enumerate(rows) if sum(1 for v in r if v>thr) > W*0.06]
    xs=[x for x in range(W) if sum(1 for y in range(H) if rows[y][x]>thr) > H*0.06]
    if not ys or not xs: return None
    y0,y1=max(0,min(ys)-pad),min(H-1,max(ys)+pad)
    x0,x1=max(0,min(xs)-pad),min(W-1,max(xs)+pad)
    return (x0/W, y0/H, (x1-x0)/W, (y1-y0)/H)
for p in sys.argv[1:]:
    b=box(p)
    print(f"  {p.split('/')[-1]:<16} " + (f"x={b[0]:.3f} y={b[1]:.3f} w={b[2]:.3f} h={b[3]:.3f}  aspect={b[2]/b[3]:.2f}" if b else "no content"))
