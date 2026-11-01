#!/bin/bash
# L-NEW box 120 fixes (GATE-L1 / N-1): inphase.py on the box 53 corpus, same lists and repaired starts as box118/rungate.sh.
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac; echo "GAME $a $b $(timeout 900 python3 -I new/box120/inphase.py $a ${b:--} 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box120/i_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box120/i_alt.txt
