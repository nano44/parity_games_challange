#!/usr/bin/env python3
"""Box 41: INTO / case (i) / case (ii) survey (into17.analyse) over files, from the S3 start and K random start pairs (seeded).
Usage: intolib17.py K seed game.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, into17
K, rng = int(sys.argv[1]), random.Random(int(sys.argv[2])); tot = {}
for f in sys.argv[3:]:
    try:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
    except Exception: continue
    for st in [None] + [[rng.choice(g.succ[v]) for v in range(g.n)] for _ in range(K)]:
        try: C, ex, N = into17.analyse(g, st)
        except Exception as e: tot["err"] = tot.get("err", 0) + 1; continue
        tot["runs"] = tot.get("runs", 0) + 1
        for k, v in C.items():
            if k == "min_into": tot[k] = min(tot.get(k, 10 ** 6), v)
            else: tot[k] = tot.get(k, 0) + v
        bad = [e for e in ex]
        if bad: print("EX", f, st, bad[:3], flush=True)
print("TOTAL", tot, flush=True)
