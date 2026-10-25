#!/bin/bash
# REFEREE-2 succ. 6 R2-N5-SN batch. Run from this directory. Library = every experiments/**/*.pg with exactly one Odd choice vertex
# and n <= 64 (plus the packet's named instances of any n), 3 runs per file; random C^1O batches.
mkdir -p logs; rm -f logs/*.txt
X=../../../experiments
python3 sn_check.py c1o 4000 6 16 9101 > logs/c1o_9101.txt 2>&1 &
python3 sn_check.py c1o 1500 16 32 9102 > logs/c1o_9102.txt 2>&1 &
( find $X -name "*.pg"; ls $X/new/box33/instances/*.pg $X/red/so/instances/*.pg 2>/dev/null ) | sort -u > logs/files.lst
while read f; do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(set(g.succ[v]))>1]
big = '$f'.find('box33/instances')>=0 or '$f'.find('red/so/')>=0
sys.exit(0 if len(o)==1 and (g.n<=64 or (big and g.n<=400)) else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##')
  python3 sn_check.py inst $f 3 > logs/inst_$b.txt 2>&1 &
  while [ $(jobs -r | wc -l) -ge 6 ]; do sleep 1; done
done < logs/files.lst
wait
