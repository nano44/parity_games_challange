#!/bin/bash
# L-NEW box 151: wake-order relaxation of the genk nested targets NEST(k), as committed (xwake.py) and with antisymmetry
# (xwake_anti.py ANTI=1), with build.py's main gates or gate-free (FREEKP=1). Needs z3-solver.
# Usage: run.sh [check|quick]   (check = the rows used by experiments/new/check.sh; quick = about 4 min; none = full)
cd "$(dirname "$0")"; T=$(mktemp -d)
KS="2 3 4 5 6"; [ "$1" = check ] && KS="2 3 4"
for k in $KS; do python3 genk.py $k 0 $T/k$k.json > /dev/null; done
row() { # k E DEG ANTI FREEKP tool
  r=$(FREEKP=$5 ANTI=$4 DEG=$3 TMO=${TMO:-600} python3 -I $6 $T/k$1.json $2 $T/o.json 2>&1 | grep -oE -- '-> [a-z]+' | head -1)
  echo "NEST k $1 E $2 DEG $3 ANTI $4 FREEKP $5 $(basename $6 .py) $r"; }
if [ "$1" = check ]; then
  row 3 0 1 0 0 xwake.py; row 3 0 0 1 0 xwake_anti.py; row 3 1 0 1 0 xwake_anti.py; row 2 2 0 1 0 xwake_anti.py
  row 4 2 0 1 0 xwake_anti.py; row 3 1 0 1 1 xwake_anti.py; row 4 2 0 1 1 xwake_anti.py; rm -rf "$T"; exit 0; fi
row 3 0 1 0 0 xwake.py; row 3 1 1 0 0 xwake.py
for k in 2 3 4 5; do row $k 0 0 1 0 xwake_anti.py; done
row 2 1 0 1 0 xwake_anti.py; row 2 2 0 1 0 xwake_anti.py; row 3 1 0 1 0 xwake_anti.py; row 4 1 0 1 0 xwake_anti.py; row 4 2 0 1 0 xwake_anti.py
row 2 1 0 1 1 xwake_anti.py; row 3 1 0 1 1 xwake_anti.py; row 3 2 0 1 1 xwake_anti.py; row 4 1 0 1 1 xwake_anti.py; row 4 2 0 1 1 xwake_anti.py
if [ "$1" != quick ]; then
  row 3 2 0 1 0 xwake_anti.py; row 4 3 0 1 0 xwake_anti.py; row 5 1 0 1 0 xwake_anti.py; row 5 2 0 1 0 xwake_anti.py
  row 5 1 0 1 1 xwake_anti.py; row 5 2 0 1 1 xwake_anti.py
fi
rm -rf "$T"
