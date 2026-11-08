#!/usr/bin/env bash
# L-SI box 88: the MIRROR towers HP6b, HP7b, HP8b (box84/pair84.py, MUP = 1). Lane lengths are an untuned extrapolation of HP4_mup's
# (HP2-5_mup were tuned per h in box 84); HP6b was the best of three h = 6 guesses (maxk 4). Run from experiments/si/box88; byte-equal to inst/.
set -euo pipefail
cd "$(dirname "$0")/.."; t=$(mktemp -d)
python3 -I -B ../box84/pair84.py 6 1,3,9,19,30,45 7,10,30,40,60 $t/HP6b.json 1
python3 -I -B ../box84/pair84.py 7 1,3,9,19,30,45,63 7,10,30,40,60,85 $t/HP7b.json 1
python3 -I -B ../box84/pair84.py 8 1,3,9,19,30,45,63,84 7,10,30,40,60,85,112 $t/HP8b.json 1
for f in HP6b HP7b HP8b; do cmp $t/$f.json inst/$f.json; cmp $t/$f.names.json inst/$f.names.json; done; rm -rf "$t"; echo "HPb rebuild: SAME"
