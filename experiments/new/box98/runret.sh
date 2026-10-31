#!/bin/bash
# L-NEW box 98: retpay.py on box 50b's corpus (as box97/runod.sh) and the box-97 pins.
cd "$(dirname "$0")/../.."
one() { timeout 300 python3 -I new/box98/retpay.py "$@" 2>&1 | sed "s|^|GAME $1 |"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box98/ret_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box98/ret_alt.txt
for f in sbq2_K8_m16 obs_K12_m24 latew_K16_m32; do one new/box97/inst/$f.pg new/box97/inst/$f.start; done > new/box98/ret_pins.txt
