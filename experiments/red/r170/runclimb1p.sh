#!/bin/bash
# R170 one-player climbs (KO = 0, no Odd vertices at all: ODD=0) on denser graphs (MAXDEG = n - 1): is N5 (= its one window) superlinear?
cd "$(dirname "$0")"; mkdir -p out
for n in 8 10 12 16 20; do
  echo "ODD=0 MAXDEG=$((n-1)) FBFREE=1 timeout 4000 python3 -I climb170.py $n 0 3 ${ITERS:-30000} out/p_n${n} > out/climbp_n${n}.txt 2>&1"
done | xargs -P 2 -I{} bash -c "{}"
