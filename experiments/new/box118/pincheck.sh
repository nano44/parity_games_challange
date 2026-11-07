#!/bin/bash
# L-NEW box 118 pins (the R17-transfer DEAD instances): Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), and n5b
# state by state (si/root/n5bcmp.py). Run from anywhere; needs tools/oink/build (scripts/setup_oink.sh).
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "n5-epoch/instances/lend107_n32 n5-epoch/instances/lend107_n32.start" "new/box116/inst/fbg_K12_m6_m24 new/box116/inst/fbg_K12_m6_m24_fixed.start"; do
  set -- $p; b=$(basename $1)
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
  python3 -I new/box118/gate.py $1.pg $2 | tail -1
done
rm -rf $t
