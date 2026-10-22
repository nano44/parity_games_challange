#!/usr/bin/env python3
"""Relabel a .pg file with ids ordered by (priority, random tie-break with SEED). Usage: randrel.py IN OUT SEED"""
import sys, re, random
random.seed(int(sys.argv[3]))
V = []
for l in open(sys.argv[1]):
    l = l.strip().rstrip(';').strip()
    if not l or l.startswith('parity'): continue
    m = re.match(r'^(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)', l)
    V.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(',')]))
order = sorted(V, key=lambda x: (x[1], random.random()))
new = {v[0]: i for i, v in enumerate(order)}
with open(sys.argv[2], 'w') as f:
    f.write(f'parity {len(V)-1};\n')
    for v in order: f.write(f'{new[v[0]]} {v[1]} {v[2]} ' + ','.join(str(new[w]) for w in v[3]) + ';\n')
