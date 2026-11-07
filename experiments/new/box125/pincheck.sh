#!/bin/bash
# L-NEW box 125 pin: nep92_n40 with nep92_n40.start (92 sbar-changes in one tau-stretch of 95 transitions at n = 40; one Odd vertex flips 67
# times). Oink 8fbf0a7 --zlk / --tl verified vs N5's regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box125/chain.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
set -- n5-epoch/instances/nep92_n40 n5-epoch/instances/nep92_n40.start; b=$(basename $1)
echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
python3 -I new/box125/chain.py $1.pg $2
rm -rf $t
