#!/usr/bin/env bash
# L-SI box 102: DEEP3's exact quantity (internal gates after t0, e-depth), Lemma PROPAGATE and CORE-ABOVE counters (deep102.py) on box 99's
# 26 instances and 400 random genomes (rand191.rgen seed 10001); control PCTRL=1 (other face's target; propfail must fire) on 3 instances.
# Engines (read-only, extracted at run time): L-RED 65 how3_232 at claude/l-red 59daaef2 (env RED); L-NEW at claude/l-new fcba92fc (env LNEW).
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
python3 -I deep102.py inst $L > out/deep102_inst.out || exit 1
PCTRL=1 python3 -I deep102.py inst $J/MWR4_2.json $I/DHIB26_2804.json $I/DWT20_2803.json > out/deep102_ctrl.out || exit 1
python3 -I deep102.py rand 10001 400 > out/deep102_rand.out || exit 1
echo DONE
