#!/bin/bash
# Box 217 track B (L-NEW successor 76): enumeration-depth climbs on ladders, (i) xtw: Xi-target = W-target («self-fuelling»), (ii) free
# Xi-targets; CLIMB217_OBJ=enum, CLIMB217_LADDER=1, w 2, degree 2, d 3..10, seeds 1-2; resumable; FINAL lines to out/climbX217.out.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1 CLIMB217_OBJ=enum CLIMB217_LADDER=1; IT=${1:-30000}; mkdir -p out/rec
for s in 1 2; do for d in 3 4 5 6 7 8 9 10; do for xtw in 1 0; do
  suf=$([ $xtw = 1 ] && echo _xtw); [ -f out/rec/rec_w2_d${d}_D2_s${s}_enum_lad$suf.json ] && continue
  CLIMB217_XTW=$xtw timeout 3600 python3 -I climb217.py 2 $d 2 $s $IT out/rec | grep '^FINAL' | sed "s/^/xtw $xtw /" >> out/climbX217.out || echo "TIMEOUT d $d seed $s xtw $xtw" >> out/climbX217.out
done; done; done
