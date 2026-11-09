#!/bin/bash
# L-LOWER 13: single-mover culprits of a pgad UNSAT: for each core mover x = 0..15, re-solve with SKIP=x (x's constraints dropped).
# Usage: culprit.sh BASE TARGET PREFIX XS G OUT [R0]. Output: one line listing the x whose drop makes it SAT.
B=$1; C=$2; P=$3; XS=$4; G=$5; OUT=$6; R0=${7:-0-63}; cd "$(dirname "$0")"; L=""
for x in $(seq 0 15); do
  q=$(SKIP=$x timeout 3000 python3 pgad.py $B $C $P $XS $G /dev/null $R0 2>&1 | grep RESULT | tail -1)
  case "$q" in *UNSAT*) ;; *"RESULT SAT"*) L="$L $x";; *) L="$L ?$x";; esac
done
echo "$(basename $B .txt) $(basename $C .txt) XS $XS G $G prefix $P  single-mover drops giving SAT:${L:- none}" >> $OUT
