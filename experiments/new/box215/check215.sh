#!/bin/bash
# Box 215 KEYSIDE-ALL (L-NEW successor 75): key-side must-0 counters (keyside215.py) on a small check set (two Xi-cyclic genomes, one
# tower, 20 random Xi-cyclic genomes) and the three firing controls. Run from experiments/new/box215; output diffed against check215.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 -I keyside215.py ../box212/inst/DBL4_d20_F30.json ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json
python3 -I keyside215.py --rand 2190 20 rand cyc
KM_MODE=xi python3 -I keyside215.py ../box212/inst/DBL4_d20_F30.json ../box207/inst/CFI3_n48.json | sed 's/^/ctrlxi /'
KS_CTRL=1 python3 -I keyside215.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlperm /'
KS_CTRL=2 python3 -I keyside215.py ../box207/inst/CFI3_n48.json | sed 's/^/ctrlown /'
