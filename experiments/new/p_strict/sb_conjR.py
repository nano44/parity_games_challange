#!/usr/bin/env python3
"""Box 9, Conjecture R (one-player switch-best). Within a λ-phase (every vertex's cycle node unchanged), an improving edge (x, w) at step
k that was already in an arena H_j earlier in the same phase must be CYCLE-CLOSING at k (the ρ_k-play from w passes x). Also checks
the consequence used for the bound: every step whose improving set lies inside the phase union is followed by a λ change (or by
termination). Random one-player games + given instances (with .start). Usage: sb_conjR.py games seed nmax [inst.pg ...]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def play_passes(g, s, w, x):
    seen = set(); v = w
    while v not in seen:
        if v == x: return True
        seen.add(v); v = s[v] if g.owner[v] == 0 else g.succ[v][0]
    return False
def run(g, s):
    E = Engine(g); U = None; lamprev = None; badR = badC = 0; k = 0; pend = False
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); lam = tuple(vs[x][0] for x in range(g.n))
        if pend and lam == lamprev and Is: badC += 1          # an all-old step was not followed by a λ change
        pend = False
        if lam != lamprev: U = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
        lamprev = lam
        if not Is: return k, badR, badC
        old = [(v, w) for v, w in Is if w in U[v] and w != s[v]]
        badR += sum(not play_passes(g, s, w, v) for v, w in old)
        if not any(w not in U[v] for v, w in Is): pend = True
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        for v in A: U[v] |= A[v]
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(x); k += 1
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); runs = R = C = 0; ex = None
gl = []
for _ in range(games):
    n = rng.randint(3, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    gl.append((pg.Game(pr, owner, succ), None))
for p in sys.argv[4:]:
    g = pg.read(p); s = [g.succ[v][0] for v in range(g.n)]
    if os.path.exists(p + ".start"):
        for tok in open(p + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s[a] = b
    gl.append((g, s))
for g, s0 in gl:
    for _ in range(1 if s0 else 3):
        s = s0 or [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
        k, r, c = run(g, list(s)); runs += 1; R += r > 0; C += c > 0
        if (r or c) and not ex: ex = (pg.dumps(g), s, r, c)
print(f"runs={runs}: runs with a re-entering NON-cycle-closing edge: {R}; runs with an all-old step not followed by a λ change: {C}")
if ex: print(ex)
