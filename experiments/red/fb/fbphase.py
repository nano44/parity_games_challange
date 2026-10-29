#!/usr/bin/env python3
"""L-RED successor 24: f = in-phase fallbacks per phase (CONJECTURE FB-LIN: f <= n). A phase = maximal stretch of states with tau and both
cycle-node maps (Xi_sigma, Xi_tau) constant (as phsw.py); a fallback transition i -> i+1 is in-phase if lam[i] == lam[i+1].
Usage: fbphase.py GAME.pg START|S3 [...]   prints n, iterations, max f, phase, fallback-free run max, f/n."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T

def fstats(g, start, cap=10 ** 5):
    states = []; it, fb, ph, mp, s, t, hist = T.run(g, start, cap=cap, log=lambda *a: None, states=states)
    if len(states) == len(hist): raise RuntimeError("cap reached")
    E, Ed = T.Engine(g), T.Engine(T.dual(g))
    lam = [(t, tuple(x[0] for x in E.evaluate(s)[0]), tuple(x[0] for x in Ed.evaluate(t)[0])) for s, t in states]
    best = (0, None); a = 0; cur = 0
    for i, (kind, sw, tw) in enumerate(hist):
        if lam[i + 1] != lam[i]:
            cur = 0; a = i + 1; continue
        if kind == "FB":
            cur += 1
            if cur > best[0]: best = (cur, a)
    return best[0], best[1], it

MODE_RF = 2   # 1: RF = in-phase fallbacks re-switching a vertex already fallback-switched in the phase; 2: R1 = the same over single-switch fallbacks only; 3: FM = in-phase fallbacks switching >= 2 vertices (carries); 4: CR = multi-switch fallbacks re-switching a vertex any earlier in-phase fallback switched; 0: vertices switched >= 2 times
def reuse(g, start, cap=10 ** 5):
    """(f, R): f as fstats; R = number of Even vertices switched by in-phase fallbacks >= 2 times inside the phase with the largest R."""
    states = []; it, fb, ph, mp, s, t, hist = T.run(g, start, cap=cap, log=lambda *a: None, states=states)
    if len(states) == len(hist): raise RuntimeError("cap reached")
    E, Ed = T.Engine(g), T.Engine(T.dual(g))
    lam = [(t, tuple(x[0] for x in E.evaluate(s)[0]), tuple(x[0] for x in Ed.evaluate(t)[0])) for s, t in states]
    bestf = bestR = 0; cnt = {}; cur = 0; rf = 0
    for i, (kind, sw, tw) in enumerate(hist):
        if lam[i + 1] != lam[i]: cnt = {}; cur = 0; rf = 0; continue
        if kind == "FB":
            cur += 1; bestf = max(bestf, cur)
            if MODE_RF == 1 and any(v in cnt for v in sw): rf += 1
            if MODE_RF == 2 and len(sw) == 1 and sw[0] in cnt: rf += 1
            if MODE_RF == 3 and len(sw) >= 2: rf += 1
            if MODE_RF == 4 and len(sw) >= 2 and any(v in cnt for v in sw): rf += 1
            if MODE_RF != 2 or len(sw) == 1:
                for v in sw: cnt[v] = cnt.get(v, 0) + 1
            bestR = max(bestR, rf) if MODE_RF else max(bestR, sum(1 for c in cnt.values() if c >= 2))
    return bestf, bestR

if __name__ == "__main__":
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        g = T.pg.parse("".join(l for l in open(a[i]) if not l.lstrip().startswith("%")))
        st = ({}, {}) if a[i + 1] == "S3" else T.readstart(a[i + 1])
        f, ph, it = fstats(g, st)
        print("%s n=%d iterations=%d maxf=%d (phase from state %s) f/n=%.3f" % (os.path.basename(a[i]), g.n, it, f, ph, f / g.n))
