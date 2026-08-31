#!/usr/bin/env python3
"""Extract before/after halves from his slide exports, preserving native framing.

Earlier attempt forced a 4:5 crop after scaling and clipped heads. Instead: detect each
photo's bounding box, then letterbox it into a fixed box so nothing is ever cut.
"""
import subprocess, os, json
SRC="assets/_raw/cases"; OUT="src/public/img/cases"; G=200
BOX=(600,750)

def gray(path):
    raw=subprocess.run(["ffmpeg","-v","error","-i",path,"-vf",
        f"crop=iw*0.945:ih*0.945:iw*0.0275:ih*0.0275,scale={G}:{G}",
        "-f","rawvideo","-pix_fmt","gray","-"],capture_output=True).stdout
    return [raw[y*G:(y+1)*G] for y in range(G)] if len(raw)==G*G else None

# On face slides his "Before"/"After" text sits INSIDE the photo area (top-left /
# bottom-right), not at the outer edge, so the detected box has to be trimmed further.
FACE={'rhinoplasty','eyelid-surgery','facelift'}

def bbox(rows, x_lo, x_hi, y_lo=0.11, thr=30):
    xs0,xs1=int(G*x_lo),int(G*x_hi); ys0=int(G*y_lo)
    cols=[x for x in range(xs0,xs1) if sum(1 for y in range(ys0,G) if rows[y][x]>thr)>(G-ys0)*0.05]
    rws =[y for y in range(ys0,G)   if sum(1 for x in range(xs0,xs1) if rows[y][x]>thr)>(xs1-xs0)*0.05]
    if not cols or not rws: return None
    pad=1
    x0=max(xs0,min(cols)-pad); x1=min(xs1-1,max(cols)+pad)
    y0=max(ys0,min(rws)-pad);  y1=min(G-1,max(rws)+pad)
    if x1-x0<20 or y1-y0<20: return None
    return (x0/G,y0/G,(x1-x0)/G,(y1-y0)/G)

def cut(src,out,b):
    x,y,w,h=b; W,H=BOX
    vf=(f"crop=iw*0.945:ih*0.945:iw*0.0275:ih*0.0275,"
        f"crop=iw*{w:.4f}:ih*{h:.4f}:iw*{x:.4f}:ih*{y:.4f},"
        f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black")
    subprocess.run(["ffmpeg","-v","error","-i",src,"-vf",vf,"-q:v","4",out,"-y"],check=True)

m=json.load(open('/tmp/casemap.json')); os.makedirs(OUT,exist_ok=True)
pairs={}; ok=0
for slug,files in m.items():
    pairs[slug]=[]
    for i,fn in enumerate(sorted(files),1):
        src=os.path.join(SRC,fn); rows=gray(src)
        if not rows: continue
        bb=bbox(rows,0.09,0.49); ba=bbox(rows,0.51,0.91)
        if not bb or not ba: continue
        if slug in FACE:
            def trim(b, top=0.15, bot=0.15):
                x,y,w,h=b
                return (x, y+h*top, w, h*(1-top-bot))
            bb=trim(bb); ba=trim(ba)
        try:
            cut(src,f"{OUT}/{slug}-{i:02d}-b.jpg",bb)
            cut(src,f"{OUT}/{slug}-{i:02d}-a.jpg",ba)
            pairs[slug].append(i); ok+=1
        except subprocess.CalledProcessError: pass
json.dump(pairs,open('/tmp/pairs.json','w'),indent=1)
print("pairs:",ok,"| by procedure:",{k:len(v) for k,v in pairs.items()})
