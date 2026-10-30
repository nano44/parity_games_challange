#!/bin/bash
# L-NEW box 79: flatsrc.py (N5 and --lzc) over the 719-game corpus (box59/sbcg.lst) and alt_all (413, with starts).
cd "$(dirname "$0")/../.."
one() { a=$(timeout 900 python3 -I new/box79/flatsrc.py "$@" 2>&1 | tail -1); b=$(timeout 900 python3 -I new/box79/flatsrc.py "$@" --lzc 2>&1 | tail -1); echo "GAME $1 N5 $a LZC $b"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box79/flatsrc_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box79/flatsrc_alt.txt
