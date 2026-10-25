#!/usr/bin/env python3
"""Box 42 (2): stress for evcheck/kwfreeze2/nhcheck. (1) --starts: every lib file with a U3/U23 stretch with c_w ≻ c_θ, K random start
pairs each; (2) --climb: mutate edges / priorities of such games (keeping one Odd choice vertex), fitness = events + W-flat kind
changes in qualifying stretches; every candidate is checked by evcheck.go4 and kwfreeze2.go2.
Usage: evstress.py --starts FILE K seed | --climb FILE iters seed"""
import sys, os, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from evcheck import go4
from kwfreeze2 import go2
from kwfreeze import *

def qualifies(g):
    acc = {}; go4(g, acc, "q"); return acc.get("stretches_even", 0) + acc.get("stretches_odd", 0), acc

def rstart(g, rng):
    return ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})

def mutate(g, rng):
    h = copy.deepcopy(g); v = rng.randrange(h.n); r = rng.random()
    if r < 0.4 and h.owner[v] == 0:
        u = rng.randrange(h.n)
        if u not in h.succ[v]: h.succ[v] = sorted(h.succ[v] + [u])
    elif r < 0.7 and h.owner[v] == 0 and len(h.succ[v]) > 1:
        h.succ[v] = sorted(h.succ[v]); h.succ[v].remove(rng.choice(h.succ[v]))
    else:
        h.prio[v] = rng.randrange(0, 2 * h.n)
    return h

if __name__ == "__main__":
    a = sys.argv[1:]; root = os.path.join(HERE, "..", "..", ".."); acc4, acc2 = {}, {}
    files = [l.strip() for l in open(a[1])]
    games = []
    for f in files:
        p = f if os.path.exists(f) else os.path.join(root, f)
        try: g = load(p)
        except Exception: continue
        if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: continue
        q, _ = qualifies(g)
        if q: games.append((f, g))
    print("qualifying files:", len(games))
    if a[0] == "--starts":
        K, seed = int(a[2]), int(a[3]); rng = random.Random(seed)
        for f, g in games:
            for t in range(K):
                st = rstart(g, rng); go4(g, acc4, (f, t), st); go2(g, acc2, (f, t), st)
    else:
        iters, seed = int(a[2]), int(a[3]); rng = random.Random(seed); best = 0
        for f, g0 in games:
            cur = g0; _, ac = qualifies(cur); fit = ac.get("sum_ev", 0)
            for it in range(iters):
                h = mutate(cur, rng)
                try:
                    if sum(1 for v in range(h.n) if h.owner[v] == 1 and len(h.succ[v]) > 1) != 1 or any(not s for s in h.succ): continue
                    acc_h = {}; go4(h, acc_h, (f, it)); go2(h, acc2, (f, it))
                except Exception as e:
                    acc4["err"] = acc4.get("err", 0) + 1; continue
                for kk in ("DIR", "KC", "CB", "CW", "ES"):
                    if kk in acc_h: acc4[kk] = acc4.get(kk, 0) + acc_h[kk]; acc4.setdefault("ex_" + kk, acc_h.get("ex_" + kk))
                fh = acc_h.get("sum_ev", 0)
                if fh >= fit: cur, fit = h, fh
                acc4["cand"] = acc4.get("cand", 0) + 1
            best = max(best, fit)
        acc4["best_events"] = best
    for name, acc in (("evcheck", acc4), ("kwfreeze2", acc2)):
        viol = {k: v for k, v in acc.items() if k in ("DIR", "KC", "CB", "CW", "ES", "CS", "CS_cyc", "FZW", "FZX", "KW", "NX")}
        print(name, "violations:", viol if viol else 0, {k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
        for k, v in acc.items():
            if k.startswith("ex_") and v: print(" ", k, v)
