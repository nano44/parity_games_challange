#!/bin/bash
# Box 216 VALUE SIDE (L-NEW successor 76): V1 / V2 / V3 counters on a small check set (a tower, two Xi-cyclic genomes, 20 random
# Xi-cyclic genomes) under N5 (spec), the Howard reference (xi) for gate216's HOW items, and the firing controls.
# Run from experiments/new/box216; output diffed against check216.out by experiments/new/check.sh.
set -e
export PYTHONDONTWRITEBYTECODE=1
I="../box212/inst/DBL4_d20_F30.json ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json"
python3 -I xflip216.py $I
python3 -I xflip216.py --rand 2160 20 rand cyc
python3 -I gate216.py $I
G216_MODE=xi python3 -I gate216.py ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json | sed 's/^/howxi /'
python3 -I gate216.py --rand 2160 20 rand cyc
python3 -I split216.py $I
X216_CTRL=1 python3 -I xflip216.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlswap /'
X216_CTRL=2 python3 -I xflip216.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlxf0 /'
X216_CTRL=3 python3 -I xflip216.py ../box212/inst/DBL4_d20_F30.json | sed 's/^/ctrlperm /'
G216_CTRL=1 G216_MODE=xi python3 -I gate216.py ../box203/inst/MWR4_2.json | sed 's/^/ctrlf1 /'
G216_CTRL=2 G216_MODE=xi python3 -I gate216.py ../box203/inst/MWR4_2.json | sed 's/^/ctrlodd /'
G216_CTRL=3 G216_MODE=xi python3 -I gate216.py ../box203/inst/MWR4_2.json | sed 's/^/ctrlpexp /'
