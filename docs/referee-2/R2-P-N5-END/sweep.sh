#!/bin/bash
# REFEREE-2 34: the P-N5-END replay on own code. Run from docs/referee-2/R2-P-N5-END with CORPUS = box189/corpus of an l-new archive.
CORPUS=$1
for m in spec xi n5w; do
  python3 r2end.py --mode $m --gen 3000 3401 acyc --gen 3000 3402 any --gen 1000 3403 self ../R2-P-ACYC/setR2_600_32.jsonl $CORPUS/*.json > sweep_$m.out
done
python3 r2end.py --mode spec --eorder gate --gen 3000 3401 acyc ../R2-P-ACYC/setR2_600_32.jsonl $CORPUS/*.json > sweep_spec_gate.out
python3 r2end.py --mode spec --chkopt --gen 300 3404 any --gen 300 3405 acyc > chkopt_spec.out
python3 r2end.py --mode xi --chkopt --gen 300 3404 any > chkopt_xi.out
python3 r2end.py --mode spec --ctrl --gen 200 3406 acyc --gen 200 3407 any > ctrl_spec.out
python3 r2end.py --mode xi --ctrl --gen 200 3406 acyc --gen 200 3407 any > ctrl_xi.out
python3 r2end.py --mode spec --ctrl1 --gen 100 3408 any > ctrl1_spec.out
python3 r2end.py --mode xi --ctrl1 --gen 100 3408 any > ctrl1_xi.out
for f in sweep_*.out chkopt_*.out ctrl_*.out ctrl1_*.out; do echo "$f: $(tail -1 $f)"; done > sweep_totals.out
