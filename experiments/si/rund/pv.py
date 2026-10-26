#!/usr/bin/env python3
"""L-SI box 17: DATA for docs/si/N5-RUND-box17.md §9. Per maximal fallback-free in-phase run: its transitions T_S, and the largest number
of Xi-changes (resp. W-changes) of ONE vertex on it (cx, cw). Reports the max of cx, cw over all runs, the run with the largest T_S, and
the histogram of cx. If cx stays small while T_S grows, the length of the run comes from serialisation, not from repeated changes.
Usage: pv.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START]  (NMAX, RS env as gap.py)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
C = Counter(); HX = Counter(); BEST = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, W=[wval(E, wn, v) for v in range(g.n)], fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i:
            T = j - i
            cx = max(sum(rows[k]["vs"][v] != rows[k + 1]["vs"][v] for k in range(i, j)) for v in range(g.n))
            cw = max(sum(rows[k]["W"][v] != rows[k + 1]["W"][v] for k in range(i, j)) for v in range(g.n))
            C["runs"] += 1; C["max_cx"] = max(C["max_cx"], cx); C["max_cw"] = max(C["max_cw"], cw); HX[cx] += 1
            if T > C["max_T"]: C["max_T"] = T; BEST.append((name, i, j, g.n, "T", T, "cx", cx, "cw", cw))
            if cx >= C["max_cx"]: BEST.append((name, i, j, g.n, "T", T, "cx", cx, "cw", cw))
        i = j + 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items()))); print("HIST cx", sorted(HX.items()))
    for x in BEST[-8:]: print("RUN", x)

if __name__ == "__main__":
    main()
