#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §4: is SL41's own trajectory (F(6) = 222) realizable with closure(q5 = 10) avoiding pair 6? Re-point
(a) one of the options 10:0, 10:1, 55:0, 55:1 to any target (mover or exit), (b) both 10:0 and 10:1; keep acyclic genomes whose
closure(10) avoids 12, 13; decide exactly (ranksolve: all ranks and signs free) whether SL41's trajectory is reproduced.
Usage: rcfree.py SL41_d28.txt"""
import sys, os, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, H)
from sim6 import rd, run, topo
from ranksolve import constraints, solve
from collections import Counter
def clos(D, x):
    xt = D['xt']; seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = xt[2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
D0 = rd(sys.argv[1]); S0, O0 = run(D0); N = 2 * D0['d']
def test(edits):
    D = {k: (list(v) if isinstance(v, list) else v) for k, v in D0.items()}
    for m, y in edits: D['xt'][m] = y
    if topo(D) is None or (clos(D, 10) & {12, 13}): return None
    res, core = solve(constraints(D, S0), 2 * N); return (res is not None, {x for t, x, p in core} if core else set())
for name, cands in (('(a) one option of 10 or 55', [[(m, y)] for m in (20, 21, 110, 111) for y in range(-1, N)]),
                    ('(b) both options of 10', [[(20, y0), (21, y1)] for y0 in range(-1, N) for y1 in range(-1, N)])):
    t0 = time.time(); n = ok = 0; cm = Counter()
    for e in cands:
        r = test(e)
        if r is None: continue
        n += 1; ok += r[0]; cm.update(r[1])
    print(name, ': acyclic RC-free genomes', n, '; SL41 trajectory feasible:', ok, '; movers in the open set (genomes):', cm.most_common(6), '; %d s' % (time.time() - t0))
