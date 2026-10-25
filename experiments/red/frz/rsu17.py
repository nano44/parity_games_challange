#!/usr/bin/env python3
"""Box 41: random 𝒞^1O games; per |U|: max over θ-runs of f − (|U| − 1) (pf) and over phases of g − (|U| − 2) (hat), plus the max
number of in-θ-run fallbacks f. Saves the first game attaining each new per-|U| maximum. Usage: rsu17.py seed secs nmin nmax OUT"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pg, shrink17 as S
from soclimb import dump
seed, secs, nmin, nmax, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); t0 = time.time(); PF = {}; HAT = {}; cnt = 0
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax)
    prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3, 3, 4))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 3)))))
    G = [prio, owner, succ]
    try:
        g = pg.Game(*G)
        if len(sox.oddchoice(g)) != 1: continue
        X, FB, o = S.runs(g)
    except Exception: continue
    cnt += 1; N = len(X); a = 0
    while a < N:
        b = a
        while b + 1 < N and X[b + 1][0] == X[a][0] and X[b + 1][2] == X[a][2]: b += 1
        ct = X[a][1][0]; u = sum(1 for z in X[a][0] if z == ct); gph = sum(FB[k] for k in range(a, b))
        if u not in HAT or gph - (u - 2) > HAT[u]:
            HAT[u] = gph - (u - 2)
            if u >= 3 and HAT[u] >= -1: dump(G, f"{out}_hat_U{u}_e{HAT[u]}.pg")
        s0 = a
        while s0 <= b:
            e0 = s0
            while e0 + 1 <= b and X[e0 + 1][1] == X[s0][1]: e0 += 1
            f = sum(FB[k] for k in range(s0, e0))
            if u not in PF or f - (u - 1) > PF[u]:
                PF[u] = f - (u - 1)
                if u >= 2 and PF[u] >= -1: dump(G, f"{out}_pf_U{u}_e{PF[u]}.pg")
            s0 = e0 + 1
        a = b + 1
print("games", cnt, flush=True)
print("PF max excess by |U|", sorted(PF.items())[:14], flush=True)
print("HAT max excess by |U|", sorted(HAT.items())[:14], flush=True)
