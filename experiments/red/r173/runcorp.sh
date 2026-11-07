#!/bin/bash
# R173: portalck.py on the box 53 corpus (same lists and start repairs as red/r170/runcorp.sh). Output red/r173/out/corp.txt.
cd "$(dirname "$0")/../.."
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac
  r=$(timeout 900 python3 -I red/r173/portalck.py $a ${b:--} 2>&1 | tail -3 | tr '\n' '#'); echo "GAME $a ${b:--} $r"; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P ${P:-4} -I{} bash -c 'one "{}"'
  cat si/root/logs/alt_all.lst | xargs -P ${P:-4} -L 1 bash -c 'one "$@"' _ ; } > red/r173/out/corp.txt
