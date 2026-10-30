#!/bin/bash
# L-RED R149: casc/retcause_br.py (L-NEW retcause.py @ 2311683e + BRCHAIN + XDEG) over box 50b's corpus, 300 s per game, from experiments/.
# LNEW_BOX21=<git archive of l-new 2311683e>/experiments/new/box21 bash red/casc/runxd.sh OUT
cd "$(dirname "$0")/../.."
one() { TOP=1 timeout 300 python3 -I red/casc/retcause_br.py "$@" 2>&1 | grep -E '^RUN|XDEG|BRCHAIN|Error|Trace' | sed "s|^|GAME $1 |"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . ; cat si/root/logs/alt_all.lst; } | xargs -P ${P:-2} -L 1 bash -c 'one "$@"' _ > "$1"
