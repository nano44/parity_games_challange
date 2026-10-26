#!/usr/bin/env python3
"""Box 45 DATA for Lemma REC-0 (docs/new/N5-NEP-box45.md §5): per phase of N5, N0 := epochs with D_E = empty (sigma-bar|Q = tau|Q),
f := in-phase fallbacks; checks N0 <= (f + 1)(n + 1) + 4n(n - 1) + 1 (R0_V). Also: N0PRE := D=empty epochs whose last transition is an
S4a step from an all-unsplit state into an all-unsplit state (the steps REC-0 charges n - 1 per fallback-free run), max over runs (RUNMAX),
and the max of N0 and of N0 / (f + 1). Usage: rec0.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = dict(runs=0, phases=0, R0_V=0, N0MAX=0, N0MAX_n=0, N0_F=0.0, RUNMAX=0, FMAX=0)
def wvals(g, s, t):
    succ = [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    return Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(s))[0]
def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; C["runs"] += 1
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = wvals(g, s, t)
        lam = tuple(x[0] for x in vs); unsplit = all(w[v][0] == lam[v] for v in range(g.n))
        rows.append(dict(lam=lam, t=tuple(t), q=tuple(sb[q] for q in Q), d0=all(sb[q] == t[q] for q in Q), un=unsplit, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, rows, i, j); i = j + 1
def phase(g, rows, a, b):
    C["phases"] += 1; n = g.n
    f = sum(rows[k]["fb"] for k in range(a, b)); C["FMAX"] = max(C["FMAX"], f)
    eps = []; k = a
    while k <= b:
        e = k
        while e + 1 <= b and rows[e + 1]["q"] == rows[k]["q"]: e += 1
        eps.append((k, e)); k = e + 1
    d0 = [(x, y) for (x, y) in eps if rows[x]["d0"]]; N0 = len(d0)
    if N0 > (f + 1) * (n + 1) + 4 * n * (n - 1) + 1: C["R0_V"] += 1
    if N0 > C["N0MAX"]: C["N0MAX"], C["N0MAX_n"] = N0, n
    C["N0_F"] = max(C["N0_F"], round(N0 / (f + 1), 2))
    run = 0
    for (x, y) in d0:
        if y < b and not rows[y]["fb"] and rows[y]["un"] and rows[y + 1]["un"]: run += 1
        if y < b and rows[y]["fb"]: run = 0
        C["RUNMAX"] = max(C["RUNMAX"], run)
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: pass
    print(", ".join(f"{k} {v}" for k, v in C.items()))
