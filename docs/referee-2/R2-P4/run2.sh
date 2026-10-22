#!/bin/bash
# usage: run.sh listfile outfile relabel_seeds
SP=/tmp/claude-0/-home-user-parity-games-challange/ed877541-f327-55e7-9156-81a7b36a0873/scratchpad
O=$SP/oinkp/build/oink; T=$(mktemp -d $SP/tmpXXXX)
while read f; do
  for rev in 0 1; do
    for s in $(seq 0 $3); do
      if [ $s = 0 ]; then g=$f; else python3 -I $SP/relabel.py $f $s $T/g.pg || continue; g=$T/g.pg; fi
      if [ $rev = 1 ]; then r=$(R2_REV=1 timeout 60 $O --dtl --no-single --no-wcwc --no-loops $g 2>&1 >/dev/null | grep -E "R2FDLSUM|R2FDL search" | tr "\n" " "); else r=$(timeout 60 $O --dtl --no-single --no-wcwc --no-loops $g 2>&1 >/dev/null| grep -E "R2FDLSUM|R2FDL search" | tr "\n" " "); fi
      echo "$f rev=$rev s=$s $r"
    done
  done
done < $1 > $2
