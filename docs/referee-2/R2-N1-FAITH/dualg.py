#!/usr/bin/env python3
"""Dual game: swap owners, priority p -> p+1. Rewards become (-1)^(p+1) n^(p+1) = -n * r: Max/Min and Even/Odd swap roles.
Usage: dualg.py IN OUT"""
import sys, re
out = []
for l in open(sys.argv[1]):
    s = l.strip().rstrip(';')
    if not s or s.startswith('%'): continue
    if s.startswith('parity'): out.append(s + ';'); continue
    m = re.match(r'^(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)', s)
    out.append(f'{m.group(1)} {int(m.group(2)) + 1} {1 - int(m.group(3))} {m.group(4)};')
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
