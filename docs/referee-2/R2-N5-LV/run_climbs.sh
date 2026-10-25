#!/bin/bash
# REFEREE-2 succ. 9: four 1200 s climbs against P-N5-LV (run from this directory); lane instances are inputs only.
mkdir -p climb
R=../../..
python3 lv_climb.py lv 9401 8 14 1200 > climb/lv_9401.txt 2>&1 &
python3 lv_climb.py lv 9402 8 14 1200 $R/experiments/red/so/instances/tev_cex_n40.pg > climb/lv_9402.txt 2>&1 &
python3 lv_climb.py lv 9403 8 14 1200 $R/experiments/si/xing/instances/zcl_fb2_n32.pg > climb/lv_9403.txt 2>&1 &
python3 lv_climb.py lv 9404 10 16 1200 > climb/lv_9404.txt 2>&1 &
wait
