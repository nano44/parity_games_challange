#!/bin/sh
# REFEREE-2 batch for P-N5-RE; logs in logs/. Run from this directory.
R=../../..
python3 re_check.py random 3000 6 14 2 own > logs/rand_own_s2.txt 2>&1
for s in 11 12 13; do python3 re_check.py random 8000 6 16 $s own > logs/rand_own_s$s.txt 2>&1; done
python3 re_check.py random 4000 6 16 21 spec > logs/rand_spec_s21.txt 2>&1
for f in experiments/new/box21/instances/fts_best16.pg experiments/red/n5inj/instances/theta_tp32.pg \
         experiments/red/n5inj/instances/returns_rt48.pg experiments/red/n5inj/instances/returns_ph64.pg \
         experiments/new/box25/instances/tr20_s4.pg experiments/new/box22/instances/i1h_fts_best16.pg \
         experiments/new/box25/thetare_n.pg experiments/new/box25/thetare_min.pg experiments/new/box21/instances/oneodd_c24.pg \
         experiments/new/box25/instances/rtt24.pg experiments/new/box25/instances/rtt16.pg experiments/new/box25/fbh_drop9.pg \
         experiments/new/box25/wdrop_cyc.pg experiments/new/box25/wdrop_canon.pg R2-N5-RE/nc_fail_n12.pg R2-N5-RE/climb/c12_s54.pg R2-N5-RE/climb/c10_s51.pg; do
  case $f in R2-N5-RE/*) p=${f#R2-N5-RE/};; *) p=$R/$f;; esac
  b=$(basename $f .pg); st=""; [ -f ${p%.pg}.start ] && st=${p%.pg}.start
  python3 re_check.py inst $p $st spec > logs/inst_spec_$b.txt 2>&1
  python3 re_check.py inst $p $st own 30 > logs/inst_own_$b.txt 2>&1
done
python3 re_check.py inst climb/c12_s54.pg own 300 > logs/inst_own300_c12_s54.txt 2>&1
python3 sg_check.py 5000 6 16 31 own cyc > logs/sg_own_s31.txt
python3 sg_check.py 3000 6 16 32 own any > logs/sg_own_any_s32.txt
python3 sg_check.py 2000 6 16 33 spec cyc > logs/sg_spec_s33.txt
grep -H RESULT logs/*.txt
