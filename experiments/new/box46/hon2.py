#!/usr/bin/env python3
"""Box 46 DATA for (b) (docs/new/N5-REC1-box46.md §6): gaps between consecutive W-honest states of a phase. For each gap, fb := fallbacks in
it, FBH := whether its FIRST transition is the fallback; LEV (Xi-level over simple paths of G_tau, levels.level) at both ends. Counts:
gaps, fallback-free gaps with no rise (NORISE_FF, HON step 1 predicts 0), gaps with a fallback (FBGAP) and those of them with no rise
(NORISE_FB), split by FBH. Usage: hon2.py STARTS SEED (--list FILE | --rand C LO HI GSEED) [--nmax N] [--budget B]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
import hon
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def check(g, start, budget, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        a, b = i, j; i = j + 1; n = g.n; tau = rows[a]["t"]
        H = [k for k in range(a, b + 1) if rows[k]["hon"]]
        if len(H) < 2: continue
        frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
        try: lev = {k: L.level(E, g, frame, rows[k]["xi"], (), budget) for k in H}
        except Unknown: inc("UNK"); continue
        for h0, h1 in zip(H, H[1:]):
            inc("gaps"); fb = sum(rows[k]["fb"] for k in range(h0, h1)); nr = lev[h1] <= lev[h0] < n - 1
            if lev[h1] < lev[h0]: inc("MONO_V")
            if not fb:
                if nr: inc("NORISE_FF")
                continue
            tag = "AT_H" if rows[h0]["fb"] else "INSIDE"
            inc("FBGAP_" + tag)
            if nr: inc("NORISE_FB_" + tag)
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 24, 1000000
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    for g in gs:
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st, budget)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())))
