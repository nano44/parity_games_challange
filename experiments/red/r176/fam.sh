#!/bin/bash
# R176: topfix family (new/box52/out/topfix_nK + start): per game the ODIFF>=1 window with the largest charge depth (gatechg VERB),
# and PHNF / LAMNF per window (r172 climb172.phnf_windows = port of L-NEW box 122 windows.py). Output out/fam.txt
cd "$(dirname "$0")/../.."
for k in 3 4 6 8 10 12; do g=new/box52/out/topfix_n$k
  echo "== topfix_n$k $(grep -c . $g.pg)"
  VERB=1 python3 -I red/r176/gatechg.py $g.pg $g.start | grep "^  WIN" | awk '$4!=0' | sort -t' ' -k10 -n | tail -1
  python3 -I -c "import sys; sys.path.insert(0, 'red/r172'); import climb172 as c; from n5x import load, readstart, start_pair, Engine, dual; g = load('$g.pg'); s, t = start_pair(g, Engine(g), Engine(dual(g)), readstart('$g.start')); W, K = c.phnf_windows(g, s, t); print('K', K, 'best', max(((w['PHNF'], w['L'], w['ODIFF'], w['FB'], w.get('LAMNF')) for w in W if w['ODIFF'] >= 1), default=None))"
done
