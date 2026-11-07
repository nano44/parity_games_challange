#!/bin/bash
# R170: freeze.py (MINL=2) on the box 53 corpus lists used by L-NEW box 121 (new/box59/sbcg.lst, si/root/logs/alt_all.lst; repaired starts
# for comp54_n80 / n3cov_lean as in box121/runcorp.sh). Output red/r170/out/corp.txt (one FREEZE summary line per run + window lines).
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac
  r=$(MINL=2 timeout 900 python3 -I red/r170/freeze.py $a ${b:--} 2>&1); echo "GAME $a ${b:--} $(echo "$r" | tr '\n' '#')"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P ${P:-2} -I{} bash -c 'one "{}"'
  cat si/root/logs/alt_all.lst | xargs -P ${P:-2} -L 1 bash -c 'one "$@"' _ ; } > red/r170/out/corp.txt
