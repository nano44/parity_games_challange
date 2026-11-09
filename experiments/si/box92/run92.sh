#!/usr/bin/env bash
# L-SI box 92: gate92 (GATE-LOW-NULL) on both engines (pins as box91/pins.txt) over box 91's frozen instances + control. Output: out/*.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
I=../box91/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json"
python3 -I gate92.py own $L > out/own92.out || exit 1
python3 -I gate92.py g3 $L > out/g392.out || exit 1
CTRL=low python3 -I gate92.py own $I/MW8_2.json $I/C6G8_n54.json | sed 's/^own/ctrl=low own/' > out/ctrl92.out || exit 1
echo DONE
