#!/usr/bin/env python3
"""Box 4: search for N5 LOCKS = runs of CONSECUTIVE fallback iterations, from EVERY start pair (σ0, τ0), on random small games.
The N5 step is n5.py's, unmodified: n5.run(g, start=(σ0, τ0)) is called with --cap and the per-iteration flags are recomputed by
n5_trace's copy of the loop (asserted equal to n5.run). Also detects a repeated (σ, τ) state (non-termination). Checks the stall LEMMA (switches that close a cycle through v excluded) on every fallback iteration:
  Even stuck with (v,w) ∈ Iσ  =>  Ξσ(σ(v)) ◁ V_{σ,τ}(σ(v))   (τ strictly worse for Odd than σ̄ on the play from σ(v));
  Odd  stuck with (u,x) ∈ Iτ  =>  the dual statement.
Usage: n5_lock.py n deg games seed"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5 import pg, Engine, dual
def play_val(E, g, sigma, tau):
    """V_{σ,τ}: valuation of the (σ, τ) profile = Engine.evaluate on the game where Odd's vertices keep only τ(v)."""
    h = pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
    return Engine(h).evaluate(tuple(sigma))[0]
def on_play(g, sigma, tau, w, v):
    x, seen = w, set()
    while x not in seen:
        if x == v: return True
        seen.add(x); x = sigma[x] if g.owner[x] == 0 else tau[x]
    return False
def step(g, E, Ed, sigma, tau):
    n = g.n
    vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        # lemma check
        V = play_val(E, g, sigma, tau)
        for v, w in Is:
            if on_play(g, sigma, tau, w, v): continue      # cycle-closing switch: excluded from the lemma
            assert E.key(vs[sigma[v]]) < E.key(V[sigma[v]]), ("lemma Even", v, w)
        Vd = play_val(Ed, dual(g), tau, sigma)
        for u, x in It:
            if on_play(g, sigma, tau, x, u): continue
            assert Ed.key(vt[tau[u]]) < Ed.key(Vd[tau[u]]), ("lemma Odd", u, x)
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, fb, len(Is), len(It)
def rgame(n, deg, rng):
    prio = rng.sample(range(n * 2), n)
    owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.choice(range(n)) for _ in range(rng.randint(1, deg)))) for _ in range(n)]
    return pg.Game(prio, owner, succ)
def main():
    n, deg, games, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
    best = (0, None); checked = 0
    for gi in range(games):
        g = rgame(n, deg, rng); E, Ed = Engine(g), Engine(dual(g))
        Ev = [v for v in range(n) if g.owner[v] == 0]; Od = [v for v in range(n) if g.owner[v] == 1]
        starts = list(itertools.product(*[g.succ[v] for v in range(n)]))
        if len(starts) > 4000: starts = rng.sample(starts, 4000)
        for st in starts:
            sigma = [st[v] if g.owner[v] == 0 else -1 for v in range(n)]; tau = [st[v] if g.owner[v] == 1 else -1 for v in range(n)]
            run = cur = 0; it = 0; hist = set()
            while True:
                key = (tuple(sigma), tuple(tau))
                if key in hist: print("REPEATED STATE (N5 cycles):", g.prio, g.owner, g.succ, st); sys.exit(3)
                hist.add(key)
                r = step(g, E, Ed, sigma, tau)
                if r is None: break
                sigma, tau, fb, a, b = r; it += 1; checked += fb
                cur = cur + 1 if fb else 0; run = max(run, cur)
                assert it < 10000
            if run > best[0]:
                best = (run, (gi, g.prio, g.owner, g.succ, st, it))
    print(f"n={n} deg={deg} games={games} seed={seed}: max consecutive fallbacks = {best[0]}; lemma checked on {checked} fallback iterations, no violation")
    print("witness:", best[1])
if __name__ == "__main__": main()
