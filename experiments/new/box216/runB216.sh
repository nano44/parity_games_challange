#!/bin/bash
# Box 216 worker B (resumable): V1 split216 and qt3_196 (N5 spec mode) on the frozen set; then random Xi-cyclic genomes for all tools.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
S216_MODE=spec bash run216.sh out/split_frozen_spec.out python3 -I split216.py
Q196_MODE=spec bash run216.sh out/qt3_frozen_spec.out python3 -I ../box196/qt3_196.py --files
R=out/rand216.out; touch $R
for seed in 2161 2162 2163; do
  for t in xflip216 gate216; do
    grep -q "^$t $seed " $R || echo "$t $seed $(timeout 3000 python3 -I $t.py --rand $seed 200 rand cyc || echo TIMEOUT)" >> $R
  done
done
for seed in 2161 2162; do grep -q "^qt3 $seed " $R || echo "qt3 $seed $(Q196_MODE=spec timeout 3000 python3 -I ../box196/qt3_196.py rand $seed 200 | tail -1 || echo TIMEOUT)" >> $R; done
echo DONE >> $R
