#!/usr/bin/env python3
"""Box 8: phase structure of switch-best on ONE-PLAYER games. A phase = maximal run of steps in which every vertex's cycle node is
unchanged. Reports max steps per phase and max number of phases, on random one-player games (random starts) and on given instances
(with .start files when present). The O(n^3) route needs: phases ≤ n(n-1)+1 (true by monotonicity) and steps per phase ≤ O(n).
Usage: sb_phaselen.py games seed nmax [inst.pg ...]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def run(g, s):
    E = Engine(g); lams = []
    while True:
        vs, _ = E.evaluate(tuple(s)); lams.append(tuple(vs[v][0] for v in range(g.n))); Is = E.improving(tuple(s), vs)
        if not Is: break
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(x)
    # phase lengths: steps k -> k+1 with lams[k+1] == lams[k] extend the current phase
    ph, cur = [], 0
    for k in range(len(lams) - 1):
        if lams[k + 1] == lams[k]: cur += 1
        else: ph.append(cur + 1); cur = 0
    ph.append(cur)
    return len(lams) - 1, max(ph), len(ph)
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); mx = (0, 0); ex = None
for _ in range(games):
    n = rng.randint(3, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(pr, owner, succ)
    for _ in range(3):
        s = [rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)]; L, mp, nph = run(g, s)
        if mp > mx[0]: mx = (mp, n); ex = (L, mp, nph)
print("random: max steps in one phase", mx[0], "(at n =", mx[1], ")", "example (steps, max phase, #phases)", ex)
for p in sys.argv[4:]:
    g = pg.read(p); s = [g.succ[v][0] for v in range(g.n)]
    if os.path.exists(p + ".start"):
        for tok in open(p + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s[a] = b
    print(os.path.basename(p), "n", g.n, "(steps, max steps in one phase, #phases)", run(g, s))
