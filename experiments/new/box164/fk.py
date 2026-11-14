#!/usr/bin/env python3
"""mu_k: max multiplicity of one record (x, decisive beta) over forced runs with <= k flips (P-IDEAL-FLIP §1 counting: frames with no
step are free; a flip is a change of c between consecutive frames). Usage: fk.py k file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, "finf.py")).read(); exec(src.split("def analyse")[0])
import itertools
def muk(G, k):
    g = Gen(G); N = g.N; U = [x for x in range(N) if g.lev[x] >= 1]
    base = tuple(G["start"][x] if g.lev[x] == 0 else 0 for x in range(N)); states = []
    for bits in itertools.product((0, 1), repeat=len(U)):
        s = list(base)
        for x, b in zip(U, bits): s[x] = b
        states.append(tuple(s))
    nxt = {}
    for s in states:
        for c in (0, 1):
            t = cstep(g, s, c)
            nxt[(s, c)] = None if t == s else (t, [(x, decisive(g, chain(g, s, x, t[x]), chain(g, s, x, s[x]))) for x in U if t[x] != s[x]])
    recs = set(r for v in nxt.values() if v for r in v[1])
    def best(w):
        memo = {}
        def f(s, c, j):  # at state s, current bit c, j flips left; may move with c or flip (j>0)
            key = (s, c, j)
            if key in memo: return memo[key]
            v = 0; n = nxt[(s, c)]
            if n: v = max(v, w(n[1]) + f(n[0], c, j))
            if j > 0:
                n2 = nxt[(s, 1 - c)]
                if n2: v = max(v, w(n2[1]) + f(n2[0], 1 - c, j - 1))
            memo[key] = v; return v
        return max(f(s, c, k) for s in states for c in (0, 1))
    T = best(lambda rs: 1); mu, arg = 0, None
    for r in recs:
        v = best(lambda rs: int(r in rs))
        if v > mu: mu, arg = v, r
    return T, mu, arg
if __name__ == "__main__":
    sys.setrecursionlimit(100000); k = int(sys.argv[1])
    for f in sys.argv[2:]:
        G = json.load(open(f)); print(os.path.basename(f), "k %d T_k %d mu_k %d record %s" % ((k,) + muk(G, k)))
