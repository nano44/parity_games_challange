#!/bin/bash
# L-LOWER 18: ONE full pgad6 question on a BASE (the base's design fixed except the clients XS; signs, helper gates, helper starts free;
# FIXC 16,17). Usage: n.sh TAG BASE P R XS XORD OUTDIR [TL=2900] (env FENC). Memory cap 13 GB (ulimit). Last line "n exit".
TAG=$1; B=$2; P=$3; R=$4; XS=$5; XO=$6; OD=$7; TL=${8:-2900}; here=$(cd "$(dirname "$0")" && pwd); L=$OD/$TAG.log; s=$(date +%s)
ulimit -v 13000000
F6R=$R XALL=1 XORD=$XO FIXC=16,17 timeout $TL python3 $here/pgad6.py $B $here/../l10/out/core8_HIT7.txt $P $XS '' $OD/$TAG > $L.raw 2>&1; rc=$?
grep -v "^PGAD" $L.raw | cut -c1-250 > $L; rm -f $L.raw
echo "$TAG base $(basename $B) XS $XS XORD $XO FIXC 16,17 P $P R $R secs $(( $(date +%s)-s )) rc $rc" >> $L
if grep -q "RESULT SAT" $L; then (cd $here/..; python3 l13/prefcheck.py $OD/${TAG}_dec.txt l10/out/core8_HIT7.txt $FENC | tail -1
  python3 l16/f6check.py $OD/${TAG}_dec.txt l10/out/core8_HIT7.txt 510 13 | cut -c1-200
  python3 l18/inframe.py l17/run/A2_solved.txt $OD/${TAG}_dec.txt 8,10,11,12,14,15 16,17 | cut -c1-120) >> $L; fi
echo "n exit" >> $L
