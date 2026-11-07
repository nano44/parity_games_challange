#!/bin/bash
# R172 TF-PH climbs: MINODIFF = KO, KO = 1, 2, n 12 / 16 / 24, seed 1; plus two seeded from R170 champions. Output out/ph_*.txt
cd "$(dirname "$0")"; mkdir -p out
{ for n in 12 16 24; do for ko in 1 2; do echo "env MINODIFF=$ko python3 -I climb172.py $n $ko 1 ${ITERS:-8000} out/ph_n${n}_k${ko} > out/ph_n${n}_k${ko}.txt 2>&1"; done; done
  echo "env MINODIFF=2 python3 -I climb172.py 32 2 2 ${ITERS:-8000} out/ph_seed32 ../r170/out/d_n32_k2_s1.pg ../r170/out/d_n32_k2_s1.start > out/ph_seed32.txt 2>&1"
  echo "env MINODIFF=1 python3 -I climb172.py 24 1 2 ${ITERS:-8000} out/ph_seed24 ../r170/out/d_n24_k1_s1.pg ../r170/out/d_n24_k1_s1.start > out/ph_seed24.txt 2>&1"; } | xargs -P 4 -I{} bash -c "timeout 3600 {}"
