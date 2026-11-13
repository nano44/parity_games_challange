#!/bin/bash
# Box 213 KEY-WINDOW (L-NEW successor 75): G-1 counters (key213.py), KEY-TAU counters (keymu213.py), G-2 counters (g2_213.py) on a small
# check set, with their firing controls, and N-4's totals (n4fix213.py, read-only mode). Run from experiments/new/box213; output diffed
# against check213.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 -I key213.py inst/TAUESC_rand2150.json inst/TAUESC_dense2151.json ../box212/inst/DBL4_d20_F30.json
KEY_CTRL=1 python3 -I key213.py inst/TAUESC_dense2151.json | sed 's/^/ctrlkey /'
python3 -I keymu213.py ../box212/inst/DBL4_d20_F30.json ../box207/inst/CFI3_n48.json inst/TAUESC_rand2150.json
python3 -I keymu213.py --rand 2180 30 rand
KM_MODE=xi python3 -I keymu213.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlxi /'
KM_CTRL=1 python3 -I keymu213.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlrev /'
python3 -I kcount213.py ../box212/inst/DBL4_d20_F30.json
python3 -I g2_213.py ../box212/inst/DBL4_d20_F30.json ../box203/inst/MWR4_2.json
python3 -I g2_213.py --rand 7 30 acyc
(cd ../../.. && python3 -I experiments/new/box213/n4fix213.py | cut -c1-80)
