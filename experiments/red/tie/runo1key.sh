#!/bin/bash
# L-RED R152: o1key.py over box 50b's corpus (sbcg 719 + alt 413) and the casc / xcn pins, 300 s per game.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I red/tie/o1key.py "$@" 2>&1 | tail -1)"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . ; cat si/root/logs/alt_all.lst; for f in red/casc/instances/*.pg red/xcn/instances/*.pg; do s=${f%.pg}.start; [ -f $s ] && echo "$f $s" || echo $f; done; } | xargs -P ${P:-4} -L 1 bash -c 'one "$@"' _ > red/tie/o1key_corpus.txt
