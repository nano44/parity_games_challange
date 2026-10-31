#!/bin/bash
# L-SI box 56: srcfuel.py on box 50b's corpus (sbcg + alt lists).
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/grow56/srcfuel.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/grow56/fuel_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/grow56/fuel_alt.txt
