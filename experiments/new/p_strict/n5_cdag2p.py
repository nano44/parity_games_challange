#!/usr/bin/env python3
"""Box 8: N5 (n5.run, unmodified) on TWO-PLAYER complete DAGs: vertices 1..n with edges to every lower vertex, sink 0 (priority 0
self-loop); owners and the priority order random (distinct priorities), random starts (σ_0, τ_0). Reports max iterations by n;
every max-setting run is checked (zielonka + verify.py). Usage: n5_cdag2p.py games starts seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
games, starts, seed, nmax = map(int, sys.argv[1:5]); rng = random.Random(seed); worst = {}; bad = 0
for _ in range(games):
    n = rng.randint(3, nmax); owner = [0] + [rng.randrange(2) for _ in range(n)]; pr = [0] + rng.sample(range(1, 3 * n), n)
    g = pg.Game(pr, owner, [[0]] + [list(range(v)) for v in range(1, n + 1)])
    for _ in range(starts):
        st = ({v: rng.randrange(v) for v in range(1, n + 1) if owner[v] == 0}, {v: rng.randrange(v) for v in range(1, n + 1) if owner[v] == 1})
        it, fb, win, ws, ev = n5.run(g, "n5", st)
        if it > worst.get(n, (0,))[0]:
            zw, _ = zielonka.solve_with_strategy(g); ok = list(win) == list(zw) and not verify.check(g, win, ws); bad += not ok
            worst[n] = (it, fb)
print("max (iterations, fallbacks) by n:", dict(sorted(worst.items())), "; checked max runs failing:", bad)
