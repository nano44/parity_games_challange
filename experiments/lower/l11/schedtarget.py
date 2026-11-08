#!/usr/bin/env python3
"""L-LOWER 11: write l7/sched.py's sequential (non-tight) h-capped core target in ttarget.py's file format. Usage: schedtarget.py h a1,a2,.. OUT"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
for p in ('../l6', '../l7'): sys.path.insert(0, os.path.join(here, p))
from sched import schedule
h = int(sys.argv[1]); al = list(map(int, sys.argv[2].split(','))); D, S = schedule(h, alpha=al)
with open(sys.argv[3], 'w') as f:
    f.write(f'# sched h {h} alpha {al}\ngate ' + ' '.join(map(str, D['gate'][:4 * h])) + '\n')
    for s in S: f.write(' '.join(map(str, s[:2 * h])) + '\n')
