#!/bin/bash
# REFEREE-2 R2-N5-LP batch. Run from this directory. Library = every experiments/**/*.pg with exactly one Odd choice vertex and n <= 64.
mkdir -p logs; rm -f logs/lp_*.txt logs/inst_*.txt
python3 lp_check.py general 3000 4 12 921 > logs/lp_gen_921.txt 2>&1 &
python3 lp_check.py general 800 12 20 922 > logs/lp_gen_922.txt 2>&1 &
python3 lp_check.py c1o 3000 6 14 923 > logs/lp_c1o_923.txt 2>&1 &
python3 lp_check.py c1o 800 14 24 924 > logs/lp_c1o_924.txt 2>&1 &
for f in $(find ../../../experiments -name "*.pg" | sort); do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(g.succ[v])>1]; sys.exit(0 if len(o)==1 and g.n<=64 else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##'); python3 lp_check.py inst $f 3 > logs/inst_$b.txt 2>&1
done
wait
