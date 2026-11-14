#!/usr/bin/env bash
# L-SI box 74 self-check (~15 s): the realised m = 3 genomes replay with L-NEW's Gen (flip-free F = 7 in a 7-step run; F = 10 in a
# 10-step run with 2 external bit changes; top pair flips at every step); frame mode flips at m = 2 reproduces F_max = 4 (K 0),
# 6 (K 2: F >= 7 UNSAT), 7 (K unlimited: F >= 8 UNSAT) (needs python-sat; skipped without it).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
o=$(python3 -I replayflip.py out/fl7_m3_s2.json); [ "${o%% stored*}" = "T 7 F 7" ]
o=$(python3 -I replayflip.py out/fl10_K2_m3_s1.json); [ "${o%% stored*}" = "T 10 F 10" ]
echo "box 74 realised flip genomes: PASS"
python3 -I -c "import pysat" 2>/dev/null || { echo "box 74: python-sat missing, frame controls skipped"; exit 0; }
r() { local o; o=$(K=$1 python3 -I ../box70/frame.py 2 flips $2 $3); printf '%s\n' "$o" | grep -o -- "-> [A-Z]*" | head -n 1; }
[ "$(r 0 4 4)" = "-> SAT" ]; [ "$(r 2 7 6)" = "-> SAT" ]; [ "$(r 2 7 7)" = "-> UNSAT" ]; [ "$(r -1 9 7)" = "-> SAT" ]; [ "$(r -1 9 8)" = "-> UNSAT" ]
echo "box 74 frame flips controls: PASS"
