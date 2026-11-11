#!/bin/bash
# L-LOWER 15: k* grid of kr.py. For each P in PLIST and each client set in CSETS (space-separated, e.g. "8 11 12 13 8,11,12,13"),
# k = 1..4 ascending until the first SAT; one line per (P, set). Resumable. Usage: grid.sh GENOME TARGET "PLIST" "CSETS" OUT [TLIM]
G=$1; C=$2; PL=$3; CS=$4; OUT=$5; TL=${6:-2900}; cd "$(dirname "$0")/.."
for P in $PL; do for X in $CS; do
  grep -q "^P $P clients $X " $OUT 2>/dev/null && continue
  line="P $P clients $X"; ks=""
  for k in 1 2 3 4; do
    r=$(timeout $TL python3 l15/kr.py $G $C $k $P $X | grep -E "^KR|^RESULT" | tr '\n' ' ')
    R=$(echo "$r" | grep -o "RESULT [A-Z]*" | cut -d' ' -f2); [ -z "$R" ] && R=NO_ANSWER
    ks="$ks k$k:$R"; info=$(echo "$r" | grep -o "(free pre-states, changes R) {[^}]*}")
    [ "$R" = SAT ] && break; [ "$R" = NO_ANSWER ] && break
  done
  echo "$line $info |$ks" >> $OUT
done; done
