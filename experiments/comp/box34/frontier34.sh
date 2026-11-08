#!/bin/bash
# L-COMP box 34 (b'): inverse frontier chains (shrink34.py). A chain shrinks for the highest target first, then seeds each lower target
# with the previous result (a genome with C >= t+1 has C >= t). Usage: frontier34.sh NAME SEEDFILE KIND(C|m) HI LO RNG [POLISH]
cd "$(dirname "$0")" || exit 1
NAME=$1; SEED=$2; KIND=$3; HI=$4; LO=$5; RNG=$6; POL=${7:-3}
mkdir -p out/frontier/log; cur=$SEED
for t in $(seq $HI -1 $LO); do
  out=out/frontier/log/${NAME}_${KIND}${t}.txt
  if ! grep -q '^FINAL' "$out" 2>/dev/null; then nice python3 shrink34.py "$cur" ${KIND}${t} $RNG "$out" --polish $POL || { echo "FAIL $out"; exit 1; }; fi
  cur=$(grep '^FINAL' "$out" | tail -1 | sed 's/.* frozen //'); grep '^FINAL' "$out" | tail -1 | cut -c1-140
done
