#!/usr/bin/env python3
"""N10c test on YES-instances (where its only errors can be): for each game G, the Even query on G[W_E] and the Even query on
dual(G)[W_O] (= Odd wins all of G[W_O]); and on NO-instances the answer must be NO (asserted: it is by construction).
Usage: condtest.py random S0 COUNT NMIN NMAX | condtest.py files f.pg ..."""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sa"))
import pg, gen, zielonka
from gaps import sub, dual
from cond import condition
if sys.argv[1] == "random":
    s0, cnt, nmin, nmax = map(int, sys.argv[2:6]); games = []
    for seed in range(s0, s0 + cnt):
        rnd = random.Random(seed); n = rnd.randint(nmin, nmax)
        games.append((f"r{seed}", gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed)))
else:
    games = [(os.path.basename(f), pg.read(f)) for f in sys.argv[2:]]
t0 = time.time(); yes = stuck = no_ok = 0; calls = 0
for name, g in games:
    win = zielonka.solve(g); WE = {v for v in range(g.n) if win[v] == 0}; WO = set(range(g.n)) - WE
    qs = []
    if WE:
        qs.append(("YE", sub(g, WE)))
    if WO:
        qs.append(("YO", dual(sub(g, WO))))
    if WE and WO:
        qs.append(("NO", g))
    for q, h in qs:
        sig, c = condition(h); calls += c
        if q == "NO":
            assert sig is None; no_ok += 1
        elif sig is None:
            stuck += 1; print(f"STUCK {name} {q} n={h.n}", flush=True)
        else:
            yes += 1
print(f"{len(games)} games: YES-instances solved {yes}, STUCK {stuck}; NO-instances answered NO {no_ok}; oracle calls {calls}; "
      f"{time.time()-t0:.0f}s", flush=True)
