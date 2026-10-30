#!/bin/bash
# L-RED R148: casc/retcause_xr.py (L-NEW retcause.py + one XROOT line) over box 50b's corpus, 300 s per game. Run from a git archive of
# l-new b376575c (needs experiments/new/box21 and the corpus files): ROOT=<archive>/experiments bash runxr.sh OUT
cd "$ROOT"; cp "$(dirname "$0")/retcause_xr.py" new/box99/retcause_xr.py 2>/dev/null || true
one() { TOP=3 timeout 300 python3 -I new/box99/retcause_xr.py "$@" 2>&1 | grep -E '^RUN|XROOT|Error|Trace' | sed "s|^|GAME $1 |"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . ; cat si/root/logs/alt_all.lst; } | xargs -P ${P:-2} -L 1 bash -c 'one "$@"' _ > "$1"
