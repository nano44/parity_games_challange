#!/bin/bash
# L-NEW box 117 pins: Oink (pinned 8fbf0a7, --zlk verified, --tl second solver) against N5's regions at its stop (box107/pinwin.py), and
# n5b state by state via si/root/n5bcmp.py. fb3_K4_m6_m12_m12 is L-RED's R165 pin (l-red b31f9477), copied unchanged. Run from anywhere.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "new/box117/inst/fb3_K4_m6_m12_m12 new/box117/inst/fb3_K4_m6_m12_m12.start"; do
  set -- $p; b=$(basename $1)
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  cmp -s <(grep -E '^[0-9]+ [01]' $t/$b.zlk.sol | awk '{print $1,$2}' | sort -n) <(grep -E '^[0-9]+ [01]' $t/$b.tl.sol | awk '{print $1,$2}' | sort -n) && echo "OINK $b zlk = tl regions" || echo "OINK $b zlk != tl regions"
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
done
rm -rf $t
