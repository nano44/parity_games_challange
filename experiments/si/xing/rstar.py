#!/usr/bin/env python3
"""L-SI box 4 (c), tropical lens. Parametric one-player game H_k: G with priorities made injective (Engine's p'), every Odd vertex
forced to τ_k, and o's out-edges replaced by a FROZEN COPY of the honest play from o at state k (o -> σ̄_k(o) -> ... -> cycle; copies
carry the same p' and are forced). In H_k vertex o has value θ_k. R*_k := original vertices ≠ o whose Even-optimal play in H_k
reaches o. Lemma TROP (docs/si/N5-X-box4.md): in H(θ), V_y(θ) = max(Π*_y ⊕ θ, f*_y), so R*(θ) is an up-set chain in θ.
Per phase: θ-changes, θ-changes with R* changed, entries/leaves aligned with R* (entry of y ∈ R*_{k+1}, leave of y ∉ R*_{k+1}).
Usage: rstar.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def gadget(g, E, s, t, sb, o):
    n = g.n; pp = list(E.pp); owner = list(g.owner); succ = [list(x) for x in g.succ]
    for v in range(n):
        if owner[v] == 1: succ[v] = [t[v]] if v != o else succ[v]
    # honest play from o under (s, sb)
    nxt = lambda v: s[v] if g.owner[v] == 0 else sb[v]
    play = [o]; seen = {o}
    while True:
        u = nxt(play[-1])
        if u in seen: loop = u; break
        play.append(u); seen.add(u)
    copy = {}
    for u in play: copy[u] = len(pp); pp.append(pp[u]); owner.append(1); succ.append(None)
    for u in play[:-1]: succ[copy[u]] = [copy[nxt(u)]]
    succ[copy[play[-1]]] = [copy[loop]]
    succ[o] = [copy[nxt(o)]]; owner[o] = 1          # o keeps its own priority; frozen continuation
    return pg.Game(pp, owner, succ)

def opt_strategy(h):
    Ed = Engine(dual(h)); _, best = Ed.evaluate(tuple(-1 if h.owner[v] == 0 else h.succ[v][0] for v in range(h.n)))
    return [best[v] if h.owner[v] == 0 else h.succ[v][0] for v in range(h.n)]

def reaches(h, s, o, n):
    R = set()
    for v in range(n):
        if v == o: continue
        x, seen = v, set()
        while x not in seen and x != o: seen.add(x); x = s[x]
        if x == o: R.add(v)
    return R

def scan(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows:
        _, sb = E.evaluate(tuple(r["s"])); h = gadget(g, E, r["s"], r["t"], sb, o)
        r["Rs"] = reaches(h, opt_strategy(h), o, g.n)
    out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), T=y - x, tc=0, tcRs=0, Rs_nonnested=0, X=0, ent=0, ent_al=0, lv=0, lv_al=0, misfit_max=0)
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if a["th"] != b["th"]:
                st["tc"] += 1; st["tcRs"] += a["Rs"] != b["Rs"]
            st["Rs_nonnested"] += not (a["Rs"] <= b["Rs"])
            if a["R"] != b["R"]:
                st["X"] += 1
                for v in b["R"] - a["R"]: st["ent"] += 1; st["ent_al"] += v in b["Rs"]
                for v in a["R"] - b["R"]: st["lv"] += 1; st["lv_al"] += v not in b["Rs"]
            st["misfit_max"] = max(st["misfit_max"], len(b["R"] ^ b["Rs"]))
        out.append(st)
    return g.n, out

if __name__ == "__main__":
    for p in sys.argv[1:]:
        n, out = scan(p); best = max(out, key=lambda s: (s["X"], s["tc"]))
        print(os.path.basename(p), "n", n, best)
