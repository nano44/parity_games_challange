#!/usr/bin/env python3
"""L-RED 67 R237 / box 105 preparation: the SPEC-exact own engine n5s237 against the reference engine (box 190 n5v on si.Engine) STATE
BY STATE on Gamma3-shaped games of random FREE genomes (L-SI box 104's generator freereach104.rand_free and builder free104.build_free:
the OBJECTS only). Counters (unit: genomes): trajdiff (the (sigma, tau) trajectories differ at some state), itdiff, fbdiff, wrong
(regions of the own engine against harness Zielonka). CTRL=1: the own engine runs the OTHER mode (trajdiff must fire).
Env BOX104, LNEW, LRED (as wr237.py). Usage: xg237.py MODE SEED COUNT [DMAX WMAX DEGMAX]   (MODE spec|xi)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.environ["BOX104"])
import freereach104 as FR
import n5v, n5, n5x, zielonka
from si import Engine
import n5s237 as X
mode, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); dm, wm, gm = (int(a) for a in sys.argv[4:7]) if len(sys.argv) > 6 else (4, 3, 3)
mine_mode = mode if os.environ.get("CTRL") != "1" else {"spec": "xi", "xi": "spec"}[mode]
rng = random.Random(seed); tot = dict(trajdiff=0, itdiff=0, fbdiff=0, wrong=0); mx = 0; sumit = 0; mn = 0; first = None
for i in range(cnt):
    G, pb, pe = FR.rand_free(rng, dm, wm, gm); g, sig, tau0, V = FR.F.build_free(G, pb, pe); n = g.n
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); ref = [(list(sigma), list(tau))]; its = fbs = 0
    while True:
        r = n5v.step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau, _, _, fb = r; its += 1; fbs += fb; ref.append((list(sigma), list(tau)))
    tr = []; it, fb, win, s, sb = X.run(list(g.prio), list(g.owner), [list(x) for x in g.succ], mine_mode, trace=tr)
    mine = [([sg.get(v, -1) for v in range(n)], [tu.get(v, -1) for v in range(n)]) for sg, tu in tr]
    refn = [([a[v] if g.owner[v] == 0 else -1 for v in range(n)], [b[v] if g.owner[v] == 1 else -1 for v in range(n)]) for a, b in ref]
    d = int(mine != refn); tot["trajdiff"] += d; tot["itdiff"] += int(it != its); tot["fbdiff"] += int(fb != fbs)
    z = zielonka.solve(g); tot["wrong"] += int(any((0 if win[v] else 1) != z[v] for v in range(n))); mx = max(mx, it); sumit += it; mn = max(mn, n)
    if d and first is None: first = (i, n, it, its)
print(f"XG237 mode {mode} seed {seed} free genomes {cnt} d<={dm} w<={wm} deg<={gm}:", " ".join(f"{k} {v}" for k, v in tot.items()),
      f"| max iterations {mx} sum {sumit} max |V| {mn} | first differing genome {first}", flush=True)
