#!/bin/bash
# L-NEW box 138 pin sbmany_n57 (climb138.py MODE=sb from L-RED cnmov_k8_n57, seed 6): many sbar changes inside one short FL run;
# its S-stretch (sbar allowed to change) has acyclic D''' and obeys CASC-M'''. Default best-reward start written out by start_pair.
# Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), rel.py, dmerge3.py, anchor.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for b in sbmany_n57; do p=new/box138/$b; st=new/box138/${b}_default.start
echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
python3 -I new/box138/rel.py $p.pg $st
python3 -I new/box138/dmerge3.py $p.pg $st
python3 -I new/box132/anchor.py $p.pg $st
done
rm -rf $t
