#!/bin/bash
# L-NEW box 107: hier2.py on the box 53 corpus and the five pins (as runfin.sh).
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box107/hier2.py "$@" 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box107/hier2_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box107/hier2_alt.txt
for f in red/tie/instances/u23sw64_n32 si/runlin/instances/runfam_K40 red/xich/instances/obs_K12_m24 red/wlev/instances/src2_K3 red/wlev/instances/rcl_K24; do one $f.pg $f.start; done > new/box107/hier2_pins.txt
