#!/bin/bash
# REFEREE-2 succ. 12: climbs against P-N5-NEEDB (run from this directory); seed games are inputs only.
mkdir -p climb
python3 needb_climb.py lv 12001 8 14 1500 ../R2-N5-LV2/climb/block_9501.pg > climb/lv_12001.txt 2>&1 &
python3 needb_climb.py lv 12002 8 16 1500 > climb/lv_12002.txt 2>&1 &
python3 needb_climb.py rise 12003 8 14 1500 ../R2-N5-ENT/climb/best_rise_9201.pg > climb/rise_12003.txt 2>&1 &
wait
python3 needb_climb.py lv 12004 8 14 1200 climb/best_lv_12001.pg > climb/lv_12004.txt 2>&1 &
python3 needb_climb.py rise 12005 10 16 1200 > climb/rise_12005.txt 2>&1 &
python3 needb_climb.py rise 12006 8 14 1200 ../R2-N5-ENT/climb/best_rise_9202.pg > climb/rise_12006.txt 2>&1 &
wait
echo DONE > climb/ALLDONE
