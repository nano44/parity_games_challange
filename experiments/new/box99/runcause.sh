#!/bin/bash
# L-NEW box 99: retcause.py on box 50b's corpus (as box97/runod.sh) and the box-97 pins; one RUN line + its ROOT line per W-run with returns.
cd "$(dirname "$0")/../.."
one() { TOP=3 timeout 300 python3 -I new/box99/retcause.py "$@" 2>&1 | grep -E '^RUN|ROOT|Error|Trace' | sed "s|^|GAME $1 |"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box99/cause_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box99/cause_alt.txt
for f in sbq2_K8_m16 obs_K12_m24 latew_K16_m32; do TOP=8 timeout 1200 python3 -I new/box99/retcause.py new/box97/inst/$f.pg new/box97/inst/$f.start | sed "s|^|GAME $f |"; done > new/box99/cause_pins.txt
