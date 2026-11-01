#!/bin/bash
# L-NEW box 127: expir.py (expiration / alternation-free test inside W-runs) on the box 125 corpus (box 59 sbcg list + si/root alt_all,
# box 113's repaired starts for comp54_n80 and n3cov_lean, as in box125/runcorp.sh).
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac
  timeout 900 python3 -I new/box127/expir.py $a ${b:--} 2>&1 | grep '^EXP\|Error\|error' | sed "s|^|GAME $a $b |"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box127/c_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box127/c_alt.txt
