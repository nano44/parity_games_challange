#!/bin/bash
# REFEREE-2 succ. 7 climbs for R2-N5-L2 (seconds each = $1, default 600).
S=${1:-600}; X=../../../experiments; mkdir -p climb
J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 1; done; }
job; python3 l2_climb.py frz 51 4 7 $S > climb/frz_51.txt 2>&1 &
job; python3 l2_climb.py frz 52 0 0 $S $X/new/box34/instances/onedrop_cex_n32.pg > climb/frz_52.txt 2>&1 &
job; python3 l2_climb.py tog 61 5 12 $S > climb/tog_61.txt 2>&1 &
job; python3 l2_climb.py tog 62 0 0 $S $X/new/box34/instances/oneh_cex_n32.pg > climb/tog_62.txt 2>&1 &
job; python3 l2_climb.py frz 53 6 10 $S > climb/frz_53.txt 2>&1 &
job; python3 l2_climb.py tog 63 0 0 $S $X/new/box34/instances/onedrop_cex_n32.pg > climb/tog_63.txt 2>&1 &
wait
