#!/bin/bash
# L-LOWER 12: first infeasible prefix t of a fixed-wiring, fixed-rank (W0-R) question with L-COMP's enc32 (read-only copy):
# for base genome G and core target C, prefixes t = 1..TMAX ascending until the first UNSAT (CaDiCaL). Output lines "G C t RESULT".
# Usage: fscan.sh G C TMAX OUT
G=$1; C=$2; TM=$3; OUT=$4; cd "$(dirname "$0")"
for t in $(seq 1 $TM); do
  r=$(timeout 1200 python3 enc32_lcomp.py $G $C 8 --fix ranks --solve cadical --prefix $t 2>&1 | grep RESULT | tail -1)
  echo "$(basename $G) $(basename $C) prefix $t ${r:-NO_ANSWER}" >> $OUT
  case "$r" in *UNSAT*) break;; esac
done
