#!/usr/bin/env python3
"""Box 192: TIE-PERSIST check on a general game. Replays N5'-xi (box190 n5v.py mode xi, unmodified) and, for the sigma-step window
[A, B] (indices into the sigma-changing iterations S, 1-based), takes the vertex x switched at step B and the play pi from x under
(sigma_B, sigma-bar_B) up to its cycle node w. TIE-PERSIST asks: for every Even z on pi before w and every step k in [A, B-1], z is a
TIE vertex at k and sigma_B(z) is in TIE_k(z). Prints each failing (z, k) with the reason. Usage: tiep192.py GAME.json A B"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190")]
import n5v
from si import Engine
pg = n5v.pg; dual = n5v.dual
G = json.load(open(sys.argv[1])); A, Bk = int(sys.argv[2]), int(sys.argv[3]); g = pg.Game(*G); n = g.n
st, fb, E = n5v.run(g, "xi")
steps = [(s, t, ns) for (s, t), (ns, nt) in zip(st, st[1:]) if ns != s]   # step k (1-based) = steps[k-1]: sigma s -> ns, tau t
def tie(s, t):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    opt = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    vh, _ = Er.evaluate(tuple(t[v] if g.owner[v] == 1 else -1 for v in range(n)))
    T = {}
    for v in range(n):
        if g.owner[v] != 0: continue
        if len(opt[v]) >= 2 and vh[v][0] != v:
            T[v] = {w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]} or None
        else: T[v] = None
    return T
sB, tB, nsB = steps[Bk - 1]
x = [v for v in range(n) if g.owner[v] == 0 and nsB[v] != sB[v]]
vsB, sbB = E.evaluate(tuple(nsB))
for x0 in x:
    w = vsB[x0][0]; pi = []; v = x0
    while v != w and v not in pi: pi.append(v); v = nsB[v] if g.owner[v] == 0 else sbB[v]
    print("switched", x0, "cycle node", w, "play", pi + [w])
    fails = 0
    for k in range(A, Bk):
        s, t, _ = steps[k - 1]; T = tie(s, t)
        for z in pi:
            if g.owner[z] != 0: continue
            if T[z] is None: print(f"  k {k}: z {z} not a TIE vertex"); fails += 1
            elif nsB[z] not in T[z]: print(f"  k {k}: z {z} edge to {nsB[z]} not in TIE_k(z) = {sorted(T[z])}"); fails += 1
    print("TIE-PERSIST failures", fails)
