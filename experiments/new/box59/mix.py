#!/usr/bin/env python3
"""L-NEW box 62: N5 / N5-SF frame mixes. Same loop as box54/n5sf.py; EOPP = who Odd plays in Even's arena (S4a): 'tau' (N5) or 'sbar'
(N5-SF); OOPP = who Even plays in Odd's arena (S4b): 'sigma' (N5) or 'tbar' (N5-SF). Improving sets, S4c, S5 as SPEC.
EOPP=tau OOPP=sigma reproduces N5 (asserted on the first call against box21 n5x.trace when CHECK=1). Usage: mix.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54"))
import n5sf, pg
from n5x import Engine, dual, load
EO, OO = os.environ.get("EOPP", "tau"), os.environ.get("OOPP", "sigma")
def step(g, E, Ed, sigma, tau):
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    oppE = sbar if EO == "sbar" else tau
    oppO = tbar if OO == "tbar" else sigma
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [oppE[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(oppE[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [oppO[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(oppO[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb, vs, sbar
n5sf.step = step
g = load(sys.argv[1]); E, T = n5sf.trace(g)
runs, cur = [], 0
for a, b in zip(T, T[1:]):
    if a["t"] != b["t"]: runs.append(cur); cur = 0
    if a["s"] != b["s"]: cur += 1
runs.append(cur)
m = sum(len(set(x)) for x in g.succ)
print(f"MIX {os.path.basename(sys.argv[1])} EOPP {EO} OOPP {OO} iterations {len(T) - 1} cycle {T[-1].get('cycle', False)} "
      f"tau-changes {sum(1 for a, b in zip(T, T[1:]) if a['t'] != b['t'])} n {g.n} n+m {g.n + m} max-tau-stretch {max(runs)}", flush=True)
