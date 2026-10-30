#!/bin/bash
# L-NEW box 67: ../box68/zflat.py over experiments/si/root/logs/alt_all.lst (game [start] per line, paths relative to experiments/), 3 jobs.
cd "$(dirname "$0")/../.."; OUT=new/box68/zflat_alt.txt; : > $OUT
cat si/root/logs/alt_all.lst | xargs -P 3 -L 1 bash -c 'r=$(timeout 900 python3 -I new/box67/../box68/zflat.py "$@" 2>&1 | tail -1); echo "GAME $1 $r"' _ >> $OUT
