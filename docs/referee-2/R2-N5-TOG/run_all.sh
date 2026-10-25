#!/bin/bash
# REFEREE-2 succ. 7 R2-N5-TOG batch + climbs (run from this directory; climb seconds = $1, default 600). LIB = experiments/new/box34/lib.txt
# + experiments/new/box34/instances + experiments/new/box35/instances (inputs only), 3 starts x {det, --rand}; random C^1O n 4-14.
S=${1:-600}; mkdir -p logs climb; rm -f logs/*.txt
R=../../..; J=4; job() { while [ $(jobs -r | wc -l) -ge $J ]; do sleep 0.5; done; }
{ cat $R/experiments/new/box34/lib.txt; ls $R/experiments/new/box34/instances/*.pg $R/experiments/new/box35/instances/*.pg | sed "s#^$R/##"; } | sort -u > logs/files.lst
while read f; do
  b=$(echo $f | sed 's#experiments/##; s#/#_#g; s#.pg$##')
  job; python3 tog_check.py inst $R/$f 3 > logs/f_$b.txt 2>&1 &
  job; python3 tog_check.py inst $R/$f 3 --rand > logs/frand_$b.txt 2>&1 &
done < logs/files.lst
for s in 1 2 3 4; do job; python3 tog_check.py random 5000 4 14 95$s > logs/rand_$s.txt 2>&1 & done
for s in 5 6; do job; python3 tog_check.py random 5000 4 14 95$s --rand > logs/rand_$s.txt 2>&1 & done
wait
X=$R/experiments/new/box35/instances
job; python3 tog_climb.py tog 81 5 12 $S > climb/tog_81.txt 2>&1 &
job; python3 tog_climb.py tog 82 0 0 $S $X/onerun_cex_n32.pg > climb/tog_82.txt 2>&1 &
job; python3 tog_climb.py tog 83 0 0 $S $X/fbrestart_cex_n12.pg > climb/tog_83.txt 2>&1 &
job; python3 tog_climb.py tog 84 8 16 $S > climb/tog_84.txt 2>&1 &
wait
