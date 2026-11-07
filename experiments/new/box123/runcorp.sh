#!/bin/bash
# L-NEW box 123: fbcount.py (TWO-FIX windows with fallbacks) on the box 53 corpus (box 118's lists and repaired starts).
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac
  timeout 900 python3 -I new/box123/fbcount.py $a ${b:--} 2>&1 | sed "s|^|GAME $a $b |"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box123/f_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box123/f_alt.txt
