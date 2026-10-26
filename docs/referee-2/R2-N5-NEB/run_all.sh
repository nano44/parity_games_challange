#!/bin/bash
# REFEREE-2 succ. 9 R2-N5-NEB batch (run from this directory). files.lst = R2-N5-OUT's list (tracked experiments/**/*.pg on C^1O with
# n <= 64, united with the C^1O files of experiments/new/box37/lib37.txt). Inputs only. Traces own / rand / spec, 3 starts each.
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=${J:-4}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  for m in own rand spec; do job; timeout 1800 python3 neb_check.py inst $R/$f 3 $m > logs/${m}_$b.txt 2>&1 & done
done < files.lst
for s in 1 2; do for m in own rand spec; do job; python3 neb_check.py random 10000 4 14 93$s $m > logs/rnd_${m}_$s.txt 2>&1 & done; done
for m in own rand; do job; python3 neb_check.py random 2000 15 30 933 $m > logs/rnd_${m}_3.txt 2>&1 & done
job; python3 neb_check.py chain 200000 934 > logs/chain.txt 2>&1 &
wait
