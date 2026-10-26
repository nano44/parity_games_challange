#!/bin/sh
# REFEREE succ. 12: P-N5-2T batches. Run from docs/referee/scratch. lib2o.txt is the lane's file LIST (input only; no lane code run).
RANDSTARTS=6 python3 -I twot_probe.py lib > twot_logs/lib41_rs6.txt 2>&1 &
RANDSTARTS=6 PATHN=16 python3 -I twot_probe.py list ../../../experiments/si/fb2o/lib2o.txt > twot_logs/lib2o_rs6.txt 2>&1 &
RANDSTARTS=2 python3 -I twot_probe.py rand 3000 4 12 2 52 > twot_logs/rand2o_s52.txt 2>&1 &
TWOT_MUT=1 RANDSTARTS=2 python3 -I twot_probe.py lib > twot_logs/mut_lib41_rs2.txt 2>&1 &
wait
