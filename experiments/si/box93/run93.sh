#!/usr/bin/env bash
# L-SI box 93: np93 (K7: NP-SHAPE / E-FACE-PAYS) on both engines (pins as box91/pins.txt) over box 91's frozen instances, L-NEW's
# k1fail_202 and the K7 probe genomes (inst/, SHA1SUMS); control CTRL=swap. Output: out/*.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
I=../box91/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json inst/k1fail_202.json inst/Ku_8.json inst/Ku_16.json inst/Kprev_8.json"
python3 -I np93.py own $L > out/own93.out || exit 1
python3 -I ../box91/mult91.py own inst/Ku_4.json inst/Ku_8.json inst/Ku_16.json inst/Kprev_8.json > out/probe93_own.out || exit 1
{ for c in swap tight; do CTRL=$c python3 -I np93.py own $I/MW8_2.json $I/C6G8_n54.json | sed "s/^own/ctrl=$c own/"; done; } > out/ctrl93.out || exit 1
python3 -I np93.py g3 $L > out/g393.out || exit 1
python3 -I ../box91/mult91.py g3 inst/Ku_4.json inst/Ku_8.json inst/Ku_16.json inst/Kprev_8.json > out/probe93_g3.out || exit 1
echo DONE
# K6 towers (h = 4, 5) on both engines: T3, C (mult91)
K6=$(ls k6/inst/*.json | grep -v names)
python3 -I ../box91/mult91.py own $K6 > out/k6_own.out || exit 1
python3 -I ../box91/mult91.py g3 $K6 > out/k6_g3.out || exit 1
echo DONE-K6
