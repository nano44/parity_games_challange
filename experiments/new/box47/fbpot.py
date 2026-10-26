#!/usr/bin/env python3
"""Box 47 DATA: per-vertex levels ell_t(x) := the largest j <= n-1 with Xi_t(x) >= value(r) for every simple G_tau path r from x with <= j edges
to a cycle node of the phase's lambda (so LEV(t) = min_x ell_t(x)). Xi is non-decreasing, so each ell(x) is (PROVED, elementary). At every
in-phase S4c fallback t -> t+1: POT_FLAT = sum_x ell does not rise; EVEN_FLAT = no Even vertex's ell rises; XIFLAT = Xi_{t+1} = Xi_t (R15 (b) Lemma B: a flat switch-all); POT_FLAT_XIUP = Xi rises but no ell does; reports how the Odd-binding fallbacks
(LEV_odd(t) <= LEV(t) < n-1) fare. Usage: fbpot.py STARTS SEED (--list FILE | files) [--nmax N] [--budget B] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from levels import load, step, start_pair, Engine, dual, Unknown
from n5x import readstart
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
VERB = os.environ.get("VERB") == "1"
def ells(E, g, frame, xi, lam, budget):
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for z in frame[v]: pred[z].append(v)
    best = [n] * n; cnt = 0
    for c in [c for c in range(n) if lam[c] == c]:
        rc = E.rank[c]; stack = [(c, 0, 0, 1 << c)]
        while stack:
            x, mask, ln, vis = stack.pop(); cnt += 1
            if cnt > budget: raise Unknown()
            if E.key((c, mask, ln)) > E.key(xi[x]) and ln < best[x]: best[x] = ln
            if ln == n - 1: continue
            for p in pred[x]:
                if vis >> p & 1: continue
                stack.append((p, mask | (E.bit[p] if E.rank[p] > rc else 0), ln + 1, vis | 1 << p))
    return [min(b - 1, n - 1) for b in best]
def run(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        if any(rows[k]["fb"] for k in range(i, j)):
            try: phase(g, E, rows, i, j, budget, nm, start)
            except Unknown: inc("UNK_phases")
        i = j + 1
def phase(g, E, rows, a, b, budget, nm, start):
    n = g.n; lam = rows[a]["lam"]; tau = rows[a]["t"]
    frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
    cache = {}
    def EL(k):
        if k not in cache: cache[k] = ells(E, g, frame, rows[k]["xi"], lam, budget)
        return cache[k]
    for t in range(a, b):
        if not rows[t]["fb"]: continue
        e0, e1 = EL(t), EL(t + 1); inc("fallbacks")
        if any(y < x for x, y in zip(e0, e1)): inc("MONO_V")
        L = min(e0); Lo = min(e0[v] for v in range(n) if g.owner[v] == 1) if any(g.owner[v] == 1 for v in range(n)) else n - 1
        kind = "SAT" if L >= n - 1 else ("NB" if Lo > L else "OB")
        xiflat = list(rows[t]["xi"]) == list(rows[t + 1]["xi"])
        if xiflat: inc("XIFLAT_" + kind)
        if sum(e1) == sum(e0):
            inc("POT_FLAT_" + kind)
            if not xiflat: inc("POT_FLAT_XIUP_" + kind)
            if VERB: print(f"POT_FLAT {kind} {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] fallback {t} ell {e0}", flush=True)
        if not any(e1[v] > e0[v] for v in range(n) if g.owner[v] == 0): inc("EVEN_FLAT_" + kind)
        inc("ALL_" + kind)
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 34, 1000000; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, budget, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
