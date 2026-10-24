#!/usr/bin/env python3
"""L-SI box 5: check Lemma GAP (docs/si/P-N5-Z-box5.md §6): at every S4c fallback inside a phase with (h) at k, every switched edge
y -> z with y ∈ R_k, z ∈ F_k has Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y) (Engine keys). Also re-checks NOFE (tail on o's W-play).
Usage: gapcheck.py game.pg ...  |  gapcheck.py --rand N lo hi seed [--randstart]"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def oplay(g, s, t, o):
    nxt = lambda v: s[v] if g.owner[v] == 0 else t[v]
    p = [o]; seen = {o}
    while True:
        u = nxt(p[-1])
        if u in seen: return set(p)
        p.append(u); seen.add(u)

def check(g, start=None, strict=True):
    rows, ph = profile(g, start)
    if strict: assert_run(g, rows, start)
    o = annotate(g, rows); E = Engine(g); c = dict(gap=0, gapv=0, nofe=0, nofev=0)
    for (x, y) in ph:
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if not a["fb"]: continue
            Xi, _ = E.evaluate(tuple(a["s"])); _, W = wvals(g, a["s"], a["t"]); P = oplay(g, a["s"], a["t"], o)
            for v in range(g.n):
                if g.owner[v] != 0 or a["s"][v] == b["s"][v]: continue
                z = b["s"][v]; sv = a["s"][v]
                if v in a["R"] and z not in a["R"] and z != o and all(a["h"]):
                    c["gap"] += 1; c["gapv"] += not (E.key(Xi[sv]) < E.key(Xi[z]) <= E.key(W[sv]))
                if v not in a["R"] and (z in a["R"] or z == o):
                    c["nofe"] += 1; c["nofev"] += v not in P
    return c

if __name__ == "__main__":
    a = sys.argv[1:]; tot = dict(gap=0, gapv=0, nofe=0, nofev=0)
    if a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25")); from common import rand_c1o
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            for k, v in check(g, st, strict=False).items(): tot[k] += v
    else:
        for p in a:
            for k, v in check(load(p)).items(): tot[k] += v
    print(tot)
