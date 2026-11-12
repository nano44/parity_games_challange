#!/usr/bin/env bash
# L-SI box 100: trace (MWR4_2 full), interval decomposition (iv100) and TWO-CROSS counters (cross100) on box 99's 26 instances + 400 random
# genomes (rand191.rgen seed 10001), plus the CTRL=1 control on 3 instances; cross100 with CMAX=3 (deep = flips charged to depth > 3). Engines (read-only, extracted at run time): L-RED 65 how3_232 at
# claude/l-red 59daaef2 (env RED); L-NEW Gamma3 / rand191 at claude/l-new fcba92fc (env LNEW). Output: out/
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red" "$T/new"
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 59daaef2 experiments/red | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/new" || exit 3
export RED="$T/red" LNEW="$T/new"
I=../box91/inst; J=../box93/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/k1fail_202.json $J/Ku_4.json $J/Ku_8.json $J/Ku_16.json $J/Kprev_8.json $J/MWR4_2.json $J/MWR8_2.json $J/MWR16_2.json $(ls ../box98/inst/C98_*.json)"
python3 -I trace100.py $J/MWR4_2.json > out/trace_MWR4_2.out || exit 1
python3 -I iv100.py $L > out/iv100.out || exit 1
CMAX=3 python3 -I cross100.py inst $L > out/cross100_inst.out || exit 1
CTRL=1 CMAX=3 python3 -I cross100.py inst $J/MWR4_2.json ../box98/inst/C98_4_5_3.json $I/C6G8_n54.json > out/cross100_ctrl.out || exit 1
CMAX=3 python3 -I cross100.py rand 10001 400 > out/cross100_rand.out || exit 1
echo DONE
