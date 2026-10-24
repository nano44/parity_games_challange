#!/usr/bin/env python3
"""Investigate a Step (K) failure under SPEC: state k of the SPEC run of game.pg (S3 start). Usage: dbg_k.py game.pg k y z"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(root, p))
import pg as lpg, n5
from si import Engine
g = rc.parse(open(sys.argv[1]).read()); k, y, z = map(int, sys.argv[2:5])
o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
def br(v, dual):
    def rr(w_):
        p = g.prio[w_] + (1 if dual else 0); r_ = p if p % 2 == 0 else -p
        return (r_, w_ if r_ % 2 == 0 else -w_)
    return max(g.succ[v], key=rr)
s = [br(v, False) for v in range(g.n)]; t = [br(v, True) for v in range(g.n)]
states, fbs = rc.n5_spec(g, o, s, t)
sg, tu = states[k]; S = rc.analyse(g, o, sg, tu)
print("fallback at k:", fbs[k], " sigma_k(y) =", sg[y], " (y,z) in my Is:", (y, z) in S.Is)
lg = lpg.Game(list(g.prio), list(g.owner), [list(x) for x in g.succ]); E = Engine(lg)
vs, _ = E.evaluate(tuple(sg)); Is = E.improving(tuple(sg), vs)
print("(y,z) in si.py Is:", (y, z) in set(Is), " |my Is| =", len(S.Is), " |si Is| =", len(Is), " equal:", set(map(tuple, Is)) == set(S.Is))
f2 = list(S.f); f2[y] = z
print("W_k(y) =", S.W[y], "  single switch value at y =", g.play(f2, y)[0], " cmp:", g.cmp(g.play(f2, y)[0], S.W[y]))
# my arena optimum vs SPEC's
arena = [sorted({sg[v]} | {zz for xx, zz in S.Is if xx == v}) if g.owner[v] == 0 else [S.f[v]] for v in range(g.n)]
_, opt = rc.even_optimum(g, S.f, arena)
print("my arena optimum strictly above W_k somewhere:", [v for v in range(g.n) if g.cmp(opt[v], S.W[v]) > 0])
succ = [sorted(set(arena[v])) if g.owner[v] == 0 else [tu[v]] for v in range(g.n)]
Er = Engine(n5.dual(lpg.Game(list(g.prio), list(g.owner), succ)))
_, best = Er.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(g.n)))
print("SPEC S4a result == sigma_k on Even:", all(best[v] == sg[v] for v in range(g.n) if g.owner[v] == 0))
fb = [best[v] if g.owner[v] == 0 else S.f[v] for v in range(g.n)]
print("SPEC optimum's W vs my optimum, differing vertices:", [v for v in range(g.n) if rc.vals_of(g, fb)[0][v] != opt[v]])
print("--- valuation comparison")
def tri(val):
    c, mask, ln = val
    return (c, frozenset(v for v in range(g.n) if mask >> E.rank[v] & 1), ln)
for v in range(g.n):
    a = S.Xi[v]; b = tri(vs[v])
    if a != b: print("v", v, "mine", (a[0], sorted(a[1]), a[2]), "si", (b[0], sorted(b[1]), b[2]), "cmp(mine, si) =", g.cmp(a, b))
print("my Is - si Is:", sorted(set(S.Is) - set(map(tuple, Is))), " si - mine:", sorted(set(map(tuple, Is)) - set(S.Is)))
print("o =", o, "succ(o) =", g.succ[o], "my sbar(o) =", S.sbar)
