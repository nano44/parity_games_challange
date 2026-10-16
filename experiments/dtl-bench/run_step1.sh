#!/usr/bin/env bash
# Step (1) of the Lead's order: exhaustive tiny games (TARGET class: priorities 0..n) and 10,000 seeded random games.
set -uo pipefail
cd "$(dirname "$0")"
for np in "1 1" "2 2" "3 3"; do set -- $np
  python3 bench.py exhaustive $1 $2 --csv results/exhaustive_n$1_P$2.csv --jobs 4 | tail -4; done
python3 ../harness/gen.py corpus out/g10k 10000 20261015 --nmin 1 --nmax 200 | tail -1
python3 bench.py files out/g10k --csv results/g10k.csv --jobs 4 --timeout 120 --pyzlk-max 200 | tail -8
