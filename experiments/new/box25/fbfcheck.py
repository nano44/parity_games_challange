#!/usr/bin/env python3
"""Box 27, Lemma FBF check: after an Even fallback at a throttled (h)-state, for the rest of the same (τ, joint-λ, θ, w)-stretch with
(h): no vertex enters R, and no vertex staying in R changes its route (path to o). Usage: fbfcheck.py game.pg [start] | --random N lo hi seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from reentry import path
from collections import Counter
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []; k = 0
    while k < 400:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(key=((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])), ok=h and E.key(Xi[o]) < E.key(W[o]),
                         R=Rset(g, s, t, o), s=tuple(s), t=tuple(t), fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4] and list(r[1]) == list(t); s, t = list(r[0]), list(r[1]); k += 1
    armed = False
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        if not (a["ok"] and b["ok"] and a["key"] == b["key"]): armed = False; continue
        if armed:
            cnt["checked_transitions"] += 1
            if b["R"] - a["R"]: cnt["ENTRY_AFTER_FB"] += 1
            for x in a["R"] & b["R"]:
                if x != o and path(g, a["s"], a["t"], x, o) != path(g, b["s"], b["t"], x, o): cnt["ROUTE_CHANGE_AFTER_FB"] += 1
        if a["fb"]: armed = True; cnt["throttled_fallbacks"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.1)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(cnt))
    else:
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], dict(cnt))
