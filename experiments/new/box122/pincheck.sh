#!/bin/bash
# L-NEW box 122 pins: gci3_n24 (largest PHNF / (n-1) in ODIFF 1 windows, 20 / 23; with its start file gci3_n24.start),
# farrise25_n32 (most fallbacks in one ODIFF 1 window, 28; default start written out), b5_os_n40 (box 121's default start; ODIFF 1 trace).
# Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box122/windows.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "n5-epoch/instances/gci3_n24 n5-epoch/instances/gci3_n24.start" "red/so/instances/farrise25_n32 new/box122/inst/farrise25_n32_default.start" "n5-exhaustive/instances/b5_os_n40 new/box121/inst/b5_os_n40_default.start"; do
  set -- $p; b=$(basename $1); echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
  python3 -I new/box122/windows.py $1.pg $2 4
done
rm -rf $t
