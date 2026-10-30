#!/bin/bash
# L-RED R148: casc/retcause_xr.py (L-NEW retcause.py + one XROOT line) over box 50b's corpus, 300 s per game, from experiments/.
# Needs L-NEW's box21 (n5x): LNEW_BOX21=<git archive of l-new b376575c>/experiments/new/box21 bash red/casc/runxr.sh OUT
cd "$(dirname "$0")/../.."
one() { TOP=3 timeout 300 python3 -I red/casc/retcause_xr.py "$@" 2>&1 | grep -E '^RUN|XROOT|Error|Trace' | sed "s|^|GAME $1 |"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . ; cat si/root/logs/alt_all.lst; } | xargs -P ${P:-2} -L 1 bash -c 'one "$@"' _ > "$1"
