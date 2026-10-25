#!/bin/bash
# REFEREE-2 succ. 7 R2-N5-L2 batch (run from this directory). LIB (experiments/new/box34/lib.txt, inputs only) x 3 starts x {det, --rand};
# the packet's instances; random C^1O games (n 4-14, as the lane's --rand ranges).
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.5; done; }
for f in $(cat $R/experiments/new/box34/lib.txt); do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; python3 l2_check.py inst $R/$f 3 > logs/lib_$b.txt 2>&1 &
  job; python3 l2_check.py inst $R/$f 3 --rand > logs/librand_$b.txt 2>&1 &
done
for f in oneh_cex_n32 onedrop_cex_n32; do job; python3 l2_check.py inst $R/experiments/new/box34/instances/$f.pg 20 --rand > logs/named_$f.txt 2>&1 & done
for s in 1 2 3 4; do job; python3 l2_check.py random 5000 4 9 81$s > logs/rand_small_$s.txt 2>&1 & done
for s in 1 2; do job; python3 l2_check.py random 3000 8 14 82$s --rand > logs/rand_mid_$s.txt 2>&1 & done
wait
