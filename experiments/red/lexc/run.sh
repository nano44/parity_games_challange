#!/bin/bash
# L-RED R143: settle.py over box 50b's corpus (L-SI lists: sbcg 719 + alt 413), 300 s per game, 4 parallel.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I red/lexc/settle.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > red/lexc/settle_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > red/lexc/settle_alt.txt
