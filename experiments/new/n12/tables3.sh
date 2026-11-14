#!/bin/bash
# N12 record tables, part 3: the combined kill family U_N = counter_symsi_N + 50 odd pendants on the top vertex + one top-priority pendant.
# usage: bash tables3.sh > out/tables3.txt   (same line format as tables.sh)
set -u
cd "$(dirname "$0")"
for pol in Sbig topx duet; do
  for N in 5 6 7 8 9 10 11; do
    r=$(python3 n12.py --policy $pol inst/symsi_u50T0_$N.pg | tail -1); set -- $r
    echo "KILL-U-$pol symsi_u50T0 $N $2 $4 $6 $8 ${10} ${12} ${14} ${16} ${18} ${20} ${22} ${24} ${26} ${28}"
  done
done
