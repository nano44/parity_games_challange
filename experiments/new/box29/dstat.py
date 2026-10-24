#!/usr/bin/env python3
"""Box 29: at OTHER states (and on O' transitions), the disagreement set D := {v : Ξ(v) ≠ W(v)}, whether D = {o}, whether θ's / w's
cycle node is o itself. Usage: dstat.py game.pg [start] | dstat.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def tally(g, start, cnt):
    rows, out = phases(g, start); o = odd_choice(g); E = Engine(g)
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if not (a["other"] or b["other"]) or a["R"] != b["R"]: continue
        if a["Xk"] == b["Xk"] and a["Wk"] == b["Wk"]: continue
        for r in (a, b):
            if not r["other"]: continue
            Xi, sb = E.evaluate(tuple(r["s"])); _, W = wvals(g, r["s"], r["t"])
            D = [v for v in range(g.n) if r["Xk"][v] != r["Wk"][v]]
            key = (clause(r["h"]), "D={o}" if D == [o] else f"|D|={len(D)}" if len(D) <= 2 else "|D|>2",
                   "cθ=o" if Xi[o][0] == o else "cθ≠o", "cw=o" if W[o][0] == o else "cw≠o")
            cnt[key] = cnt.get(key, 0) + 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = {}
    if a[0] != "--rand":
        g = load(a[0]); tally(g, readstart(a[1]) if len(a) > 1 else None, cnt)
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            tally(g, start, cnt)
    for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]): print(v, k)
