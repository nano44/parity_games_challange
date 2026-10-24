#!/usr/bin/env python3
"""Box 26: random search for the smallest o-cyclic C^1O game (canonical start) with a pure throttle-release re-entry (reentry.py
class THETA, (h) at both ends). Usage: thetasearch.py N nmin nmax seed out"""
from common import *
from reentry import run
from collections import Counter
if __name__ == "__main__":
    N, lo, hi, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]; rng = random.Random(seed); best = None
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None or (best and g.n >= best): continue
        c = Counter(); run(g, None, c)
        if c["THETA"] - c["THETA_noh"] > 0:
            best = g.n; print("hit n", g.n, "game", i, flush=True)
            open(f"{out}_n{g.n}.pg", "w").write(f"parity {g.n-1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    print("done best", best)
