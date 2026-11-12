#!/bin/bash
# L-COMP box 38 item 2: U-constrained T3 climbs (climb38.py SCORE T3, KONE 0) in fixed N + M bands. Resumable (climb38 OUT.state; a log
# with DONE is skipped). Seeds: U = 0 form of gen37(n) (every upward Xi-option -> K0): out/lad/g/g37n4_down_greedy_U0.json (N + M 145),
# inst/gen37_n9_U0.json (N + M 290).
cd "$(dirname "$0")"
run() { [ -f out/climb38_$1.log ] && grep -q DONE out/climb38_$1.log && return; python3 climb38.py $1 $2 $3 $4 $5 $6 out/climb38_$1.log T3 $8 0 "${@:9}"; }
S1=out/lad/g/g37n4_down_greedy_U0.json; S2=inst/gen37_n9_U0.json
for B in 0 2 -1; do run L150B${B} 140 160 6 1500 382 - $B $S1; done
for B in 0 2 -1; do run L290B${B} 280 300 4 800 383 - $B $S2; done
echo CLDONE
