#!/usr/bin/env bash
# L-SI box 91: extract the pinned engines (pins.txt) with git archive and run mult91 on both engines + controls. Output: out/*.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
L="inst/WC4_2.json inst/WC16_2.json inst/FW8_2.json inst/FW16_2.json inst/MW8_2.json inst/MW32_2.json inst/C6G8_n54.json inst/RWX_n95.json inst/DWT20_2803.json inst/DHIB26_2804.json inst/DHIB18_2805.json"
python3 -I mult91.py own $L > out/own91.out || exit 1
python3 -I mult91.py g3 $L > out/g391.out || exit 1
{ for c in a0 pre gr uz; do CTRL=$c python3 -I mult91.py own inst/MW8_2.json inst/C6G8_n54.json | sed "s/^own/ctrl=$c own/"; done; } > out/ctrl91.out || exit 1
echo DONE
