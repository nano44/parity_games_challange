#!/usr/bin/env bash
# L-SI box 93 K6: the box 86 LAG TOWER at h = 4, 5 (cfg in k6/cfg, built with box86/lag86.py, measured with the box 84-86 tools on the
# box81 IDEAL-CYC reference; output dir arg or k6/). Read-only use of box81 / box84 / box85 / box86 files.
set -euo pipefail; cd "$(dirname "$0")"; d=${1:-.}; mkdir -p "$d/inst" "$d/out"; B=../../box81
for c in cfg/*.json; do python3 -I -B ../../box86/lag86.py "$c" "$d/inst/$(basename "$c")"; done
L=$(ls "$d"/inst/*.json | grep -v names)
for g in $L; do i=$(basename "$g" .json); python3 -I -B ../../box85/ana85.py $B "$g" > "$d/out/ana_$i.out"; python3 -I -B ../../box85/dec85.py $B "$g" > "$d/out/dec_$i.out"; done
python3 -I -B ../../box85/flipu85.py $B $L > "$d/out/flipu85.out"; python3 -I -B ../../box85/pool85.py $B $L > "$d/out/pool85.out"
python3 -I -B ../../box84/m3/lb84.py $B $L > "$d/out/lb84.out"; python3 -I -B ../../box84/m2/priv84.py $B $L > "$d/out/priv84.out"
python3 -I -B ../../box86/latch86.py $B $L > "$d/out/latch86.out"
