#!/usr/bin/env python3
"""Box 46 DATA (CONJECTURE FB-WLEV, docs/new/N5-REC1-box46.md §6): at every in-phase S4c fallback k -> k+1, does the W-level not drop?
WLEV(k) := the largest j <= n - 1 with W_k(x) >= value(r) for every x and every simple path r of G_tau with <= j edges to a cycle node c
of lambda (the PHASE's Xi cycle-node map, not W's). Counts fallbacks, FBW_V (WLEV(k+1) < WLEV(k)), W pointwise drops (WDROP).
Usage: fbwlev.py STARTS SEED (--list FILE | --rand C LO HI GSEED) [--nmax N] [--budget B]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L, hon
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
C = {}; FIRST = []
def inc(k, v=1): C[k] = C.get(k, 0) + v
def wlev(E, g, frame, w, lam, budget):
    # level() takes cycle nodes from xi[c][0] == c; feed it W with lambda's cycle nodes marked: use a copy where cycle nodes are lam's
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for z in frame[v]: pred[z].append(v)
    best = n; cnt = 0
    for c in [c for c in range(n) if lam[c] == c]:
        rc = E.rank[c]; stack = [(c, 0, 0, 1 << c)]
        while stack:
            x, mask, ln, vis = stack.pop(); cnt += 1
            if cnt > budget: raise Unknown()
            if ln >= best: continue
            if E.key((c, mask, ln)) > E.key(w[x]): best = ln; continue
            if ln == n - 1: continue
            for p in pred[x]:
                if vis >> p & 1: continue
                stack.append((p, mask | (E.bit[p] if E.rank[p] > rc else 0), ln + 1, vis | 1 << p))
    return min(best - 1, n - 1)
def check(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), w=w, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if not a["fb"] or (a["lam"], a["t"]) != (b["lam"], b["t"]): continue
        frame = [[a["t"][v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
        try: l0, l1 = wlev(E, g, frame, a["w"], a["lam"], budget), wlev(E, g, frame, b["w"], a["lam"], budget)
        except Unknown: inc("UNK"); continue
        inc("fallbacks"); inc("fb_at_honest" if a["hon"] else "fb_at_nothonest")
        if any(E.key(x) < E.key(y) for x, y in zip(b["w"], a["w"])): inc("WDROP")
        if l1 < l0:
            inc("FBW_V_" + ("hon" if a["hon"] else "nothon"))
            if not FIRST: FIRST.append((nm, start is not None, k, l0, l1))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 24, 1000000
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    for nm, g in gs:
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st, budget, nm)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())), "FIRST", FIRST)
