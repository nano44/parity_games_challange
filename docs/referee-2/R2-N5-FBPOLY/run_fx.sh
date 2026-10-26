#!/bin/bash
# REFEREE-2 succ. 11: re-run of the files with EXIT fallbacks (3 traces) after adding the FX slack maxima (no check changed); logs_fx/.
R=../../..; J=${J:-2}; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.3; done; }
while read b; do
  f=$(while read l; do [ "$(echo $l | sed 's#experiments/##; s#/#_#g; s#.pg$##')" = "$b" ] && echo $l && break; done < files.lst)
  for m in own rand spec; do job; timeout 1800 python3 fbpoly_check.py inst $R/$f 3 $m > logs_fx/${m}_$b.txt 2>&1 & done
done < exitfiles.lst
for m in own rand spec; do job; python3 fbpoly_check.py random 10000 4 14 412 $m > logs_fx/rnd_${m}_2.txt 2>&1 & done
wait
