#!/usr/bin/env python3
"""L-LOWER 10: Lemma FUEL-DOUBLING check. For every mover x of a genome's run: M(x) = moves; K(x) = number of steps t at which
some mover of closure(x) moves; the lemma says that between two consecutive moves of x (at t < t') some closure mover moves at a
step in [t, t' - 1], hence M(x) <= 1 + K(x). Also reports |closure(x)| vs log2 M(x). Usage: fuel.py GENOME.txt"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
D = rd(sys.argv[1]); S, O = run(D); N = 2 * D['d']; T = len(S) - 1
def clos(x):
    seen = set(); st = [x]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = D['xt'][2 * y + k]
            if z >= 0 and z not in seen: seen.add(z); st.append(z)
    return seen
mv = {x: [t for t in range(1, T + 1) if S[t][x] != S[t - 1][x]] for x in range(N)}
bad = 0; tight = []
for x in range(N):
    C = clos(x); steps = sorted({t for y in C for t in mv[y]})
    for a, b in zip(mv[x], mv[x][1:]):
        if not any(a <= t <= b - 1 for t in steps): bad += 1
    if len(mv[x]) >= 2: tight.append((len(mv[x]), len(C), round(math.log2(len(mv[x])), 1)))
print('T', T, 'gap violations of FUEL-DOUBLING:', bad)
print('movers with >= 2 moves: (moves, |closure|, log2 moves), sorted by moves:', sorted(tight, reverse=True)[:16])
