#!/usr/bin/env python3
"""Box 10: climb TWO-PLAYER games for the most Even moves of N5 inside one λ-phase of one σ̄-segment (σ̄ = Odd's best reply constant, every
cycle node of Ξσ constant). (P-N5) would bound this by n − 1 (+ flat). Fitness = (max in-phase-segment Even moves, iterations, −n). Mutations as
n5_seeded_climb.py; optional growth. Every improved best is checked (regions = Zielonka, verify.py) and written with its sha1.
Usage: seg_climb.py seed.pg|random:N steps seed OUT.pg [grow]"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
from n5_lock import step
from n5 import Engine, dual
src, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; grow = len(sys.argv) > 5; rng = random.Random(seed)
if src.startswith("random:"):
    n = int(src.split(":")[1]); g0 = pg.Game(rng.sample(range(2 * n), n), [rng.randrange(2) for _ in range(n)], [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)])
else: g0 = pg.read(src)
cur = (list(g0.prio), list(g0.owner), [list(x) for x in g0.succ])
VC = os.environ.get("FIT") == "vc"   # count only Even-moving iterations that change the honest valuation Xi_sigma
def fit(c, cap=3000):
    g = pg.Game(*c); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = 0; seg = None; k = mx = 0
    vs, sbar = E.evaluate(tuple(s))
    while it < cap:
        key = (tuple(sbar[v] if g.owner[v] == 1 else -1 for v in range(g.n)), tuple(vs[v][0] for v in range(g.n)))
        if key != seg: seg, k = key, 0
        r = step(g, E, Ed, s, t)
        if r is None: break
        vs2, sbar2 = E.evaluate(tuple(r[0]))
        if r[0] != s and (not VC or any(E.key(vs2[v]) != E.key(vs[v]) for v in range(g.n))): k += 1; mx = max(mx, k)
        s, t = r[0], r[1]; vs, sbar = vs2, sbar2; it += 1
    return (mx, it, -g.n), g
best, _ = fit(cur); print("start", best, flush=True)
for tt in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; n = len(pr); r = rng.random(); v = rng.randrange(n)
    if grow and r < 0.05:
        pr.append(max(pr) + 1 + rng.randrange(3)); ow.append(rng.randrange(2)); sc.append(sorted(set(rng.randrange(n) for _ in range(2))))
        u = rng.randrange(n); sc[u] = sorted(set(sc[u] + [n]))
    elif r < 0.55: i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
    elif r < 0.65 and len(sc[v]) < 4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.9: a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else: ow[v] = 1 - ow[v]
    f, g = fit((pr, ow, sc))
    if f >= best:
        if f > best:
            it, fb, win, ws, ev = n5.run(g, "n5", cap=5000); zw, _ = zielonka.solve_with_strategy(g); ok = list(win) == list(zw) and not verify.check(g, win, ws)
            txt = pg.dumps(g); open(out, "w").write(txt)
            print(f"step {tt} inphase-seg-moves {f[0]} iterations {f[1]} n {g.n} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
        best, cur = f, (pr, ow, sc)
print("best", best)
