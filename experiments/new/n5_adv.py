#!/usr/bin/env python3
"""Box 3: first killer attempt against N5 (adversarial hill climb). Random game with n vertices, max out-degree 3, priorities
0..n-1 (distinct); mutations: change one edge target, swap two priorities, flip an owner. Fitness = N5 iterations (+ 0.5 per
fallback: the fallback trigger is the place where N5 hands control to classical switch-all). Sideways moves allowed.
Every improved best is checked (Zielonka + verify.py) and written to DIR/best_n<n>_seed<s>.pg.
Usage: n5_adv.py n steps seed DIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
rng = random.Random(seed)
prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
def fit(pr, ow, sc):
    g = pg.Game(pr, ow, sc); it, fb, win, ws, _ = n5.run(g, cap=5000); return it + 0.5 * fb, it, fb, g, win, ws
best = fit(prio, owner, succ); cur = (prio, owner, succ)
print("start", best[1], best[2], flush=True)
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
    f = fit(pr, ow, sc)
    if f[0] >= best[0]:
        if f[0] > best[0]:
            g, win, ws = f[3], f[4], f[5]
            ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
            print(f"step {s} iterations {f[1]} fallbacks {f[2]} check {'OK' if ok else 'FAIL'}", flush=True)
            open(os.path.join(d, f"best_n{n}_seed{seed}.pg"), "w").write(pg.dumps(g))
        best, cur = f, (pr, ow, sc)
print("best", best[1], best[2])
