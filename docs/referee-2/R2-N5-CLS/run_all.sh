#!/bin/bash
# REFEREE-2 succ. 6 R2-N5-CLS batch. Run from this directory.
# Set = library (every experiments/**/*.pg with exactly one Odd choice vertex, n <= 64) + the lane's named.txt and coarse instances
# (any n) + j7_n32/j7_n48; 3 runs per file (S3 start + 2 random). Random: general (TRANSFER, CN) and C^1O.
mkdir -p logs; rm -f logs/*.txt
X=../../../experiments
python3 cls_check.py general 3000 4 12 971 > logs/gen_971.txt 2>&1 &
python3 cls_check.py c1o 4000 6 16 972 > logs/c1o_972.txt 2>&1 &
python3 cls_check.py c1o 1000 16 28 973 > logs/c1o_973.txt 2>&1 &
PHKEY=fine python3 cls_check.py c1o 4000 6 16 974 > logs/c1o_fine_974.txt 2>&1 &
( find $X -name "*.pg"; sed 's#^experiments#'$X'#' $X/si/coarse/named.txt; ls $X/si/coarse/instances/*.pg $X/red/xing/instances/j7_n*.pg ) | sort -u > logs/files.lst
while read f; do
  python3 -c "
import sys; sys.path.insert(0,'../R2-N5-RE'); import re_check as RC
g=RC.parse(open('$f').read()); o=[v for v in range(g.n) if g.owner[v]==1 and len(set(g.succ[v]))>1]
big = '$f'.find('si/coarse')>=0 or '$f'.find('j7_n')>=0
sys.exit(0 if len(o)==1 and (g.n<=64 or big) else 1)" 2>/dev/null || continue
  b=$(echo $f | sed 's#../../../experiments/##; s#/#_#g; s#.pg$##')
  python3 cls_check.py inst $f 3 > logs/inst_$b.txt 2>&1 &
  while [ $(jobs -r | wc -l) -ge 6 ]; do sleep 1; done
done < logs/files.lst
wait
PHKEY=fine python3 cls_check.py inst $X/si/coarse/instances/jcl_zcl_cu_n48.pg 3 > logs/fine_jcl_zcl_cu_n48.txt 2>&1
