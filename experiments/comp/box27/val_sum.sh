#!/bin/bash
# validate cnf.py RUN2 (two forced runs of one genome: KF=1 run of length b, flip-free run of length a) at m 2 (d 3) against the
# exhaustive bfk.c SUM result (max V0+V1 = 9, pairs up to (4,5)): a+b = 9 SAT for (4,5); a+b = 10 UNSAT for a = 0..4 (b = 10-a)
cd "$(dirname "$0")"; mkdir -p out_free0
for ab in "4 5" "0 10" "1 9" "2 8" "3 7" "4 6"; do set -- $ab
  FREE0=1 KF=1 RUN2=$1 python3 cnf.py 3 $2 out_free0/sum_d3_a$1_b$2.json | grep RESULT | sed "s/^/a $1 b $2 /"; done
