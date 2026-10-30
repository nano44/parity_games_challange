#!/bin/bash
# L-SI box 51b §6: deepint.py over box 50b's corpus (sbcg 719 + alt 413, 300 s per game) and box 87's SHALLOW-k killers.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/gate/deepint.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/gate/deep2_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/gate/deep2_alt.txt
for N in 2 3 4 5 6 7 8; do one new/box54/out/switchbestexp_$N.pg; done > si/gate/deep2_extra.txt
one new/box54/out/hf/counter_symsi_8.pg >> si/gate/deep2_extra.txt
