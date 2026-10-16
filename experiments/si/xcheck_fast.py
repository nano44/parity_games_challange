#!/usr/bin/env python3
"""Cross-check of the C++ engine vjfast against si.py: valuations on random games x random strategies (exact), iteration
counts of the deterministic rules from the best-reward start, regions = py-zlk and strategies verified for every rule
including rar.  Usage: xcheck_fast.py [--games N] [--nmax 14]"""
import sys, os, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, si, verify, zielonka
games = int(sys.argv[sys.argv.index("--games") + 1]) if "--games" in sys.argv else 400
nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 14
rng = random.Random(11); bad = 0; FAST = os.environ.get("FAST_BIN", os.path.join(HERE, "vjfast"))
for gi in range(games):
    n = rng.randint(1, nmax); d = rng.randint(1, n + 1)
    g = pg.Game([rng.randrange(d) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                [sorted(rng.sample(range(n), rng.randint(1, min(n, 4)))) for _ in range(n)])
    f = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False); f.write(pg.dumps(g)); f.close()
    e = si.Engine(g)
    for t in range(3):
        strat = tuple(-1 if g.owner[v] == 1 else rng.choice(e.succ[v]) for v in range(n))
        val, _ = e.evaluate(strat)
        spec = " ".join(f"{v}:{strat[v]}" for v in range(n) if strat[v] >= 0)
        out = subprocess.run([FAST, "valu", f.name, "--strat", spec], capture_output=True, text=True).stdout
        for line in out.splitlines():
            v, c, rs, ln = line.split(" ", 3); v = int(v); c = int(c); ln = int(ln)
            rs = [int(x) for x in rs.strip("[]").split(",") if x]
            mask = sum(1 << r for r in rs)
            if (c, mask, ln) != val[v]:
                bad += 1; print("VALUATION MISMATCH", f.name, spec, v, (c, mask, ln), val[v]); break
    ref = zielonka.solve(g)
    for rule in ["switch-all", "msf", "lsf", "zadeh", "cunningham", "rar", "random-edge"]:
        r = subprocess.run([FAST, rule, f.name, f.name + ".sol", "--seed", "3"], capture_output=True, text=True)
        k = int(r.stderr.split()[2])
        sol = open(f.name + ".sol").read(); win = pg.read_sol(sol, n); st = verify.read_strategy(sol, n)
        errs = verify.check(g, win, st)
        if win != ref or errs:
            bad += 1; print("RULE FAIL", rule, f.name, win, ref, errs[:2])
        if rule in ("switch-all", "msf", "lsf", "zadeh", "cunningham"):
            k2 = si.solve(g, rule)[2]
            if k != k2:
                bad += 1; print("COUNT MISMATCH", rule, f.name, k, k2)
    os.unlink(f.name); os.unlink(f.name + ".sol")
print(f"xcheck_fast: {games} games, {bad} problems", "XCHECK-FAST PASS" if bad == 0 else "XCHECK-FAST FAILED")
