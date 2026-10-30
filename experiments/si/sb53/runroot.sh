#!/bin/bash
# L-SI box 53: rootflip.py on box 50b's corpus (sbcg + alt lists) and the L-RED families (as si/heads52/rundset.sh).
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 600 python3 -I si/sb53/rootflip.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > si/sb53/root_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > si/sb53/root_alt.txt
for f in latew_K16_m32 fx_K8_m32; do one si/gate/inst/$f.pg si/gate/inst/$f.start; done > si/sb53/root_red.txt
