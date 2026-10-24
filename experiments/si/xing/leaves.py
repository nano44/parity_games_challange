#!/usr/bin/env python3
"""L-SI box 4: leave transitions. Per joint λ-phase: X, L = transitions with a leave (R_k ⊄ R_{k+1}), L_fb (of them at fallbacks),
L_ar (arena), longest entry-only run between leave transitions, and the check X ≤ L + (L+1)(n−1) (Lemma LV).
Also, at each leave transition: state kinds (E: Ξ = W at k; T: θ ◁ w with (h); N: (h) fails), θ/w change flags.
Usage: leaves.py game.pg ...  |  leaves.py --rand N lo hi seed [--randstart]"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def kindstate(r):
    if r["Xk"] == r["Wk"]: return "E"
    return "T" if all(r["h"]) else "N"

def per_phase(g, start=None):
    rows, ph = profile(g, start); assert_run(g, rows, start); o = annotate(g, rows); out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), T=y - x, X=0, L=0, L_fb=0, L_ar=0, Eruns=0, kinds={}, ent_fb=0, noact=0)
        run = 0
        for k in range(x, y):
            A, B = rows[k]["R"], rows[k + 1]["R"]
            if A == B: continue
            st["X"] += 1; S, act, pas = classify(g, rows, k, o)
            st["noact"] += not act
            if B - A and rows[k]["fb"]: st["ent_fb"] += 1
            if A - B:
                st["L"] += 1; st["L_fb" if rows[k]["fb"] else "L_ar"] += 1
                kk = kindstate(rows[k]) + ("θ" if rows[k]["th"] != rows[k + 1]["th"] else "") + ("w" if rows[k]["w"] != rows[k + 1]["w"] else "")
                st["kinds"][kk] = st["kinds"].get(kk, 0) + 1; run = 0
            else:
                run += 1; st["Eruns"] = max(st["Eruns"], run)
        assert st["X"] <= st["L"] + (st["L"] + 1) * (g.n - 1)
        out.append(st)
    return out

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] != "--rand":
        for p in a:
            g = load(p); out = per_phase(g); best = max(out, key=lambda s: (s["X"], s["T"]))
            print(f"{os.path.basename(p):22s} n {g.n:3d}", {k: best[k] for k in ("T", "X", "L", "L_fb", "L_ar", "Eruns", "ent_fb", "noact", "kinds")})
        sys.exit()
    sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
    from common import rand_c1o
    RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
    tot = dict(games=0, phases=0, X=0, L=0, L_fb=0, L_ar=0, ent_fb=0, noact=0); mx = dict(X=0, L=0); kinds = {}
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        tot["games"] += 1
        for st in per_phase(g, start):
            tot["phases"] += 1
            for k in ("X", "L", "L_fb", "L_ar", "ent_fb", "noact"): tot[k] += st[k]
            for k in ("X", "L"): mx[k] = max(mx[k], st[k])
            for kk, c in st["kinds"].items(): kinds[kk] = kinds.get(kk, 0) + c
    print("totals", tot, "max per phase", mx, "leave-transition state kinds", kinds)
