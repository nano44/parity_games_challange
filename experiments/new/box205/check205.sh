#!/bin/bash
# Box 205 (L-NEW successor 69): Lemma BETA-LOC counters on small sets; run from experiments/new/box205. Output diffed against check205.out.
set -e
python3 betaloc205.py ../box203/inst/MWR4_2.json ../box202/k1fail_202.json inst/naive_k1_s71.json
python3 betaloc205.py --rand k1 75 100
python3 betaloc205.py --rand rand 76 100
BL_CTRL=1 python3 betaloc205.py --rand k1 75 100 | sed 's/^/ctrl1 /'
