#!/bin/bash
# L-NEW box 72: silentlz.py (box70/silent.py on N5-LZC) over the 719-game corpus (box59/sbcg.lst) and alt_all (413, with starts).
cd "$(dirname "$0")/../.."
one() { r=$(timeout 900 python3 -I new/box72/silentlz.py "$@" 2>&1 | tail -1); echo "GAME $1 $r"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box72/silentlz_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box72/silentlz_alt.txt
