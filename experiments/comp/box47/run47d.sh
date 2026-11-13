#!/bin/bash
# L-COMP box 47: search lanes, second runner (run47c.sh is kept unchanged while lane K32 runs it). search47 + one47.h (the 1P(G) port), compiled
# per lane into bin/search47_<LANE> (a running binary is never overwritten). SCORE=K: score (k_A6, kfront, T), BEST lines also log khalf.
# Lanes (Lead 10:03Z priority: K lanes, then the min-d ladder, then T lanes):
#   K28 / K36 / K40: HIT7 (box 212's HIT7_d28_F254) lifted by 0 / 8 / 12 TOP-ADD pad levels (lift47.py; my lift, not L-RED's file);
#   L<d>: min-d ladder at depth d, seed = rand47.py (w 2, degree 2, seed 4800 + d), N + M <= 6 d + 40;
#   T<N>: objective T_key, seed HIT7 lifted to N movers.
# Each launch runs ~6,600 s, then exits; re-launch resumes (OUT.state). Usage: run47d.sh LANE
set -u; cd "$(dirname "$0")"; mkdir -p out/lanes inst/seeds bin; L=$1
gcc -O2 -Wno-unused-function -Wno-misleading-indentation -I. -DMODEL='"one47.h"' -o bin/search47_$L search47.c -lm || exit 1
lift() { local out=inst/seeds/$3; [ -f $out.txt ] || { python3 -B lift47.py inst/towers/$1.json $2 $out.json >/dev/null && python3 -B gen47.py j2t $out.json $out.txt; }; S=$out.txt; }
case "$L" in
K28) lift HIT7_d28_F254 0 HIT7_d28; CAP=260; SC=K ;;
K36) lift HIT7_d28_F254 8 HIT7_d36; CAP=340; SC=K ;;
K40) lift HIT7_d28_F254 12 HIT7_d40; CAP=380; SC=K ;;
L*) d=${L#L}; S=inst/seeds/rand_w2_d${d}.txt; [ -f $S ] || { python3 -B rand47.py 2 $d 2 $((4800 + d)) inst/seeds/rand_w2_d${d}.json && python3 -B gen47.py j2t inst/seeds/rand_w2_d${d}.json $S; }; CAP=$((6 * d + 40)); SC=K ;;
T*) n=${L#T}; lift HIT7_d28_F254 $(( (n - 56) / 2 )) HIT7_N$n; CAP=$(( 3 * n + 40 )); SC=T ;;
*) echo usage; exit 2 ;;
esac
SD=$(( 4700 + $(echo $L | tr -dc 0-9) ))
SCORE=$SC timeout 6600 ./bin/search47_$L $S out/lanes/$L $CAP 4000000000 $SD ${TEMP0:-2.0} ${UNIT:-200000}
echo "run47d $L exit $?"
