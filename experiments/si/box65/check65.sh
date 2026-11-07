#!/usr/bin/env bash
# L-SI box 65 self-check (~10 s): GAIN-IND (IND 0) and pinned one-flip gains on the L-NEW witnesses; bfg.c (copy of L-COMP bfk.c +
# GAIN hook) gives g*(1) = 2; the committed m = 2 enumeration outputs say g*(2) = 4 in both parts.
set -euo pipefail
cd "$(dirname "$0")"
o=$(python3 -I gain.py ../box64/wit/*.json)
echo "$o" | grep -q "TOTAL IND 0"
echo "$o" | grep -q "^kf1_d4_t10.json {'m': 3, 'g': 5, 'GJ': {1: 5, 2: 4, 3: 1}"
echo "$o" | grep -q "^iso_d2_3.json {'m': 1, 'g': 2, 'GJ': {1: 2}"
# frozen champions (pin/, sha1 in pin/pins.sha1; out/ holds live climb outputs and is NOT pinned)
sha1sum -c --quiet pin/pins.sha1
p=$(python3 -I gain.py pin/*.json)
echo "$p" | grep -q "TOTAL IND 0"
echo "$p" | grep -q "^j1_m3_s1.json {'m': 3, 'g': 7, 'GJ': {1: 7, 2: 5, 3: 5}"
echo "$p" | grep -q "^g_m4_s2.json {'m': 4, 'g': 9,"
echo "$p" | grep -q "^j1_m5_s1.json {'m': 5, 'g': 11,"
# independent replay with L-NEW's box 150 Gen: ONE-FLIP-2M kill (gain 7 > 6 at m 3)
python3 -I replay_g.py pin/j1_m3_s1.json "[1,0,0,1,1,0]" 1 | grep -q "gain 7$"
if command -v gcc >/dev/null; then gcc -O2 -DKMAX=1 -o bfg_check bfg.c && ./bfg_check 1 0 1 | grep -q "GAIN g\*(1) part 0/1 = 2" && rm -f bfg_check; fi
[ "$(grep -h 'GAIN g\*(2)' out/bfg_m2_p0.txt out/bfg_m2_p1.txt | awk '{print $NF}' | sort -u)" = "4" ]
echo "box 65 gain: PASS"
