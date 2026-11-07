#!/bin/bash
# L-NEW box 107 pins: Oink (pinned 8fbf0a7, --zlk, solution verified; --tl as second solver) against N5's regions at its stop, and
# n5b (L-COMP's independent N5) state by state via si/root/n5bcmp.py. Run from experiments/.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "red/tie/instances/u23sw64_n32 red/tie/instances/u23sw64_n32.start" "si/runlin/instances/runfam_K40 si/runlin/instances/runfam_K40.start" \
         "red/xich/instances/obs_K12_m24 red/xich/instances/obs_K12_m24.start" "red/wlev/instances/src2_K3 red/wlev/instances/src2_K3.start" \
         "red/wlev/instances/rcl_K24 red/wlev/instances/rcl_K24.start" "red/xing/instances/x31_rx48 new/box107/inst/x31_rx48.start"; do
  set -- $p; b=$(basename $1)
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  cmp -s <(grep -E '^[0-9]+ [01]' $t/$b.zlk.sol | awk '{print $1,$2}' | sort -n) <(grep -E '^[0-9]+ [01]' $t/$b.tl.sol | awk '{print $1,$2}' | sort -n) && echo "OINK $b zlk = tl regions" || echo "OINK $b zlk != tl regions"
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
done
rm -rf $t
