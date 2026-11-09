#!/bin/bash
# L-LOWER 13: helper-count scan of pgad.py. Usage: scan.sh BASE TARGET XS KMIN KMAX P OUT [R0] [TLIM]
# For k = KMIN..KMAX, G = movers 64-k..63: ascending prefixes t = 1..P until the first UNSAT (or a NO_ANSWER after TLIM s, default
# 3600; from k-1's last SAT prefix on, see v2 below). One line per k: last SAT prefix, first UNSAT prefix (or the undecided one). The decoded model of the last SAT prefix is kept
# in out/<base>_X<XS>_k<k>_dec.txt. Resumable: a k with a line in OUT is skipped.
B=$1; C=$2; XS=$3; K0=$4; KM=$5; P=$6; OUT=$7; R0=${8:-0-63}; TL=${9:-3600}; cd "$(dirname "$0")"; mkdir -p out
for k in $(seq $K0 $KM); do
  G="$((64-k))-63"; tag="$(basename $B .txt) $(basename $C .txt) XS $XS k $k G $G R0 $R0 P $P"
  grep -qF "$tag " $OUT 2>/dev/null && continue
  last=0; res="ALL_SAT"; pre=out/$(basename $B .txt)_$(basename $C .txt)_X${XS//,/_}_k$k
  # v2 (helpers keep their own base targets): the k question contains the k-1 one, so start at k-1's last SAT prefix
  t0=1; if [ $k -gt $K0 ] || [ -s $OUT ]; then pl=$(grep -F "XS $XS k $((k-1)) " $OUT 2>/dev/null | grep -o "last_SAT [0-9]*" | tail -1 | awk '{print $2}'); [ -n "$pl" ] && [ "$pl" -gt 0 ] && t0=$pl; fi
  for t in $(seq $t0 $P); do
    q=$(timeout $TL python3 pgad.py $B $C $t $XS $G ${pre}_t$t $R0 2>&1 | grep -E "RESULT|SOLVE|CHECK" | tr '\n' ' ')
    case "$q" in
      *MISMATCH*) res="DECODE_MISMATCH_at $t"; break;;
      *UNSAT*) res="UNSAT_at $t ($q)"; break;;
      *"RESULT SAT"*) last=$t; [ -f ${pre}_t$((t-1))_dec.txt ] && rm -f ${pre}_t$((t-1))_dec.txt;;
      *) res="NO_ANSWER_at $t (limit $TL s)"; break;;
    esac
  done
  echo "$tag  last_SAT $last  $res  $(date -u +%H:%MZ)" >> $OUT
done
