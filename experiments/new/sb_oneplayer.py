#!/usr/bin/env python3
"""Box 6 (K8, constant case): hill climb for long SWITCH-BEST runs on ONE-PLAYER games (every Odd vertex has one successor, so Odd's
reply is constant). Switch-best step = optimum of the improvement arena H_σ (switch-all SI on H_σ, si.py Engine.run).
Mutations: edge target / priority swap (Odd vertices keep out-degree 1). Usage: sb_oneplayer.py n steps seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5 import pg, Engine
def sblen(g, cap=10000):
    E = Engine(g); s = list(E.initial("best")); k = 0
    while k < cap:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: return k
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(sb); k += 1
    return k
n, steps, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
best = sblen(pg.Game(prio, owner, succ)); cur = (prio, owner, succ); print("start", best, flush=True)
for s_ in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]
    if rng.random() < 0.7:
        v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
        if ow[v] == 0 and rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    else:
        a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    f = sblen(pg.Game(pr, ow, sc))
    if f >= best:
        if f > best: print(f"step {s_} switch-best steps {f}", flush=True)
        best, cur = f, (pr, ow, sc)
print("best", best)
