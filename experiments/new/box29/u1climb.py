#!/usr/bin/env python3
"""Box 29 (U1) climb: route-form OTHER pieces with c_w more relevant than c_θ. Fitness = (R-only Ξ-changing transitions after the
κ-freeze in one piece, R-only Ξ-changing transitions in the piece, piece length). Usage: u1climb.py n seed secs out [seed.pg]"""
import sys, os, random, time
from otherx import *
from p3check import route
from climb_fix import mutate

def u1fit_g(g):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) < 400:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        rf = (not all(h)) and Xk != Wk and h[1] and (h[0] or Xi[o][0] == o) and E.rank[W[o][0]] > E.rank[Xi[o][0]]
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), rf=rf, R=reach_o(g, s, t, o), th=Xk[o], w=Wk[o],
                         cw=W[o][0], Xk=Xk, nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    best = (0, 0, 0); k = 0
    while k < len(rows):
        if not rows[k]["rf"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        Vhi = {v for v in range(g.n) if E.rank[v] > E.rank[rows[k]["cw"]]}; Rs = sorted(rows[k]["R"]); Rset = rows[k]["R"] | {o}
        kap = [tuple(frozenset(route(r["nxt"], v, o)) & Vhi for v in Rs) for r in rows[k:j + 1]]
        last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
        ronly = lambda i: any(rows[i]["Xk"][v] != rows[i + 1]["Xk"][v] for v in Rset) and all(rows[i]["Xk"][v] == rows[i + 1]["Xk"][v] for v in range(g.n) if v not in Rset)
        best = max(best, (sum(ronly(i) for i in range(k + last, j)), sum(ronly(i) for i in range(k, j)), j - k)); k = j + 1
    return best

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1, -1)
    try: return u1fit_g(g)
    except Exception: return (-1, -1, -1)

if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    g = load(sys.argv[5]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
