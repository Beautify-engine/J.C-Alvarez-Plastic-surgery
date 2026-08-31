#!/bin/bash
# Site image treatment — warm editorial grade + halation bloom + film grain.
#   ./tools/grade.sh photo.jpg          standard
#   ./tools/grade.sh photo.jpg air      hazier, lifted blacks  (light bands)
#   ./tools/grade.sh photo.jpg deep     deeper blacks          (dark bands, hero, gallery)
#   ./tools/grade.sh folder/ air        batch a whole folder
#   ./tools/grade.sh warm.jpg air -n   neutralise an already-warm source first
set -e
# -n / --neutralize : grey-world white balance BEFORE grading. Use on sources that are
# already warm (tungsten, wood, golden hour) so the grade does not stack into orange.
NEUTRALIZE=0
ARGS=()
for a in "$@"; do
  case "$a" in
    -n|--neutralize) NEUTRALIZE=1 ;;
    *) ARGS+=("$a") ;;
  esac
done
IN="${ARGS[0]}"; P="${ARGS[1]:-standard}"
LUT="design/lut/jc-grade-$P.cube"
[ -f "$LUT" ] || { echo "grade must be: clean | clean-deep | air | standard | deep | band | cool | cool-deep"; exit 1; }

#            bloom  blur  grain
case "$P" in
  air)      BL=0.55; SIG=40; GR=16; TH=0.55 ;;
  standard) BL=0.46; SIG=32; GR=14; TH=0.55 ;;
  deep)     BL=0.34; SIG=24; GR=11; TH=0.58 ;;
  band)     BL=0.30; SIG=22; GR=11; TH=0.58 ;;
  clean)      BL=0.24; SIG=30; GR=12; TH=0.80 ;;
  clean-deep) BL=0.20; SIG=26; GR=11; TH=0.82 ;;
  cool)      BL=0.16; SIG=34; GR=12; TH=0.74 ;;
  cool-deep) BL=0.13; SIG=26; GR=10; TH=0.76 ;;
esac

case "$P" in
  cool|cool-deep) CB="rs=-0.05:gs=0.01:bs=0.09" ;;
  clean|clean-deep) CB="rs=0.02:gs=0.01:bs=0.00" ;;
  *) CB="rs=0.14:gs=0.04:bs=-0.07" ;;
esac
CHAIN="lut3d=$LUT,split=2[base][hi];\
[hi]curves=all='0/0 $TH/0 1/1',gblur=sigma=$SIG,colorbalance=$CB[glow];\
[base][glow]blend=all_mode=screen:all_opacity=$BL,\
noise=alls=$GR:allf=t+u,format=yuv420p"

# grey-world: average the frame to one pixel, derive per-channel gain toward neutral
wb_prefix(){
  local px gains r g b avg
  px=$(ffmpeg -v error -i "$1" -vf "scale=1:1" -f rawvideo -pix_fmt rgb24 - 2>/dev/null | xxd -p | head -c 6)
  r=$((16#${px:0:2})); g=$((16#${px:2:2})); b=$((16#${px:4:2}))
  [ "$r" -eq 0 ] && r=1; [ "$g" -eq 0 ] && g=1; [ "$b" -eq 0 ] && b=1
  avg=$(( (r+g+b)/3 ))
  # damped correction (0.75) so we neutralise the cast without killing the mood
  awk -v r=$r -v g=$g -v b=$b -v a=$avg 'BEGIN{
    d=0.75
    fr=1+((a/r)-1)*d; fg=1+((a/g)-1)*d; fb=1+((a/b)-1)*d
    printf "colorchannelmixer=rr=%.4f:gg=%.4f:bb=%.4f,", fr, fg, fb }'
}

run(){
  local pre=""
  [ "$NEUTRALIZE" = "1" ] && pre="$(wb_prefix "$1")"
  ffmpeg -v error -i "$1" -vf "${pre}${CHAIN}" -q:v 2 "$2" -y
}

if [ -d "$IN" ]; then
  OUT="$IN/graded-$P"; mkdir -p "$OUT"
  shopt -s nullglob nocaseglob
  for f in "$IN"/*.{jpg,jpeg,png,webp,tif,tiff}; do
    run "$f" "$OUT/$(basename "${f%.*}").jpg" && echo "  ✓ $(basename "$f")"
  done
  echo "→ $OUT"
else
  run "$IN" "${IN%.*}-$P.jpg" && echo "→ ${IN%.*}-$P.jpg"
fi
