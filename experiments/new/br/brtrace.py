#!/usr/bin/env python3
"""Box 11: per-iteration trace of best-reply states along N5's run: id of σ̄_k among the distinct σ̄ seen so far (A, B, ...), same for τ̄_k,
Even/Odd moves, fallback. Shows toggling (global returns). Usage: brtrace.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
g = pg.read(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
ids = {"sb": {}, "tb": {}}
def lab(key, st):
    d = ids[key]
    if st not in d: d[st] = chr(65 + len(d)) if len(d) < 26 else str(len(d))
    return d[st]
k = 0; line = []
while True:
    sb = tuple(E.evaluate(tuple(s))[1][v] for v in O); tb = tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
    r = step(g, E, Ed, s, t)
    if r is None: break
    em = [(v, s[v], r[0][v]) for v in V0 if r[0][v] != s[v]]; om = [(v, t[v], r[1][v]) for v in O if r[1][v] != t[v]]
    print(f"it {k}: σ̄={lab('sb', sb)} τ̄={lab('tb', tb)} | Even moves {em} | Odd moves {om} {'fb' if r[2] else ''}")
    s, t = r[0], r[1]; k += 1
print("distinct σ̄ states", len(ids["sb"]), "distinct τ̄ states", len(ids["tb"]))
for st, l in ids["sb"].items(): print(" σ̄", l, dict(zip(O, st)))
