#!/bin/sh
# REFEREE-2 batch for P-N5-Z; logs in logs/. Run from this directory.
R=../../..
python3 z_check.py random 5000 6 14 131 own > logs/rand_own_s131.txt 2>&1
python3 z_check.py random 5000 6 16 132 own > logs/rand_own_s132.txt 2>&1
python3 z_check.py random 3000 6 14 133 spec > logs/rand_spec_s133.txt 2>&1
for p in $R/experiments/si/xing/instances/*.pg $R/experiments/si/orlens/instances/*.pg $R/experiments/new/box28/instances/*.pg \
         $R/experiments/new/box29/instances/*.pg ../R2-N5-X/ext/fbref_cex_n32.pg $R/experiments/red/n5inj/instances/returns_rt48.pg \
         $R/experiments/new/box21/instances/fts_best16.pg; do
  b=$(basename $p .pg); st=""; [ -f ${p%.pg}.start ] && st=${p%.pg}.start
  python3 z_check.py inst $p $st spec > logs/inst_spec_$b.txt 2>&1
  python3 z_check.py inst $p $st own 20 > logs/inst_own_$b.txt 2>&1
done
grep -H RESULT logs/*.txt
