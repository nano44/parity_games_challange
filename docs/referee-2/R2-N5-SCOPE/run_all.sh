#!/bin/bash
# REFEREE-2 succ. 8 R2-N5-SCOPE batch (run from this directory). files.lst = tracked experiments/**/*.pg on C^1O with n <= 64 (mklib.py),
# gfiles.lst = the other tracked .pg with n <= 24 (general games, CN-LAST only). Inputs only. 4 parallel jobs.
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; timeout 1200 python3 scope_check.py inst $R/$f 3 > logs/f_$b.txt 2>&1 &
  job; timeout 1200 python3 scope_check.py inst $R/$f 3 --rand > logs/frand_$b.txt 2>&1 &
done < files.lst
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; timeout 1200 python3 scope_check.py ginst $R/$f 3 > logs/g_$b.txt 2>&1 &
done < gfiles.lst
for s in 1 2; do job; python3 scope_check.py random 10000 4 14 81$s > logs/rand_$s.txt 2>&1 & done
for s in 3 4; do job; python3 scope_check.py random 10000 4 14 81$s --rand > logs/rand_$s.txt 2>&1 & done
for s in 5 6; do job; python3 scope_check.py random 2000 15 30 81$s --rand > logs/rand_$s.txt 2>&1 & done
for s in 1 2; do job; python3 scope_check.py general 10000 3 12 82$s > logs/gen_$s.txt 2>&1 & done
for s in 3 4; do job; python3 scope_check.py general 10000 3 12 82$s --rand > logs/gen_$s.txt 2>&1 & done
wait
