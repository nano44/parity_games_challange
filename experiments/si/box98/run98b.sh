#!/usr/bin/env bash
# L-SI box 98: climb98 (max T3 per shape), seed 9801, 600 iterations, shapes (d, w, D) = (2,2,3) (2,3,3) (3,3,3) (3,4,3) (4,4,3) (4,5,3)
# (5,5,3). Engine pin l-new fcba92fc. Output: out/climb98.out (BEST genomes are frozen into inst/ by freeze98.sh).
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T" || exit 3
export ROOT="$T"
python3 -I climb98.py 9801 600 2 2 3 2 3 3 3 3 3 3 4 3 4 4 3 4 5 3 5 5 3 > out/climb98.out || exit 1
echo DONE
