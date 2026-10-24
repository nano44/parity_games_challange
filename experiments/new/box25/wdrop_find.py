#!/usr/bin/env python3
"""Box 25: smallest C^1O game + start pair where an Even fallback step (τ fixed) LOWERS W = V_{σ,τ} at some vertex.
Searches n = nmin.. upward (random games, random starts), writes the first hit. Usage: wdrop_find.py nmin nmax tries seed out [--acyclic]"""
from common import *
from abovefind import write
def hit(g, start):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: return None
        ns, nt, Is, It, fb, _, _ = r
        if fb and list(nt) == list(t):
            Eg, W0 = wvals(g, s, t); _, W1 = wvals(g, ns, t)
            bad = [v for v in range(g.n) if Eg.key(W1[v]) < Eg.key(W0[v])]
            if bad: return k, bad
        s, t = ns, nt; k += 1
if __name__ == "__main__":
    lo, hi, tries, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    cyc = "--acyclic" not in sys.argv; rng = random.Random(seed)
    for n in range(lo, hi + 1):
        for _ in range(tries):
            g = rand_c1o(rng, n, n, cyclic=cyc, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 1})
            h = hit(g, start)
            if h: write(g, start, out); print("n", n, "fallback at state", h[0], "W drops at", h[1]); sys.exit(0)
    print("none")
