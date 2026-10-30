#!/bin/bash
# REFEREE s20: fsw_strong.py (SW-KEEP strong form) over the union of box 77's games (sibling .start if present, plus best-reward start), N5 and N5-LZC.
cd "$(dirname "$0")/../../../../experiments"; O=../docs/referee/scratch/fixd_logs; mkdir -p $O/strong
xargs -P 4 -I{} bash -c 'for e in "" --lzc; do f=$0/strong/$(echo "{} ${e:-N5}" | tr "/ " "__").txt; timeout 1800 python3 -I ../docs/referee/scratch/fsw_strong.py {} $e > $f 2>&1; echo "RC $?" >> $f; done' $O < $O/strong_games.lst
cat $O/strong/*.txt | grep -vE '^(EX|RC 0)' | awk '{s[$1]+=$2} END{for(k in s) print k, s[k]}' | sort > $O/strong_sum.txt; grep -h '^EX\|^RC [^0]' $O/strong/*.txt | head -20 >> $O/strong_sum.txt; echo DONE >> $O/strong_sum.txt
