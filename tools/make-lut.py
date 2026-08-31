#!/usr/bin/env python3
"""Site colour grade — warm editorial haze (Hims/Hers register), tuned to the token set.
Highlights resolve to --paper #f7f6f3. Shadows lift to a warm matte, never pure black."""
import sys
N=33
# name: (black point, white point, saturation, contrast, tint weight, highlight rolloff, tint target)
PRESETS={
 # --- warm family (portraits, team, facility, light bands) ---
 'air':      ((0.115,0.106,0.104), (0.968,0.962,0.953), 0.82, 0.10, 0.045, 0.22, (0.87,0.835,0.78), 0.12),
 'standard': ((0.082,0.076,0.076), (0.968,0.962,0.953), 0.80, 0.16, 0.038, 0.17, (0.87,0.835,0.78), 0.12),
 'deep':     ((0.046,0.048,0.052), (0.959,0.954,0.946), 0.76, 0.24, 0.030, 0.12, (0.87,0.835,0.78), 0.12),
 # black point == --ink #16232a, for full-bleed images that dissolve into the dark band
 'band':     ((0.086,0.137,0.165), (0.959,0.954,0.946), 0.78, 0.20, 0.032, 0.14, (0.87,0.835,0.78), 0.12),
 # --- clean family: NATURAL colour. No desaturation. Polish comes from contrast,
 #     a whisper of black lift, grain and bloom — not from draining the colour out. ---
 'clean':     ((0.055,0.056,0.060), (0.960,0.955,0.946), 1.05, 0.34, 0.010, 0.22, (0.88,0.84,0.79), 0.42, 0.16, 0.20),
 'clean-deep':((0.040,0.042,0.048), (0.952,0.948,0.940), 1.06, 0.40, 0.008, 0.18, (0.88,0.84,0.79), 0.42, 0.20, 0.16),
 # --- cool family (clinical, calm, cooler cast) ---
 'cool':     ((0.062,0.078,0.094), (0.945,0.954,0.961), 0.94, 0.30, 0.026, 0.34, (0.86,0.80,0.73), 0.20),
 'cool-deep':((0.034,0.046,0.060), (0.940,0.950,0.958), 0.92, 0.36, 0.022, 0.30, (0.86,0.80,0.73), 0.20),
}

SH=(0.36,0.46,0.52)   # shadow tint  — cool slate, pulls toward --ink family
HL=(1.00,0.975,0.93)  # highlight tint — warm ivory, pulls toward --paper
def smoothstep(x): return x*x*(3-2*x)
def build(name):
    BLK,WHT,SAT,CON,TINTW,ROLL,TINT,CLAMP=PRESETS[name][:8]
    SPLIT_S,SPLIT_H=(PRESETS[name][8:10] or (0.0,0.0)) if len(PRESETS[name])>8 else (0.0,0.0)
    out=['TITLE "JC Alvarez — %s"'%name,f'LUT_3D_SIZE {N}','DOMAIN_MIN 0 0 0','DOMAIN_MAX 1 1 1','']
    for bi in range(N):
        for gi in range(N):
            for ri in range(N):
                r,g,b=ri/(N-1),gi/(N-1),bi/(N-1)
                luma=0.2126*r+0.7152*g+0.0722*b
                # desaturate, keeping warmth
                r=luma+(r-luma)*SAT; g=luma+(g-luma)*SAT; b=luma+(b-luma)*SAT
                # gentle S-curve — low, haze means low contrast
                v=[]
                for c in (r,g,b):
                    c=max(0.,min(1.,c)); v.append(c*(1-CON)+smoothstep(c)*CON)
                r,g,b=v
                # split tone — cool shadows, warm highlights. This is what reads as "a grade"
                # without touching saturation. Weighted so midtones (skin) stay untouched.
                sw=((1.0-luma)**2)*SPLIT_S
                hw=(luma**2)*SPLIT_H
                r+=(SH[0]-r)*sw; g+=(SH[1]-g)*sw; b+=(SH[2]-b)*sw
                r+=(HL[0]-r)*hw; g+=(HL[1]-g)*hw; b+=(HL[2]-b)*hw
                # midtone tint push toward the preset's target (skin stays alive)
                mid=1.0-abs(luma-0.45)*2.0
                w=TINTW*max(0.,mid)
                r+= (TINT[0]-r)*w; g+=(TINT[1]-g)*w; b+=(TINT[2]-b)*w
                # cast guard: compress any excessive channel spread, warm OR cool
                sp=abs(r-b)-CLAMP
                if sp>0:
                    if r>b: r-=sp*0.62; b+=sp*0.30
                    else:   b-=sp*0.62; r+=sp*0.30
                    g-=sp*0.06
                # highlight rolloff — compress the top so nothing clips harshly
                res=[]
                for c,lo,hi in ((r,BLK[0],WHT[0]),(g,BLK[1],WHT[1]),(b,BLK[2],WHT[2])):
                    c=max(0.,min(1.,c))
                    c=c-ROLL*max(0.,c-0.72)*(c-0.72)/0.28
                    res.append(max(0.,min(1., lo+(hi-lo)*c)))
                out.append("%.6f %.6f %.6f"%tuple(res))
    open(f'design/lut/jc-grade-{name}.cube','w').write('\n'.join(out)+'\n')
    print(f"  wrote jc-grade-{name}.cube")
for n in PRESETS: build(n)
