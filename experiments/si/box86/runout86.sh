#!/usr/bin/env bash
# L-SI box 86: regenerate instances from cfg/ into inst/ (or DIR/inst) and their outputs into out/ (or DIR/out): ana85, dec85,
# flipu85, pool85, lb84, priv84, latch86.
set -euo pipefail; cd "$(dirname "$0")"; d=${1:-.}; mkdir -p "$d/inst" "$d/out"; B=../box81
for c in cfg/*.json; do python3 -I -B lag86.py "$c" "$d/inst/$(basename "$c")"; done
L=$(ls inst/*.json | grep -v names)
for g in $L; do i=$(basename "$g" .json); python3 -I -B ../box85/ana85.py $B "$g" > "$d/out/ana_$i.out"; python3 -I -B ../box85/dec85.py $B "$g" > "$d/out/dec_$i.out"; done
python3 -I -B ../box85/flipu85.py $B $L > "$d/out/flipu85.out"; python3 -I -B ../box85/pool85.py $B $L > "$d/out/pool85.out"
python3 -I -B ../box84/m3/lb84.py $B $L > "$d/out/lb84.out"; python3 -I -B ../box84/m2/priv84.py $B $L > "$d/out/priv84.out"
python3 -I -B latch86.py $B $L > "$d/out/latch86.out"
