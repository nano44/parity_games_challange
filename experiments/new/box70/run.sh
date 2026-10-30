#!/bin/bash
# L-NEW box 70: silent.py over L-SI's corpus list (experiments/si/odd/sbcg.lst at l-si, = box59/sbcg.lst) and alt_all (with starts).
cd "$(dirname "$0")/../.."
one() { r=$(timeout 900 python3 -I new/box70/silent.py "$@" 2>&1 | tail -1); echo "GAME $1 $r"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | sed 's#^new/#new/#' | xargs -P 3 -I{} bash -c 'one "{}"' > new/box70/silent_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 3 -L 1 bash -c 'one "$@"' _ > new/box70/silent_alt.txt
