#!/usr/bin/env python3
"""L-RED 67 R237: self-check of the SPEC-exact own engine n5s237 against the reference engine (box 190 n5v on si.Engine) STATE BY
STATE on random games: equal trajectories (sigma, tau at every state), equal iteration and fallback counts, regions = harness
Zielonka. Counters: trajdiff (games whose trajectories differ), itdiff, fbdiff, wrong. Env BOX104, LNEW, LRED (as wr237.py).
CTRL=1: the own engine runs the OTHER mode (trajdiff must fire).
Usage: xs237.py MODE SEED COUNT NMAX   (MODE spec|xi)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.environ["BOX104"])
import free104  # sets the engine paths
import pg, n5v, n5, n5x, gen, zielonka
from si import Engine
import n5s237 as X
mode, seed, cnt, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
import random
mine_mode = mode if os.environ.get("CTRL") != "1" else {"spec": "xi", "xi": "spec"}[mode]
rng = random.Random(seed); tot = dict(trajdiff=0, itdiff=0, fbdiff=0, wrong=0); mx = 0; first = None; sumit = 0
for i in range(cnt):
    n = rng.randint(2, nmax); g = gen.random_game(n, rng.randint(1, n + 1), 1, min(n, 4), rng.randrange(10 ** 9))
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); ref = [(list(sigma), list(tau))]; its = fbs = 0
    while True:
        r = n5v.step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau, _, _, fb = r; its += 1; fbs += fb; ref.append((list(sigma), list(tau)))
    tr = []; it, fb, win, s, sb = X.run(list(g.prio), list(g.owner), [list(x) for x in g.succ], mine_mode, trace=tr)
    mine = [([sg.get(v, -1) for v in range(n)], [tu.get(v, -1) for v in range(n)]) for sg, tu in tr]
    refn = [([a[v] if g.owner[v] == 0 else -1 for v in range(n)], [b[v] if g.owner[v] == 1 else -1 for v in range(n)]) for a, b in ref]
    d = int(mine != refn); tot["trajdiff"] += d; tot["itdiff"] += int(it != its); tot["fbdiff"] += int(fb != fbs)
    z = zielonka.solve(g); tot["wrong"] += int(any((0 if win[v] else 1) != z[v] for v in range(n))); mx = max(mx, it); sumit += it
    if d and first is None: first = (i, n, it, its)
print(f"XS237 mode {mode} seed {seed} games {cnt} nmax {nmax}:", " ".join(f"{k} {v}" for k, v in tot.items()), f"| max iterations {mx} sum {sumit} | first differing game {first}", flush=True)
