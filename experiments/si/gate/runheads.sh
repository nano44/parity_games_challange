#!/bin/bash
# L-SI box 51b §11: heads.py (§13 head Xi-changes per W-run) on box 50b's corpus and the L-RED families.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I si/gate/heads.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/gate/heads_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/gate/heads_alt.txt
for f in latew_K16_m32 fx_K8_m32; do one si/gate/inst/$f.pg si/gate/inst/$f.start; done > si/gate/heads_red.txt
