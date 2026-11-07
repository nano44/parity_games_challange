#!/bin/bash
# L-NEW box 137 pin ret2_n37 (adversarial climb climb137.py from L-RED's ovk_n37, seed 1): one FL run, ONE epoch (GCH 0), x = 15 re-enters
# option 2 twice and 36 once more (2 -> 36 -> 8 -> 2 -> 36 -> 8 -> 2); vertex 36 makes the move 33 -> 31 twice with sbar, tau, Xi on
# ODIFF and Xi on CN constant. Default best-reward start written out by start_pair (validated by N5X strict start check).
# Pin cwmov2_n57 (climb from L-RED cnmov_k8_n57, seed 3): 2 FL moves whose old and new options are in the c-world (Lemma DEFICIT holds).
# Oink 8fbf0a7 --zlk / --tl verified vs N5 regions (box107/pinwin.py), n5b state by state (si/root/n5bcmp.py), rel.py, anchor.py.
cd "$(dirname "$0")/../.."; O=../tools/oink/build/oink; t=$(mktemp -d)
for b in ret2_n37 cwmov2_n57; do p=new/box137/$b; st=new/box137/${b}_default.start
echo "PIN $b $(sha1sum < $p.pg | cut -c1-12) start $(sha1sum < $st | cut -c1-12)"
for s in zlk tl; do "$O" --$s -v $p.pg $t/$b.$s.sol > $t/$b.$s.log 2>&1; grep -q "solution verified" $t/$b.$s.log && echo "OINK $b --$s verified" || echo "OINK $b --$s NOT verified"; done
python3 -I new/box107/pinwin.py $p.pg $st $t/$b.zlk.sol
timeout 3000 python3 -I si/root/n5bcmp.py $p.pg $st | head -1
python3 -I new/box137/rel.py $p.pg $st
python3 -I new/box132/anchor.py $p.pg $st
done
rm -rf $t
