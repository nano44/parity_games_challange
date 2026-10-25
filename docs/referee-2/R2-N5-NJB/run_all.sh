#!/bin/bash
# REFEREE-2 succ. 7 R2-N5-NJB batch (run from this directory). LIB = experiments/new/box33/lib.txt (= box34 lib, 234 files), NAMED =
# experiments/si/coarse/named.txt + instances/*.pg + instances/box9/*.pg (inputs only); 3 starts x {det, --rand}; random C^1O.
mkdir -p logs; rm -f logs/*.txt
R=../../..; J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.5; done; }
{ awk '{print $1}' $R/experiments/new/box33/lib.txt; awk '{print $1}' $R/experiments/si/coarse/named.txt; ls $R/experiments/si/coarse/instances/*.pg $R/experiments/si/coarse/instances/box9/*.pg | sed "s#^$R/##"; } | sort -u > logs/files.lst
while read f; do
  [ -f "$R/$f" ] || continue
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; python3 njb_check.py inst $R/$f 3 > logs/f_$b.txt 2>&1 &
  job; python3 njb_check.py inst $R/$f 3 --rand > logs/frand_$b.txt 2>&1 &
done < logs/files.lst
for s in 1 2 3; do job; python3 njb_check.py random 4000 6 16 91$s > logs/rand_$s.txt 2>&1 & done
job; python3 njb_check.py random 2000 12 24 914 --rand > logs/rand_4.txt 2>&1 &
wait
