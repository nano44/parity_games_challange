#!/bin/bash
# L-NEW box 120 fixes: the two DEAD pins (lend107_n32, fbg_K12_m6_m24 with repaired start): Oink 8fbf0a7 --zlk / --tl verified vs N5's
# regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), and box120/inphase.py (both phase groupings). Needs tools/oink/build.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "n5-epoch/instances/lend107_n32 n5-epoch/instances/lend107_n32.start" "new/box116/inst/fbg_K12_m6_m24 new/box116/inst/fbg_K12_m6_m24_fixed.start"; do
  set -- $p; b=$(basename $1); echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
  python3 -I new/box120/inphase.py $1.pg $2
done
rm -rf $t
