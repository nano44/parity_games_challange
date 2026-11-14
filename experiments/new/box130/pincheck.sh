#!/bin/bash
# L-NEW box 130 pin: u2flat73_n32 (n 32, default best-reward start written out by start_pair): one ODIFF >= 1 TWO-FIX window with 73
# W-flat moves (the corpus maximum) but only 7 FL transitions (W unchanged everywhere); Oink 8fbf0a7 --zlk / --tl verified vs N5 regions
# (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box130/flatcnt.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
set -- red/xing/instances/u2flat73_n32 new/box130/u2flat73_n32_default.start; b=$(basename $1)
echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
python3 -I new/box130/flatcnt.py $1.pg $2
rm -rf $t
