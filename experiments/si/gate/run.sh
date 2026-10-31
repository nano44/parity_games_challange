#!/bin/bash
# L-SI box 51b: gate.py over box 50b's corpus (sbcg 719 + alt 413, 300 s per game) and the two L-RED quadratic families.
cd "$(dirname "$0")/../.."
one() { echo "GAME $1 $(timeout 300 python3 -I si/gate/gate.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/gate/gate_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/gate/gate_alt.txt
for f in latew_K16_m32 fx_K8_m32; do one si/gate/inst/$f.pg si/gate/inst/$f.start; done > si/gate/gate_red.txt
