#!/bin/bash
# L-NEW box 52: comparator graft on R109's topfix family (red/seg/hnh1.py N topfix): flippair -> graft (mode ab) -> rlv. Run from experiments/.
B=new/box52
for N in "$@"; do
  g=$B/out/topfix_n$N; [ -f $g.pg ] || python3 -I red/seg/hnh1.py $N topfix $g.pg $g.start > /dev/null 2>&1
  read a b fl ph <<<"$(python3 -I $B/flippair.py $g.pg $g.start | tr -d '(),')"
  python3 $B/graft.py $g.pg $g.start $a $b ${g}_cmp.pg ${g}_cmp.start 0 ab
  base=$(python3 -I $B/rlv.py --one $g.pg $g.start | grep ^TOP | head -1)
  cmp=$(python3 -I $B/rlv.py --one ${g}_cmp.pg ${g}_cmp.start | grep -E "^TOP|PASS|FAIL" | tr '\n' ' ')
  echo "N=$N pair=($a,$b) flips=$fl | base $base | graft $cmp"
done
