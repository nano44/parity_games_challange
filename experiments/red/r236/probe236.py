#!/usr/bin/env python3
"""L-RED 66 R236: for a cls236 game, at the first differing state t, compare the two engines' choices at every vertex where they differ:
is n5v's choice optimal in the S4a / S4b arena under n5x236's W* (TIE) or not (DIVERGENCE); was either step a fallback (Is/It, A sets).
Usage: probe236.py SEED INDEX NMAX (env LNEW)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness"), os.path.join(os.environ["LNEW"], "experiments/new/box190")]
import n5x236 as X, gen, n5v
seed, i, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
n = 2 + (i % (nmax - 1)); g = gen.random_game(n, max(2, n // 2), 1, 3, seed * 100000 + i)
prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]
tr = []; X.run(prio, owner, succ, trace=tr); st, fbs, E = n5v.run(g, "xi")
t = next(k for k in range(1, min(len(tr), len(st))) if tuple(tr[k][0].get(v, -1) for v in range(n)) != tuple(x if owner[v] == 0 else -1 for v, x in enumerate(st[k][0])) or tuple(tr[k][1].get(v, -1) for v in range(n)) != tuple(x if owner[v] == 1 else -1 for v, x in enumerate(st[k][1])))
sig, tau = tr[t - 1]; print("game", i, "n", n, "prio", prio, "owner", owner, "succ", succ)
print("common state t-1 =", t - 1, "sigma", sig, "tau", tau)
V = X.Val(prio); Vd = X.Val([p + 1 for p in prio]); downer = [1 - o for o in owner]
vs, _ = X.optimum(V, owner, succ, [sig.get(v) for v in range(n)], 1, {v: succ[v][0] for v in tau}, False)
vt, _ = X.optimum(Vd, downer, succ, [tau.get(v) for v in range(n)], 1, {v: succ[v][0] for v in sig}, False)
Is = {v: [w for w in succ[v] if w != sig[v] and V.better(vs[w], vs[sig[v]])] for v in sig}; Is = {k: x for k, x in Is.items() if x}
It = {v: [w for w in succ[v] if w != tau[v] and Vd.better(vt[w], vt[tau[v]])] for v in tau}; It = {k: x for k, x in It.items() if x}
print("Is", Is, "It", It)
A = [sorted({tau[v]} | set(It.get(v, []))) if owner[v] == 1 else [sig[v]] for v in range(n)]
W, _ = X.optimum(V, owner, A, [sig.get(v) for v in range(n)], 1, dict(tau), False)
for v in tau:
    mine, theirs = tr[t][1][v], st[t][1][v]
    if mine != theirs:
        opt = lambda w: (X.ext(V, v, W[w]) == W[v]) if W[v][0] != v else (W[w][0] == v and not W[w][1])
        print("Odd", v, "A", A[v], "W*(v)", W[v], "mine", mine, "opt", opt(mine), "n5v", theirs, "opt", opt(theirs), "W*", W[mine], W[theirs])
A = [sorted({sig[v]} | set(Is.get(v, []))) if owner[v] == 0 else [tau[v]] for v in range(n)]
W, _ = X.optimum(V, owner, A, [tau.get(v) for v in range(n)], 0, dict(sig), True)
for v in sig:
    mine, theirs = tr[t][0][v], st[t][0][v]
    if mine != theirs:
        opt = lambda w: (X.ext(V, v, W[w]) == W[v]) if W[v][0] != v else (W[w][0] == v and not W[w][1])
        print("Even", v, "A", A[v], "W*(v)", W[v], "mine", mine, "opt", opt(mine), "n5v", theirs, "opt", opt(theirs), "Xi", vs[mine], vs[theirs])
