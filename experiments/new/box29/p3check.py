#!/usr/bin/env python3
"""Box 29, pattern "3" (H1 ∧ H2 ∧ ¬H3): maximal runs inside one phase with R, θ, w constant and pattern 3 at every state.
Per run: which cycle node is more relevant (c_θ = λ_Ξ(o) or c_w = λ_W(o), by Engine rank); κ := route vertices above the more
relevant one; index of the last κ change on R (Lemma P3 freeze: ≤ |R|; route paths have ≤ |R| edges); Ξ-changing transitions (bound n² + n when c_θ is the
more relevant). Usage: p3check.py game.pg [start] | p3check.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def route(nxt, v, o):
    p = []
    while v != o and v not in p: p.append(v); v = nxt[v]
    return p

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0]); R = reach_o(g, s, t, o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), p3=h == (True, True, False), R=R,
                         th=E.key(Xi[o]), w=E.key(W[o]), cth=Xi[o][0], cw=W[o][0], Xk=[E.key(Xi[v]) for v in range(g.n)],
                         nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    k = 0
    while k < len(rows):
        if not rows[k]["p3"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["p3"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        if j > k:
            hi = rows[k]["cth"] if E.rank[rows[k]["cth"]] > E.rank[rows[k]["cw"]] else rows[k]["cw"]
            which = "cθ more relevant" if hi == rows[k]["cth"] else "cw more relevant"
            Vhi = {v for v in range(g.n) if E.rank[v] > E.rank[hi]}
            kap = [tuple(frozenset(route(r["nxt"], v, o)) & Vhi for v in sorted(rows[k]["R"])) for r in rows[k:j + 1]]
            last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
            xc = sum(rows[i]["Xk"] != rows[i + 1]["Xk"] for i in range(k, j))
            acc[which + ": runs"] = acc.get(which + ": runs", 0) + 1
            acc[which + ": freeze fails (> |R|)"] = acc.get(which + ": freeze fails (> |R|)", 0) + (last > len(rows[k]["R"]))
            acc[which + ": max Ξ-changing"] = max(acc.get(which + ": max Ξ-changing", 0), xc)
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
    print(acc)
