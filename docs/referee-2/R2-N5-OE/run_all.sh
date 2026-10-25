#!/bin/bash
# REFEREE-2 succ. 6 R2-N5-OE batch. Run from this directory. Library = every experiments/**/*.pg with exactly one Odd choice vertex
# and n <= 64 (same selection as R2-N5-LP/run_all.sh). Random batches: general games (U-loc) and C^1O (everything).
mkdir -p logs; rm -f logs/oe_*.txt logs/inst_*.txt
python3 oe_check.py general 3000 4 12 941 > logs/oe_gen_941.txt 2>&1 &
python3 oe_check.py general 800 12 20 942 > logs/oe_gen_942.txt 2>&1 &
python3 oe_check.py c1o 3000 6 14 943 > logs/oe_c1o_943.txt 2>&1 &
python3 oe_check.py c1o 800 14 24 944 > logs/oe_c1o_944.txt 2>&1 &
for f in $(find ../../../experiments -name "*.pg" | sort); do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(set(g.succ[v]))>1]; sys.exit(0 if len(o)==1 and g.n<=64 else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##'); python3 oe_check.py inst $f 3 > logs/inst_$b.txt 2>&1
done
wait
