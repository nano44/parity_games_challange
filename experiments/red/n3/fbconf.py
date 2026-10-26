#!/usr/bin/env python3
"""Per phase: f (in-phase S4c fallbacks), distinct configurations sigma-bar|Q at fallback SOURCES, max fallbacks per configuration
(the quantities of L-NEW 26's Theorem FB-C, P-N5-FBC). Also |Q|, prod deg(q). Usage: fbconf.py GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
from phlen import readany
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else readany(sys.argv[1], g)
E, rows = n3x.trace(g, st)
Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
prod = 1
for q in Q: prod *= len(set(g.succ[q]))
keys = [(r["lam"], r["tau"]) for r in rows]; i = 0
while i < len(rows):
    j = i
    while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
    cf = Counter(tuple(rows[k]["nxt"][q] for q in Q) for k in range(i, j) if rows[k]["fb"])
    f = sum(cf.values())
    if j > i and f:
        print(f"phase@{i} T={j-i} f={f} distinct_configs={len(cf)} max_fb_per_config={max(cf.values())} |Q|={len(Q)} prod_deg={prod} 4n^2-3n={4*g.n*g.n-3*g.n} configs={dict(cf)}")
    i = j + 1
