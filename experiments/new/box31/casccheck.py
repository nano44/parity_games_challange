#!/usr/bin/env python3
"""Box 31 (a): Lemma CASC on real N5 runs. Route-form pieces (both frames in route form; phase, R, θ, w constant). Inside a piece,
a W-FLAT RUN is a maximal run of consecutive non-fallback transitions with W unchanged on R. Claim: an R-vertex of W-level ℓ
(ℓ = W-length − W(o)-length = |π_v|) switches only at run steps 0..ℓ-2. Reports pieces, runs, switches, violations, and the
largest per-vertex switch count in one run (the U1-T quantity). Usage: casccheck.py game.pg [start] | --rand N lo hi seed"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box29"))
from otherx import *

def rows_of(g, start=None, cap=10 ** 6):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        rf = (h[0] or Xi[o][0] == o) and (h[1] or W[o][0] == o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), rf=rf, R=reach_o(g, s, t, o), th=E.key(Xi[o]),
                         w=E.key(W[o]), cth=Xi[o][0], cw=W[o][0], Wk=[E.key(W[v]) for v in range(g.n)], Wl=[W[v][2] for v in range(g.n)],
                         s=list(s), fb=0, U1=E.rank[W[o][0]] > E.rank[Xi[o][0]]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = r[0], r[1]
    return rows, o

def analyse(g, start, acc):
    rows, o = rows_of(g, start); k = 0
    while k < len(rows):
        if not rows[k]["rf"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        if j > k:
            acc["pieces"] += 1; acc["U1pieces"] += rows[k]["U1"]; Rs = [v for v in rows[k]["R"] if v != o]
            i = k
            while i < j:
                if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in Rs): i += 1; continue
                a = i; per = {}
                while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in Rs):
                    st = i - a
                    for v in Rs:
                        if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]:
                            lvl = rows[i]["Wl"][v] - rows[i]["Wl"][o]; acc["switches"] += 1; per[v] = per.get(v, 0) + 1
                            if not st <= lvl - 2: acc["viol"] += 1; acc.setdefault("ex", (k, i, v, st, lvl))
                    i += 1
                acc["runs"] += 1; acc["maxrunlen"] = max(acc["maxrunlen"], i - a)
                if per: acc["maxper"] = max(acc["maxper"], max(per.values()))
        k = j + 1

if __name__ == "__main__":
    acc = dict(pieces=0, U1pieces=0, runs=0, switches=0, viol=0, maxper=0, maxrunlen=0); a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            analyse(g, None, acc); d += 1
    else:
        g = load(a[0]); analyse(g, readstart(a[1]) if len(a) > 1 else None, acc)
    print("CASC", acc)
