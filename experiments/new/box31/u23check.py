#!/usr/bin/env python3
"""Box 31 (b): W-flat runs outside route form. Stretches = maximal runs of a phase with R, θ, w constant.
U2 (¬H1, c_θ ≠ o; W frame in route form): CASC check with level |π_v| = W-length(v) − W-length(o)  [claim CASC-U2: no violation].
U3 (¬H2, c_w ≠ o; honest frame in route form): kind A = c_w on v's σ-route to o, kind B otherwise. EVENTS = a switch that changes
  the switching vertex's kind, or a switch of c_w itself. Sub-runs split at events. Claims CASC-U3: (i) a non-event switch of a kind-B
  vertex at W-level λ happens only at sub-run step ≤ λ − d − 2 (d = W-length of o); (ii) no non-event switch at sub-run step ≥ 2|R|.
Usage: u23check.py game.pg | --rand N lo hi seed"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box29"))
from otherx import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tbcheck import odd1

def route(nxt, v, o):
    p = []
    while v != o and v not in p: p.append(v); v = nxt[v]
    return p

def rows_u(g, cap=10 ** 6):
    E, Ed = Engine(g), Engine(dual(g)); o = odd1(g); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), R=reach_o(g, s, t, o), th=E.key(Xi[o]), w=E.key(W[o]),
                         rfX=h1 or Xi[o][0] == o, rfW=h2 or W[o][0] == o, cw=W[o][0], Wk=[E.key(W[v]) for v in range(g.n)],
                         Wl=[W[v][2] for v in range(g.n)], s=list(s), nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = r[0], r[1]
    return rows, o

def analyse(g, acc):
    rows, o = rows_u(g); k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        r0 = rows[k]; kind = None
        if not r0["rfX"] and r0["rfW"]: kind = "U2"
        if r0["rfX"] and not r0["rfW"]: kind = "U3"
        if kind and j > k:
            acc[kind + "_stretches"] = acc.get(kind + "_stretches", 0) + 1; Rs = [v for v in r0["R"] if v != o]; i = k; cw = r0["cw"]
            while i < j:
                if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in Rs): i += 1; continue
                a = i; c0 = i; ev = 0
                while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in Rs):
                    A0 = {v for v in Rs if cw in route(rows[i]["nxt"], v, o)}; A1 = {v for v in Rs if cw in route(rows[i + 1]["nxt"], v, o)}
                    evt = False
                    for v in Rs:
                        if g.owner[v] != 0 or rows[i]["s"][v] == rows[i + 1]["s"][v]: continue
                        acc[kind + "_sw"] = acc.get(kind + "_sw", 0) + 1
                        if kind == "U2":
                            if i - a > rows[i]["Wl"][v] - rows[i]["Wl"][o] - 2: acc["U2_viol"] = acc.get("U2_viol", 0) + 1; acc.setdefault("ex2", (k, i, v))
                        else:
                            if v == cw or ((v in A0) != (v in A1)): evt = True; acc["U3_events"] = acc.get("U3_events", 0) + 1; acc["U3_ev_cw" if v == cw else "U3_ev_kind"] = acc.get("U3_ev_cw" if v == cw else "U3_ev_kind", 0) + 1; continue
                            d = rows[i]["Wl"][o]
                            if v not in A0 and i - c0 > rows[i]["Wl"][v] - d - 2: acc["U3_violB"] = acc.get("U3_violB", 0) + 1; acc.setdefault("ex3", (k, i, v))
                            if i - c0 >= 2 * (len(Rs) + 1): acc["U3_viol2R"] = acc.get("U3_viol2R", 0) + 1
                    i += 1
                    if evt: c0 = i; ev += 1
                acc["max_ev_per_run"] = max(acc.get("max_ev_per_run", 0), ev); acc["maxflat"] = max(acc.get("maxflat", 0), i - a)
        k = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            analyse(g, acc); d += 1
    else: analyse(load(a[0]), acc)
    print("U23", acc)
