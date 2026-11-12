#!/usr/bin/env bash
# L-SI box 104, Addendum A, O2 probe runner: head-to-head hill climbs of N5 (spec) iterations on free vs E-DOM genomes of the same shape.
# Usage: runc104.sh STEPS "D W DEG" ... ; env SEEDS (default "1 2 3"); output out/climb104.out (appended per climb).
# The frozen out/climb104.out: bash runc104.sh 3000 "4 3 3" "6 2 3" "8 2 2"   (remove out/climb104.out first; about 40 min, one core).
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red"
STEPS=$1; shift
for shape in "$@"; do for seed in ${SEEDS:-1 2 3}; do for mode in free edom; do
  python3 -I climb104.py $mode $seed $shape $STEPS >> out/climb104.out 2>> climb104.err || echo "CLIMB104 FAILED $mode $seed $shape" >> out/climb104.out
done; done; done
echo DONE
