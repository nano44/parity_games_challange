#!/bin/sh
# REFEREE-2 batch for P-N5-XA; logs in logs/. Run from this directory.
R=../../..
for s in 91 92; do python3 xa_check.py random 6000 6 14 $s own > logs/rand_own_s$s.txt 2>&1; done
python3 xa_check.py random 3000 6 14 93 spec > logs/rand_spec_s93.txt 2>&1
for f in experiments/new/box21/instances/fts_best16.pg experiments/red/n5inj/instances/theta_tp32.pg \
         experiments/red/n5inj/instances/returns_rt48.pg experiments/red/n5inj/instances/returns_ph64.pg \
         experiments/red/n5inj/instances/theta_thf16.pg experiments/new/box25/thetare_n.pg experiments/new/box25/thetare_min.pg \
         experiments/new/box22/instances/i1h_fts_best16.pg experiments/new/box25/fbh_drop9.pg experiments/new/box25/fbh_thr.pg \
         experiments/new/box25/zfrozen_thr.pg experiments/new/box25/instances/tr20_s4.pg; do
  p=$R/$f; b=$(basename $f .pg); st=""; [ -f ${p%.pg}.start ] && st=${p%.pg}.start
  python3 xa_check.py inst $p $st spec > logs/inst_spec_$b.txt 2>&1
  python3 xa_check.py inst $p $st own 30 > logs/inst_own_$b.txt 2>&1
done
for f in climb/*.pg; do b=$(basename $f .pg); python3 xa_check.py inst $f own 100 > logs/climb_own_$b.txt 2>&1; done
grep -H RESULT logs/*.txt
