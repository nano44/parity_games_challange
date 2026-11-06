#!/bin/bash
# L-RED R213: exact RISE queries at d 4 via r200/cubes.py (resumable; state in r213/cubes/), horizon 13 = T^R(4) (R197 exact), TMIN=0,
# no symmetry flags (z fixed); z = 0, 2, 4, 6 suffice (sigma_l swaps movers 2l, 2l+1 and preserves R). Rerun = resume.
cd "$(dirname "$0")"; mkdir -p cubes; P=${P:-1}
for z in ${ZS:-6 4 2 0}; do
  RISEZ=$z RISEMIN=9 TMIN=0 TL=${TL:-1200} P=$P python3 ../r200/cubes.py 4 13 cubes/d4_z${z}_r9 >> out/cubes_d4_z${z}_r9.log 2>&1
done
