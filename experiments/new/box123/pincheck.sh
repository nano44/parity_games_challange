#!/bin/bash
# L-NEW box 123 pins: frz24 (GAP-DESC DEAD: GAPF 18 -> 18 between two fallbacks with no Xi(o) change; with frz24.start),
# rise_fb38_n48 (34 fallbacks in one ODIFF 1 window, FB / (XO + 1) = 34 < n = 48; default start written to box123/inst/).
# Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box123/fbcount.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "red/n5inj/instances/frz24 red/n5inj/instances/frz24.start" "red/so/instances/rise_fb38_n48 new/box123/inst/rise_fb38_n48_default.start"; do
  set -- $p; b=$(basename $1); echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
  python3 -I new/box123/fbcount.py $1.pg $2
done
rm -rf $t
