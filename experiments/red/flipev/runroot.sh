#!/bin/bash
# L-RED R146: rootflip.py over box 50b's corpus (sbcg 719 + alt 413), 300 s per game.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I red/flipev/rootflip.py "$@" 2>&1 | tail -1)"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . ; cat si/root/logs/alt_all.lst; } | xargs -P 1 -L 1 bash -c 'one "$@"' _ > red/flipev/rootflip_corpus.txt
