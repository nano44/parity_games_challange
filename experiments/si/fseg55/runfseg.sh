#!/bin/bash
# L-SI box 55: fseg.py on box 50b's corpus (sbcg + alt lists), as si/src54/runodd.sh.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/fseg55/fseg.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/fseg55/fseg_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/fseg55/fseg_alt.txt
