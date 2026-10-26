#!/bin/bash
# REFEREE-2 succ. 8 R2-N5-P1 batch (run from this directory).
mkdir -p logs; rm -f logs/*.txt
python3 p1_check.py 6000 3 9 6101 4000 > logs/p1_6101.txt 2>&1 &
python3 p1_check.py 3000 8 12 6102 4000 > logs/p1_6102.txt 2>&1 &
python3 p1_check.py 20000 2 6 6103 4000 > logs/p1_6103.txt 2>&1 &
wait
