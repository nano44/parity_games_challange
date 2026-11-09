#!/usr/bin/env bash
# L-SI box 93: only the K6 two-engine rows of run93.sh (same pins). Output: out/k6_own.out, out/k6_g3.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
K6=$(ls k6/inst/*.json | grep -v names)
python3 -I ../box91/mult91.py own $K6 > out/k6_own.out || exit 1
python3 -I ../box91/mult91.py g3 $K6 > out/k6_g3.out || exit 1
echo DONE-K6
