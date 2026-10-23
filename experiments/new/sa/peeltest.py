#!/usr/bin/env python3
"""N9b test: certified peeling on random games and files; prints STUCK cases (kill) and any disagreement (bug)."""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg, gen, zielonka
from peel import peel
if sys.argv[1] == "random":
    s0, cnt, nmin, nmax = map(int, sys.argv[2:6])
    games = []
    for seed in range(s0, s0 + cnt):
        rnd = random.Random(seed); n = rnd.randint(nmin, nmax)
        games.append((f"r{seed}", gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed)))
else:
    games = [(os.path.basename(f), pg.read(f)) for f in sys.argv[2:]]
stuck = solved = 0; t0 = time.time()
for name, g in games:
    w, rounds, left = peel(g)
    if w is None:
        stuck += 1; print(f"STUCK {name} n={g.n} rounds={rounds} left={len(left)}", flush=True)
    else:
        assert w == zielonka.solve(g), name
        solved += 1
print(f"{len(games)} games: solved {solved} (all agree with Zielonka), stuck {stuck}, {time.time()-t0:.0f}s", flush=True)
