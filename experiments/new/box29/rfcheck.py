#!/usr/bin/env python3
"""Box 29: route-form OTHER runs (H2, and H1 or λ_Ξ(o) = o; maximal runs in one phase with R, θ, w constant): κ := route vertices
above the more relevant of c_θ, c_w. Checks Lemma P^κ (last κ change at run index ≤ |R|) and counts Ξ-changing transitions AFTER the
κ-freeze, split by which cycle node is higher (P3' proves ≤ n·|R| of them when c_θ is higher; OPEN when c_w is higher).
Usage: rfcheck.py game.pg [start] | rfcheck.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *
from p3check import route

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        rf = (not all(h)) and Xk != Wk and h[1] and (h[0] or Xi[o][0] == o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), rf=rf, R=reach_o(g, s, t, o), th=Xk[o], w=Wk[o],
                         cth=Xi[o][0], cw=W[o][0], Xk=Xk, nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    k = 0
    while k < len(rows):
        if not rows[k]["rf"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        if j > k:
            hi = rows[k]["cth"] if E.rank[rows[k]["cth"]] > E.rank[rows[k]["cw"]] else rows[k]["cw"]
            which = "cθ higher" if hi == rows[k]["cth"] else "cw higher"
            Vhi = {v for v in range(g.n) if E.rank[v] > E.rank[hi]}; Rs = sorted(rows[k]["R"])
            kap = [tuple(frozenset(route(r["nxt"], v, o)) & Vhi for v in Rs) for r in rows[k:j + 1]]
            last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
            post = sum(rows[i]["Xk"] != rows[i + 1]["Xk"] for i in range(k + last, j))
            for key, val in ((which + ": runs", 1), (which + ": κ-freeze fails (> |R|)", int(last > len(Rs))),
                             (which + ": Ξ-changing after κ-freeze", post), (which + ": run transitions", j - k)):
                acc[key] = acc.get(key, 0) + val
            acc[which + ": max run length"] = max(acc.get(which + ": max run length", 0), j - k)
        k = j + 1

if __name__ == "__main__":
    a = sys.argv[1:]; acc = {}
    if a[0] != "--rand":
        g = load(a[0]); analyse(g, readstart(a[1]) if len(a) > 1 else None, acc)
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            analyse(g, start, acc)
    for k, v in sorted(acc.items()): print(k, v)
