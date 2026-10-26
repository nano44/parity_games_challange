#!/usr/bin/env python3
"""Box 45d: random small games (n NMIN..NMAX, >= 1 Odd choice vertex) × EVERY start pair (product of successor sets, capped at CAP),
through h3_19.analyse; prints any FAIL (C2-H3, TC-CLASS, WM-G, FRZ, R-STICK_D, SN-PREFIX_D, X-EP) and the best FRZ move gap.
Usage: exh19.py seed secs nmin nmax cap"""
import sys, os, json, random, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h3_19, pg
seed, secs, nmin, nmax, cap = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rng = random.Random(seed); t0 = time.time(); games = runs = 0; best = -10 ** 9; bestg = None; fails = {}; nonvac = 0
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax); prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.5 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for v in range(n)]
    g = pg.Game(prio, owner, succ)
    if not any(owner[v] == 1 and len(succ[v]) > 1 for v in range(n)): continue
    tot = 1
    for s in succ: tot *= len(s)
    if tot > cap: continue
    games += 1
    for st in itertools.product(*succ):
        r = h3_19.analyse(g, list(st)); runs += 1; nonvac += r["frz_nonvac"]
        for x in r["fails"]:
            fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
            if fails[x.split()[0]] <= 3: print("FAIL", x, json.dumps(dict(prio=prio, owner=owner, succ=succ, start=list(st))), flush=True)
        if r["frz_move_gap"] > best: best = r["frz_move_gap"]; bestg = dict(prio=prio, owner=owner, succ=succ, start=list(st), r=r)
print("GAMES", games, "RUNS", runs, "FRZ_NONVAC", nonvac, "FAILS", fails, "BEST_MOVE_GAP", best, json.dumps(bestg), flush=True)
