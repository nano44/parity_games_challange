#!/bin/bash
# REFEREE-2 succ. 10: climbs against P-N5-LV2 (run from this directory); seeds are inputs only. 9501 was started first, alone, at 16:40Z
# (1500 s, seeded with my predecessor's u* = none witness); the other three run together after the batches.
mkdir -p climb
[ "$1" = all ] && python3 lv2_climb.py none 9501 8 14 1500 ../R2-N5-LV/climb/best_lv_9401.pg > climb/none_9501.txt 2>&1 &
python3 lv2_climb.py none 9502 8 14 1200 > climb/none_9502.txt 2>&1 &
python3 lv2_climb.py none 9503 10 16 1200 > climb/none_9503.txt 2>&1 &
python3 lv2_climb.py blk 9504 8 14 1200 > climb/blk_9504.txt 2>&1 &
[ "$1" = witness ] && python3 lv2_climb.py blk 9505 8 14 400 climb/best_none_9501.pg > climb/blk_9505.txt 2>&1 &
[ "$1" = replay ] && python3 lv2_climb.py none0 9501 8 14 1500 ../R2-N5-LV/climb/best_lv_9401.pg > climb/replay_9501.txt 2>&1 &
wait
