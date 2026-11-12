#!/usr/bin/env bash
# L-SI box 105, D1: key105.py (the direct simulator of KEY(G*)) validated against N5 (box190 n5v.py mode spec) from S3 on Gamma3*(G*).
# Engines read-only by git archive: claude/l-new fcba92fc (experiments/new, si.py, harness, hard-families, n5-second), claude/l-red
# 8c01d40e (r217, for box104/free104.py's imports). Outputs out/key_rand.out, out/key_ctrl.out, out/key_json.out, out/quotes105.out.
# About 10 min, one core.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red" BOX104="${BOX104:-$SI/box104}"
python3 -I key105.py rand 1051 2000 4 3 3 > out/key_rand.out || exit 1
python3 -I key105.py rand 1052 1000 6 4 3 >> out/key_rand.out || exit 1
python3 -I key105.py rand 1053 1000 8 2 2 >> out/key_rand.out || exit 1
CTRL=1 python3 -I key105.py rand 1051 200 4 3 3 > out/key_ctrl.out || exit 1
I=$SI/box91/inst; J=$SI/box93/inst
python3 -I key105.py json $I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/*.json $SI/box98/inst/C98_*.json > out/key_json.out || exit 1
(cd "$TOP" && python3 -I "$OLDPWD/quotes105.py" src) > out/quotes105.out || exit 1
echo DONE
