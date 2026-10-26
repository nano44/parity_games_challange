#!/usr/bin/env python3
"""REFEREE succ. 12: fbred_probe.run_check on given files WITHOUT the n <= 64 skip (for the R-N5-FBRED §C data comparison).
Starts: S3 best-reward start + RANDSTARTS random starts seeded by the RELATIVE file name (as fbred_probe.main). Usage: fbred_big.py files..."""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, dual_probe as D, fbred_probe as F
nr = int(os.environ.get("RANDSTARTS", "0"))
for f in sys.argv[1:]:
    name = os.path.relpath(f, P.ROOT); g = RE.parse(f); cnt = Counter()
    for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
        c1 = Counter()
        try: F.run_check(g, st, c1, name + ("@r%d" % i if i else ""))
        except RuntimeError: c1["maxit"] += 1
        print(name, "n", g.n, "start", i, " ".join("%s=%d" % (k, v) for k, v in sorted(c1.items()) if k.startswith("max") or k.endswith("FAIL") or k in ("phases", "fallbacks")), flush=True)
