#!/bin/bash
# L-NEW box 108: newedge.py on the box 53 corpus (as box107/runfin.sh) and carrier.py on the depth-2 pins.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box108/newedge.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 3 -I{} bash -c 'one "{}"' > new/box108/ne_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 3 -L 1 bash -c 'one "$@"' _ > new/box108/ne_alt.txt
