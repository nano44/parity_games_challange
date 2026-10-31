#!/usr/bin/env python3
"""L-RED R142: second BIP(rho, tau) engine on L-SI's experiments/si/si.py (as experiments/new/n5.py uses it), independent of n5b.
Same definition as bip.py. Usage: bip2.py GAME.pg RHO_TAU_SIGMA.start  (prints steps)"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("si", "harness", "new"): sys.path.insert(0, os.path.join(EXP, p))
import pg
from si import Engine
from n5 import dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n; d = {}
for l in open(sys.argv[2]):
    a = l.split(); d[a[0]] = dict(map(int, x.split(":")) for x in a[1:])
rho = [d["RHO"].get(v, -1) for v in range(n)]; tau = [d["TAU0"].get(v, -1) for v in range(n)]; sig = [d["SIGMA0"].get(v, -1) for v in range(n)]
Er = Engine(pg.Game(list(g.prio), list(g.owner), [[rho[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
it = 0
while it < 10000:
    vr, _ = Er.evaluate(tuple(sig)); I = Er.improving(tuple(sig), vr)
    if not I: break
    opt = {v: {sig[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in I: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    ns = [best[v] if g.owner[v] == 0 else -1 for v in range(n)]
    if ns == sig: break
    sig = ns; it += 1
print(f"BIP2 {os.path.basename(sys.argv[1])} n {n} steps {it}")
