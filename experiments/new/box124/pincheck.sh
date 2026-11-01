#!/bin/bash
# L-NEW box 124 pin: b5_os_n24 (Lemma-P invariant DEAD inside TWO-FIX pieces; n5x's default start written to box124/inst/).
# Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box124/lemmap.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
set -- n5-exhaustive/instances/b5_os_n24 new/box124/inst/b5_os_n24_default.start; b=$(basename $1)
echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
python3 -I new/box124/lemmap.py $1.pg $2
rm -rf $t
