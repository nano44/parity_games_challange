#!/bin/sh
# REFEREE-2 batch for P-N5-NH; logs in logs/. Run from this directory.
R=../../..
python3 nh_check.py random 3000 6 14 111 own > logs/rand_own_s111.txt 2>&1
python3 nh_check.py random 5000 6 14 112 own > logs/rand_own_s112.txt 2>&1
python3 nh_check.py random 3000 6 14 113 spec > logs/rand_spec_s113.txt 2>&1
for p in $R/experiments/new/box29/instances/*.pg $R/experiments/new/box28/instances/*.pg ../R2-N5-X/ext/fbref_cex_n32.pg \
         $R/experiments/new/box21/instances/fts_best16.pg $R/experiments/red/n5inj/instances/theta_tp32.pg \
         $R/experiments/red/n5inj/instances/returns_rt48.pg $R/experiments/new/box25/instances/rtt24.pg \
         $R/experiments/new/box25/wdrop_cyc.pg $R/experiments/new/box25/fbh_thr.pg; do
  b=$(basename $p .pg); st=""; [ -f ${p%.pg}.start ] && st=${p%.pg}.start
  python3 nh_check.py inst $p $st spec > logs/inst_spec_$b.txt 2>&1
  python3 nh_check.py inst $p $st own 20 > logs/inst_own_$b.txt 2>&1
done
for f in climb/*.pg; do b=$(basename $f .pg); python3 nh_check.py inst $f own 100 > logs/climb_own_$b.txt 2>&1; python3 nh_check.py inst $f spec > logs/climb_spec_$b.txt 2>&1; done
grep -H RESULT logs/*.txt
