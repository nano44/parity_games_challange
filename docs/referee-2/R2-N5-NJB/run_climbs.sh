#!/bin/bash
# REFEREE-2 succ. 7 climbs for R2-N5-NJB (seconds each = $1, default 600). Seeds: lane climb bests (inputs only).
S=${1:-600}; X=../../../experiments/si/coarse/instances/box9; mkdir -p climb
J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 1; done; }
job; python3 njb_climb.py mn 71 0 0 $S $X/cl9_mn_a.pg > climb/mn_71.txt 2>&1 &
job; python3 njb_climb.py mn 72 0 0 $S $X/cl9_rep_a.pg > climb/mn_72.txt 2>&1 &
job; python3 njb_climb.py norf 73 0 0 $S $X/cl9_norf_a.pg > climb/norf_73.txt 2>&1 &
job; python3 njb_climb.py dirty 74 0 0 $S $X/cl9_rep_b.pg > climb/dirty_74.txt 2>&1 &
job; python3 njb_climb.py norf 75 0 0 $S $X/cl9_norf_b.pg > climb/norf_75.txt 2>&1 &
job; python3 njb_climb.py mn 76 0 0 $S $X/cl9_mn_b.pg > climb/mn_76.txt 2>&1 &
job; python3 njb_climb.py dirty 77 8 16 $S > climb/dirty_77.txt 2>&1 &
job; python3 njb_climb.py norf 78 8 16 $S > climb/norf_78.txt 2>&1 &
wait
