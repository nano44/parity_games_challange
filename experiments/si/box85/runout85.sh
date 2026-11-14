#!/usr/bin/env bash
# L-SI box 85: (re)compute the outputs of every frozen instance into DIR (default out/): ana85, dec85, flipu85, pool85, lb84, priv84.
set -euo pipefail; cd "$(dirname "$0")"; d=${1:-out}; B=../box81
for g in inst/*.json; do case $g in *.names.json) continue;; esac; i=$(basename "$g" .json)
  python3 -I -B ana85.py $B "$g" > "$d/ana_$i.out"; python3 -I -B dec85.py $B "$g" > "$d/dec_$i.out"
done
ls inst/*.json | grep -v names > "$d/.list"
python3 -I -B flipu85.py $B $(cat "$d/.list") > "$d/flipu85.out"; python3 -I -B pool85.py $B $(cat "$d/.list") > "$d/pool85.out"
python3 -I -B ../box84/m3/lb84.py $B $(cat "$d/.list") > "$d/lb84.out"; python3 -I -B ../box84/m2/priv84.py $B $(cat "$d/.list") > "$d/priv84.out"
rm -f "$d/.list"
