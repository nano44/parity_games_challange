#!/usr/bin/env python3
"""Box 43, route (3) data: the disagreement set D_k := {Odd u : sigma-bar_k(u) != tau_k(u)} (sigma-bar = Odd's optimal reply to
sigma_k, SPEC S1). On C^1O, D_k is a subset of {o}. Per run: max |D_k|, max number of transitions inside one phase ((lambda, tau)
constant) at which D_k changes ("D-changes"), and the same for its R-set R_D (vertices whose (sigma, tau)-play meets D_k). Class tag
kE/kO = numbers of Even/Odd choice vertices. DATA.
Usage: dset.py --list FILE | --rand COUNT NLO NHI SEED [--frontier] | files..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual

def meets(g, s, t, D):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; R = set()
    for v in range(g.n):
        x, seen = v, set()
        while x not in seen:
            if x in D: R.add(v); break
            seen.add(x); x = nxt[x]
    return frozenset(R)

def prof(g, st=None, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s))
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        rows.append((tuple(x[0] for x in vs), tuple(t), D, meets(g, s, t, D)))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    mD = max(len(r[2]) for r in rows); dc = rc = cd = cr = 0
    for a, b in zip(rows, rows[1:]):
        if (a[0], a[1]) != (b[0], b[1]): cd = cr = 0; continue
        cd += a[2] != b[2]; cr += a[3] != b[3]; dc = max(dc, cd); rc = max(rc, cr)
    return dict(n=g.n, it=len(rows) - 1, maxD=mD, Dch=dc, RDch=rc)

def cls(g):
    return (sum(1 for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) > 1), sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1))

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    if "--frontier" in a: gs = [g for g in gs if min(cls(g)) >= 2]
    best = {}
    for g in gs:
        p = prof(g); c = cls(g); key = "1O" if c[1] == 1 else ("1E" if c[0] <= 1 else "frontier")
        b = best.setdefault(key, dict(runs=0, maxD=0, Dch=0, RDch=0, it=0))
        b["runs"] += 1
        for k in ("maxD", "Dch", "RDch", "it"): b[k] = max(b[k], p[k])
    for k, v in best.items(): print(k, v)
