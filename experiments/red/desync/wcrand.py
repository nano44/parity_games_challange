#!/usr/bin/env python3
"""L-RED R135: random falsification test of Lemma WAIT-CYCLE on real N5 runs (n5b SPEC).
At each state s and Even X, each successor g != sigma(X) that is NOT offered at X (not in I_sigma(X)) and whose sigma-bar-play passes X before
repeating a vertex (X itself not on its own play's cycle) is recorded with its Even pattern on pi (the play from g to X). A VIOLATION is a later
state with sigma(X) = g and the same Even pattern on pi. Lemma WAIT-CYCLE says: 0 violations.
Usage: wcrand.py SEED GAMES NMIN NMAX   |   wcrand.py --game GAME.pg START (one given game and start pair)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
GIVEN = sys.argv[1] == "--game"
if GIVEN: seed, games, nmin, nmax = 0, 1, 0, 0
else: seed, games, nmin, nmax = map(int, sys.argv[1:5])
rng = random.Random(seed)
rec_total = viol = runs = 0
for _ in range(games):
    n = rng.randint(nmin, nmax)
    pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    sc = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    g = n5b.pg.Game(pr, ow, sc) if not GIVEN else n5b.pg.read(sys.argv[2]); n = g.n; N = n5b.N5(g); N.mode = "spec"; tr = []
    st = n5b.read_start(sys.argv[3], g) if GIVEN else (None, None)
    try: N.run(st[0], st[1], trace=tr)
    except Exception: continue
    runs += 1; recs = {}
    for s_i, (sig, tau) in enumerate(tr):
        vs, sbar = N.opt(N.SG, list(sig)); Is = N.improving(N.SG, sig, N.ev(N.SG, list(sig)))
        nxt = lambda v: sig[v] if g.owner[v] == 0 else sbar[v]
        for X in range(n):
            if g.owner[X] != 0: continue
            for (Xr, gg), pats in list(recs.items()):
                if Xr == X and sig[X] == gg and any(all(sig[v] == w for v, w in p) for p in pats): viol += 1; print("VIOLATION", seed, pr, ow, sc, X, gg, s_i)
            seen, y = set(), sig[X]
            while y not in seen and y != X: seen.add(y); y = nxt(y)
            if y == X: continue                                    # X on its own play's cycle: outside the lemma
            for gg in g.succ[X]:
                if gg == sig[X] or gg in Is.get(X, []): continue
                path, y, ok = [], gg, False
                while y not in path:
                    if y == X: ok = True; break
                    path.append(y); y = nxt(y)
                if ok:
                    pat = tuple((v, sig[v]) for v in path if g.owner[v] == 0)
                    recs.setdefault((X, gg), set()).add(pat); rec_total += 1
print(f"WCRAND seed {seed} runs {runs} self-routed-blocks {rec_total} violations {viol}")
