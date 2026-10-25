#!/bin/bash
# REFEREE-2 succ. 10: second batch on files_new.lst = tracked C^1O .pg files (n <= 64) added since R2-N5-OUT's list (lane instances and
# earlier REFEREE-2 climb outputs; docs/referee/ excluded). Inputs only. Traces own / rand / spec, 3 starts each.
mkdir -p logs_new; rm -f logs_new/*.txt
R=../../..; J=${J:-4}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  for m in own rand spec; do job; timeout 1800 python3 lv2_check.py inst $R/$f 3 $m > logs_new/${m}_$b.txt 2>&1 & done
done < files_new.lst
wait
