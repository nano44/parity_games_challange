#!/bin/bash
# L-NEW box 84: waits.py over the box-83 corpus (box59/sbcg.lst, 719 games; alt_all, 413 with starts). 300 s per game.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I new/box84/waits.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 6 -I{} bash -c 'one "{}"' > new/box84/waits_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 6 -L 1 bash -c 'one "$@"' _ > new/box84/waits_alt.txt
