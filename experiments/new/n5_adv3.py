#!/usr/bin/env python3
"""Box 4 (Lead 21:35Z): climb for Ξ-FLAT iterations (neither Ξσ nor Ξτ strictly rises) and REPEATED STATES. N5's step is
n5_lock.step (n5.py's loop, unmodified algorithm); this wrapper only observes: a repeated (σ, τ) pair is reported and the instance
saved (an incomplete run would be a kill), flat iterations are counted. Every improved best is re-run through n5.run UNMODIFIED
(counts asserted) and checked (zielonka.py + verify.py). Fitness = (flat iterations, iterations). Usage: n5_adv3.py n steps seed DIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
def flatrun(g, d=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = flat = 0; seen = set()
    xs, xt = E.evaluate(tuple(s))[0], Ed.evaluate(tuple(t))[0]
    while it < 5000:
        key = (tuple(s), tuple(t))
        if key in seen:
            print("REPEATED STATE", flush=True)
            if d: open(os.path.join(d, "REPEATED.pg"), "w").write(pg.dumps(g))
            return 10 ** 6, it
        seen.add(key)
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]; it += 1
        ys, yt = E.evaluate(tuple(s))[0], Ed.evaluate(tuple(t))[0]
        rise_s = any(E.key(ys[v]) > E.key(xs[v]) for v in range(g.n)); rise_t = any(Ed.key(yt[v]) > Ed.key(xt[v]) for v in range(g.n))
        flat += not rise_s and not rise_t; xs, xt = ys, yt
    return flat, it
if __name__ == "__main__":
    n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed)
    prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    best = flatrun(pg.Game(prio, owner, succ), d); cur = (prio, owner, succ); print("start", best, flush=True)
    for s_ in range(steps):
        pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]
        k = rng.random()
        if k < 0.6:
            v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
            if rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
        elif k < 0.8:
            a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
        elif k < 0.9:
            a = rng.randrange(n); pr[a] = pr[rng.randrange(n)]      # allow EQUAL priorities (ties by index)
        else:
            v = rng.randrange(n); ow[v] = 1 - ow[v]
        g = pg.Game(pr, ow, sc); f = flatrun(g, d)
        if f >= best:
            if f > best:
                it, fb, win, ws, _ = n5.run(g, cap=5000); assert it == f[1]
                ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
                print(f"step {s_} flat {f[0]} iterations {f[1]} check {'OK' if ok else 'FAIL'}", flush=True)
                open(os.path.join(d, f"flat_n{n}_seed{seed}.pg"), "w").write(pg.dumps(g))
            best, cur = f, (pr, ow, sc)
    print("best", best)
