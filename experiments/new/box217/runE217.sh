#!/bin/bash
# Box 217 track B (L-NEW successor 76): enumeration-depth climbs (CLIMB217_OBJ=enum: maximise (k(G), T_key)), ladder-shaped W-graph
# (CLIMB217_LADDER=1, the towers' shape), w 2, degree 2, d = 3..12, seeds 1-3; resumable; FINAL lines to out/climbE217.out.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1 CLIMB217_OBJ=enum CLIMB217_LADDER=1; IT=${1:-50000}; mkdir -p out/rec
for s in 1 2 3; do for d in 3 4 5 6 7 8 9 10 11 12; do
  [ -f out/rec/rec_w2_d${d}_D2_s${s}_enum_lad.json ] && continue
  timeout 3600 python3 -I climb217.py 2 $d 2 $s $IT out/rec | grep '^FINAL' >> out/climbE217.out || echo "TIMEOUT d $d seed $s" >> out/climbE217.out
done; done
