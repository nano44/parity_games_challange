#!/usr/bin/env bash
# REFEREE s33: the nine firing controls of wrap_replay.py, 300 random games each (family rand, seed 3310, n <= 8), both modes.
cd "$(dirname "$0")"; mkdir -p wrap_logs
for c in 1 2 3 4 5 6 7 8 9; do for mode in xi spec; do
  CTRL=$c python3 -I wrap_replay.py $mode rand 3310 300 8 > wrap_logs/ctrl_${c}_${mode}.out 2>&1
done; done
echo "ctrl done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
