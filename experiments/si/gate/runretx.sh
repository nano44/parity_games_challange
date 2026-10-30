#!/bin/bash
# L-SI box 51b §11: retx.py (RETURN-CHARGE' over whole runs, W-run bound) on box 50b's corpus and the L-RED families.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/gate/retx.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/gate/retx_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/gate/retx_alt.txt
for f in latew_K16_m32 fx_K8_m32; do one si/gate/inst/$f.pg si/gate/inst/$f.start; done > si/gate/retx_red.txt
