#!/usr/bin/env bash
# L-SI box 100: L1 probe (one-player Howard length in G_C[sbar], Odd fixed) on the one-giant-SCC instances of box 99's 26 (seed 100, K = 3
# random face maps, S = 2 random starts per face map, both tie rules). Engine L-RED 65 at claude/l-red 59daaef2 (env RED). Output: out/l1probe100.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red" "$T/new"
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 59daaef2 experiments/red | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/new" || exit 3
export RED="$T/red" LNEW="$T/new"
I=../box91/inst; J=../box93/inst
python3 -I l1probe100.py 100 3 2 $(ls ../box98/inst/C98_*.json) $J/MWR4_2.json $J/MWR8_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB18_2805.json $I/DHIB26_2804.json $J/MWR16_2.json > out/l1probe100.out || exit 1
echo DONE
