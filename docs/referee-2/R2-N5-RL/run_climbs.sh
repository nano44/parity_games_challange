#!/bin/bash
# REFEREE-2 succ. 8 R2-N5-RL climbs (seconds = $1, default 1200), 4 in parallel.
S=${1:-1200}; mkdir -p climb; R=../../..
python3 rl_climb.py cyc 61 8 14 $S > climb/cyc_61.txt 2>&1 &
python3 rl_climb.py cyc 62 10 18 $S > climb/cyc_62.txt 2>&1 &
python3 rl_climb.py cyc 63 0 0 $S $R/experiments/si/coarse/instances/box9/cl9_norf_a.pg > climb/cyc_63.txt 2>&1 &
python3 rl_climb.py cyc 64 0 0 $S $R/experiments/si/riselast/instances/rl_a.pg > climb/cyc_64.txt 2>&1 &
wait
