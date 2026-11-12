#!/usr/bin/env bash
# L-SI box 101: Lemma LAM-GAP counters on random one-player games (lamgap101.py; VJ engine L-RED 65 own.py at claude/l-red 59daaef2, env RED).
# (1) seed 1, 3000 games n <= 9, opt / path checks at n <= 7; (2) seed 2 same; (3) seed 3, 2000 games n <= 40 (gap / length only);
# controls: CTRL=1 (bound |Ch| / 2, must fire), PCTRL=1 (paths with <= k + 1 choices, must fire). Output: out/
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red"
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 59daaef2 experiments/red | tar -x -C "$T/red" || exit 3
export RED="$T/red"
python3 -I lamgap101.py 1 3000 9 7 > out/lamgap_s1.out || exit 1
python3 -I lamgap101.py 2 3000 9 7 > out/lamgap_s2.out || exit 1
python3 -I lamgap101.py 3 2000 40 0 > out/lamgap_s3_n40.out || exit 1
CTRL=1 python3 -I lamgap101.py 1 3000 9 7 > out/lamgap_ctrl.out || exit 1
PCTRL=1 python3 -I lamgap101.py 2 3000 9 7 > out/lamgap_pctrl.out || exit 1
echo DONE
