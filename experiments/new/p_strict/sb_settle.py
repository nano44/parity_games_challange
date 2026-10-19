#!/usr/bin/env python3
"""Box 8: test the potentials (#settled, #cycle-node-optimal) and the 'settling' hypothesis for switch-best on ONE-PLAYER games (Odd out-degree 1): every switch-best step makes at least
one more vertex reach its optimal valuation Ω* (then #steps ≤ n). Games: random one-player games with cycles, random starts, plus the
climbed instances given on the command line. Switch-best = N5 on a one-player game (n5.run is not used; the step is sbstep as in
sb_flipback.py). Usage: sb_settle.py games seed nmax [extra.pg ...]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def run(g, s):
    E = Engine(g); traj = [list(s)]
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: break
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(sb); traj.append(s)
    fin = E.evaluate(tuple(traj[-1]))[0]; opt = [E.key(x) for x in fin]
    settled = [sum(E.key(x) == o for x, o in zip(E.evaluate(tuple(t))[0], opt)) for t in traj]
    lam = [sum(x[0] == f[0] for x, f in zip(E.evaluate(tuple(t))[0], fin)) for t in traj]
    return len(traj) - 1, (settled, lam)
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); fails = fails2 = fails3 = runs = 0; ex2 = None; worst = 0; ex = None
gl = []
for _ in range(games):
    n = rng.randint(3, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    gl.append(pg.Game(pr, owner, succ))
for p in sys.argv[4:]: gl.append(pg.read(p))
for g in gl:
    for _ in range(3):
        s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
        L, (st, lm) = run(g, s); runs += 1; worst = max(worst, L - g.n)
        if any(st[k + 1] <= st[k] for k in range(L)): fails += 1; ex = ex or (g.n, L, st, lm)
        f2 = any(st[k + 1] + lm[k + 1] <= st[k] + lm[k] for k in range(L)); fails2 += f2; ex2 = ex2 or ((g.n, L, st, lm) if f2 else None)
        f3 = any((lm[k + 1], st[k + 1]) <= (lm[k], st[k]) for k in range(L)); fails3 += f3
print(f"runs={runs} non-settling step: {fails} | settled+lambda-optimal not increasing: {fails2} | (lambda-opt, settled) lex not increasing: {fails3} | max(steps - n)={worst}")
print("example settled/lambda:", ex2)
