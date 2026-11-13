#!/bin/bash
# Box 209 (L-NEW successor 72): Lemma LEVEL3 / PLATEAU3 / Theorem T3-ALL must-0 counters on Gamma3 runs (engine: N5'-xi from S3, n5v):
# level208.py --g3 on six frozen genomes (k = 1, 2, 4), both controls (must fire), plat209.py on four genomes and its control, a small
# random set, and the --dump / --hist round trip through plat209.py. Run from experiments/new/box209. Output diffed against check209.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
L=../box208/level208.py
python3 $L --g3 ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d9_N18.json ../box202/inst/WC8_2.json
LV_CTRL=1 python3 $L --g3 ../box207/inst/CFI3_n48.json | sed 's/^/ctrl1 /'
LV_CTRL=2 python3 $L --g3 ../box203/inst/MWR4_2.json | sed 's/^/ctrl2 /'
python3 plat209.py ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d9_N18.json
PL_CTRL=1 python3 plat209.py ../box206/inst/K1D4_n48.json | sed 's/^/ctrlp /'
python3 plat209.py --rand 2105 40 k1 | sed 's/^/rnd /'
t=$(mktemp -d); python3 $L --g3 --dump "$t/hist_K1D4.json" ../box206/inst/K1D4_n48.json > /dev/null
python3 plat209.py --hist "$t/hist_K1D4.json" | sed 's/^/hist /'; rm -rf "$t"
