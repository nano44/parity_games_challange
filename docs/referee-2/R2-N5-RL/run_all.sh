#!/bin/bash
# REFEREE-2 succ. 8 R2-N5-RL batch (run from this directory). files.lst = tracked experiments/**/*.pg on C^1O, n <= 64 (../R2-N5-SCOPE/mklib.py).
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; timeout 1500 python3 rl_check.py inst $R/$f 3 > logs/f_$b.txt 2>&1 &
  job; timeout 1500 python3 rl_check.py inst $R/$f 3 --rand > logs/frand_$b.txt 2>&1 &
done < files.lst
for s in 1 2; do job; python3 rl_check.py random 10000 4 14 71$s > logs/rand_$s.txt 2>&1 & done
for s in 3 4; do job; python3 rl_check.py random 10000 4 14 71$s --rand > logs/rand_$s.txt 2>&1 & done
for s in 5 6; do job; python3 rl_check.py random 2000 15 30 71$s --rand > logs/rand_$s.txt 2>&1 & done
wait
