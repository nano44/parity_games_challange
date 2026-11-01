#!/bin/bash
# L-NEW box 128 pin: topfix_n10 (n 210, PGSolver best-reward default start written out explicitly by start_pair): the per-h count
# STRICT_h <= sum_X (1 + lambda_Xi(X) changes) FAILS (h 192, stretch [6,64]: 36 W-strict moves, bound 20, hub class 193 re-entered 18 times,
# no Xi-cycle-node change at any class). Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state
# (si/root/n5bcmp.py), box128/pcount.py and witness.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
set -- new/box52/out/topfix_n10 new/box128/topfix_n10_default.start; b=$(basename $1)
echo "PIN $b $(sha1sum < $1.pg | cut -c1-12) start $(sha1sum < $2 | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $1.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $1.pg $2 $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $1.pg $2 | head -1
python3 -I new/box128/pcount.py $1.pg $2
python3 -I new/box128/witness.py $1.pg $2 | head -3
rm -rf $t
