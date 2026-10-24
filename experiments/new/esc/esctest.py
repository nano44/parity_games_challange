#!/usr/bin/env python3
"""N10a tests: L2 (one-player exactness) and two-player gap search with the four queries of sa/gaps.py.
Usage: esctest.py random S0 COUNT NMIN NMAX | esctest.py files f.pg ... | esctest.py oneplayer S0 COUNT NMIN NMAX | esctest.py exh N P"""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sa"))
import pg, gen, zielonka, exhaustive
from gaps import queries
from esc import esc_feasible
from peel import region_lp_sigma
TAU = "--tau" in sys.argv
if TAU:
    sys.argv.remove("--tau")


def taus_for(h):
    """N10b: Odd strategies from the Odd-side REGION LP (levels 0 and 1, argmax rounding), as in peel.py."""
    if all(o == 0 for o in h.owner):
        return []
    succ = [sorted(set(x)) for x in h.succ]
    out = []
    for lev in (0, 1):
        sig, _ = region_lp_sigma([p + 1 for p in h.prio], [1 - o for o in h.owner], succ, lev)
        if sig not in out:
            out.append(sig)
    return out


def run(games, tag):
    gaps = nq = 0; t0 = time.time()
    for name, g in games:
        for q, h, truth in queries(g):
            f, cuts, it = esc_feasible(h, taus=taus_for(h) if TAU else ())
            nq += 1
            if truth:
                assert f, (name, q, "infeasible on a yes-instance: bug")
            elif f:
                gaps += 1; print(f"GAP {name} {q} n={h.n} cuts={cuts}", flush=True)
    print(f"{tag}{' [N10b: ESC-tau]' if TAU else ' [N10a: ESC1]'}: {len(games)} games, {nq} queries, {gaps} gaps, {time.time()-t0:.0f}s", flush=True)


def rgames(s0, cnt, nmin, nmax, oneplayer=None):
    out = []
    for seed in range(s0, s0 + cnt):
        rnd = random.Random(seed); n = rnd.randint(nmin, nmax)
        g = gen.random_game(n, rnd.randint(2, n + 1), 1, min(3, n), seed)
        if oneplayer is not None:
            g = pg.Game(g.prio, [oneplayer] * g.n, g.succ)
        out.append((f"r{seed}", g))
    return out


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "random":
        a = list(map(int, sys.argv[2:6])); run(rgames(*a), f"random {a}")
    elif m == "oneplayer":
        a = list(map(int, sys.argv[2:6]))
        run(rgames(*a, oneplayer=0), f"one-player Even {a}"); run(rgames(*a, oneplayer=1), f"one-player Odd {a}")
    elif m == "exh":
        n, P = int(sys.argv[2]), int(sys.argv[3]); stride = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        run([(f"x{n}_{P}_{i}", g) for i, g in enumerate(exhaustive.iter_games(n, P)) if i % stride == 0],
            f"exhaustive n={n} P={P} every {stride}-th")
    else:
        run([(os.path.basename(f), pg.read(f)) for f in sys.argv[2:]], "files")
