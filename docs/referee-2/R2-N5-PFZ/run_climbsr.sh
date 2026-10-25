#!/bin/bash
# REFEREE-2 succ. 11: climbs against REFEREE's PFZ-1 repair (FIT rtl, PFZR=1), run from this directory; seeds are inputs only.
export PFZR=1; mkdir -p climb
python3 pfzx_climb.py rtl 9701 6 10 1500 > climb/rtl_9701.txt 2>&1 &
python3 pfzx_climb.py rtl 9702 6 10 1500 climb/best_brki_9602.pg > climb/rtl_9702.txt 2>&1 &
wait
