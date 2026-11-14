#!/bin/bash
# R170 climbs: KO = 1, 2, 3 at n = 12..48 (seeds 1-2), FBFREE=1 (fallback-free windows). Output out/climb_*.txt
cd "$(dirname "$0")"; mkdir -p out
for n in 12 16 24 32 48; do for ko in 2 1 3; do for s in 1 2; do
  echo "FBFREE=1 timeout 3000 python3 -I climb170.py $n $ko $s ${ITERS:-20000} out/c_n${n}_k${ko}_s${s} > out/climb_n${n}_k${ko}_s${s}.txt 2>&1"
done; done; done | xargs -P 4 -I{} bash -c "{}"
