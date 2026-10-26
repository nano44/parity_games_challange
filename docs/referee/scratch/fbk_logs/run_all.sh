#!/bin/sh
# REFEREE succ. 12: P-N5-FBK batches. Run from docs/referee/scratch. lib2o.txt: the lane's file LIST (input only).
RANDSTARTS=6 python3 -I fbk_probe.py lib > fbk_logs/lib41_rs6.txt 2>&1 &
RANDSTARTS=6 PATHN=24 python3 -I fbk_probe.py list ../../../experiments/si/fb2o/lib2o.txt > fbk_logs/lib2o_rs6.txt 2>&1 &
RANDSTARTS=2 python3 -I fbk_probe.py rand 2000 4 12 3 62 > fbk_logs/rand3o_s62.txt 2>&1 &
RANDSTARTS=2 python3 -I fbk_probe.py rand 2000 5 12 4 63 > fbk_logs/rand4o_s63.txt 2>&1 &
FBK_MUT=1 RANDSTARTS=6 PATHN=24 python3 -I fbk_probe.py list ../../../experiments/si/fb2o/lib2o.txt > fbk_logs/mut_lib2o_rs6.txt 2>&1 &
wait
