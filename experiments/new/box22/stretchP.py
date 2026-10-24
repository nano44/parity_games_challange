#!/usr/bin/env python3
"""Box 22: candidate inductive invariants inside (θ, w, τ, λ)-stretches of frozen N5 runs on C^1O (one Odd choice vertex o).
A stretch starts at state k0; at state k0 + j we test, for every vertex x and every simple path r with <= j edges:
  I1 (G_τ, W):    W_{k}(x) ⪰ value_w(r)      r a path in G_τ (o follows τ(o)) ending at a cycle node u of W_{k0}
  I2 (K^θ, Ξ):    Ξ_{k}(x) ⪰ value_θ(r)      r a path to a cycle node u of Ξ_{k0} avoiding o, or a path ending AT o valued π_r ⊕ θ
  I3 (o-free, Ξ): Ξ_{k}(x) ⪰ value(r)        r a path avoiding o to a cycle node of Ξ_{k0}
Reports the first violation per invariant (game, stretch, step, x, r). Usage: stretchP.py N nmin nmax seed [--frozen tstar|canon]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
def pathval(Eg, u, verts, L):
    P = 0
    for y in verts:
        if Eg.rank[y] > Eg.rank[u]: P |= Eg.bit[y]
    return (u, P, L)
def prefix(Eg, verts, a):
    c, P, l = a
    for y in verts:
        if Eg.rank[y] > Eg.rank[c]: P |= Eg.bit[y]
    return (c, P, l + len(verts))
def back_paths(succ, u, kmax, avoid):
    """simple paths r = (x, ..., u) with <= kmax edges, as (x, list of vertices before u), not using vertices in avoid (except u)."""
    n = len(succ); out = []
    pred = [[y for y in range(n) if x in succ[y]] for x in range(n)]
    def rec(x, verts, on):
        out.append((x, list(verts)))
        if len(verts) == kmax: return
        for y in pred[x]:
            if y not in on and y not in avoid: rec(y, verts + [y], on | {y})
    rec(u, [], {u})
    return out
def check_state(g, E, o, s, t, s0, j, res, tag):
    n = g.n; Eg, W = wvals(g, s, t); X, _ = E.evaluate(s); Eg0, W0 = wvals(g, s0, t); X0, _ = E.evaluate(s0)
    succT = [g.succ[v] if g.owner[v] == 0 or v != o else [t[o]] for v in range(n)]
    succT = [succT[v] if g.owner[v] == 0 or v == o else [t[v]] for v in range(n)]
    theta = X[o]
    if "I1" not in res:
        for u in {w[0] for w in W0}:
            for x, verts in back_paths(succT, u, j, set()):
                if E.key(W[x]) < E.key(pathval(Eg, u, [x] + verts[:-1] if verts else [], len(verts))) if False else E.key(W[x]) < E.key(pathval(Eg, u, ([u] + verts)[1:], len(verts))):
                    res["I1"] = (tag, j, x, u, verts); break
            if "I1" in res: break
    succO = [g.succ[v] if g.owner[v] == 0 else ([t[v]] if v != o else []) for v in range(n)]
    for inv in ("I2", "I3"):
        if inv in res: continue
        for u in {x0[0] for x0 in X0}:
            if u == o: continue
            for x, verts in back_paths(succO, u, j, {o}):
                val = pathval(Eg, u, verts, len(verts))
                if E.key(X[x]) < E.key(val): res[inv] = (tag, j, x, u, verts); break
            if inv in res: break
        if inv == "I2" and "I2" not in res:
            for x, verts in back_paths(succO, o, j, set()):
                if not verts: continue
                val = prefix(Eg, verts, theta)
                if E.key(X[x]) < E.key(val): res["I2"] = (tag, j, x, "o", verts); break
def run(N, a, b, seed, mode):
    rng = random.Random(seed); res = {}; first = {}
    for gi in range(N):
        n = rng.randint(a, b); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
        succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
        g = pg.Game([rng.randrange(n) for _ in range(n)], owner, succ); E = Engine(g)
        st, _ = trace(g, check=False)
        if mode == "tstar":
            s0, ts = st[0][0], st[-1][1]
            st, _ = trace(g, ({v: s0[v] for v in range(n) if owner[v] == 0}, {o: ts[o]}), check=False)
        key = []
        for s, t in st:
            X, _ = E.evaluate(s); key.append((X[o], wvals(g, s, t)[1][o], t, tuple(x[0] for x in X)))
        k0 = 0
        for k in range(1, len(st)):
            if key[k] != key[k0]: k0 = k; continue
            before = set(res)
            check_state(g, E, o, st[k][0], st[k][1], st[k0][0], k - k0, res, (gi, n, k0, k))
            for inv in set(res) - before: first[inv] = (n, g.prio, g.owner, g.succ, st[k0], res[inv])
        if len(res) == 3: break
    for inv in ("I1", "I2", "I3"):
        print(inv, "violated" if inv in res else "no violation", res.get(inv))
        if inv in first: print("   game n", first[inv][0], "prio", first[inv][1], "owner", first[inv][2], "succ", first[inv][3])
if __name__ == "__main__":
    a = sys.argv[1:]; mode = a[a.index("--frozen") + 1] if "--frozen" in a else "canon"
    run(int(a[0]), int(a[1]), int(a[2]), int(a[3]), mode)
