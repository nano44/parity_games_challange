#!/usr/bin/env python3
"""Box 30 (U1): in route-form OTHER pieces with c_w more relevant than c_θ, the per-vertex number of Ξ-changes on R after the
κ-freeze (κ := route vertices above c_w), the number of those at W-flat transitions, and whether W lengths ever move backwards.
Usage: u1vertex.py game.pg [start]"""
import sys
from otherx import *
from p3check import route
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, readstart(sys.argv[2]) if len(sys.argv) > 2 else None); rows = []
while True:
    Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
    Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
    h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
    rf = (not all(h)) and Xk != Wk and (h[0] or Xi[o][0] == o) and (h[1] or W[o][0] == o) and E.rank[W[o][0]] > E.rank[Xi[o][0]]
    rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), rf=rf, R=reach_o(g, s, t, o), th=Xk[o], w=Wk[o], cw=W[o][0],
                     Xk=Xk, Wk=Wk, nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]))
    r = step(g, E, Ed, s, t)
    if r is None: break
    s, t = r[0], r[1]
k = 0
while k < len(rows):
    if not rows[k]["rf"]: k += 1; continue
    j = k
    while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
    Vhi = {v for v in range(g.n) if E.rank[v] > E.rank[rows[k]["cw"]]}; Rs = sorted(rows[k]["R"])
    kap = [tuple(frozenset(route(r["nxt"], v, o)) & Vhi for v in Rs) for r in rows[k:j + 1]]
    last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
    per = {v: 0 for v in Rs}; wflat = 0; back = 0
    for i in range(k + last, j):
        a, b = rows[i], rows[i + 1]
        ch = [v for v in Rs if a["Xk"][v] != b["Xk"][v]]
        for v in ch: per[v] += 1
        if ch and all(a["Wk"][v] == b["Wk"][v] for v in range(g.n)): wflat += 1
        back += sum(1 for v in Rs if b["Wk"][v] < a["Wk"][v])
    print(f"piece {k}..{j} |R| {len(Rs)} freeze at {last}: post-freeze R-changes per vertex max {max(per.values()) if per else 0}, total {sum(per.values())}, W-flat transitions {wflat}, W decreases on R {back}")
    k = j + 1
