#!/bin/bash
# REFEREE-2 R2-N5-U23 batch. Run from this directory.
mkdir -p logs; rm -f logs/*.txt
python3 u23_check.py random 4000 6 14 801 > logs/rand_801.txt 2>&1 &
python3 u23_check.py random 1500 14 24 802 > logs/rand_802.txt 2>&1 &
for f in ../../../experiments/new/box31/instances/*.pg ../../../experiments/new/box29/instances/*.pg ../../../experiments/red/xing/instances/*.pg ../../../experiments/n5-exhaustive/instances/*.pg $(sed 's#^#../../../#' ../../../experiments/si/coarse/named.txt); do
  [ -f "$f" ] || continue
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(g.succ[v])>1]; sys.exit(0 if len(o)==1 else 1)" || continue
  b=$(basename $f .pg); python3 u23_check.py inst $f 10 > logs/inst_$b.txt 2>&1
done
wait
