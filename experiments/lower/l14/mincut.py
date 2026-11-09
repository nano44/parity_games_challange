#!/usr/bin/env python3
"""L-LOWER 14: for a base genome B and a sink mover X, the least number of HELPER movers (level >= 8, i.e. movers >= 16) whose
removal leaves core mover y with no Xi-path to X (vertex cut over helpers only; core movers other than y, X may not be cut).
kappa(y) = infinity if y reaches X through core movers only. Lemma L14-A: for every helper set G with |G| < kappa(y), y reaches X
through a path avoiding G, so no acyclic rewiring of the options of X and G puts y into closure(X).
Usage: mincut.py GENOME X"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l12'))
import enc32_lcomp as e
from collections import deque, defaultdict
def maxflow(cap, s, t):
    f = 0; flow = defaultdict(int); adj = defaultdict(set)
    for (a, b) in cap: adj[a].add(b); adj[b].add(a)
    while True:
        par = {s: None}; q = deque([s])
        while q and t not in par:
            a = q.popleft()
            for b in adj[a]:
                if b not in par and cap.get((a, b), 0) - flow[(a, b)] + flow[(b, a)] > 0: par[b] = a; q.append(b)
        if t not in par: return f
        path = []; b = t
        while par[b] is not None: path.append((par[b], b)); b = par[b]
        d = min(cap.get(e, 0) - flow[e] + flow[(e[1], e[0])] for e in path)
        for (a, b) in path:
            r = min(d, flow[(b, a)]); flow[(b, a)] -= r; flow[(a, b)] += d - r
        f += d
        if f >= 10 ** 6: return f
D = e.rdgen(sys.argv[1]); X = int(sys.argv[2]); xt = D['xt']; N = 2 * D['d']; INF = 10 ** 6
out = {}
for y in range(16):
    if y == X: continue
    cap = {}
    for m in range(N):
        cap[(('i', m), ('o', m))] = 1 if m >= 16 else INF
        for k in (0, 1):
            w = xt[2 * m + k]
            if w >= 0: cap[(('o', m), ('i', w))] = INF
    v = maxflow(cap, ('o', y), ('i', X))
    out[y] = 'inf' if v >= INF else v
print('genome', os.path.basename(sys.argv[1]), 'X', X, 'kappa(y) for core y:', out)
