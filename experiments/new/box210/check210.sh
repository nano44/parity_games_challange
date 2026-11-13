#!/bin/bash
# Box 210 (L-NEW successor 72): Lemma G-CLASS / GEN-LEVEL / GEN-PLATEAU must-0 counters on three family games and 200 random games, the
# three controls (must fire), the cross-check against si.Engine on one game, and one scale profile.
# Run from experiments/new/box210. Output diffed against check210.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 gen210.py --pg ../box191/inst/sae_2.pg ../box191/inst/sae_3.pg ../../n5-box21/instances/friedmannsubexp_2.pg
python3 gen210.py 2119 200 8 6 3 1
GEN_CTRL=1 python3 gen210.py 2116 100 16 10 3 1 | sed 's/^/ctrl1 /'
GEN_CTRL=2 python3 gen210.py 2117 100 8 6 3 0 | sed 's/^/ctrl2 /'
GEN_CTRL=3 python3 gen210.py 2118 1000 6 6 3 1 | sed 's/^/ctrl3 /'
python3 gen210.py --xcheck ../box191/inst/sae_2.pg
python3 scale210.py --blocks ../box191/inst/sae_3.pg
