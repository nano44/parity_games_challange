#!/usr/bin/env python3
"""Box 8: switch-best (= N5 on a one-player game) on GENERAL one-player games (cycles allowed; Odd vertices out-degree 1), random
starts. Reports max iterations by n, and checks the final regions against harness Zielonka + verify.py. Usage: sb_1p_general.py games seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); worst = {}; bad = 0
for gi in range(games):
    n = rng.randint(2, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(pr, owner, succ); zw, _ = zielonka.solve_with_strategy(g)
    for _ in range(4):
        st = {v: rng.choice(succ[v]) for v in range(n) if owner[v] == 0}
        it, fb, win, ws, ev = n5.run(g, "n5", (st, {}))
        bad += (list(win) != list(zw)) or bool(verify.check(g, win, ws))
        worst[n] = max(worst.get(n, 0), it)
print("max iterations by n:", dict(sorted(worst.items())), " incorrect runs:", bad)
