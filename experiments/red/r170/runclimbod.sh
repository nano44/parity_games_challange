#!/bin/bash
# R170 climbs scoring only fallback-free windows with ODIFF >= KO (MINODIFF=KO): KO = 1, 2 at n 12..32, seeds 1-2. Output out/climbod_*.txt
cd "$(dirname "$0")"; mkdir -p out
for n in 12 16 24 32; do for ko in 1 2; do for s in 1 2; do
  echo "MINODIFF=$ko FBFREE=1 timeout 3000 python3 -I climb170.py $n $ko $s ${ITERS:-20000} out/d_n${n}_k${ko}_s${s} > out/climbod_n${n}_k${ko}_s${s}.txt 2>&1"
done; done; done | xargs -P 4 -I{} bash -c "{}"
