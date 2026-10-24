#!/usr/bin/env python3
"""Box 25: like wdrop_find.py but CANONICAL start (best-reward), o-cyclic C^1O. Usage: wdrop_canon.py nmin nmax tries seed out"""
from common import *
from abovefind import write
from wdrop_find import hit
if __name__ == "__main__":
    lo, hi, tries, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]; rng = random.Random(seed)
    for n in range(lo, hi + 1):
        for _ in range(tries):
            g = rand_c1o(rng, n, n, forced=0.0)
            if g is None: continue
            h = hit(g, None)
            if h:
                E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None)
                write(g, ({v: s[v] for v in range(n) if g.owner[v] == 0}, {v: t[v] for v in range(n) if g.owner[v] == 1}), out)
                print("n", n, "fallback at state", h[0], "W drops at", h[1]); sys.exit(0)
    print("none")
