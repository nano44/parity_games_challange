#!/usr/bin/env python3
"""box 80: pulse structure of doubling levels. For each level l >= 1 that doubles: per l-window the steps u1 < u2 of the two moves;
pulse length u2 - u1; window length; first-mover identity; and for l = 0 the moves."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'box76'))
import collections
from sim80 import Sim, stats, keyorder, capped
for p in sys.argv[1:]:
    G = json.load(open(p)); sim = Sim(G); S = sim.run(); T, F, mv = stats(sim, S); h = capped(F)
    O = [keyorder(sim, s) for s in S]
    print(p.split("/")[-1], "T", T, "capped", h)
    for l in range(0, min(h + 1, sim.N // 2)):
        mvs = [t for t in range(1, T + 1) if S[t][2 * l] != S[t - 1][2 * l] or S[t][2 * l + 1] != S[t - 1][2 * l + 1]]
        edges = [t for t in range(1, T + 1) if O[t][l] != O[t - 1][l]]
        if l == 0:
            print("  l 0 moves at", mvs, "edges", edges); continue
        b = [t for t in range(1, T + 1) if O[t][l - 1] != O[t - 1][l - 1]]
        bnd = [1] + b + [T + 1]
        pl = []; wl = []
        for a, z in zip(bnd, bnd[1:]):
            if a == z: continue
            m = [t for t in mvs if a <= t < z]; wl.append(z - a)
            pl.append(m[1] - m[0] if len(m) == 2 else None)
        print("  l %d F %d windows %d pulse-length hist %s window-length min %d" % (l, F[l], len(wl),
              dict(sorted(collections.Counter(pl).items(), key=lambda kv: (kv[0] is None, kv[0] or 0))), min(wl)))
