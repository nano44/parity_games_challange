#!/bin/bash
# Box 191 XI-CYCLIC frozen checks (run from experiments/new/box191; ~1 min). Prints the four tables; check.sh diffs them with check191.out.
set -e
python3 -I eq191.py inst/cyc*.json ../box189/corpus/*.json
python3 -I rand191.py eq 300 1
python3 -I seg1p191.py 300 11
python3 -I subrun191.py inst/DEAD_SEG2P_d4_N8.json inst/DEAD_SEG2P_d7_N14.json inst/DEAD_SEG2P_d9_N18.json
python3 -I brseg_gen191.py inst/sae_2.pg inst/sae_3.pg inst/sae_4.pg inst/sae_5.pg
