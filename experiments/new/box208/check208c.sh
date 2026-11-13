#!/bin/bash
# Box 208 Addendum B (L-NEW successor 72): the third implementation rv208.py (every reference state b) on three frozen genomes, its
# control (must fire), its cross-check against box191 idealcyc / si.Engine, and a small random set of its own generator.
# Run from experiments/new/box208. Output diffed against check208c.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 rv208.py ../box207/inst/CFI3_n48.json ../box191/inst/DEAD_SEG2P_d4_N8.json ../box206/inst/K1D4_n48.json
RV_CTRL=1 python3 rv208.py --T ../box203/inst/MWR4_2.json | grep -v "^VIOLATION" | sed 's/^/ctrl /'
python3 rv208.py --xcheck ../box207/inst/RINT_n48.json ../box191/inst/DEAD_SEG2P_d9_N18.json
python3 rv208.py --rand 2098 150 rand,cyc,self,up,down,dense,flat
