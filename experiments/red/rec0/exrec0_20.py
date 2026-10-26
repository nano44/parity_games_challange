#!/usr/bin/env python3
"""Box 46: random small games (n NMIN..NMAX, >= QMIN Odd choice vertices) × EVERY start pair (product of successor sets, <= CAP),
through rec0_20.analyse with full level checks (STEP1, STEP2, BASE, WLEB, SAT, KIND3, PRE, REC0, EP0, PREFIX, WM, XIW).
Usage: exrec0_20.py seed secs nmin nmax qmin cap"""
import sys, os, json, random, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rec0_20 as R0, pg
seed, secs, nmin, nmax, qmin, cap = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
rng = random.Random(seed); t0 = time.time(); games = runs = 0; fails = {}; best = {}; tot = dict(step1=0, lvl=0, ovf=0)
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax); prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.5 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for v in range(n)]
    if sum(1 for v in range(n) if owner[v] == 1 and len(succ[v]) > 1) < qmin: continue
    tot_ = 1
    for s in succ: tot_ *= len(s)
    if tot_ > cap: continue
    g = pg.Game(prio, owner, succ); games += 1
    for st in itertools.product(*succ):
        r = R0.analyse(g, list(st)); runs += 1; tot["step1"] += r["step1"]; tot["lvl"] += r["lvl_checks"]; tot["ovf"] += r["overflow"]
        for x in r["fails"]:
            k = x.split()[0]; fails[k] = fails.get(k, 0) + 1
            if fails[k] <= 3: print("FAIL", x, json.dumps(dict(prio=prio, owner=owner, succ=succ, start=list(st))), flush=True)
        for k in ("N0", "N0f", "kind3", "kind3gap", "span", "pre", "pregap", "Nep", "fmax"):
            if k not in best or r[k] > best[k]: best[k] = r[k]
print("GAMES", games, "RUNS", runs, "TOT", tot, "FAILS", fails, "BEST", best, flush=True)
