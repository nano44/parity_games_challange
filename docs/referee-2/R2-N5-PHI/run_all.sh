#!/bin/bash
# REFEREE-2 succ. 11 R2-N5-PHI batch (run from this directory). files.lst = R2-N5-FBPOLY/files.lst (492 tracked C^1O files, n <= 64).
# Inputs only. Traces own / rand / spec, 3 starts each; random C^1O batches.
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=${J:-4}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  for m in own rand spec; do job; timeout 1800 python3 phi_check.py inst $R/$f 3 $m > logs/${m}_$b.txt 2>&1 & done
done < files.lst
for s in 1 2; do for m in own rand spec; do job; python3 phi_check.py random 10000 4 14 14$s $m > logs/rnd_${m}_$s.txt 2>&1 & done; done
for m in own rand; do job; python3 phi_check.py random 2000 15 30 143 $m > logs/rnd_${m}_3.txt 2>&1 & done
wait
