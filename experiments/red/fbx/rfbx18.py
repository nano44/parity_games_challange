#!/usr/bin/env python3
"""Box 42: random 𝒞^1O games × random start pairs through fbx18.analyse (every check). First failing (game, start) per check name is
saved as OUT_<name>.json. Usage: rfbx18.py seed secs nmin nmax starts OUT"""
import sys, os, random, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import fbx18, sox, pg
seed, secs, nmin, nmax, K, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); t0 = time.time(); acc = {}; saved = set()
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax)
    prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
    try: g = pg.Game(prio, owner, succ)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1: continue
    for r in range(K):
        st = None if r == 0 else [rng.choice(g.succ[v]) for v in range(n)]
        before = {k: v for k, v in acc.items() if k.startswith("FAIL_")}
        try: fbx18.analyse(g, acc, "rand", st)
        except AssertionError: continue
        for k, v in acc.items():
            if k.startswith("FAIL_") and v > before.get(k, 0) and k not in saved:
                saved.add(k); json.dump(dict(prio=prio, owner=owner, succ=succ, start=st), open(f"{out}_{k}.json", "w"))
                print("HIT", k, n, flush=True)
print(json.dumps(acc, sort_keys=True), flush=True)
