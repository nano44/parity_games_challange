#!/usr/bin/env python3
"""Box 33: attack on L-NEW's CONJECTURE (U1-T) (docs/new/N5-U1-box30.md §1-§3): after the κ_w-freeze of a U1 piece, each R-vertex has
<= 2 Ξ-changes per value of its W-length. Piece, freeze and R exactly as L-NEW's experiments/new/box29/u1vertex.py (imported helpers
unmodified; the loop below is u1vertex's, with the per-vertex count split by the vertex's W value (post-freeze W order on routes is
length only, §1)). Reports per game: max changes of one vertex at one W value (U1-T says <= 2), kind-(T) (W-flat) transitions,
post-freeze R-changes, and 'own' = max switches of one R-vertex's OWN successor at one unchanged W value (the spec §3 cascade).
As a climb: fitness = (max per (vertex, W value), kind (T), post-freeze total); with --own: (own, max per (vertex, W), kind (T)).
Usage: u1t.py game.pg ... | u1t.py --climb n seed secs out seed.pg"""
import sys, os, random, time
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "new", "box29"); sys.path.insert(0, B)
from otherx import *
from p3check import route
from climb_fix import mutate

def u1t(g, cap=400):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        rf = (not all(h)) and Xk != Wk and (h[0] or Xi[o][0] == o) and (h[1] or W[o][0] == o) and E.rank[W[o][0]] > E.rank[Xi[o][0]]
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), rf=rf, R=reach_o(g, s, t, o), th=Xk[o], w=Wk[o],
                         cw=W[o][0], Xk=Xk, Wk=Wk, nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    best = dict(maxvw=0, kindT=0, post=0, own=0, pieces=0, Rmax=0, where=None); k = 0
    while k < len(rows):
        if not rows[k]["rf"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        Vhi = {v for v in range(g.n) if E.rank[v] > E.rank[rows[k]["cw"]]}; Rs = sorted(rows[k]["R"])
        kap = [tuple(frozenset(route(r["nxt"], v, o)) & Vhi for v in Rs) for r in rows[k:j + 1]]
        last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
        per = {}; own = {}; wflat = 0; tot = 0
        for i in range(k + last, j):
            a, b = rows[i], rows[i + 1]
            ch = [v for v in Rs if a["Xk"][v] != b["Xk"][v]]
            for v in ch: per[(v, a["Wk"][v])] = per.get((v, a["Wk"][v]), 0) + 1; tot += 1
            for v in Rs:
                if a["nxt"][v] != b["nxt"][v] and a["Wk"][v] == b["Wk"][v]: own[(v, a["Wk"][v])] = own.get((v, a["Wk"][v]), 0) + 1
            if ch and all(a["Wk"][v] == b["Wk"][v] for v in range(g.n)): wflat += 1
        mv = max(per.values()) if per else 0; mo = max(own.values()) if own else 0
        best["pieces"] += 1
        if ((mo, mv, wflat, tot) if OWN else (mv, wflat, tot, mo)) > ((best["own"], best["maxvw"], best["kindT"], best["post"]) if OWN else (best["maxvw"], best["kindT"], best["post"], best["own"])):
            best.update(maxvw=mv, kindT=wflat, post=tot, own=mo, Rmax=len(Rs), where=(k, j, last))
        k = j + 1
    return best

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not x for x in G[2]): return (-1, -1, -1), None
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1, -1), None
    try: b = u1t(g)
    except Exception: return (-1, -1, -1), None
    return ((b["own"], b["maxvw"], b["kindT"]) if OWN else (b["maxvw"], b["kindT"], b["post"])), b
OWN = "--own" in sys.argv

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--own"]
    if a[0] == "--climb":
        n, seed, secs, out, sp = int(a[1]), int(a[2]), float(a[3]), a[4], a[5]; rng = random.Random(seed)
        g = load(sp); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, c = fit(G); print("START", f, c, flush=True)
        t0 = time.time(); it = 0
        while time.time() - t0 < secs:
            H = mutate(rng, G); it += 1; fh, ch = fit(H)
            if fh >= f:
                if fh > f:
                    print(f"{time.time()-t0:7.0f}s it {it} fit {fh} {ch}", flush=True)
                    open(out + ".pg", "w").write(f"parity {g.n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(g.n)))
                G, f = H, fh
        print("FINAL", f, it, flush=True)
    else:
        for p in a:
            g = load(p); print(os.path.basename(p), "n", g.n, u1t(g), flush=True)
