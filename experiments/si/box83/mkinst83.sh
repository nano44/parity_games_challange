#!/usr/bin/env bash
# L-SI box 83: regenerate the frozen LADDER-R instances (ladder83.py) into inst/.
set -euo pipefail; cd "$(dirname "$0")"
python3 -I -B ladder83.py 2 1,4 inst/LR2_none.json 0 none
python3 -I -B ladder83.py 2 1,4 inst/LR2_exitup.json 0 exitup 2,2
python3 -I -B ladder83.py 2 1,4 inst/LR2_chainup.json 0 chainup 2,2
python3 -I -B ladder83.py 3 1,4,7 inst/LR3_exitup.json 0 exitup 2,2,2
python3 -I -B ladder83.py 3 1,4,7 inst/LR3_chainup.json 0 chainup 2,2,2
python3 -I -B ladder83.py 6 1,4,7,10,13,16 inst/LR6_exitup.json 0 exitup 2,2,2,2,2,2
