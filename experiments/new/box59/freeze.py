#!/usr/bin/env python3
"""L-NEW box 63: ODD-FREEZE probe on plain N5 (box21/n5x.trace, S3 start). For every tau-change at an Odd vertex o from e to e' (k -> k+1):
H(k+1) := under (tau_(k+1), its Even best reply tbar(tau_(k+1)) [Ed.evaluate]) the play from e reaches o before repeating a vertex, and the
most relevant vertex on that path e..o (o included) has even priority. RET := tau_l(o) = e again for some l > k+1. Counts leaves, H-leaves,
returns, H-returns (= kill instances of ODD-FREEZE in its at-leave-time form). Usage: freeze.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, Engine, dual, readstart
g = load(sys.argv[1]); n = g.n; Ed = Engine(dual(g)); E = Engine(g)
st, fb = trace(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None, check=False)
def H(t, e, o):
    _, tb = Ed.evaluate(t); v = e; path = []; seen = set()
    while v not in seen:
        seen.add(v); path.append(v)
        if v == o: break
        v = t[v] if g.owner[v] == 1 else tb[v]
    if path[-1] != o: return False
    top = max(path, key=lambda x: E.rank[x]); return g.prio[top] % 2 == 0
L = Hn = R = HR = 0; kill = None
for k in range(len(st) - 1):
    t, t2 = st[k][1], st[k + 1][1]
    for o in range(n):
        if g.owner[o] != 1 or t[o] == t2[o]: continue
        e = t[o]; L += 1; h = H(t2, e, o); Hn += h
        ret = any(st[l][1][o] == e for l in range(k + 2, len(st)))
        R += ret; HR += h and ret
        if h and ret and kill is None: kill = (k, o, e)
print(f"FREEZE {os.path.basename(sys.argv[1])} n {n} N5_iter {len(st) - 1} leaves {L} H-leaves {Hn} returns {R} H-returns {HR} kill {kill} {'PASS' if HR == 0 else 'KILL'}", flush=True)
