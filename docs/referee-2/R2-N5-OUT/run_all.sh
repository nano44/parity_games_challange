#!/bin/bash
# REFEREE-2 succ. 9 R2-N5-OUT batch (run from this directory). files.lst = tracked experiments/**/*.pg on C^1O with n <= 64 (mklib.py)
# united with the C^1O files of the lane's experiments/new/box37/lib37.txt and rfroz_cex_n16.pg. Inputs only. Three traces per file:
# own (my N5, deterministic), rand (my N5, random optimum choices), spec (state sequence of experiments/new/n5.py).
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=${J:-6}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  for m in own rand spec; do job; timeout 1800 python3 out_check.py inst $R/$f 3 $m > logs/${m}_$b.txt 2>&1 & done
done < files.lst
for s in 1 2; do for m in own rand spec; do job; python3 out_check.py random 10000 4 14 91$s $m > logs/rnd_${m}_$s.txt 2>&1 & done; done
for m in own rand; do job; python3 out_check.py random 2000 15 30 913 $m > logs/rnd_${m}_3.txt 2>&1 & done
job; python3 out_check.py t123 200000 914 > logs/t123.txt 2>&1 &
wait
