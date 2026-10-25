#!/bin/bash
# REFEREE-2 R2-N5-FB batch. Run from this directory. Every log ends with RESULT.
mkdir -p logs; rm -f logs/*.txt
python3 fb_check.py general 3000 4 12 731 > logs/gen_731.txt 2>&1 &
python3 fb_check.py general 1000 12 20 732 > logs/gen_732.txt 2>&1 &
python3 fb_check.py c1o 3000 6 14 733 > logs/c1o_733.txt 2>&1 &
python3 fb_check.py c1o 1000 14 24 734 > logs/c1o_734.txt 2>&1 &
for f in $(cat ../../../experiments/si/coarse/named.txt); do
  b=$(basename $f .pg); python3 fb_check.py inst ../../../$f 5 > logs/inst_$b.txt 2>&1
done
wait
