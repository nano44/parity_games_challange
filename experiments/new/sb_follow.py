#!/usr/bin/env python3
"""Box 5: climb (from a given game, perturbation mutations as n5_perturb.py) maximising how long N5 follows SWITCH-BEST's exact
σ-trajectory (sb_traj.py's test), with switch-best's own length as tie-break: fitness = (follow, switch-best steps). Each improved
best is checked (zielonka.py + verify.py on N5's output; n5.run unmodified) and saved.
Usage: sb_follow.py game.pg steps seed OUT.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, verify, n5
from n5_lock import step
from n5 import Engine, dual
def follow(g, cap=400):
    E, Ed = Engine(g), Engine(dual(g))
    def sbstep(s):
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: return None
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb)
    traj = [list(E.initial("best"))]
    while len(traj) < cap:
        nx = sbstep(traj[-1])
        if nx is None: break
        traj.append(nx)
    s, t = list(E.initial("best")), list(Ed.initial("best")); k = 0
    while k + 1 < len(traj):
        r = step(g, E, Ed, s, t)
        if r is None or r[0] != traj[k + 1]: break
        s, t = r[0], r[1]; k += 1
    return k, len(traj) - 1
g0 = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); steps, seed, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed); n = g0.n; cur = (list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]); best = follow(g0); print("start", best, flush=True)
for s_ in range(steps):
    pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; k = rng.random()
    if k < 0.6:
        v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
    elif k < 0.9:
        a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    else:
        v = rng.randrange(n); ow[v] = 1 - ow[v]
    g = pg.Game(pr, ow, sc)
    try: f = follow(g)
    except RuntimeError: continue
    if f >= best:
        if f > best:
            it, fb, win, ws, _ = n5.run(g, cap=20000); ok = win == zielonka.solve(g) and not verify.check(g, win, list(ws))
            print(f"step {s_} follow {f[0]} of switch-best {f[1]} (N5 iterations {it}) check {'OK' if ok else 'FAIL'}", flush=True)
            open(out, "w").write(pg.dumps(g))
        best, cur = f, (pr, ow, sc)
print("best", best)
