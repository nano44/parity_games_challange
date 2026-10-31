#!/bin/bash
# L-NEW box 111: desc.py on the box 53 corpus.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box111/desc.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box111/desc_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box111/desc_alt.txt
