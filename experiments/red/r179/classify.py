#!/usr/bin/env python3
"""L-RED R179: classify each XICH (j, o) of odxi: OCYC if o lies on the cycle of its own Xi-play at j-1 or j (the Odd vertex's
sigma-bar edge closes a cycle through o), else LASSO; FIRST if j is the first transition of its FL run; MOVERS on o's Xi-play.
Usage: classify.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
import odxi
from n5x import load, start_pair, Engine, dual, step
def cyc_of(succ, x):
    seq = []; pos = {}; y = x
    while y not in pos: pos[y] = len(seq); seq.append(y); y = succ[y]
    return set(seq[pos[y]:]), seq
for p in sys.argv[1:]:
    g = load(p); n, own = g.n, g.owner; R = odxi.analyse(g)
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed); S = [list(s)]; T = [list(t)]
    while True:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(list(r[0])); T.append(list(r[1]))
    SB = [E.evaluate(tuple(x))[1] for x in S]
    flj = set(R["flj"])
    c = dict(OCYC=0, LASSO=0, FIRST=0, LATER=0)
    for j, o, a, b in R["pairs"]:
        sx = lambda k: [S[k][v] if own[v] == 0 else SB[j][v] for v in range(n)]
        c0, _ = cyc_of(sx(j - 1), o); c1, _ = cyc_of(sx(j), o)
        c["OCYC" if (o in c0 or o in c1) else "LASSO"] += 1
        c["FIRST" if (j - 1) not in flj else "LATER"] += 1
    print(os.path.basename(p), "n", n, "xich", R["xich"], c)
