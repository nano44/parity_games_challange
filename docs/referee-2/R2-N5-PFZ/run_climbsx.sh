#!/bin/bash
# REFEREE-2 succ. 10: two 1200 s climbs against P-N5-PFZ-ext BRK-POLY' (i) (run from this directory); seeds are inputs only.
mkdir -p climb
python3 pfzx_climb.py brki 9601 6 10 1200 > climb/brki_9601.txt 2>&1 &
python3 pfzx_climb.py brki 9602 6 10 1200 ../R2-N5-SN/climb/stick_a_best.pg > climb/brki_9602.txt 2>&1 &
wait
