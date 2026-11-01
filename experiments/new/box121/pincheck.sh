#!/bin/bash
# L-NEW box 121 pins: cp_K4 (PHL DEAD; TWO-FIX 43 vs 2), b5_os_n40 (TWO-FIX ODIFF 1, 77 vs 7; no start file: box121/inst/b5_os_n40_default.start writes out the
# default start), s3quad_K8_m30 (TWO-FIX 263 vs 2). Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), n5b state by
# state (si/root/n5bcmp.py), brtree.py and twofix.py. Needs tools/oink/build (scripts/setup_oink.sh).
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in "new/box113/inst/cp_K4 new/box113/inst/cp_K4.start" "n5-exhaustive/instances/b5_os_n40 new/box121/inst/b5_os_n40_default.start" "red/seg/instances/s3quad_K8_m30 new/box116/inst/s3quad_K8_m30_default.start"; do
  set -- $p; b=$(basename $1); echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
  python3 -I new/box121/brtree.py $1.pg $2; python3 -I new/box121/twofix.py $1.pg $2
done
rm -rf $t
