#!/usr/bin/env bash
# L-SI box 98: freeze the climb bests of out/climb98.out into inst/C98_<d>_<w>_<D>.json (one genome per file) and write inst/SHA1SUMS.
set -eu
cd "$(dirname "$0")"
mkdir -p inst
grep '^BEST ' out/climb98.out | while read -r _ d w D js; do printf '%s\n' "$js" > "inst/C98_${d}_${w}_${D}.json"; done
(cd inst && sha1sum C98_*.json > SHA1SUMS)
