#!/bin/bash
# L-LOWER 18: ONE pgad6 question (one per task). Usage: q.sh TAG BASE P R HINT|- OUTDIR [TL=2900]
# Fixed frame (BOX L18): XS 8,11,12,14,15, XORD 8,11,12,15,14, XALL=1, FIXC 16,17, G empty, target ../l10/out/core8_HIT7.txt.
# On SAT: replay (l13/prefcheck.py, sim6 = fenc; FENC env = fenc binary) and f6check rows 0..510. Last line: "q exit <rc>".
TAG=$1; B=$2; P=$3; R=$4; HINT=$5; OD=$6; TL=${7:-2900}; here=$(cd "$(dirname "$0")" && pwd); T=$here/../l10/out/core8_HIT7.txt
LOG=$OD/$TAG.log; s=$(date +%s)
if [ "$HINT" != "-" ]; then export PHASE=$HINT; else unset PHASE; fi
F6R=$R XALL=1 XORD=8,11,12,15,14 FIXC=16,17 timeout $TL python3 $here/pgad6.py $B $T $P 8,11,12,14,15 '' $OD/$TAG > $LOG.raw 2>&1; rc=$?
grep -v "^PGAD" $LOG.raw | cut -c1-260 > $LOG; rm -f $LOG.raw
echo "TAG $TAG P $P R $R HINT $(basename $HINT) secs $(( $(date +%s)-s )) rc $rc" >> $LOG
if grep -q "RESULT SAT" $LOG; then
  (cd $here/..; python3 l13/prefcheck.py $OD/${TAG}_dec.txt l10/out/core8_HIT7.txt $FENC | tail -1; python3 l16/f6check.py $OD/${TAG}_dec.txt l10/out/core8_HIT7.txt 510 13 | cut -c1-200) >> $LOG
fi
echo "q exit $rc" >> $LOG
