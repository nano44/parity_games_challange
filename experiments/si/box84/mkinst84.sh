#!/usr/bin/env bash
# L-SI box 84: regenerate the frozen HUB PAIR (MIRROR) instances (pair84.py) into inst/.
set -euo pipefail; cd "$(dirname "$0")"
python3 -I -B pair84.py 2 1,4 8 inst/HP2_mup.json 1
python3 -I -B pair84.py 3 1,3,6 6,12 inst/HP3_mup.json 1
python3 -I -B pair84.py 3 1,3,6 6,12 inst/HP3_mup0.json 0
python3 -I -B pair84.py 4 1,3,9,19 7,10,30 inst/HP4_mup.json 1
python3 -I -B pair84.py 5 2,4,12,17,22 5,17,20,34 inst/HP5_mup.json 1
