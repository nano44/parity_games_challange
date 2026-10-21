#!/usr/bin/env python3
"""Box 9 (flip variant, n5_flip_climb.py): fitness = (max switches of ONE Odd vertex inside the frozen-σ tail, tail, -n). Original: climb N5 iterations (n5.run, unmodified, best-reward start) SEEDED from a given game. Mutations: retarget/add an edge, swap two
priorities, flip an owner; optional growth: add a fresh vertex (prob 0.05) so n can increase. Every improved best is checked (regions =
harness Zielonka, verify.py) and written with its sha1. Usage: n5_flip_climb.py seed.pg steps seed OUT.pg [grow]"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
src, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; grow = len(sys.argv) > 5
g0 = pg.read(src); rng = random.Random(seed)
cur = (list(g0.prio), list(g0.owner), [list(x) for x in g0.succ])
from n5_lock import step
from n5 import Engine, dual
def fit(c):
    g = pg.Game(*c); it, fb, win, ws, ev = n5.run(g, "n5", cap=5000)
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); last = -1; k = 0; cnt = {}
    while k < 5000:
        r = step(g, E, Ed, s, t)
        if r is None: break
        if r[0] != s: last = k; cnt = {}
        else:
            for v in range(g.n):
                if r[1][v] != t[v]: cnt[v] = cnt.get(v, 0) + 1
        s, t = r[0], r[1]; k += 1
    assert k == it
    return (max(cnt.values(), default=0), k - last - 1, -g.n), g, win, ws
best = fit(cur)[0]; print("start", best, flush=True)
for t in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; n = len(pr); r = rng.random(); v = rng.randrange(n)
    if grow and r < float(os.environ.get("GROWP", "0.05")):
        pr.append(max(pr) + 1 + rng.randrange(3)); ow.append(rng.randrange(2)); sc.append(sorted(set(rng.randrange(n) for _ in range(2))))
        u = rng.randrange(n); sc[u] = sorted(set(sc[u] + [n]))
    elif r < 0.55: i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
    elif r < 0.65 and len(sc[v]) < 4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.9: a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else: ow[v] = 1 - ow[v]
    f, g, win, ws = fit((pr, ow, sc))
    if f >= best:
        if f > best:
            zw, _ = zielonka.solve_with_strategy(g); ok = list(win) == list(zw) and not verify.check(g, win, ws)
            txt = pg.dumps(g); open(out, "w").write(txt)
            print(f"step {t} maxflips {f[0]} tail {f[1]} n {g.n} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
        best, cur = f, (pr, ow, sc)
print("best", best)
