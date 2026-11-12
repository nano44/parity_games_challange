#!/bin/bash
# L-LOWER 18: batch of LNS questions around one hint. Usage: lnsb.sh TAG BASE HINT OUTDIR TL "P:R:LNS:LNSFREE" ...   (LNS may be "-" = none)
# Frame as q.sh (L18); env XSL / XORDL override the clients and their order (frame L18b: XSL=8,10,11,12,14,15 XORDL=8,11,10,12,15,14). On SAT: replay (FENC env) + f6check 0..510. Log OUTDIR/TAG.log, last line "lnsb exit".
TAG=$1; B=$2; H=$3; OD=$4; TL=$5; shift 5; here=$(cd "$(dirname "$0")" && pwd); LOG=$OD/$TAG.log
for q in "$@"; do
  IFS=: read P R F C <<< "$q"; [ "$F" = "-" ] && F=""; t=${TAG}_P${P}R${R}_${F//,/-}_${C//,/-}; s=$(date +%s)
  r=$(LNS=$F LNSFREE=$C PHASE=$H F6R=$R XALL=1 XORD=${XORDL:-8,11,12,15,14} FIXC=16,17 timeout $TL python3 $here/pgad6.py $B $here/../l10/out/core8_HIT7.txt $P ${XSL:-8,11,12,14,15} '' $OD/$t 2>&1 | grep -E "^RESULT|^CHECK" | cut -c1-120 | tr '\n' ' ')
  echo "$t P $P R $R LNS $F FREE $C: ${r:-NO_ANSWER} secs $(( $(date +%s)-s ))" >> $LOG
  if [[ "$r" == *"RESULT SAT"* ]]; then (cd $here/..; python3 l13/prefcheck.py $OD/${t}_dec.txt l10/out/core8_HIT7.txt $FENC | tail -1; python3 l16/f6check.py $OD/${t}_dec.txt l10/out/core8_HIT7.txt 510 13 | cut -c1-160) >> $LOG; fi
done
echo "lnsb exit" >> $LOG
