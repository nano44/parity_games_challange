#!/bin/bash
# R171 FB climbs: seeds farrise25_n32 (seeds 1, 2), rise_fb38_n48 (seed 1), random n 32 KO 1 and KO 2. Output out/fbc_*.txt
cd "$(dirname "$0")"; mkdir -p out
{ echo "python3 -I climb171.py 1 ${ITERS:-6000} out/fbc_far1 ../so/instances/farrise25_n32.pg - > out/fbc_far1.txt 2>&1"
  echo "python3 -I climb171.py 2 ${ITERS:-6000} out/fbc_far2 ../so/instances/farrise25_n32.pg - > out/fbc_far2.txt 2>&1"
  echo "python3 -I climb171.py 1 ${ITERS:-6000} out/fbc_rise1 ../so/instances/rise_fb38_n48.pg - > out/fbc_rise1.txt 2>&1"
  echo "env N=32 KO=1 python3 -I climb171.py 3 ${ITERS:-6000} out/fbc_r32k1 > out/fbc_r32k1.txt 2>&1"
  echo "env N=32 KO=2 python3 -I climb171.py 4 ${ITERS:-6000} out/fbc_r32k2 > out/fbc_r32k2.txt 2>&1"; } | xargs -P 4 -I{} bash -c "timeout 4000 {}"
