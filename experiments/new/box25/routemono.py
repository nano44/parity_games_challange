#!/usr/bin/env python3
"""Box 26, (RM): inside a (τ, joint-λ)-phase, for x ∈ R_k ∩ R_{k+1}, is x's route value (path to o, compared with one terminal
T = W_{k+1}(o), Lemma G (c)) non-decreasing? Counts decreases at arena / fallback steps, split by (h) at both states.
Also counts strict increases per vertex inside θ-constant intervals (max). Usage: routemono.py game.pg [start] | --random N lo hi seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from reentry import path
from collections import Counter
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(s=tuple(s), t=tuple(t), lam=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), th=E.key(Xi[o]), Wo=W[o], R=Rset(g, s, t, o), h=h, fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; rows[-1]["fb"] = fb; s, t = ns, nt
    inc = Counter(); th0 = None
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["lam"] != b["lam"]: inc = Counter(); continue
        if a["th"] != b["th"]: inc = Counter()
        for x in range(g.n):
            if g.owner[x] != 0 or x == o or x not in a["R"] or x not in b["R"]: continue
            pa, pb = path(g, a["s"], a["t"], x, o), path(g, b["s"], b["t"], x, o)
            if pa is None or pb is None: continue
            def val(p):
                v = b["Wo"]
                for u in reversed(p): v = E.extend(u, v)
                return E.key(v)
            va, vb = val(pa), val(pb); hh = "h" if (a["h"] and b["h"]) else "noh"; kind = "fb" if a["fb"] else "arena"
            if vb < va: cnt[f"DEC_{kind}_{hh}"] += 1
            elif vb > va:
                cnt[f"inc_{kind}_{hh}"] += 1; inc[x] += 1; cnt["max_inc_per_vertex_theta_interval"] = max(cnt["max_inc_per_vertex_theta_interval"], inc[x])
            else: cnt["eq"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(sorted(cnt.items())))
    else:
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], g.n, dict(sorted(cnt.items())))
