#!/bin/bash
# L-SI box 54: oddadd.py on box 50b's corpus (sbcg + alt lists), as si/sb53/runceil.sh.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/src54/oddadd.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/src54/odd_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/src54/odd_alt.txt
