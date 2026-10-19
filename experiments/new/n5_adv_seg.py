#!/usr/bin/env python3
"""Box 8 K10: climb for a LONG σ̄-SEGMENT along N5's own run (the per-segment premise K9 needs, now that (P*) is false). Fitness =
(max Even moves within one segment where Odd's best reply σ̄_k is constant, iterations), along n5_lock.step (= n5.py's loop). Mutations as n5_adv4.py. Every improved best is re-run through n5.run UNMODIFIED (iterations asserted) and
checked (harness zielonka.py + verify.py). Usage: n5_adv_seg.py n steps seed DIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
def segrun(g):
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
    def br(): return tuple(E.evaluate(tuple(s))[1][v] for v in O), tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
    bs, bt = br(); seg = best = it = 0
    while it < 5000:
        r = step(g, E, Ed, s, t)
        if r is None: break
        it += 1; seg += r[0] != s; s, t = r[0], r[1]; ns, nt = br()
        if ns != bs: seg = 0
        best = max(best, seg); bs, bt = ns, nt
    return best, it
if __name__ == "__main__":
    n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed)
    prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    best = segrun(pg.Game(prio, owner, succ)); cur = (prio, owner, succ); print("start", best, flush=True)
    for s_ in range(steps):
        pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; k = rng.random()
        if k < 0.6:
            v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
            if rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
        elif k < 0.9:
            a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
        else:
            v = rng.randrange(n); ow[v] = 1 - ow[v]
        g = pg.Game(pr, ow, sc); f = segrun(g)
        if f >= best:
            if f > best:
                it, fb, win, ws, _ = n5.run(g, cap=5000); assert it == f[1]
                ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
                print(f"step {s_} segment {f[0]} iterations {f[1]} check {'OK' if ok else 'FAIL'}", flush=True)
                open(os.path.join(d, f"seg_n{n}_seed{seed}.pg"), "w").write(pg.dumps(g))
            best, cur = f, (pr, ow, sc)
    print("best", best)
