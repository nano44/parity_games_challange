#!/usr/bin/env python3
"""Box 8: test invariant SB2 for switch-best on ONE-PLAYER games: every step either settles a new vertex (Ω = Ω*) or strictly raises
some vertex's cycle node in VJ00's reward order. (SB2 gives #steps ≤ n + n(n-1).) Random one-player games with cycles, random starts,
plus files given. Usage: sb_settle2.py games seed nmax [extra.pg ...]"""
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
    V = [E.evaluate(tuple(t))[0] for t in traj]; opt = [E.key(x) for x in V[-1]]
    bad = []
    for k in range(len(traj) - 1):
        newset = any(E.key(V[k + 1][v]) == opt[v] and E.key(V[k][v]) != opt[v] for v in range(g.n))
        lamup = any(E.rew[V[k + 1][v][0]] != E.rew[V[k][v][0]] for v in range(g.n))
        if not newset and not lamup: bad.append(k)
    return len(traj) - 1, bad
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); fails = runs = 0; ex = None
gl = []
for _ in range(games):
    n = rng.randint(3, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    gl.append(pg.Game(pr, owner, succ))
for p in sys.argv[4:]: gl.append(pg.read(p))
for g in gl:
    for _ in range(4):
        s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
        L, bad = run(g, s); runs += 1
        if bad: fails += 1; ex = ex or (pg.dumps(g), s, bad)
print(f"runs={runs} runs with a step that neither settles a vertex nor raises a cycle node: {fails}")
if ex: print(ex)
