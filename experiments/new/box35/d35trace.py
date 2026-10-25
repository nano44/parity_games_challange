#!/usr/bin/env python3
"""Box 35: per-state trace of an N5 run on a C^1O game around H1-drops: phase key, h1, h2, sigma-bar(o), theta, |R|, fb, and Even's
switches with Xi values on o's honest path. Usage: d35trace.py game.pg [k0 k1]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
from relfr import *

def hpath(g, s, sb, o, v):
    nx = lambda u: s[u] if g.owner[u] == 0 else sb[u]
    p, seen = [v], {v}
    while True:
        u = nx(p[-1])
        if u in seen: return p, u
        p.append(u); seen.add(u)

if __name__ == "__main__":
    g = load(sys.argv[1]); E = Engine(g); o = odd1(g)
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, _ = rows_w(g); k0, k1 = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, len(rows) - 1)
    print("o", o, "succ", sorted(set(g.succ[o])), "n", g.n)
    for k in range(k0, k1 + 1):
        r = rows[k]; s = r["s"]; Xi = r["Xi"]; _, sb = E.evaluate(tuple(s))
        p, back = hpath(g, s, sb, o, o)
        pi = {v: g.prio[v] for v in p}
        print(f"k{k} ph{hash(r['ph'])%1000:03d} h1={int(r['h1'])} h2={int(h2(r['nxt'], o))} sb(o)={sb[o]} th={Xi[o]} w={r['W'][o]} |R|={len(r['R'])} fb={r['fb']}")
        print("   honest path o:", [(v, g.prio[v]) for v in p], "-> back to", back)
        if k < len(rows) - 1:
            t = rows[k + 1]["s"]; ch = [(v, s[v], t[v]) for v in range(g.n) if g.owner[v] == 0 and s[v] != t[v]]
            print("   Even switches ->", ch)
