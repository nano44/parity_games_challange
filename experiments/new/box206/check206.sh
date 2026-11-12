#!/bin/bash
# Box 206 (L-NEW successor 70): change-depth counters (depth206.py) and the LD-ASC DEAD witness (ascdepth206.py); run from
# experiments/new/box206. Output diffed against check206.out.
set -e
python3 depth206.py ../box203/inst/MWR4_2.json ../box202/k1fail_202.json inst/K1D4_n48.json ../box202/inst/WC8_2.json
DEP_ALL=1 python3 depth206.py ../box203/inst/MWR4_2.json | sed 's/^/all /'
python3 depth206.py --rand k1 66 100
DEP_CTRL=1 python3 depth206.py ../box203/inst/MWR4_2.json | sed 's/^/ctrl1 /'
python3 ascdepth206.py ../box204/inst/K1F34_n84.json ../box202/inst/WC8_2.json
LDA_CTRL=1 python3 ascdepth206.py ../box202/inst/WC8_2.json | sed 's/^/ctrl2 /'
python3 div206.py inst/K1L7_n48.json ../box202/inst/WC8_2.json
python3 div206.py --rand k1 69 50
DIV_CTRL=1 python3 div206.py inst/K1L7_n48.json | sed 's/^/ctrl3 /'
