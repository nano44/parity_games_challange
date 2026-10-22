#!/usr/bin/env python3
"""R-N5K9: longest VJ00 improvement chain over ALL policies (any non-empty unambiguous subset per step, flat steps included),
over all start strategies, in random one-player games (every ⊖ vertex out-degree 1). The strategy graph is acyclic by R15 (c),
so this is a longest path in a DAG. Also counts the longest chain counting only Omega-strict steps. VJ00-only oracle (n5t_probe).
Usage: python3 -I docs/referee/scratch/n5k9_longest.py [games per n] [nmin] [nmax] [seed]"""
import sys, os, random, itertools
sys.path.insert(0, os.path.join(os.getcwd(), "docs/referee/scratch"))
from n5t_probe import omega, improvements
from functools import lru_cache
G = int(sys.argv[1]) if len(sys.argv) > 1 else 50; n0 = int(sys.argv[2]) if len(sys.argv) > 2 else 4
n1 = int(sys.argv[3]) if len(sys.argv) > 3 else 6; rnd = random.Random(int(sys.argv[4]) if len(sys.argv) > 4 else 5)
for n in range(n0, n1 + 1):
    best = bests = 0
    for _ in range(G):
        owner = [rnd.randint(0, 1) for _ in range(n)]; plus = [rnd.random() < 0.5 for _ in range(n)]
        succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) if owner[v] == 0 else [rnd.randrange(n)] for v in range(n)]
        ev = [v for v in range(n) if owner[v] == 0]
        strats = []
        for ch in itertools.product(*[succ[v] for v in ev]):
            s = [None] * n
            for v, w in zip(ev, ch): s[v] = w
            strats.append(tuple(s))
        Om = {s: omega(n, owner, succ, plus, list(s)) for s in strats}
        nxt = {}
        for s in strats:
            imp = improvements(n, owner, succ, plus, list(s), Om[s]); vs = list(imp); out = set()
            for pick in itertools.product(*[[None] + imp[v] for v in vs]):
                if all(p is None for p in pick): continue
                t = list(s)
                for v, w in zip(vs, pick):
                    if w is not None: t[v] = w
                out.add(tuple(t))
            nxt[s] = out
        @lru_cache(None)
        def L(s): return max((1 + L(t) for t in nxt[s]), default=0)
        @lru_cache(None)
        def LS(s): return max(((Om[t] != Om[s]) + LS(t) for t in nxt[s]), default=0)
        best = max(best, max(L(s) for s in strats)); bests = max(bests, max(LS(s) for s in strats))
    print(f"n={n} games={G}: longest chain (all policies, flat incl.) = {best}; max Omega-strict steps on a chain = {bests}")
