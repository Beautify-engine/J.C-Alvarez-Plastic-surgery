#!/bin/bash
# Portrait (9:16) hero cut. Same edit as the desktop version — all cuts, no
# dissolves — with each shot cropped on its own column, because a 9:16 crop shows
# only ~32% of the frame and one object-position cannot serve five setups (D-039).
# Where the BODY is the subject (the marking, the result) the crop centres the body.
set -euo pipefail
IN="assets/hero vid.mp4"
CW=1215                    # 2160 * 9/16

SEGS=(
  "0.10  2.70  0.58"   # marking — the marked abdomen and his gloved hand
  "2.70  5.10  0.38"   # studio two-shot — patient left, him right
  "5.10  6.87  0.58"   # pre-op, him with the chart
  "6.87  8.75  0.50"   # at the desk
  "13.35 14.80 0.60"   # the result — the body is the subject
)

CHAIN=""; LABELS=""; n=0
for s in "${SEGS[@]}"; do
  read -r st en p <<< "$s"
  X=$(python3 -c "print(int((3840-$CW)*$p))")
  CHAIN+="[0:v]trim=${st}:${en},setpts=PTS-STARTPTS,crop=${CW}:2160:${X}:0,scale=608:1080,fps=25,settb=AVTB[s${n}];"
  LABELS+="[s${n}]"; n=$((n+1))
done
CHAIN+="${LABELS}concat=n=${n}:v=1:a=0,format=yuv420p[v]"

ffmpeg -y -v error -i "$IN" -filter_complex "$CHAIN" -map "[v]" -an \
  -c:v libx264 -crf 30 -preset slow -movflags +faststart src/public/video/hero-m-608.mp4
ffmpeg -y -v error -i src/public/video/hero-m-608.mp4 -an \
  -c:v libvpx-vp9 -crf 42 -b:v 0 -row-mt 1 -deadline good -cpu-used 2 \
  src/public/video/hero-m-608.webm
ffmpeg -y -v error -i src/public/video/hero-m-608.mp4 -frames:v 1 -q:v 5 \
  src/public/img/hero-poster-m.jpg
