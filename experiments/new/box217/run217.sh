#!/bin/bash
# Box 217 climbs (L-NEW successor 76), resumable: a (d, seed) whose record file exists is skipped. FINAL lines to out/climb217.out.
# Usage: bash run217.sh ITERS SEEDS "D-LIST"     (w = 2, degree 2)
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; IT=$1; SEEDS=$2; DL=$3; mkdir -p out/rec
for s in $(seq 1 $SEEDS); do for d in $DL; do
  [ -f out/rec/rec_w2_d${d}_D2_s$s.json ] && continue
  timeout 3600 python3 -I climb217.py 2 $d 2 $s $IT out/rec | grep '^FINAL' >> out/climb217.out || echo "TIMEOUT d $d seed $s" >> out/climb217.out
done; done
