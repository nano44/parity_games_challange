#!/usr/bin/env python3
"""Box 4 killer attempt 3: hill climb for LOCKS. Same mutations as n5_adv.py; fitness = (longest run of CONSECUTIVE fallback
iterations, fallbacks, iterations) of N5 from the best-reward start. Step = n5_lock.step (n5.py's loop; every improved best is
re-run through n5.run UNMODIFIED and the counts asserted equal) and checked (Zielonka + verify.py).
Usage: n5_adv2.py n steps seed DIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
rng = random.Random(seed)
prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
def fit(pr, ow, sc):
    g = pg.Game(pr, ow, sc); E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best")); it = fb = run = cur = 0
    while it < 5000:
        r = step(g, E, Ed, sigma, tau)
        if r is None: break
        sigma, tau, f, _, _ = r; it += 1; fb += f; cur = cur + 1 if f else 0; run = max(run, cur)
    return (run, fb, it), g
best, _ = fit(prio, owner, succ); cur = (prio, owner, succ)
print("start", best, flush=True)
for s in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]
    k = rng.random()
    if k < 0.6:
        v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
        if rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif k < 0.9:
        a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else:
        v = rng.randrange(n); ow[v] = 1 - ow[v]
    f, g = fit(pr, ow, sc)
    if f >= best:
        if f > best:
            it, fb, win, ws, _ = n5.run(g, cap=5000); assert (it, fb) == (f[2], f[1])
            ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
            print(f"step {s} run {f[0]} fallbacks {f[1]} iterations {f[2]} check {'OK' if ok else 'FAIL'}", flush=True)
            open(os.path.join(d, f"lock_n{n}_seed{seed}.pg"), "w").write(pg.dumps(g))
        best, cur = f, (pr, ow, sc)
print("best", best)
