#!/bin/bash
# Box 208 (L-NEW successor 72): Lemma LEVEL / Theorem WIN must-0 counters (class facts K1, K3, K4, K5; L1-L4; the window counters) on
# seven frozen genomes (k = 1 and k = 2), both controls (must fire), a small random k = 1 set, and the --dump / --hist round trip.
# Addendum A: plat208.py's plateau counters on three genomes and its control. Run from experiments/new/box208. Output diffed against check208.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 level208.py ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/CWRR4_n.json ../box202/inst/WC8_2.json ../box202/k1fail_202.json
LV_CTRL=1 python3 level208.py ../box207/inst/CFI3_n48.json | sed 's/^/ctrl1 /'
LV_CTRL=2 python3 level208.py ../box203/inst/MWR4_2.json | sed 's/^/ctrl2 /'
python3 level208.py --rand 2087 60 k1 | sed 's/^/rnd /'
python3 plat208.py ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/K1L10_n48.json
PL_CTRL=1 python3 plat208.py ../box206/inst/K1D4_n48.json | sed 's/^/ctrlp /'
t=$(mktemp -d); python3 level208.py --dump "$t/hist_CFI3.json" ../box207/inst/CFI3_n48.json > /dev/null
python3 level208.py --hist "$t/hist_CFI3.json" | sed 's/^/hist /'; rm -rf "$t"
