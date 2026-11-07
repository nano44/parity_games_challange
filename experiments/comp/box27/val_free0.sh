#!/bin/bash
# validate cnf.py FREE0 (ISO, KF) against the exhaustive bfk.c table T_k(2) = 4,5,7,8,..,9: L = T SAT and L = T+1 UNSAT at d 3
cd "$(dirname "$0")"
for kt in "0 4" "1 5" "2 7" "3 8" "6 9"; do set -- $kt
  for L in $2 $(( $2 + 1 )); do FREE0=1 KF=$1 python3 cnf.py 3 $L out_free0/free0_d3_k$1_L$L.json | grep RESULT | sed "s/^/KF $1 /"; done; done
