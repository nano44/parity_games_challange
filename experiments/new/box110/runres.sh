#!/bin/bash
# L-NEW box 110: resets.py on the box 53 corpus and the quadratic pins.
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 300 python3 -I new/box110/resets.py "$@" 2>&1 | tail -1)"; }; export -f one
for p in "new/box110/sbq2_K8_m16 new/box110/sbq2_K8_m16.start" "red/xich/instances/obs_K12_m24 red/xich/instances/obs_K12_m24.start" "red/wlev/instances/src2_K3 red/wlev/instances/src2_K3.start"; do set -- $p; one $1.pg $2; done > new/box110/res_pins.txt
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box110/res_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box110/res_alt.txt
