#!/bin/bash
# REFEREE-2 succ. 6 R2-N5-FBW batch. Run from this directory. Library = every experiments/**/*.pg with exactly one Odd choice vertex,
# n <= 64 (si/coarse instances incl. box9 any n <= 128), 3 runs per file; random general games (FBW, P-OPT) and random C^1O.
mkdir -p logs; rm -f logs/*.txt
X=../../../experiments
python3 fbw_check.py general 3000 4 12 9511 > logs/gen_9511.txt 2>&1 &
python3 fbw_check.py general 1000 12 20 9512 > logs/gen_9512.txt 2>&1 &
python3 fbw_check.py c1o 4000 6 16 9513 > logs/c1o_9513.txt 2>&1 &
python3 fbw_check.py c1o 1500 16 32 9514 > logs/c1o_9514.txt 2>&1 &
find $X -name "*.pg" | sort > logs/files.lst
while read f; do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(set(g.succ[v]))>1]
big = '$f'.find('si/coarse')>=0
sys.exit(0 if len(o)==1 and (g.n<=64 or (big and g.n<=128)) else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##')
  python3 fbw_check.py inst $f 3 > logs/inst_$b.txt 2>&1 &
  while [ $(jobs -r | wc -l) -ge 6 ]; do sleep 1; done
done < logs/files.lst
wait
