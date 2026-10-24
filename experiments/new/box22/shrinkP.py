#!/usr/bin/env python3
"""Box 22: greedy shrink of a C^1O game (canonical N5 run) keeping a violation of an inductive invariant inside a
(θ, w, τ, λ)-stretch. INV = I1 (Lemma P in G_τ for W) | I2 (honest Lemma P in K^θ) | I3 (honest, o-free paths).
Moves: delete a vertex (redirect in-edges to its first other successor), drop an edge, lower a priority to the next free value.
Usage: shrinkP.py in.pg out.pg INV"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from stretchP import back_paths, pathval, prefix
HREQ = os.environ.get("HREQ") == "1"; NOFB = os.environ.get("NOFB") == "1"
def violation(G, inv):
    prio, owner, succ = G; n = len(prio)
    odd = [v for v in range(n) if owner[v] == 1 and len(succ[v]) > 1]
    if len(odd) != 1 or any(not s for s in succ): return None
    o = odd[0]; g = pg.Game(list(prio), list(owner), [list(s) for s in succ]); E = Engine(g)
    try: st, _ = trace(g, check=False)
    except Exception: return None
    fbs = []                                       # fallback flag of each transition k-1 -> k (S4c fired)
    if NOFB:
        E2, Ed2 = Engine(g), Engine(dual(g))
        for k in range(1, len(st)):
            r = step(g, E2, Ed2, list(st[k - 1][0]), list(st[k - 1][1])); fbs.append(r[4])
    key = []
    for s, t in st:
        X, _ = E.evaluate(s); key.append((X[o], wvals(g, s, t)[1][o], t, tuple(x[0] for x in X)))
    k0 = 0
    for k in range(1, len(st)):
        if key[k] != key[k0]: k0 = k; continue
        if NOFB and any(fbs[i - 1] for i in range(k0 + 1, k + 1)): continue   # a fallback inside the stretch so far
        j = k - k0; s, t = st[k]; s0 = st[k0][0]
        Eg, W = wvals(g, s, t); X, _ = E.evaluate(s)
        if HREQ:   # Lemma G's (h) at this state and at the stretch start: same cycle node at o, o on no cycle of either play
            _, W0h = wvals(g, s0, t); X0h, _ = E.evaluate(s0)
            if X[o][0] != W[o][0] or X[o][0] == o or W[o][0] == o or X0h[o][0] != W0h[o][0]: continue
            cyc = {x[0] for x in X} | {w[0] for w in W}
            if len(cyc) != 1: continue        # single-sink stretch state (the setting of §3.5-3.6)
        if inv == "I4":   # W beats every o-free path (<= j edges) and every o-path valued at the honest θ = Ξ(o)
            X0, _ = E.evaluate(s0); succO = [g.succ[v] if g.owner[v] == 0 else ([t[v]] if v != o else []) for v in range(n)]
            for u in {x0[0] for x0 in X0}:
                if u == o: continue
                for x, verts in back_paths(succO, u, j, {o}):
                    if E.key(W[x]) < E.key(pathval(Eg, u, verts, len(verts))): return (k0, j, x, u, verts, "o-free")
            _, sbar = E.evaluate(s); cont = set(); y = sbar[o]          # o's honest continuation (Odd plays σ̄, Even σ)
            while y not in cont and y != o:
                cont.add(y); y = s[y] if g.owner[y] == 0 else (sbar[y] if sbar[y] is not None and sbar[y] >= 0 else g.succ[y][0])
            for x, verts in back_paths(succO, o, j, cont):
                if verts and E.key(W[x]) < E.key(prefix(Eg, verts, X[o])): return (k0, j, x, "o", verts, "o-path")
            continue
        if inv == "I1":
            _, W0 = wvals(g, s0, t); succT = [g.succ[v] if g.owner[v] == 0 else [t[v]] for v in range(n)]
            for u in {w[0] for w in W0}:
                for x, verts in back_paths(succT, u, j, set()):
                    if E.key(W[x]) < E.key(pathval(Eg, u, verts, len(verts))): return (k0, j, x, u, verts)
        else:
            X0, _ = E.evaluate(s0); succO = [g.succ[v] if g.owner[v] == 0 else ([t[v]] if v != o else []) for v in range(n)]
            for u in {x0[0] for x0 in X0}:
                if u == o: continue
                for x, verts in back_paths(succO, u, j, {o}):
                    if E.key(X[x]) < E.key(pathval(Eg, u, verts, len(verts))): return (k0, j, x, u, verts)
            if inv == "I2":
                for x, verts in back_paths(succO, o, j, set()):
                    if verts and E.key(X[x]) < E.key(prefix(Eg, verts, X[o])): return (k0, j, x, "o", verts)
    return None
def delvert(G, v):
    prio, owner, succ = G; n = len(prio); tgt = next((w for w in succ[v] if w != v), None)
    if tgt is None: return None
    m = lambda w: w if w < v else w - 1
    return [prio[:v] + prio[v + 1:], owner[:v] + owner[v + 1:], [sorted({m(tgt if w == v else w) for w in succ[u]}) for u in range(n) if u != v]]
if __name__ == "__main__":
    g = load(sys.argv[1]); G = [list(g.prio), list(g.owner), [list(s) for s in g.succ]]; inv = sys.argv[3]
    assert violation(G, inv), "no violation to keep"
    changed = True
    while changed:
        changed = False
        for v in range(len(G[0])):
            H = delvert(G, v)
            if H and violation(H, inv): G = H; changed = True; print("n ->", len(G[0]), flush=True); break
        if changed: continue
        for v in range(len(G[0])):
            for w in list(G[2][v]):
                if len(G[2][v]) > 1:
                    H = [G[0], G[1], [list(s) for s in G[2]]]; H[2][v].remove(w)
                    if violation(H, inv): G = H; changed = True; break
            if changed: break
    n = len(G[0])
    with open(sys.argv[2], "w") as f:
        f.write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
    print("final n", n, "edges", sum(map(len, G[2])), "violation", violation(G, inv))
