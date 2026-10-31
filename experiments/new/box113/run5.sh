#!/bin/bash
# L-NEW box 113: desc5.py on the box 53 corpus (same lists as box 111 rundesc.sh).
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box113/desc5.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box113/d5_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box113/d5_alt.txt
