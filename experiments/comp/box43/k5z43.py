#!/usr/bin/env python3
"""L-COMP box 43 item 1 (b): every (K5) failure of the lifted counters, classified. For each (mover x, successor y, step t) with
class_(t+1)(x) < class_t(y) (lev43's k5, W = the escapes): check R118 (c) DOM in VALUES, Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)) [domfail, must be 0:
DOM holds for Howard on every game], then z := the most relevant vertex of Π(ext(x, Ω_t(y))) Δ Π_(t+1)(x). Box 208's (K5) proof is
DOM + «x has priority 0 … ext(x, ·) adds nothing to Π» + (K2) COARSE, and (K2) needs z to be an e-vertex (E-DOM). Tally of z:
  zodd  = z is ODD, not an escape, more relevant than the least relevant escape (E-DOM fails at z);
  zmov  = z = x itself (the mover is more relevant than an escape: [DEF] «Even movers of priority 0» fails);
  zeven = z even, not an escape, above the least relevant escape;  zesc = z is an escape (would contradict (K2)'s proof);  zlow = other.
Usage: k5z43.py lmcs|switchall NMIN NMAX"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lev43
from n5b import SpecSI
for N in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
    g, st, names = (lev43.lmcs if sys.argv[1] == "lmcs" else lev43.switchall)(N); Hs = lev43.howard(g, st); W = lev43.escapes(g); si = SpecSI(g)
    rk = lambda v: (g.prio[v], v); lo = min(W, key=rk); bit = {v: 1 << i for i, v in enumerate(sorted(W, key=rk))}
    cl = lambda val: ((g.prio[val[0]] if g.prio[val[0]] % 2 == 0 else -g.prio[val[0]]), sum(bit[u] for u in val[1] if u in bit))
    c = collections.Counter(); zs = collections.Counter()
    for t in range(len(Hs) - 1):
        v0, v1 = Hs[t][0], Hs[t + 1][0]
        for x in range(g.n):
            if g.owner[x] != 0 or len(set(g.succ[x])) < 2: continue
            for y in g.succ[x]:
                if not cl(v1[x]) < cl(v0[y]): continue
                c["k5"] += 1
                e = (v0[y][0], frozenset(v0[y][1]) | ({x} if rk(x) > rk(v0[y][0]) else frozenset()), v0[y][2] + 1)
                if si.nvo(v1[x], e) < 0: c["domfail"] += 1
                D = set(e[1]) ^ set(v1[x][1])
                if not D: c["zlow"] += 1; continue
                z = max(D, key=rk)
                k = "zesc" if z in W else "zmov" if z == x else "zlow" if rk(z) < rk(lo) else "zodd" if g.prio[z] % 2 else "zeven"
                c[k] += 1; zs[names[z].rstrip("0123456789")] += 1
    print("%s N %d T %d | %s | z by name: %s" % (sys.argv[1], N, len(Hs) - 1, " ".join("%s %d" % (k, c[k]) for k in ("k5", "domfail", "zodd", "zmov", "zeven", "zesc", "zlow")),
          " ".join("%s %d" % kv for kv in sorted(zs.items()))), flush=True)
