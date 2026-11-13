#!/usr/bin/env bash
# L-SI box 98: asc98 (ascents, D^tot_E, U) on both engines over box 91's 11 + box 93's 8 frozen instances. Output: out/asc98_{own,g3}.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
I=../box91/inst; J=../box93/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/k1fail_202.json $J/Ku_4.json $J/Ku_8.json $J/Ku_16.json $J/Kprev_8.json $J/MWR4_2.json $J/MWR8_2.json $J/MWR16_2.json"
python3 -I asc98.py own $L > out/asc98_own.out || exit 1
python3 -I asc98.py g3 $L > out/asc98_g3.out || exit 1
echo DONE
