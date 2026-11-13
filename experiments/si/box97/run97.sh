#!/usr/bin/env bash
# L-SI box 97: std97 ([STD3] on N5'-xi's run before the first fallback) on box 91's 11 + box 93's 8 frozen instances and 600 random
# genomes (rand191.rgen, seed 9701, d 1-5, w 1-3, degree 2-3); control CTRL=post on two instances. Engine pin: l-new fcba92fc. Output: out/
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T" || exit 3
export ROOT="$T"
I=../box91/inst; J=../box93/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/k1fail_202.json $J/Ku_4.json $J/Ku_8.json $J/Ku_16.json $J/Kprev_8.json $J/MWR4_2.json $J/MWR8_2.json $J/MWR16_2.json"
python3 -I std97.py inst $L > out/inst97.out || exit 1
CTRL=post python3 -I std97.py inst $J/MWR4_2.json $I/C6G8_n54.json > out/ctrl97.out || exit 1
python3 -I std97.py rand 9701 600 > out/rand97.out || exit 1
echo DONE
