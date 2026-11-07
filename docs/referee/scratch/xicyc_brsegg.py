"""REFEREE successor 26: BR-SEG-G (a) random search with own engine. Howard (keep current on ties, else larger index), Odd's reply by
local improvement from the previous reply (sticky), brute-force cross-check of the values on every state when the game is small.
Counts: runs, steps, H0-failing steps (no switched Even x with Lambda != x before and after), p-runs > n_E among stretches whose steps
all satisfy H0, DOM failures (Omega_(t+1)(x) < ext(x, Omega_t(y)) for some Even x not its own cycle node at t+1, successor y).
Usage: xicyc_brsegg.py COUNT SEED n [brute]"""
import sys, os, random; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
cnt, seed, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); BR = len(sys.argv) > 4; rng = random.Random(seed)
tot = dict(runs=0, steps=0, h0fail=0, viol=0, domfail=0, brute_bad=0, maxratio=0.0)
for i in range(cnt):
    pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    su = [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)]
    E = VJ(pr, ow, su); nE = sum(1 for v in range(n) if ow[v] == 0) or 1
    s = [su[v][0] if ow[v] == 0 else None for v in range(n)]; st, val = E.best_reply(s)
    if BR and any(E.cmp(a, b) for a, b in zip(E.brute(s), val)): tot["brute_bad"] += 1
    run = 0; tot["runs"] += 1
    for _ in range(10000):
        ns = list(s)
        for v in range(n):
            if ow[v]: continue
            b = s[v]
            for u in su[v]:
                if E.cmp(val[u], val[b]) > 0 or (E.cmp(val[u], val[b]) == 0 and b != s[v] and u > b): b = u
            ns[v] = b
        if ns == s: break
        nst, nval = E.best_reply(ns, st)
        if BR and any(E.cmp(a, b) for a, b in zip(E.brute(ns), nval)): tot["brute_bad"] += 1
        h0 = any(ns[v] != s[v] and val[v][0] != v and nval[v][0] != v for v in range(n))
        for v in range(n):
            if ow[v] == 0 and nval[v][0] != v and any(E.cmp(nval[v], E.ext(v, val[u])) < 0 for u in su[v]): tot["domfail"] += 1; break
        C = any(nval[v][0] != val[v][0] for v in range(n)); R = any(nst[v] != st[v] for v in range(n) if ow[v] == 1)
        tot["steps"] += 1; tot["h0fail"] += not h0
        if C or R or not h0: run = 0
        else:
            run += 1
            if run > nE: tot["viol"] += 1
            tot["maxratio"] = max(tot["maxratio"], run / nE)
        s, st, val = ns, nst, nval
print(f"BR-SEG-G random count {cnt} seed {seed} n {n} prio 0..{2*n-1} brute {BR}:", tot)
