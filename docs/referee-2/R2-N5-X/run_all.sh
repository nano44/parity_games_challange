#!/bin/sh
# REFEREE-2 batch for P-N5-X; logs in logs/. Run from this directory.
R=../../..
for s in 101 102; do python3 x_check.py random 6000 6 14 $s own > logs/rand_own_s$s.txt 2>&1; done
python3 x_check.py random 3000 6 14 103 spec > logs/rand_spec_s103.txt 2>&1
for p in $R/experiments/new/box28/instances/*.pg ext/fbref_cex_n32.pg $R/experiments/new/box21/instances/fts_best16.pg \
         $R/experiments/red/n5inj/instances/theta_tp32.pg $R/experiments/red/n5inj/instances/returns_rt48.pg \
         $R/experiments/red/n5inj/instances/returns_ph64.pg $R/experiments/new/box25/instances/rtt24.pg \
         $R/experiments/new/box25/instances/tr20_s4.pg $R/experiments/new/box25/fbh_thr.pg $R/experiments/new/box25/wdrop_cyc.pg \
         ../R2-N5-RE/climb/c12_s54.pg; do
  b=$(basename $p .pg); st=""; [ -f ${p%.pg}.start ] && st=${p%.pg}.start
  python3 x_check.py inst $p $st spec > logs/inst_spec_$b.txt 2>&1
  python3 x_check.py inst $p $st own 20 > logs/inst_own_$b.txt 2>&1
done
grep -H RESULT logs/*.txt
