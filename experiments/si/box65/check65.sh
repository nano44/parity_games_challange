#!/usr/bin/env bash
# L-SI box 65 self-check (~10 s): GAIN-IND (IND 0) and pinned one-flip gains on the L-NEW witnesses; bfg.c (copy of L-COMP bfk.c +
# GAIN hook) gives g*(1) = 2; the committed m = 2 enumeration outputs say g*(2) = 4 in both parts.
set -euo pipefail
cd "$(dirname "$0")"
o=$(python3 -I gain.py ../box64/wit/*.json)
echo "$o" | grep -q "TOTAL IND 0"
echo "$o" | grep -q "^kf1_d4_t10.json {'m': 3, 'g': 5, 'GJ': {1: 5, 2: 4, 3: 1}"
echo "$o" | grep -q "^iso_d2_3.json {'m': 1, 'g': 2, 'GJ': {1: 2}"
python3 -I gain.py out/j1_m3_s1.json | grep -q "'g': 6, 'GJ': {1: 6"
if command -v gcc >/dev/null; then gcc -O2 -DKMAX=1 -o bfg_check bfg.c && ./bfg_check 1 0 1 | grep -q "GAIN g\*(1) part 0/1 = 2" && rm -f bfg_check; fi
[ "$(grep -h 'GAIN g\*(2)' out/bfg_m2_p0.txt out/bfg_m2_p1.txt | awk '{print $NF}' | sort -u)" = "4" ]
echo "box 65 gain: PASS"
