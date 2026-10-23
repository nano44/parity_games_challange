#!/usr/bin/env python3
"""Box 21 probe E2: hill-climb random games for long FIXED-OPPONENT Even chains.
mode tstar: N5 (unmodified loop, n5x.trace) from (best-reward sigma_0, tau*), tau* = final tau of the plain run (Iτ* = ∅,
            so Odd never moves; this is a genuine N5 run from a start pair).
mode tany : Even-only dynamics with an ARBITRARY frozen tau (Odd's step suppressed; not an N5 run): sigma' = N5's S4a step
            against tau, S4c Even fallback if it stalls. The fitness is the max over K random taus (fixed per game).
Usage: climb_fix.py MODE n seed secs outprefix"""
import sys, random, time
from n5x import *
def randgame(rng, n):
    prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
    return [prio, owner, succ]
def mutate(rng, G):
    prio, owner, succ = [list(G[0]), list(G[1]), [list(s) for s in G[2]]]; n = len(prio)
    for _ in range(rng.choice((1, 1, 2, 3))):
        k = rng.randrange(5); v = rng.randrange(n)
        if k == 0: prio[v] = rng.randrange(n)
        elif k == 1: owner[v] ^= 1
        elif k == 2: succ[v] = sorted(set(succ[v]) | {rng.randrange(n)})
        elif k == 3 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
        else:
            w = rng.randrange(n); succ[v] = sorted(set(succ[v]) - {rng.choice(succ[v])} | {w}) or [w]
    return [prio, owner, succ]
def fit_tstar(G):
    g = pg.Game(*G); states, _ = trace(g, check=False)
    s0, ts = states[0][0], states[-1][1]
    st = ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: ts[v] for v in range(g.n) if g.owner[v] == 1})
    fs, _ = trace(g, st, check=False); return len(fs) - 1
def maxphase(g, states):
    """max number of N5 iterations inside one joint λ-phase (honest cycle-node maps of Ξσ and Ξτ both constant)."""
    E, Ed = Engine(g), Engine(dual(g)); lam = []
    for s, t in states:
        lam.append((tuple(x[0] for x in E.evaluate(s)[0]), tuple(x[0] for x in Ed.evaluate(t)[0])))
    best = cur = 0
    for k in range(1, len(states)):
        cur = cur + 1 if lam[k] == lam[k - 1] else 1   # iteration k belongs to the phase of its END state
        best = max(best, cur)
    return best
def fit_tstarph(G):
    g = pg.Game(*G); states, _ = trace(g, check=False)
    s0, ts = states[0][0], states[-1][1]
    st = ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: ts[v] for v in range(g.n) if g.owner[v] == 1})
    fs, _ = trace(g, st, check=False); return maxphase(g, fs)
def fit_plainph(G):
    g = pg.Game(*G); states, _ = trace(g, check=False); return maxphase(g, states)
def fit_bestph(G):
    """plain N5 from the best-reward start, counted only if Odd's best-reward tau_0 is already honest-optimal (Iτ0 = ∅):
    then the canonical N5 run IS a frozen-optimal-opponent run. Fitness = max iterations in one joint λ-phase (0 otherwise)."""
    g = pg.Game(*G); Ed = Engine(dual(g)); t0 = tuple(Ed.initial("best"))
    if Ed.improving(t0, Ed.evaluate(t0)[0]): return 0
    states, _ = trace(g, check=False); return maxphase(g, states)
def even_only(g, sigma, tau, cap=10 ** 5):
    E, Ed = Engine(g), Engine(dual(g)); k = 0
    while k < cap:
        vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if not Is: return k
        n = g.n; opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        ns = [best[v] if g.owner[v] == 0 else sigma[v] for v in range(n)]
        if ns == sigma:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        sigma = ns; k += 1
    return k
def fit_tany(G, K=6):
    g = pg.Game(*G); E, Ed = Engine(g), Engine(dual(g)); s0 = list(E.initial("best"))
    r = random.Random(str(G[0]) + str(G[2])); best = 0
    for _ in range(K):
        tau = [r.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(g.n)]
        best = max(best, even_only(g, list(s0), tau))
    return best
if __name__ == "__main__":
    mode, n, seed, secs, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    fit = {"tstar": fit_tstar, "tany": fit_tany, "tstarph": fit_tstarph, "plainph": fit_plainph, "bestph": fit_bestph}[mode]
    rng = random.Random(seed); G = randgame(rng, n); f = fit(G); t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1
        try: fh = fit(H)
        except Exception as e: continue
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                g = pg.Game(*H)
                with open(f"{out}.pg", "w") as fo:
                    fo.write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print(f"FINAL fit {f} iters {it}")
