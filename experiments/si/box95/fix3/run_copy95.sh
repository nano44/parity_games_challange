#!/usr/bin/env bash
# L-SI fixes entry 3 D-4: copy95 (copy rows as sets) on box 94's 22 frozen instances, both engines. Output: out/copy95_{own,g3}.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
A=""; for f in $(ls ../../box94/inst/*.json | grep -v names); do A="$A $f ${f%.json}.names.json"; done
python3 -I copy95.py own $A > out/copy95_own.out || exit 1
python3 -I copy95.py g3 $A > out/copy95_g3.out || exit 1
echo DONE
