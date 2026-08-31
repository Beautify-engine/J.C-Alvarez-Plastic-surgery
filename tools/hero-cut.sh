#!/bin/bash
# Desktop hero loop from assets/hero vid.mp4 (3840x2160, 14.85s).
#
# ALL CUTS, NO DISSOLVES. The source's own scene changes (2.70 / 5.10 / 6.87) play
# through as hard cuts, so adding a dissolve into the result and another at the loop
# gave the piece two different grammars — four cuts and two fades — which reads as
# arbitrary rather than designed. A cut from the result back to the marking shot is
# a cut between two unrelated scenes: it reads as an edit, not as the glitch that
# D-038 fixed (that was a jump cut WITHIN one shot, which is a different thing).
#
#   A: 0.10 -> 8.75   marking, studio two-shot, pre-op, desk
#   B: 13.35 -> 14.80 the result
#   8.83 -> 13.30 excluded: intraoperative, open draped abdomen (see D-054).
set -euo pipefail
IN="assets/hero vid.mp4"

CHAIN="\
[0:v]trim=0.10:8.75,setpts=PTS-STARTPTS,scale=1760:-2,fps=25,settb=AVTB[a];\
[0:v]trim=13.35:14.80,setpts=PTS-STARTPTS,scale=1760:-2,fps=25,settb=AVTB[b];\
[a][b]concat=n=2:v=1:a=0,format=yuv420p[v]"

ffmpeg -y -v error -i "$IN" -filter_complex "$CHAIN" -map "[v]" -an \
  -c:v libx264 -crf 28 -preset slow -movflags +faststart src/public/video/hero-1920.mp4
ffmpeg -y -v error -i src/public/video/hero-1920.mp4 -vf scale=1600:-2 -an \
  -c:v libvpx-vp9 -crf 40 -b:v 0 -row-mt 1 -deadline good -cpu-used 2 \
  src/public/video/hero-1600.webm
ffmpeg -y -v error -i src/public/video/hero-1920.mp4 -vf scale=1280:-2 -an \
  -c:v libx264 -crf 30 -preset slow -movflags +faststart src/public/video/hero-1280.mp4
ffmpeg -y -v error -i src/public/video/hero-1920.mp4 -frames:v 1 -q:v 4 -vf scale=1600:-2 \
  src/public/img/hero-poster.jpg
