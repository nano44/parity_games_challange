#!/usr/bin/env python3
"""Cross-check of si.py against the REFEREE-checked PGSolver port (experiments/hard-families/pgsolver_si.py) and py-zlk.
1. valuations: for random games and random Even strategies, Engine.evaluate == SI.evaluate (cycle node, path set, length);
2. switch-all iteration counts equal the port's on random games and on switchallexp N=1..4;
3. every rule: regions == py-zlk, both players' strategies pass harness/verify.py.
Usage: xcheck.py [--quick]"""
import sys, os, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, os.path.join(HERE, "..", "hard-families"))
import pg, gen, verify, zielonka, si, pgsolver_si

quick = "--quick" in sys.argv or "--tiny" in sys.argv
tiny = "--tiny" in sys.argv
rng = random.Random(7)


def rand_game(n, d, dmax, seed):
    return gen.generate(n, d, 1, dmax, seed) if hasattr(gen, "generate") else None


def games(count, nmax):
    out = []
    for i in range(count):
        n = rng.randint(1, nmax); d = rng.randint(1, n + 1); dmax = rng.randint(1, min(n, 4))
        g = gen_game(n, d, dmax, i)
        out.append(g)
    return out


def gen_game(n, d, dmax, seed):
    r = gen.Rng(("xcheck", n, d, dmax, seed))
    prio = [r.randrange(d) for _ in range(n)]
    owner = [r.randrange(2) for _ in range(n)]
    succ = []
    for v in range(n):
        k = r.randint(1, dmax)
        s = set()
        while len(s) < k:
            s.add(r.randrange(n))
        succ.append(sorted(s))
    return pg.Game(prio, owner, succ)


def zlk(g):
    return zielonka.solve(g)


def port_val_to_mine(e, pv):
    w, paths, ln = pv
    mask = 0
    for x in paths:
        mask |= e.bit[x]
    return (w, mask, ln)


fails = 0
N = 40 if tiny else (150 if quick else 600)
gs = games(N, 8 if tiny else (9 if quick else 14))
# 1. valuations
cnt = 0
for g in gs:
    e = si.Engine(g); port = pgsolver_si.SI(g)
    for t in range(3):
        strat = tuple(-1 if g.owner[v] == 1 else rng.choice(e.succ[v]) for v in range(g.n))
        mv, _ = e.evaluate(strat)
        pv = port.evaluate(list(strat))
        for v in range(g.n):
            if mv[v] != port_val_to_mine(e, pv[v]):
                fails += 1
                print("VALUATION MISMATCH", pg.dumps(g), strat, v, mv[v], pv[v]); break
        cnt += 1
print(f"valuations: {cnt} (game, strategy) pairs compared, {fails} mismatches")
# 2. switch-all counts vs port
mm = 0
for g in gs:
    win_p, ws_p, k_p = pgsolver_si.SI(g).solve()
    win, ws, k, ev = si.solve(g, "switch-all")
    if k != k_p - 1 or win != win_p:   # port counts the final non-improvable evaluation as one iteration
        mm += 1; print("SWITCH-ALL MISMATCH", pg.dumps(g), k, k_p, win, win_p)
print(f"switch-all vs port: {len(gs)} games, {mm} mismatches")
fails += mm
for N_ in ([1, 2] if quick else [1, 2, 3, 4]):
    txt = subprocess.run(["python3", "-I", os.path.join(HERE, "..", "hard-families", "pgsolver_port.py"), "switchallexp", str(N_)],
                         capture_output=True, text=True).stdout
    g = pg.parse(txt)
    k_p = pgsolver_si.SI(g).solve()[2]
    k = si.solve(g, "switch-all")[2]
    print(f"switchallexp N={N_}: n={g.n} port {k_p - 1} mine {k}")
    if k != k_p - 1:
        fails += 1
# 3. every rule: regions and strategies
rules = ["switch-all", "random-edge", "msf", "lsf", "steepest", "most-improved", "rar", "S4", "S4:msf"]
for rule in rules:
    bad = 0; its = 0
    for g in gs:
        win, ws, k, ev = si.solve(g, rule, seed=1)
        its += k
        zw = zlk(g)
        errs = verify.check(g, win, ws)
        if win != zw or errs:
            bad += 1
            print("RULE FAIL", rule, pg.dumps(g), win, zw, errs[:2])
    print(f"rule {rule}: {len(gs)} games, {bad} failures, {its} total iterations")
    fails += bad
print("XCHECK PASS" if fails == 0 else f"XCHECK FAILED ({fails})")
sys.exit(1 if fails else 0)
