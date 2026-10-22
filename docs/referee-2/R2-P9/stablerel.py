#!/usr/bin/env python3
"""Relabel a .pg file so vertex ids follow (priority, input id): Oink then keeps the order (Game::sort skips an ordered game,
game.cpp 480), which reproduces dtl_pyref's 'stable' CH1 order. Usage: stablerel.py IN.pg OUT.pg"""
import sys, re
lines = [l.strip() for l in open(sys.argv[1]) if l.strip()]
body = [l for l in lines if not l.startswith('parity')]
V = []
for l in body:
    l = l.rstrip(';').strip()
    m = re.match(r'^(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)(.*)$', l)
    V.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(',')], m.group(5)))
order = sorted(V, key=lambda x: (x[1], x[0]))
new = {v[0]: i for i, v in enumerate(order)}
with open(sys.argv[2], 'w') as f:
    f.write(f'parity {len(V)-1};\n')
    for v in order:
        f.write(f'{new[v[0]]} {v[1]} {v[2]} ' + ','.join(str(new[w]) for w in v[3]) + ';\n')
