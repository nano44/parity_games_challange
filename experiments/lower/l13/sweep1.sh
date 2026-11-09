#!/bin/bash
# L-LOWER 13: single-helper sweep. For each helper mover h in HLIST, G = [h]: ascending prefixes from T0 to the first UNSAT (pgad3).
# Usage: sweep1.sh BASE TARGET XS HLIST T0 P OUT [TLIM]. One line per h; resumable.
B=$1; C=$2; XS=$3; HL=$4; T0=$5; P=$6; OUT=$7; TL=${8:-1800}; cd "$(dirname "$0")"
for h in $(python3 -c "import sys
o=[]
for p in sys.argv[1].split(','):
    a,b=(p.split('-')+[p])[:2]; o+=range(int(a),int(b)+1)
print(*o)" $HL); do
  tag="$(basename $B .txt) XS $XS G $h"; grep -qF "$tag " $OUT 2>/dev/null && continue
  last=0; res=ALL_SAT
  for t in $(seq $T0 $P); do
    q=$(timeout $TL python3 pgad3.py $B $C $t $XS $h out/sw_$h 2>&1 | grep -E "RESULT|CHECK" | tr '\n' ' ')
    case "$q" in *MISMATCH*) res="MISMATCH_at $t"; break;; *UNSAT*) res="UNSAT_at $t"; break;; *"RESULT SAT"*) last=$t;; *) res="NO_ANSWER_at $t"; break;; esac
  done
  [ $last -eq 0 ] && [ "$res" != ALL_SAT ] && res="$res (T0 $T0 already UNSAT)"
  echo "$tag  last_SAT $last  $res" >> $OUT
done
