#!/usr/bin/env bash
# REFEREE successor 35: regenerates every log of R-GK-precheck.md. Run from docs/referee/scratch: bash gk_run.sh [quick|n5|all]
# quick (about 5 min): validation of the tools on landed genomes, sha1 pins, membership + L (k = 3..15), lemma checks, PERM / RENUM,
#                      N5 on Gamma3(G_k) for k = 3..9.
# n5: N5 on Gamma3(G_k) for k = 10, 11, 12, one log per k, skipped when the log already ends in «exit 0» (resumable).
set -u
R=../../..
mode="${1:-quick}"
if [ "$mode" = quick ] || [ "$mode" = all ]; then
  python3 gk_ideal.py $R/experiments/red/r178/out/big_d3_k3_W3.json $R/experiments/red/r178/out/big_d4_k3_W3.json \
    $R/experiments/red/r178/out/big_d6_k3_W3.json $R/experiments/red/r178/out/big_d8_k3_W3.json $R/experiments/red/r178/out/grow_top_N15.json \
    $R/experiments/red/r178/out/grow_top_N24.json $R/experiments/red/r178/out/grow_bottom_N24.json $R/experiments/new/box189/corpus/*.json \
    > gk_logs/val_ideal.out 2>&1; echo "exit $?" >> gk_logs/val_ideal.out
  python3 gk_reach.py . $R/experiments/new/box189/corpus/*.json > gk_logs/val_reach.out 2>&1; echo "exit $?" >> gk_logs/val_reach.out
  python3 gk_build.py sha 3 4 8 10 > gk_logs/sha.out 2>&1; echo "exit $?" >> gk_logs/sha.out
  python3 gk_member.py 3 15 -v > gk_logs/member.out 2>&1; echo "exit $?" >> gk_logs/member.out
  : > gk_logs/lemck.out
  for k in 3 4 5 6 7 8 9 10 11 12; do python3 gk_lemck.py $k 60 $((100 + k)) >> gk_logs/lemck.out 2>&1; done
  for k in 4 8 12; do python3 gk_lemck.py $k 60 $((100 + k)) revE >> gk_logs/lemck.out 2>&1; done
  echo "exit $?" >> gk_logs/lemck.out
  python3 gk_perm.py 3 6 4 35 > gk_logs/perm.out 2>&1; echo "exit $?" >> gk_logs/perm.out
  python3 gk_n5.py 3 9 > gk_logs/n5_3_9.out 2>&1; echo "exit $?" >> gk_logs/n5_3_9.out
  for k in 3 4; do python3 gk_trace.py $k; done > gk_logs/trace_3_4.out 2>&1
fi
if [ "$mode" = n5 ] || [ "$mode" = all ]; then
  for k in 10 11 12; do
    f=gk_logs/n5_$k.out
    if [ -f $f ] && tail -1 $f | grep -q '^exit 0$'; then continue; fi
    python3 gk_n5.py $k $k > $f 2>&1; echo "exit $?" >> $f
  done
fi
