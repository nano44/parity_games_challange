#!/bin/bash
# Box 210 Addendum A (L-NEW successor 72): brute210.py (brute-force reply of Odd, every even up-set, every reference state) on 500
# random split games and 500 random general split-form games, and two controls (must fire). Run from experiments/new/box210.
# Output diffed against check210b.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
python3 brute210.py rsplit 2138 500 5 6 3
python3 brute210.py rgen 2139 500 4 5 6
CTRL=H python3 brute210.py rsplit 2135 300 5 6 3 | grep -v "^  FIRST" | sed 's/^/ctrlH /'
CTRL=Hodd python3 brute210.py rsplit 2136 300 5 6 3 | grep -v "^  FIRST" | sed 's/^/ctrlHodd /'
