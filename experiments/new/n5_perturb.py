#!/usr/bin/env python3
"""Box 4 killer attempt 8: perturbation climb from a GIVEN game (e.g. Friedmann's switchallexp / switchbestexp): mutations as
n5_adv.py (edge target, priority swap, owner flip); fitness = N5 iterations (n5.run, unmodified) + 0.5 per fallback. Every improved
best is checked (zielonka.py + verify.py) and saved. Usage: n5_perturb.py game.pg steps seed OUT.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
g0 = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); steps, seed, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed); n = g0.n
def fit(pr, ow, sc):
    g = pg.Game(pr, ow, sc); it, fb, win, ws, _ = n5.run(g, cap=20000); return it + 0.5 * fb, it, fb, g, win, ws
cur = (list(g0.prio), list(g0.owner), [list(s) for s in g0.succ]); best = fit(*cur); print("start", best[1], best[2], flush=True)
for s in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; k = rng.random()
    if k < 0.6:
        v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
        if rng.random() < 0.3 and len(sc[v]) < 4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif k < 0.9:
        a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else:
        v = rng.randrange(n); ow[v] = 1 - ow[v]
    f = fit(pr, ow, sc)
    if f[0] >= best[0]:
        if f[0] > best[0]:
            ok = f[4] == zielonka.solve(f[3]) and not verify.check(f[3], f[4], list(f[5]))
            print(f"step {s} iterations {f[1]} fallbacks {f[2]} check {'OK' if ok else 'FAIL'}", flush=True)
            open(out, "w").write(pg.dumps(f[3]))
        best, cur = f, (pr, ow, sc)
print("best", best[1], best[2])
