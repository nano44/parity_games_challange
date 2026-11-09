#!/bin/bash
# L-LOWER 14: DRUP-check every single-helper UNSAT of a sweep (l13/pdrup.py with pgad3). Usage: drupsweep.sh DRUP BASE TARGET XS P HLIST OUT
# One line per helper; resumable (a helper with a line in OUT is skipped). Proof and CNF are deleted by pdrup.py.
D=$1; B=$2; C=$3; XS=$4; P=$5; HL=$6; OUT=$7; cd "$(dirname "$0")/../l13"; WD=$(mktemp -d)
for h in $(python3 -c "import sys
o=[]
for p in sys.argv[1].split(','):
    a,b=(p.split('-')+[p])[:2]; o+=range(int(a),int(b)+1)
print(*o)" $HL); do
  grep -q "XS $XS G $h " $OUT 2>/dev/null && continue
  r=$(PGAD=pgad3.py timeout 2900 python3 pdrup.py $D $WD $B $C $P $XS $h 2>&1 | tail -1)
  echo "XS $XS G $h prefix $P | $r" >> $OUT
done
rm -rf $WD
