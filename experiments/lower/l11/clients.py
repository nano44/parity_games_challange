#!/usr/bin/env python3
"""L-LOWER 11: helper sharing in a realized tower. h = capped levels of the run; core = pairs 0..h-1; helpers = the rest.
client(y) = core levels j such that a mover of pair j reaches helper y by a wiring path whose inner movers are helpers (tsat.py's
HR); also the moving helpers only (a helper that never moves in the run carries no timing). Prints the histogram of |client(y)| and,
per core level, the number of moving helpers it reads that NO other level reads (private) vs shared. Usage: clients.py GENOME.."""
import sys, os
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '../l6'))
from sim6 import rd, run, Fprof, caps
for p in sys.argv[1:]:
    D = rd(p); S, O = run(D); F = Fprof(D, O); h = caps(F); N = 2 * D['d']; K = 2 * h; xt = D['xt']
    moving = {y for y in range(K, N) if any(S[t][y] != S[t - 1][y] for t in range(1, len(S)))}
    def hreach(x):
        seen = set(); st = [w for w in (xt[2 * x], xt[2 * x + 1]) if w >= K]
        while st:
            z = st.pop()
            if z in seen: continue
            seen.add(z); st += [w for w in (xt[2 * z], xt[2 * z + 1]) if w >= K]
        return seen
    cl = {y: set() for y in range(K, N)}
    for x in range(K):
        for y in hreach(x): cl[y].add(x // 2)
    hist = Counter(len(cl[y]) for y in moving); hist0 = Counter(len(cl[y]) for y in range(K, N))
    priv = {j: sum(1 for y in moving if cl[y] == {j}) for j in range(h)}
    shared = {j: sum(1 for y in moving if j in cl[y] and len(cl[y]) > 1) for j in range(h)}
    print(f'{os.path.basename(p)}: d {D["d"]} caps {h} helpers {N - K} moving {len(moving)} | moving helpers by #client levels {sorted(hist.items())}'
          f' | all helpers {sorted(hist0.items())}\n   per level private / shared moving helpers: ' + ' '.join(f'{j}:{priv[j]}/{shared[j]}' for j in range(h)))
