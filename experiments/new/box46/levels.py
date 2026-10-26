#!/usr/bin/env python3
"""Box 46 DATA (docs/new/N5-REC1-box46.md): the PERMANENT Xi-level of a configuration C inside a phase of N5.
For a phase (lambda_Xi, tau constant) and a configuration C = sigma-bar|Q of one of its epochs, H_C := G with every Odd vertex fixed
to sigma-bar_C (= tau off D_C). LEV_C(k) := the largest j <= n - 1 such that Xi_k(x) >= value(r) for every vertex x and every simple path
r of H_C with <= j edges from x to a cycle node c of lambda (c = lambda(c)); value(r) = (c, P(r), |r|) as in RESULTS R17 Lemma P.
(UAV variant: only paths r that avoid every vertex of D_C.) Xi is non-decreasing along the phase (R15 (a)), so LEV_C is non-decreasing
at every state of the phase, for every C at once.
For consecutive C-epochs E_i, E_{i+1} of a phase (same C), with y_i the last state of E_i and x_{i+1} the first of E_{i+1}, the GAP is the
transitions y_i -> ... -> x_{i+1}. Reports per |D_C| (0, 1): gaps, fallback-free gaps, fallback-free gaps with LEV_C(x_{i+1}) <= LEV_C(y_i)
< n - 1 (NORISE; REC-0' predicts 0 for |D| = 0; NORISE_FB: the same on gaps WITH a fallback, the control), the same for UAV, LEV decreases (MONO_V, must be 0), unknown (path budget hit).
Usage: levels.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
class Unknown(Exception): pass
def level(E, g, frame, xi, avoid, budget):
    """frame[v] = successor list in H_C; xi = valuation vector at the state. Returns LEV (or raises Unknown)."""
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for w in frame[v]: pred[w].append(v)
    cyc = [c for c in range(n) if xi[c][0] == c and c not in avoid]
    best = n  # smallest violating path length
    cnt = [0]
    for c in cyc:
        rc = E.rank[c]
        # reverse DFS: path x -> ... -> c; state (x, mask, length, visited)
        stack = [(c, 0, 0, 1 << c)]
        while stack:
            x, mask, ln, vis = stack.pop(); cnt[0] += 1
            if cnt[0] > budget: raise Unknown()
            if ln >= best: continue
            if E.key((c, mask, ln)) > E.key(xi[x]): best = ln; continue
            if ln == n - 1: continue
            for p in pred[x]:
                if vis >> p & 1 or p in avoid: continue
                stack.append((p, mask | (E.bit[p] if E.rank[p] > rc else 0), ln + 1, vis | 1 << p))
    return min(best - 1, n - 1)
def check(g, start, budget, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), q=tuple(sb[q] for q in Q), sb=tuple(sb), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, E, rows, i, j, Q, budget); i = j + 1
def phase(g, E, rows, a, b, Q, budget):
    inc("phases"); n = g.n; tau = rows[a]["t"]; eps = []; k = a
    while k <= b:
        e = k
        while e + 1 <= b and rows[e + 1]["q"] == rows[k]["q"]: e += 1
        eps.append((k, e)); k = e + 1
    byc = {}
    for (x, y) in eps: byc.setdefault(rows[x]["q"], []).append((x, y))
    for conf, lst in byc.items():
        D = [q for q, w in zip(Q, conf) if w != tau[q]]
        if len(D) > 1 or len(lst) < 2: continue
        d = len(D); sbC = rows[lst[0][0]]["sb"]
        frame = [[sbC[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
        try:
            L = {}
            for (x, y) in lst:
                for z in (x, y):
                    if z not in L: L[z] = (level(E, g, frame, rows[z]["xi"], (), budget), level(E, g, frame, rows[z]["xi"], set(D), budget))
        except Unknown:
            inc(f"UNK{d}"); continue
        seq = [L[z] for (x, y) in lst for z in (x, y)]
        for p, q in zip(seq, seq[1:]):
            if q[0] < p[0] or q[1] < p[1]: inc(f"MONO_V{d}")
        for (x0, y0), (x1, y1) in zip(lst, lst[1:]):
            inc(f"gaps{d}"); fb = sum(rows[k]["fb"] for k in range(y0, x1))
            ly, lx = L[y0], L[x1]
            if fb:
                inc(f"fbgaps{d}")
                if lx[0] <= ly[0] < n - 1: inc(f"NORISE_FB{d}")
                continue
            inc(f"ffgaps{d}")
            if lx[0] <= ly[0] < n - 1: inc(f"NORISE{d}")
            if lx[1] <= ly[1] < n - 1: inc(f"NORISE_UAV{d}")
            mx(f"maxlev{d}", lx[0])
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 64, 300000
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st, budget)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())))
