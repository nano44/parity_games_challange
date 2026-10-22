#!/usr/bin/env python3
"""Box 9 (phase variant, sb_union_phase.py): U is RESET whenever some vertex's cycle node changes (a new λ-phase). Original: switch-best on ONE-PLAYER games. U_k = union of the arenas H_0..H_k. Tests (a) I_{k+1} ∩ H_k = ∅ (provable: the arena
optimum has no improving arena edge); (b) every step's arena brings at least one edge never in U_k (would give #steps ≤ |E|);
(c) whether ρ_{k+1} is optimal in U_k. Usage: sb_union_phase.py games seed nmax [inst.pg ...]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def arena_opt(g, s, A):
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(x), Eh
def run(g, s):
    E = Engine(g); U = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}; Hprev = None; fa = fb = fc = 0; k = 0; lamprev = None
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        lam = tuple(vs[x][0] for x in range(g.n))
        if Hprev is not None and lam != lamprev:
            U = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
        lamprev = lam
        if Hprev is not None:
            fa += any(w in Hprev[v] for v, w in Is)
            fb += not any(w not in U[v] for v, w in Is) and bool(Is)
        if not Is: return k, fa, fb, fc
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        for v in A: U[v] |= A[v]
        s2, _ = arena_opt(g, s, A)
        su, Eu = arena_opt(g, s, U); vu = Eu.evaluate(tuple(su))[0]; v2 = Eu.evaluate(tuple(s2))[0]
        fc += any(Eu.key(vu[x]) != Eu.key(v2[x]) for x in range(g.n))
        Hprev = A; s = s2; k += 1
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); T = [0, 0, 0, 0]; runs = 0
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
        r = run(g, list(s)); runs += 1
        for i in range(4): T[i] += r[i] > 0 if i else 0
print(f"runs={runs}: runs violating (a) I_(k+1) ∩ H_k = ∅: {T[1]}; runs with a step bringing NO never-seen edge: {T[2]}; runs where ρ_(k+1) is not optimal in U_k: {T[3]}")
