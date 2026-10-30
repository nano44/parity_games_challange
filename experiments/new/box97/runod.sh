#!/bin/bash
# L-NEW box 97: orderdet.py on box 50b's corpus (new/box59/sbcg.lst + si/root/logs/alt_all.lst, as L-SI box 53) and the box-97 pins.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(VERBOSE=1 timeout 300 python3 -I new/box97/orderdet.py "$@" 2>&1 | tr '\n' ' ')"; }; export -f one
OUT=${1:-new/box97}
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > $OUT/od_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > $OUT/od_alt.txt
for f in sbq2_K8_m16 obs_K12_m24 latew_K16_m32; do one new/box97/inst/$f.pg new/box97/inst/$f.start; done > $OUT/od_pins.txt
