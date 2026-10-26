#!/bin/bash
# REFEREE-2 succ. 9: four 1200 s climbs (run from this directory). Seeds: random C^1O (with o's self-loop) or a library game.
mkdir -p climb
R=../../..
python3 out_climb.py caseb 9101 8 14 1200 > climb/caseb_9101.txt 2>&1 &
python3 out_climb.py caseb 9102 8 14 1200 $R/experiments/n5-exhaustive/instances/b5_os_n14.pg > climb/caseb_9102.txt 2>&1 &
python3 out_climb.py brk 9103 8 14 1200 $R/experiments/n5-exhaustive/instances/b5_os_n16.pg > climb/brk_9103.txt 2>&1 &
python3 out_climb.py nea 9104 8 14 1200 $R/experiments/new/box25/instances/wd16_s2.pg > climb/nea_9104.txt 2>&1 &
wait
