#!/usr/bin/env python3
"""REFEREE climb for P-N5-SN Corollary ABS-COUNT: searches C^1O games for (a) an H1 eps-transition whose target state has not H1
(the case the packet's 'ends <= d_o - 1' step does not cover) and (b) a fallback-free run with #H1-eps > (d_o - 1) + REL_run.
Score = 100 * ABSC_FAIL + 10 * eps_H1_to_nH1 + OR_chk. Mutations keep exactly one Odd choice vertex (asserted by sn_probe.run).
FIT=h1drop scores the fixes-file §2b events instead.
Usage: absc_climb.py steps seed nmin nmax [out.pg] [seed.pg]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, sn_probe as SP


def score(g):
    c = Counter()
    try: SP.run(g, c)
    except AssertionError: raise
    if os.environ.get("FIT") == "h1drop":  # fixes §2b: in-phase H1 -> not H1 transitions, and failures of H1-DROP / H1-KEEP
        return 1000 * (c["H1DROP_FAIL"] + c["H1KEEP_FAIL"] + c["ABSCp_FAIL"]) + 10 * c["H1DROP_chk"] + c["eps_H1_Om1"] * 50 + c["OR_chk"], c
    return 100 * c["ABSC_FAIL"] + 100 * c["ABSC_phase_FAIL"] + 10 * c["eps_H1_to_nH1"] + c["OR_chk"], c


def mutate(rng, g, o):
    n = g.n; prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    m = rng.randrange(4)
    if m == 0: prio[rng.randrange(n)] = rng.randrange(n + 3)
    elif m == 1:
        v = rng.choice([v for v in range(n) if owner[v] == 0] or [o]); succ[v] = sorted(set(succ[v]) | {rng.randrange(n)})
    elif m == 2:
        v = rng.choice([v for v in range(n) if owner[v] == 0 and len(succ[v]) > 1] or [o])
        if len(succ[v]) > 1 and not (v == o and len(set(succ[v])) <= 2): succ[v].remove(rng.choice(succ[v]))
    else: succ[o] = sorted(set(succ[o]) | {rng.randrange(n)})
    return U.pg.Game(prio, owner, succ)


if __name__ == "__main__":
    steps, seed, lo, hi = map(int, sys.argv[1:5]); out = sys.argv[5] if len(sys.argv) > 5 else None
    rng = random.Random(seed); g = U.load(sys.argv[6]) if len(sys.argv) > 6 else None
    while g is None or U.trace(g)[3] < 3: g = U.rand_c1o(rng, lo, hi)
    o = U.assert_c1o(g); best, bc = score(g)
    for i in range(steps):
        h = mutate(rng, g, o)
        try: sc, c = score(h)
        except Exception: continue
        if sc >= best: g, best, bc = h, sc, c
    print("best", best, {k: v for k, v in bc.items() if "eps" in k or "ABSC" in k or "OR" in k or "H1" in k})
    if out:
        U.pg.write(g, out)
