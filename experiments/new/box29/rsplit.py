#!/usr/bin/env python3
"""Box 29: split the O' transitions (OTHER-touching, non-crossing, value-changing) into those that change a value on F (charged to
Lemma F1-ext: ≤ |F| − 1 per crossing-free interval) and R-ONLY ones (values change on R ∪ {o} only). Per phase: max R-only O'.
Usage: rsplit.py game.pg [start] | rsplit.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def rsplit(g, start=None):
    rows, out = phases(g, start); o = odd_choice(g); res = []
    for st in out:
        x, y = st["phase"]; fch = ronly = 0
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if not (a["other"] or b["other"]) or a["R"] != b["R"]: continue
            ch = [v for v in range(g.n) if a["Xk"][v] != b["Xk"][v] or a["Wk"][v] != b["Wk"][v]]
            if not ch: continue
            if any(v not in a["R"] and v != o for v in ch): fch += 1
            else: ronly += 1
        res.append(dict(phase=(x, y), Fchanging=fch, Ronly=ronly, R=len(rows[x]["R"])))
    return res

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] != "--rand":
        g = load(a[0])
        for r in rsplit(g, readstart(a[1]) if len(a) > 1 else None):
            if r["Fchanging"] or r["Ronly"]: print(os.path.basename(a[0]), "n", g.n, r)
        sys.exit()
    RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); best = (0, None); tot = [0, 0]
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        for r in rsplit(g, start):
            tot[0] += r["Fchanging"]; tot[1] += r["Ronly"]
            if r["Ronly"] > best[0]: best = (r["Ronly"], g.n)
    print("F-changing O'", tot[0], "R-only O'", tot[1], "max R-only per phase", best)
