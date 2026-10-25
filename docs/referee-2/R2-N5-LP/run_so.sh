#!/bin/bash
# REFEREE-2 P-N5-SO batch. Run from this directory.
mkdir -p logs; rm -f logs/so_*.txt
python3 so_check.py c1o 3000 6 14 931 > logs/so_c1o_931.txt 2>&1 &
python3 so_check.py c1o 800 14 24 932 > logs/so_c1o_932.txt 2>&1 &
for f in $(find ../../../experiments -name "*.pg" | sort); do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(g.succ[v])>1]; sys.exit(0 if len(o)==1 and g.n<=64 else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##'); python3 so_check.py inst $f 3 > logs/so_inst_$b.txt 2>&1
done
wait
