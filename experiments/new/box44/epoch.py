#!/usr/bin/env python3
"""Box 44 DATA for Lemma EPOCH (docs/new/N5-FBF-box44.md §9). Phase := (lambda_Xi, tau) constant; an EPOCH := maximal run of the phase
with sigma-bar restricted to Q (Odd choice vertices) constant. Per phase: N_ep (epochs), REP (epochs whose sigma-bar|Q configuration
already occurred earlier in the same phase: a repeat), f (in-phase fallbacks). Checks:
  EPF   f <= 1 + n * N_ep                                                        (Lemma EPOCH (c); viol. EPF_V)
  FRZ   in an epoch, after its (n-1)-th fallback, Xi is constant on the epoch except possibly at its last transition, and the
        epoch's remaining transitions number <= 4n(n-1) + 1                       (Lemma EPOCH (a), (b); viol. FRZ_V)
Records max N_ep, max REP, max consecutive S4a run (no fallback) inside an epoch (S4AMAX), max distinct Xi(z) per vertex per phase.
Usage: epoch.py --list FILE | --rand C LO HI SEED | files"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual
C = dict(phases=0, NEPMAX=0, NEPMAX_n=0, REPMAX=0, REPPH=0, EPF_V=0, FRZ_n=0, FRZ_V=0, S4AMAX=0, LVMAX=0)
def check(g, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q), vs, r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        phase(g, rows, i, j); i = j + 1
def phase(g, rows, a, b):
    n = g.n; C["phases"] += 1
    eps = []; k = a
    while k <= b:
        e = k
        while e + 1 <= b and rows[e + 1][2] == rows[k][2]: e += 1
        eps.append((k, e)); k = e + 1
    seen, rep = set(), 0
    for (x, y) in eps:
        if rows[x][2] in seen: rep += 1
        seen.add(rows[x][2])
    if len(eps) > C["NEPMAX"]: C["NEPMAX"], C["NEPMAX_n"] = len(eps), n
    C["REPMAX"] = max(C["REPMAX"], rep); C["REPPH"] += rep > 0
    f = sum(1 for k in range(a, b) if rows[k][4])
    if f > 1 + n * len(eps): C["EPF_V"] += 1
    for (x, y) in eps:
        run = 0
        for k in range(x, y):
            run = 0 if rows[k][4] else run + 1; C["S4AMAX"] = max(C["S4AMAX"], run)
        fbs = [k for k in range(x, min(y + 1, b)) if rows[k][4]]
        if len(fbs) >= n - 1 and n >= 2:
            st = fbs[n - 2] + 1
            if st <= y:
                C["FRZ_n"] += 1
                last = y if y < b else y            # transition y -> y+1 leaves the epoch (or the phase)
                bad = any(rows[k][3] != rows[k + 1][3] for k in range(st, y))   # transitions with both ends in the epoch
                if bad or (y - st) > 4 * n * (n - 1) + 1: C["FRZ_V"] += 1
    for z in range(n):
        C["LVMAX"] = max(C["LVMAX"], len({rows[k][3][z] for k in range(a, b + 1)}))
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs: check(g)
    print(f"runs {len(gs)}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
