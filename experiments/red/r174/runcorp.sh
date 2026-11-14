#!/bin/bash
# R174: phasepair.py + zclimb.py on the box 53 corpus, de-duplicated per RESULTS Erratum E-1: sbcg.lst (719 runs) plus only the
# alt_all.lst lines that carry a start (the start-less ones repeat sbcg runs). Starts repaired as red/r170/runcorp.sh. -> out/corp.txt
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac
  r1=$(timeout 900 python3 -I red/r174/phasepair.py $a ${b:--} 2>&1 | tail -1); r2=$(timeout 900 python3 -I red/r174/zclimb.py $a ${b:--} 2>&1 | tail -1); echo "GAME $a ${b:--} $r1 # $r2"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P ${P:-4} -I{} bash -c 'one "{}"'
  awk 'NF>=2' si/root/logs/alt_all.lst | xargs -P ${P:-4} -L 1 bash -c 'one "$@"' _ ; } > red/r174/out/corp.txt
