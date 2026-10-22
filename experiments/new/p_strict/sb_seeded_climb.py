#!/usr/bin/env python3
"""Box 8: SB1 stress test. Climb switch-best length on one-player games (all ⊕ here), SEEDED from sb_phases.F(k, m) with its start;
mutations: add/remove an edge, swap two priorities. Fitness = switch-best steps from the seeded start (also tried: start mutation).
Every improved best is checked (regions = Zielonka). Usage: sb_seeded_climb.py k m steps seed OUT.pg"""
import sys, os, random, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, zielonka
k, m, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
sp = importlib.util.spec_from_file_location('ph', os.path.join(HERE, 'sb_phases.py')); ph = importlib.util.module_from_spec(sp)
sys.argv = [sys.argv[0], str(k), str(m)]; 
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(ph)
g0, s0 = ph.build(k, m); rng = random.Random(seed); n = g0.n
cur = (list(g0.prio), [list(x) for x in g0.succ], list(s0)); best = ph.sb(pg.Game(cur[0], [0] * n, cur[1]), list(cur[2]))[0]; print("start", best, "n", n, flush=True)
for t in range(steps):
    pr, sc, st = list(cur[0]), [list(x) for x in cur[1]], list(cur[2]); r = rng.random(); v = rng.randrange(n)
    if r < 0.4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.6 and len(sc[v]) > 1: w = rng.choice(sc[v]); sc[v].remove(w); st[v] = st[v] if st[v] in sc[v] else sc[v][0]
    elif r < 0.85: a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else: st[v] = rng.choice(sc[v])
    g = pg.Game(pr, [0] * n, sc); f, fin, E = ph.sb(g, list(st))
    if f >= best:
        if f > best:
            win, _ = E.regions(tuple(fin)); ok = list(win) == list(zielonka.solve(g)); open(out, "w").write(pg.dumps(g)); open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{a}:{b}" for a, b in enumerate(st)) + "\nTAU0\n")
            print(f"step {t} switch-best steps {f} (n = {n}) check {'OK' if ok else 'FAIL'}", flush=True)
        best, cur = f, (pr, sc, st)
print("best", best, "n", n)
