#!/usr/bin/env python3
"""L-SI box 4 (b)/(d): candidate potential CORR_k := #{y ≠ o original : Ξ_k(y) equals y's optimal value in the parametric game H_k}
(rstar.py's gadget; values compared rank-free with copies mapped back to originals). Reports per longest phase: |R*| range,
CORR decreases (count, largest drop), crossing transitions where CORR does not strictly rise, and CORR's start/end.
Usage: correct.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rstar import *

def hopt_vals(h):
    Ed = Engine(dual(h)); _, best = Ed.evaluate(tuple(-1 if h.owner[v] == 0 else h.succ[v][0] for v in range(h.n)))
    s = tuple(best[v] if h.owner[v] == 0 else -1 for v in range(h.n)); Eh = Engine(h); val, _ = Eh.evaluate(s)
    return Eh, val, [best[v] if h.owner[v] == 0 else h.succ[v][0] for v in range(h.n)]

def rankfree(Eng, val, back):
    w, mask, ln = val; inv = {Eng.rank[v]: v for v in range(Eng.n)}
    return (back(w), frozenset(back(inv[r]) for r in range(Eng.n) if mask >> r & 1), ln)

def scan(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows:
        Xi, sb = E.evaluate(tuple(r["s"])); h = gadget(g, E, r["s"], r["t"], sb, o)
        # copies were appended in play order; map copy index -> original by replaying the gadget construction
        nxt = lambda v: r["s"][v] if g.owner[v] == 0 else sb[v]
        play = [o]; seen = {o}
        while True:
            u = nxt(play[-1])
            if u in seen: break
            play.append(u); seen.add(u)
        orig = {g.n + i: u for i, u in enumerate(play)}
        back = lambda v: orig.get(v, v)
        Eh, hv, hs = hopt_vals(h)
        r["Rs"] = reaches(h, hs, o, g.n)
        r["C"] = {y for y in range(g.n) if y != o and rankfree(Eh, hv[y], back) == rankfree(E, Xi[y], lambda v: v)}
    out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), T=y - x, Rs=sorted({len(rows[k]["Rs"]) for k in range(x, y + 1)}), C0=len(rows[x]["C"]), C1=len(rows[y]["C"]),
                  Cdec=0, Cdrop=0, Clost=0, X=0, X_noCrise=0, tc=0)
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]; st["tc"] += a["th"] != b["th"]
            lost = a["C"] - b["C"]; st["Clost"] += len(lost)
            if len(b["C"]) < len(a["C"]): st["Cdec"] += 1; st["Cdrop"] = max(st["Cdrop"], len(a["C"]) - len(b["C"]))
            if a["R"] != b["R"]:
                st["X"] += 1; st["X_noCrise"] += not (len(b["C"]) > len(a["C"]))
        out.append(st)
    return g.n, out

if __name__ == "__main__":
    for p in sys.argv[1:]:
        n, out = scan(p); best = max(out, key=lambda s: (s["X"], s["T"]))
        print(os.path.basename(p), "n", n, best)
