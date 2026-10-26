#!/bin/sh
# REFEREE succ. 12: P-N5-H3 batches. Run from docs/referee/scratch. lib2o.txt: the lane's file LIST (input only).
RANDSTARTS=4 python3 -I h3_probe.py lib > h3_logs/lib41_rs4.txt 2>&1 &
RANDSTARTS=6 python3 -I h3_probe.py list ../../../experiments/si/fb2o/lib2o.txt > h3_logs/lib2o_rs6.txt 2>&1 &
RANDSTARTS=2 python3 -I h3_probe.py rand 5000 5 12 2 2 82 > h3_logs/rand2o_s82.txt 2>&1 &
RANDSTARTS=2 python3 -I h3_probe.py rand 4000 5 14 2 4 83 > h3_logs/randk_s83.txt 2>&1 &
RANDSTARTS=6 python3 -I h3_probe.py ../../../experiments/n5-exhaustive/instances/frz1_n24.pg > h3_logs/frz1_n24_rs6.txt 2>&1 &
H3_MUT=1 RANDSTARTS=2 python3 -I h3_probe.py lib > h3_logs/mut_lib41_rs2.txt 2>&1 &
wait
