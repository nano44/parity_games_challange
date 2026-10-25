#!/usr/bin/env bash
# L-SI box 8: reproduce the DATA lines of docs/si/P-N5-CLS-box8.md. Logs go to experiments/si/coarse/logs/cls_*.txt.
# Set = experiments/si/coarse/named.txt (53) + experiments/si/coarse/instances/*.pg (12 pinned climb bests); each one-o asserted.
set -u
cd "$(git rev-parse --show-toplevel)"
D=experiments/si/coarse; L=${LOGDIR:-$D/logs}; mkdir -p $L; N="$(cat $D/named.txt) $(ls $D/instances/*.pg)"
python3 $D/cls2.py $N > $L/cls_cls2.txt 2>&1
python3 $D/rfinv.py $N > $L/cls_rfinv.txt 2>&1
python3 $D/clscope.py $N > $L/cls_clscope.txt 2>&1
for f in $L/cls_*.txt; do echo "$(basename $f): $(grep TOTAL $f | cut -c1-300)"; done
