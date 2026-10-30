#!/usr/bin/env python3
"""L-RED R135: longest relaxed ladder_k schedule (a SET of W-improving switches per step (N5-like), box 80 model, fleet Engine values) in which NO step
needs an UPWARD wait: every non-switching chooser that has a W-better successor has no reader pointing to it.
Exhaustive DFS over strategy states (memoised longest path; the state graph is acyclic since W rises strictly).
Usage: noup.py LADDER.pg"""
import sys, os, functools
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine
sys.setrecursionlimit(100000)
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
E = Engine(g); n = g.n; T = n - 1
ch = [v for v in range(n) if len(g.succ[v]) > 1]
readers = {v: [r for r in ch if v in g.succ[r]] for v in range(n)}
@functools.lru_cache(None)
def W(st): return E.evaluate(st)[0]
@functools.lru_cache(None)
def best(st, upok):
    w = W(st); better = [v for v in ch if any(E.key(w[x]) > E.key(w[st[v]]) for x in g.succ[v] if x != st[v])]
    res = 0
    import itertools
    for r in range(1, len(better) + 1):
        for S in itertools.combinations(better, r):
            if not upok and any(any(st[q] == x for q in readers[x]) for x in better if x not in S): continue
            opts = [[x for x in g.succ[v] if x != st[v] and E.key(w[x]) > E.key(w[st[v]])] for v in S]
            for pick in itertools.product(*opts):
                ns = list(st)
                for v, x in zip(S, pick): ns[v] = x
                ns = tuple(ns)
                if any(E.key(W(ns)[y]) < E.key(w[y]) for y in range(n)): continue   # keep W monotone (one-player: always holds)
                res = max(res, best(ns, upok) + (W(ns)[T] != w[T]))
    return res
st = tuple(g.succ[v][0] for v in range(n))
print(f"NOUP {os.path.basename(sys.argv[1])} max T-rises: no-upward-waits {best(st, False)}, unrestricted {best(st, True)}")
