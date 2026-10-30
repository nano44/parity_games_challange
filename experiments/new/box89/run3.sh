#!/bin/bash
# L-NEW box 89: relpe.py (STRICT=1: blocks inside the same frozen stretch) over the box-83 corpus (719 + 413). 300 s per game.
cd "$(dirname "$0")/../.."
one() { STRICT=1; export STRICT; echo "GAME $1 $(timeout 300 python3 -I new/box89/relpe.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box89/relpes_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box89/relpes_alt.txt
