#!/bin/bash
# L-NEW box 107: finpot.py on L-SI box 53's corpus (box59 sbcg list + si/root alt list; as si/sb53/runceil.sh) and the five pins.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box107/finpot.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box107/fin_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box107/fin_alt.txt
for f in red/tie/instances/u23sw64_n32 si/runlin/instances/runfam_K40 red/xich/instances/obs_K12_m24 red/wlev/instances/src2_K3 red/wlev/instances/rcl_K24; do one $f.pg $f.start; done > new/box107/fin_pins.txt
