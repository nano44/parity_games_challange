#!/usr/bin/env python3
"""Box 17 model check: N5 (n5b SPEC) reads priorities only through the (Omega, id)-rank and parity. For random games with arbitrary
(repeated, unordered) priorities in 0..n, compare the trajectory and box17.analyse from random start pairs against the game whose
priorities are replaced by the canonical distinct values of the same (Omega, id)-rank and parity. Usage: privar.py SEED COUNT NMAX"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import box17 as B, pg
seed, cnt, nmax = map(int, sys.argv[1:4]); rnd = random.Random(seed); bad = 0; tot = 0
for k in range(cnt):
    n = rnd.randint(2, nmax); own = [rnd.randint(0, 1) for _ in range(n)]; pr = [rnd.randint(0, n) for _ in range(n)]
    succ = [sorted(rnd.sample(range(n), rnd.randint(1, min(n, 3)))) for _ in range(n)]
    order = sorted(range(n), key=lambda v: (pr[v], v)); cp = []; p = -1
    for v in order:
        p += 1
        if p % 2 != pr[v] % 2: p += 1
        cp.append(p)
    pr2 = [None] * n
    for r, v in enumerate(order): pr2[v] = cp[r]
    g1, g2 = pg.Game(pr, own, succ), pg.Game(pr2, own, succ)
    st = (tuple(rnd.choice(succ[v]) if own[v] == 0 else -1 for v in range(n)), tuple(rnd.choice(succ[v]) if own[v] == 1 else -1 for v in range(n)))
    for s in (st, None):
        e1, e2 = B.Eng(g1), B.Eng(g2)
        R1 = B.trajectory(e1, s or e1.start()); R2 = B.trajectory(e2, s or e2.start()); tot += 1
        z1 = [(r["s"], r["t"], r["fb"], r["sb"], r["key"]) for r in R1]; z2 = [(r["s"], r["t"], r["fb"], r["sb"], r["key"]) for r in R2]
        if z1 != z2 or B.analyse(e1, R1) != B.analyse(e2, R2):
            bad += 1; print("DIFF", pr, own, succ, s)
print(f"PRIVAR runs {tot} differences {bad}")
