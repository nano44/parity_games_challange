#!/bin/bash
# L-NEW box 143 pins: L-RED R188's exact pins, copied read-only from claude/l-red ce1d19e9 (experiments/red/r188/instances/) into
# new/box143/inst/. Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py).
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for b in x3_L8_n48 g4_L12_n62; do
  p=new/box143/inst/$b; st=$p.start
  echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
done
rm -rf $t
