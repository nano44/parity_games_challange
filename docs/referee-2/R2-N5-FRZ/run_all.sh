#!/bin/bash
# REFEREE-2 succ. 7 R2-N5-FRZ batch. Run from this directory. LIB = experiments/new/box34/lib.txt (the packet's 234 files; inputs only),
# 3 starts each (S3 + 2 random), deterministic S4a and --rand S4a; packet-named instances; random C^1O games.
mkdir -p logs; rm -f logs/*.txt
R=../../..
J=4
job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.5; done; }
for f in $(cat $R/experiments/new/box34/lib.txt); do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; python3 frz_check.py inst $R/$f 3 > logs/lib_$b.txt 2>&1 &
  job; python3 frz_check.py inst $R/$f 3 --rand > logs/librand_$b.txt 2>&1 &
done
for f in experiments/n5-exhaustive/instances/b6_xl2_n32.pg experiments/new/box28/instances/x48_rt48_final.pg experiments/new/box34/instances/oneh_cex_n32.pg; do
  b=$(basename $f .pg); job; python3 frz_check.py inst $R/$f 10 --rand > logs/named_$b.txt 2>&1 &
done
for s in 1 2 3 4; do job; python3 frz_check.py random 3000 4 8 70$s > logs/rand_small_$s.txt 2>&1 & done
for s in 1 2; do job; python3 frz_check.py random 1500 8 16 71$s --rand > logs/rand_mid_$s.txt 2>&1 & done
wait
