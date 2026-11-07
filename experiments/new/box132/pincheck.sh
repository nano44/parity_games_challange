#!/bin/bash
# L-NEW box 132 pins: u23sw64_n32 (the corpus's longest FL run, 8 transitions, ONE epoch, lmax - 1 = 9) and cw11_n24 (the only FL runs
# with gating changes: 3 Xi-changes at a W-cycle node, 7 cycle-node moves). Default best-reward starts written out by start_pair.
# Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), box132/anchor.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for p in red/xing/instances/u23sw64_n32 red/kw/instances/cw11_n24; do
  b=$(basename $p); st=new/box132/${b}_default.start
  echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
  for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
  python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
  timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
  python3 -I new/box132/anchor.py $p.pg $st
done
rm -rf $t
