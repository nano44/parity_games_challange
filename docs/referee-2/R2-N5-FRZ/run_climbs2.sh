#!/bin/bash
# REFEREE-2 succ. 7 climbs, wave 2 (wave 1 = run_climbs.sh first four; its second four were killed by a session time limit and re-run here).
S=${1:-600}; X=../../../experiments
J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 1; done; }
job; python3 frz_climb.py leave 41 0 0 $S climb/best_block_11.pg > climb/leave_41.txt 2>&1 &
job; python3 frz_climb.py leave 42 0 0 $S $X/n5-exhaustive/instances/b6_xw_n40.pg > climb/leave_42.txt 2>&1 &
job; python3 frz_climb.py block 13 0 0 $S $X/red/xing/instances/fbref_cex_n32.pg > climb/block_13.txt 2>&1 &
job; python3 frz_climb.py fb 32 0 0 $S $X/red/xing/instances/j8_n32.pg > climb/fb_32.txt 2>&1 &
job; python3 frz_climb.py low 22 0 0 $S $X/red/xing/instances/j10_n24.pg > climb/low_22.txt 2>&1 &
job; python3 frz_climb.py low 23 8 14 $S > climb/low_23.txt 2>&1 &
job; python3 frz_climb.py leave 43 0 0 $S climb/best_fb_31.pg > climb/leave_43.txt 2>&1 &
job; python3 frz_climb.py fb 33 0 0 $S $X/new/box28/instances/x32_sc32_final.pg > climb/fb_33.txt 2>&1 &
wait
