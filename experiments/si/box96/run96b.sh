#!/usr/bin/env bash
# L-SI box 96, control CTRL=nopad (exceptions without the pe pads of level-0 e's) on both engines, 4 of the 19 instances. Output: out/nopad96.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
L="../box91/inst/WC4_2.json ../box91/inst/C6G8_n54.json ../box93/inst/k1fail_202.json ../box93/inst/MWR4_2.json"
{ CTRL=nopad python3 -I d96.py own $L; CTRL=nopad python3 -I d96.py g3 $L; } > out/nopad96.out || exit 1
echo DONE
