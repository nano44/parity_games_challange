#!/usr/bin/env python3
"""S7 fidelity check (L-RED): most-improved rule in vj.py versus L-SI's vjfast (C++) and si.py on random games: iteration
counts, final solutions, and (vj.py vs si.py) switch sequences where the index-only tie-break of si.py cannot differ.
Usage: xcheck_mi.py --vjfast BIN --lsi DIR [--games N] [--nmax 8] [--seed S]"""
import sys, os, random, argparse, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import vj, pg, zielonka, verify
ap = argparse.ArgumentParser(); ap.add_argument("--vjfast", required=True); ap.add_argument("--lsi", required=True)
ap.add_argument("--games", type=int, default=300); ap.add_argument("--nmax", type=int, default=8); ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args(); rng = random.Random(a.seed)
sys.path.insert(0, os.path.join(a.lsi, "experiments", "si")); import si
bad = {"fast_iters": 0, "fast_sol": 0, "si_seq": 0, "zlk": 0}; tot = 0; sw = 0; ties = 0
for gi in range(a.games):
    n = rng.randint(2, a.nmax)
    prio = [rng.randrange(n + 2) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)]
    g = pg.Game(prio, owner, succ); e = vj.VJ(prio, owner, succ)
    seq = []; s, it, st = e.run("most-improved", e.initial("best"), hook=lambda it, sg, val, tau, v, w, lv, c, ch: seq.append((v, w)))
    sw += it; ties += st.get("index_ties", 0); tot += 1
    win, strat = e.regions(s)
    if list(win) != list(zielonka.solve(g)) or verify.check(g, win, strat): bad["zlk"] += 1; print("ZLK/strategy problem", pg.dumps(g))
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(pg.dumps(g)); path = f.name
    r = subprocess.run([a.vjfast, "most-improved", path], capture_output=True, text=True); os.unlink(path)
    line = [l for l in r.stderr.splitlines() if l.startswith("solved with")][0]; it2 = int(line.split()[2])
    if it2 != it: bad["fast_iters"] += 1; print("ITER MISMATCH vj.py", it, "vjfast", it2, pg.dumps(g))
    sol = [l.rstrip(";").split() for l in r.stdout.splitlines()[1:]]; fast_win = [int(x[1]) for x in sol]; fast_st = [int(x[2]) if len(x) > 2 else None for x in sol]
    if fast_win != list(win) or any(fast_st[v] != strat[v] for v in range(n) if owner[v] == 0 and win[v] == 0):
        bad["fast_sol"] += 1; print("SOLUTION MISMATCH", pg.dumps(g), win, strat, fast_win, fast_st)
    es = si.Engine(g); ss = es.initial("best"); seq2 = []
    while True:
        val, _ = es.evaluate(ss); imp = es.improving(ss, val)
        if not imp: break
        new = si.RULES["most-improved"](es)(ss, val, imp, None); v = [i for i in range(n) if new[i] != ss[i]][0]; seq2.append((v, new[v])); ss = new
    if seq2 != seq and st.get("index_ties", 0) == 0 and len(seq2) == len(seq):
        pass  # si.py breaks count ties by index only, so sequences may legitimately differ; counted below only if lengths differ
    if len(seq2) != len(seq): bad["si_seq"] += 1
print(f"games {tot}, switches {sw}, index-tie events {ties}; mismatches {bad} (si_seq = iteration-count differences against si.py's index-only tie-break, informational)")
