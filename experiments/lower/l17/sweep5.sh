#!/bin/bash
# L-LOWER 17: sweep.sh with l16/pgad5.py (env XALL, XORD, FIXC passed through). Usage: sweep5.sh TAG BASE TARGET XS G T0 P TL (G may be empty: quote it)
TAG=$1; B=$2; C=$3; XS=$4; G=$5; T0=$6; P=$7; TL=$8
L=$(cd "$(dirname "$0")/.." && pwd); SW=${SW:-$(dirname "$0")}; LOG=$SW/$TAG.log
cd $L/l16
for t in $(seq $T0 $P); do
  grep -q "^P $t " $LOG 2>/dev/null && { grep -q "^P $t RESULT SAT" $LOG || exit 0; continue; }
  s=$(date +%s)
  q=$(timeout $TL python3 pgad5.py $B $C $t $XS "$G" $SW/${TAG}_P$t 2>&1 | grep -E "RESULT|CHECK" | tr '\n' ' ')
  [ -z "$q" ] && q="NO_ANSWER"
  echo "P $t $q secs $(( $(date +%s)-s ))" >> $LOG
  case "$q" in *MISMATCH*) exit 0;; *"RESULT SAT"*) ;; *) exit 0;; esac
done
