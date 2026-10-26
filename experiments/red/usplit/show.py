#!/usr/bin/env python3
"""Print an N5 trace (o1_19.trace): per state, D, fallback flag, σ of chosen vertices, Ξ/W path weights of chosen vertices.
Usage: show.py game.pg start.json v1,v2,..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1")); sys.path.insert(0, os.path.join(HERE, "..", "rec0"))
import o1_19 as O, pg, rec0_20 as R0
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = json.load(open(sys.argv[2]))["start"]
vs = [int(x) for x in sys.argv[3].split(",")]
S, FB, E = O.trace(g, st)
for k, (s, t) in enumerate(S):
    X, SB = E.evaluate(s)
    D = [u for u in range(g.n) if g.owner[u] == 1 and SB[u] != t[u]]
    W = [R0.playval(g, E, s, t, x) for x in range(g.n)]
    print(k, "FB" if k < len(FB) and FB[k] else "--", "D", D, " ".join(f"{v}:σ{s[v] if g.owner[v] == 0 else t[v]} Ξ{E.weight(X[v][1])}/W{E.weight(W[v][1])} c{X[v][0]}" for v in vs))
print("ITER", len(FB), "FB", sum(1 for f in FB if f))
