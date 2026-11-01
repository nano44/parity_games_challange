#!/bin/bash
# L-NEW box 133 pin: odxi_n37 = u23sw64_n32 + a 5-vertex gadget (t 32 self-loop prio 8; gates 33 -> {2, 32}, 34 -> {32, 36}; chooser
# 35 -> {33, 34}; pad 36 -> 9). Inside the FL run [1, 9]: Xi at the ODIFF gate 33 changes 5 times (XIB 5) and the chooser 35 makes an FL
# move 34 -> 33 at 5 -> 6, released by that change. Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by
# state (si/root/n5bcmp.py), box132/anchor.py, box133/odxi.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
p=new/box133/odxi_n37; b=odxi_n37; st=$p.start
echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
python3 -I new/box132/anchor.py $p.pg $st
python3 -I new/box133/odxi.py $p.pg $st
rm -rf $t
