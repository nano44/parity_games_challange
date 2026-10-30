#!/bin/bash
# L-RED R145: flipev.py over box 50b's corpus (sbcg 719 + alt 413), 300 s per game, 4 parallel.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I red/flipev/flipev.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 3 -I{} bash -c 'one "{}"' > red/flipev/flipev_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 3 -L 1 bash -c 'one "$@"' _ > red/flipev/flipev_alt.txt
