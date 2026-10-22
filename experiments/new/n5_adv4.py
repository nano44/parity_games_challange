#!/usr/bin/env python3
"""Box 5 (Lead 23:03Z): climb for HARMFUL SKIPS. Along N5's own run (n5_lock.step = n5.py's loop), an iteration is harmful if SSI's
step from the same state would give the moving side a valuation strictly above N5's at some vertex (SSI's Ξ ⋬ N5's Ξ) while SSI
switched a vertex that N5 did not move to the same edge. Fitness = (harmful iterations, iterations). Every improved best is re-run
through n5.run UNMODIFIED (counts asserted) and checked (zielonka.py + verify.py). Usage: n5_adv4.py n steps seed DIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
def harmrun(g):
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); it = harm = 0
    while it < 5000:
        vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
        if not Is and not It: break
        ns, nt = list(s), list(t)
        for v, w in Is:
            if tbar[v] == w: ns[v] = w
        for v, w in It:
            if sbar[v] == w: nt[v] = w
        r = step(g, E, Ed, s, t); it += 1; h = False
        for Eng, ssi_new, n5_new, cur in ((E, ns, r[0], s), (Ed, nt, r[1], t)):
            if any(ssi_new[v] != cur[v] and n5_new[v] != ssi_new[v] for v in range(g.n)):
                Xn = Eng.evaluate(tuple(n5_new))[0]; Xs = Eng.evaluate(tuple(ssi_new))[0]
                h |= any(Eng.key(Xs[x]) > Eng.key(Xn[x]) for x in range(g.n))
        harm += h; s, t = r[0], r[1]
    return harm, it
if __name__ == "__main__":
    n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed)
    prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    best = harmrun(pg.Game(prio, owner, succ)); cur = (prio, owner, succ); print("start", best, flush=True)
    for s_ in range(steps):
        pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; k = rng.random()
        if k < 0.6:
            v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
            if rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
        elif k < 0.9:
            a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
        else:
            v = rng.randrange(n); ow[v] = 1 - ow[v]
        g = pg.Game(pr, ow, sc); f = harmrun(g)
        if f >= best:
            if f > best:
                it, fb, win, ws, _ = n5.run(g, cap=5000); assert it == f[1]
                ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
                print(f"step {s_} harmful {f[0]} iterations {f[1]} check {'OK' if ok else 'FAIL'}", flush=True)
                open(os.path.join(d, f"harm_n{n}_seed{seed}.pg"), "w").write(pg.dumps(g))
            best, cur = f, (pr, ow, sc)
    print("best", best)
