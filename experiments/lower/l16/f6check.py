#!/usr/bin/env python3
"""L-LOWER 17: in a genome's CLAMPED run (core forced to TARGET), compare a client's better (sim6 ENC values) with its required list on
rows 0..P; prints the mismatching free pre-states. Usage: f6check.py GENOME TARGET P CLIENT"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp, P, X = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
D = sim6.rd(G); T = open(tp).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16))); order = sim6.topo(D)
l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), G, tp, str(X), str(P)], capture_output=True, text=True).stdout
req = ast.literal_eval(l[l.index('['):l.index('] |') + 1]); bad = []
for t, r in req:
    s = list(S[t]); v = sim6.values(D, s, order)
    m1 = 2 * X + 1 - s[X]; y = D['xt'][m1]; ov = sim6.bv(D, m1) + (v[y] if y >= 0 else 0)
    b = 1 - s[X] if ov > v[X] else s[X]
    if b != r: bad.append(t)
print('F6CHECK', os.path.basename(G), 'client', X, 'rows 0..%d' % P, 'free', len(req), 'mismatches', len(bad), bad[:20])
