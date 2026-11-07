#!/usr/bin/env python3
"""exhibit a forced run with <= k flips that uses one record mu_k times (independent re-run: explicit DFS, then replay with cstep).
Usage: trace2.py k file.json"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "fk.py")).read().split("\nif __name__")[0]); sys.setrecursionlimit(100000)
k = int(sys.argv[1]); G = json.load(open(sys.argv[2])); g = Gen(G); N = g.N; U = [x for x in range(N) if g.lev[x] >= 1]
T, mu, r = muk(G, k); print("T_k", T, "mu_k", mu, "record", r)
base = tuple(G["start"][x] if g.lev[x] == 0 else 0 for x in range(N)); memo = {}
def f(s, c, j):
    if (s, c, j) in memo: return memo[(s, c, j)]
    best = (0, [])
    for cc, jj in ((c, j), (1 - c, j - 1)):
        if jj < 0: continue
        t = cstep(g, s, cc)
        if t == s: continue
        rs = [(x, decisive(g, chain(g, s, x, t[x]), chain(g, s, x, s[x]))) for x in U if t[x] != s[x]]
        v, p = f(t, cc, jj); v += int(r in rs)
        if v > best[0]: best = (v, [(s, cc, t, rs)] + p)
    memo[(s, c, j)] = best; return best
cands = []
for bits in itertools.product((0, 1), repeat=len(U)):
    s = list(base)
    for x, b in zip(U, bits): s[x] = b
    for c in (0, 1): cands.append((f(tuple(s), c, k), c))
(v, path), c0 = max(cands, key=lambda z: z[0][0])
flips = sum(1 for a, b in zip(path, path[1:]) if a[1] != b[1])
print("replayed count", v, "frames", len(path), "flips", flips)
for i, (s, cc, t, rs) in enumerate(path):
    assert cstep(g, s, cc) == t
    print("frame %d c %d %s -> %s %s%s" % (i + 1, cc, "".join(str(s[x]) for x in U), "".join(str(t[x]) for x in U), rs, "  <==" if r in rs else ""))
