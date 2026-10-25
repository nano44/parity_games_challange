#!/bin/bash
# REFEREE-2 succ. 10 R2-N5-PFZ-ext batch (run from this directory). filesx.lst = R2-N5-OUT's list (tracked experiments/**/*.pg on C^1O with
# n <= 64, united with the C^1O files of experiments/new/box37/lib37.txt) + ../R2-N5-LV2/files_new.lst (newer tracked C^1O files). Inputs only. Traces own / rand / spec, 3 starts each.
mkdir -p logs_x; rm -f logs_x/*.txt
R=../../..; J=${J:-4}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  for m in own rand spec; do job; timeout 1800 python3 pfzx_check.py inst $R/$f 3 $m > logs_x/${m}_$b.txt 2>&1 & done
done < filesx.lst
for s in 1 2; do for m in own rand spec; do job; python3 pfzx_check.py random 10000 4 14 96$s $m > logs_x/rnd_${m}_$s.txt 2>&1 & done; done
for m in own rand; do job; python3 pfzx_check.py random 2000 15 30 963 $m > logs_x/rnd_${m}_3.txt 2>&1 & done
wait
