#!/bin/bash
# L-COMP box 47: UPWARD-LADDER multi-start (Lead 12:12Z; L-SI 55's class): rounds r = 1..R; in each round, one search47 run per depth d in
# DEPTHS (CLASS=UP, SCORE=KR: k_A6, then the largest sw / (|K| − 1) at level k, then T) from a fresh up47.py seed (seed 5000 + 100 d + r),
# ITERS proposals, UNIT 200000. Output out/up/U<d>_<r>.{log,state,_BEST_*}; a run with a DONE line is skipped (resumable per run; an
# interrupted run resumes from its .state). Usage: run47e.sh [R] [ITERS]   (env DEPTHS, default "6 8 10 12")
set -u; cd "$(dirname "$0")"; mkdir -p out/up inst/seeds/up bin; R=${1:-20}; IT=${2:-2000000}
gcc -O2 -Wno-unused-function -Wno-misleading-indentation -I. -DMODEL='"one47.h"' -o bin/search47_up search47.c -lm || exit 1
for r in $(seq 1 $R); do for d in ${DEPTHS:-6 8 10 12}; do
  o=out/up/U${d}_$r; grep -q '^DONE' $o.log 2>/dev/null && continue
  s=inst/seeds/up/up_d${d}_$r; [ -f $s.txt ] || { python3 -B up47.py $d $((5000 + 100 * d + r)) $s.json && python3 -B gen47.py j2t $s.json $s.txt; }
  CLASS=UP SCORE=KR ./bin/search47_up $s.txt $o 1000 $IT $((5000 + 100 * d + r)) 2.0 200000
done; done
echo "run47e done"
