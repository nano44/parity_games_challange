#!/usr/bin/env bash
# L-SI box 99: scc99 (local Howard length per SCC of D(G); CONJECTURE SCC-LIN) on box 91's 11, box 93's 8, box 98's 7 climb bests and 600
# random genomes (rand191.rgen seed 9901). Engine pin l-new fcba92fc. Output: out/
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T" || exit 3
export ROOT="$T"
I=../box91/inst; J=../box93/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/k1fail_202.json $J/Ku_4.json $J/Ku_8.json $J/Ku_16.json $J/Kprev_8.json $J/MWR4_2.json $J/MWR8_2.json $J/MWR16_2.json $(ls ../box98/inst/C98_*.json)"
python3 -I scc99.py inst $L > out/inst99.out || exit 1
python3 -I scc99.py rand 9901 600 > out/rand99.out || exit 1
echo DONE
