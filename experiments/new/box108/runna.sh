#!/bin/bash
# L-NEW box 108: na.py on the box 53 corpus (as box107/runfin.sh) .
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box108/na.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 3 -I{} bash -c 'one "{}"' > new/box108/na_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 3 -L 1 bash -c 'one "$@"' _ > new/box108/na_alt.txt
