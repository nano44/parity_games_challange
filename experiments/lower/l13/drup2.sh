#!/bin/bash
# L-LOWER 13: DRUP check of every pair UNSAT of sweep2 output IN (prefix P), worker W of NW. Resumable (skips pairs in OUT).
# Usage: drup2.sh IN BASE TARGET XS P W NW DRUP WORKDIR OUT
IN=$1; B=$2; C=$3; XS=$4; P=$5; W=$6; NW=$7; DR=$8; WD=$9; OUT=${10}; cd "$(dirname "$0")"
grep -o "G [0-9]*,[0-9]*" $IN | awk '{print $2}' | awk -v w=$W -v n=$NW 'NR % n == w' | while read g; do
  grep -qF " $XS $g SKIP" $OUT 2>/dev/null && continue
  PGAD=pgad3.py timeout 1800 python3 pdrup.py $DR $WD $B $C $P $XS $g >> $OUT 2>&1 || echo "pdrup FAILED $g" >> $OUT
done
