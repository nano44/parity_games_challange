#!/bin/bash
# L-NEW box 54: N5-SF vs N5 on the M1 hard families (Oink generators at the pinned 8fbf0a7; PGSolver ports). Run from experiments/.
O=../tools/oink/build; D=new/box54/out/hf
for f in counter_symsi tc counter_rr counter_dp counter_m counter_core counter_ortl counter_rob counter_qpt; do
  for N in 2 3 4 5 6 8; do
    $O/$f $N > $D/${f}_$N.pg 2>/dev/null || continue
    timeout 600 python3 -I new/box54/sfrun.py $D/${f}_$N.pg | grep -E "^ROW|_V" | tr '\n' ' '; echo
  done
done
for f in recursiveladder; do for N in 2 3 4 5 6; do python3 hard-families/pgsolver_port.py $f $N > $D/${f}_$N.pg 2>/dev/null || continue
  timeout 600 python3 -I new/box54/sfrun.py $D/${f}_$N.pg | grep -E "^ROW|_V" | tr '\n' ' '; echo; done; done
