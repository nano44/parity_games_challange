#!/bin/bash
# REFEREE-2 succ. 7 climbs for R2-N5-FRZ (seconds per climb = $1, default 900). Seeds: library files (inputs only) and random games.
S=${1:-900}; X=../../../experiments
mkdir -p climb
J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 1; done; }
job; python3 frz_climb.py block 11 0 0 $S $X/n5-exhaustive/instances/b6_xw_n32.pg > climb/block_11.txt 2>&1 &
job; python3 frz_climb.py block 12 0 0 $S $X/new/box28/instances/fb32_inr2_final.pg > climb/block_12.txt 2>&1 &
job; python3 frz_climb.py low 21 5 9 $S > climb/low_21.txt 2>&1 &
job; python3 frz_climb.py fb 31 0 0 $S $X/n5-exhaustive/instances/b6_xl2_n32.pg > climb/fb_31.txt 2>&1 &
job; python3 frz_climb.py block 13 0 0 $S $X/red/xing/instances/fbref_cex_n32.pg > climb/block_13.txt 2>&1 &
job; python3 frz_climb.py low 22 0 0 $S $X/red/xing/instances/j10_n24.pg > climb/low_22.txt 2>&1 &
job; python3 frz_climb.py fb 32 0 0 $S $X/red/xing/instances/j8_n32.pg > climb/fb_32.txt 2>&1 &
job; python3 frz_climb.py low 23 8 14 $S > climb/low_23.txt 2>&1 &
wait
