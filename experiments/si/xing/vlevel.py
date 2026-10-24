#!/usr/bin/env python3
"""L-SI box 5 (C): per active fallback leaver y (THR fallback, w fixed since phase start segment), its own eviction level
lev(Ξ_k(y), Ξ_{k+1}(y)). (H-VL): with w constant, each (vertex, level) pair occurs at most once. Also (CL-v): the levels of a single
vertex's successive evictions never increase. Usage: vlevel.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carries import *

def scan2(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows: r["Xi"], _ = E.evaluate(tuple(r["s"]))
    rep = 0; incr = 0; ev = 0; ex = []
    for (x, y) in ph:
        seen = {}; lastlev = {}; w0 = None
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if a["w"] != w0: seen, lastlev, w0 = {}, {}, a["w"]
            if not a["fb"]: continue
            S, act, pas = classify(g, rows, k, o)
            for v, kd in act:
                if kd != "LF": continue
                l = lev(E, a["Xi"][v], b["Xi"][v]); ev += 1
                if (v, l) in seen: rep += 1; ex.append((v, l, seen[(v, l)], k))
                seen[(v, l)] = k
                if v in lastlev and l > lastlev[v]: incr += 1
                lastlev[v] = l
    return g.n, ev, rep, incr, ex[:4]

if __name__ == "__main__":
    T = [0, 0, 0]
    for p in sys.argv[1:]:
        n, ev, rep, incr, ex = scan2(p); T[0] += ev; T[1] += rep; T[2] += incr
        if ev: print(f"{os.path.basename(p):22s} n {n:3d} active fallback evictions {ev:3d} (vertex,level) repeats {rep:3d} per-vertex level increases {incr:3d} {ex}")
    print("TOTAL evictions, repeats, increases:", T)
