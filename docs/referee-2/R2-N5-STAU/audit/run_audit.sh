#!/bin/bash
# REFEREE-2 succ. 15: regenerate the §2 audit inputs at the pin ca0a4e97 and rerun the scripts (outputs in this directory).
cd "$(dirname "$0")"
R=$(git rev-parse --show-toplevel)
git -C "$R" show ca0a4e97:docs/RESULTS.md > RESULTS_pin.md
for f in $(cat list66.txt) docs/si/P-N5-RL-box10.md docs/si/P-N5-NEEDB-box13.md docs/red/R58-n5-width.md; do
  mkdir -p "pin/$(dirname "$f")"; git -C "$R" show "ca0a4e97:$f" > "pin/$f"; done
python3 closure.py RESULTS_pin.md R48 R50 > closure.txt
python3 edges.py > edges.txt
python3 files.py > files.txt
python3 audit_grep.py $(cat list66.txt) > hits66.txt 2> hitcount.txt
