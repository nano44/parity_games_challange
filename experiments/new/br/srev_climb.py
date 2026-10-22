#!/usr/bin/env python3
"""Box 11 option (2): climb two-player games for the toggle mechanism WITH Odd moving. Fitness FIT=srev (default): max number of REVISITS of one
vertex's own strategy target along N5's run (sigma at an Even vertex or tau at an Odd vertex returns to a target it used earlier), then
iterations, then -n. FIT=it: iterations. Requires Odd to move at least once (else fitness 0). Every improved best re-run through n5.run,
regions = Zielonka, verify.py OK, written with sha1. Usage: srev_climb.py seed.pg|random:N steps seed OUT.pg [grow]"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
from n5_lock import step
from n5 import Engine, dual
MODE = os.environ.get("FIT", "srev")
src, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; grow = len(sys.argv) > 5; rng = random.Random(seed)
if src.startswith("random:"):
    n = int(src.split(":")[1]); g0 = pg.Game(rng.sample(range(2 * n), n), [rng.randrange(2) for _ in range(n)], [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)])
else: g0 = pg.read(src)
cur = (list(g0.prio), list(g0.owner), [list(x) for x in g0.succ])
def fit(c):
    g = pg.Game(*c); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = 0
    used = {v: {s[v] if g.owner[v] == 0 else t[v]} for v in range(g.n)}; rev = {v: 0 for v in range(g.n)}; oddmoves = 0
    while it < 3000:
        r = step(g, E, Ed, s, t)
        if r is None: break
        for v in range(g.n):
            new = r[0][v] if g.owner[v] == 0 else r[1][v]; old = s[v] if g.owner[v] == 0 else t[v]
            if new != old:
                if new in used[v]: rev[v] += 1
                used[v].add(new)
        oddmoves += r[1] != t; s, t = r[0], r[1]; it += 1
    mx = max(rev.values()) if oddmoves else 0
    return ((mx, it, -g.n) if MODE == "srev" else (it if oddmoves else 0, mx, -g.n)), g, (mx, it, oddmoves)
best, _, _ = fit(cur); print("start", best, flush=True)
for tt in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; n = len(pr); r = rng.random(); v = rng.randrange(n)
    if grow and r < 0.05:
        pr.append(max(pr) + 1 + rng.randrange(3)); ow.append(rng.randrange(2)); sc.append(sorted(set(rng.randrange(n) for _ in range(2))))
        u = rng.randrange(n); sc[u] = sorted(set(sc[u] + [n]))
    elif r < 0.55: i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
    elif r < 0.65 and len(sc[v]) < 4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.9: a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else: ow[v] = 1 - ow[v]
    f, g, info = fit((pr, ow, sc))
    if f >= best:
        if f > best:
            it, fb, win, ws, ev = n5.run(g, "n5", cap=5000); zw, _ = zielonka.solve_with_strategy(g); ok = list(win) == list(zw) and not verify.check(g, win, ws)
            txt = pg.dumps(g); open(out, "w").write(txt)
            print(f"step {tt} fit {f} (max revisits, iterations, odd moves) {info} n {g.n} n5-iterations {it} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
        best, cur = f, (pr, ow, sc)
print("best", best)
