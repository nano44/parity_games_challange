#!/bin/bash
# L-NEW box 144 pins: L-RED R189 lag pins, copied read-only from claude/l-red 80bfb1d0 (experiments/red/r189/instances/, sha1 = its pins.sha1) into
# new/box144/inst/. Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py).
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for b in lag1_n48 lag1u_n48 lag2c_d4_n62 nest_d3_L4_n48; do
  p=new/box144/inst/$b; st=$p.start
  echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
done
rm -rf $t
