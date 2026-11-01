#!/bin/bash
# R170 climbs at KO = 0 (one-player games: every Odd vertex has one edge; windows have ODIFF 0) and KO = 1 at n 64. FBFREE=1.
cd "$(dirname "$0")"; mkdir -p out
for a in "12 0 1" "16 0 1" "24 0 1" "32 0 1" "64 1 1" "64 2 1"; do set -- $a
  echo "FBFREE=1 timeout 5000 python3 -I climb170.py $1 $2 $3 ${ITERS:-20000} out/c_n$1_k$2_s$3 > out/climb_n$1_k$2_s$3.txt 2>&1"
done | xargs -P 2 -I{} bash -c "{}"
