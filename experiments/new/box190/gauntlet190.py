#!/usr/bin/env python3
"""Box 190 gauntlet step 2 (partial) for the N5' variants: (R) random games (harness gen.random_game, seeds 1..COUNT, n 1..NMAX):
regions vs harness Zielonka and positional strategies by harness verify.check; (F) Oink generator families: iterations per N.
Usage: gauntlet190.py random COUNT NMAX MODES  |  gauntlet190.py fam FAMILY NMAX MODES  (MODES e.g. spec,xi)"""
import sys, os, subprocess, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness")]
import n5v, pg, gen, zielonka, verify
def solve(g, mode):
    st, fb, E = n5v.run(g, mode); win, strat = n5v.solution(g, st, E); return len(st) - 1, fb, win, strat
if sys.argv[1] == "random":
    cnt, nmax, modes = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4].split(","); bad = {m: 0 for m in modes}; mx = {m: 0 for m in modes}
    for seed in range(1, cnt + 1):
        rng = random.Random(seed); n = rng.randint(1, nmax); d = rng.randint(1, n + 1)
        g = gen.random_game(n, d, 1, min(n, 4), seed)
        ref = zielonka.solve(g)
        for m in modes:
            it, fb, win, strat = solve(g, m)
            e = verify.check(g, win, strat)
            if win != ref or e: bad[m] += 1; print("BAD", m, seed, n, e[:2] if e else "regions")
            mx[m] = max(mx[m], it)
    print(f"RANDOM games {cnt} n 1..{nmax}: " + "; ".join(f"{m}: wrong {bad[m]}, max iterations {mx[m]}" for m in modes))
else:
    fam, nmax, modes = sys.argv[2], int(sys.argv[3]), sys.argv[4].split(",")
    for N in range(1, nmax + 1):
        cmd = (["python3", os.path.join(ROOT, "experiments/hard-families/pgsolver_port.py"), fam[4:], str(N)] if fam.startswith("pgs:")
               else [os.path.join(ROOT, "tools/oink/build", fam), str(N)])
        txt = subprocess.run(cmd, capture_output=True, text=True).stdout
        g = pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%"))); ref = zielonka.solve(g)
        row = []
        for m in modes:
            t = time.time(); it, fb, win, strat = solve(g, m); ok = win == ref and not verify.check(g, win, strat)
            row.append(f"{m} {it}{'' if ok else ' WRONG'}")
        print(f"{fam} N {N} n {g.n} | " + " | ".join(row), flush=True)
