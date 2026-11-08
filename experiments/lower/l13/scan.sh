#!/bin/bash
# L-LOWER 13: helper-count scan of pgad.py. Usage: scan.sh BASE TARGET XS KMAX P OUT [R0]
# For k = 1..KMAX, G = movers 64-k..63; prefix P; if UNSAT, ascending prefixes 1..P for the first UNSAT t. Resumable: skips lines in OUT.
B=$1; C=$2; XS=$3; KM=$4; P=$5; OUT=$6; R0=${7:-0-63}; cd "$(dirname "$0")"; mkdir -p out
for k in $(seq 1 $KM); do
  G="$((64-k))-63"; tag="$(basename $B .txt) XS $XS k $k G $G R0 $R0 prefix $P"
  grep -qF "$tag " $OUT 2>/dev/null && continue
  r=$(timeout 5400 python3 pgad.py $B $C $P $XS $G out/$(basename $B .txt)_X${XS//,/_}_k$k $R0 2>&1 | grep RESULT | tail -1)
  ft=-
  case "$r" in *UNSAT*)
    for t in $(seq 1 $P); do
      q=$(timeout 5400 python3 pgad.py $B $C $t $XS $G /dev/null $R0 2>&1 | grep RESULT | tail -1)
      case "$q" in *UNSAT*) ft=$t; break;; esac
    done;;
  esac
  echo "$tag  ${r:-NO_ANSWER}  first_UNSAT_t $ft" >> $OUT
done
