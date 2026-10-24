#!/usr/bin/env python3
"""Random two-player games (n vertices, out-degree 1..3, random owners, distinct priorities), canonical N5 start:
per n, max over games of the longest non-eliminating run inside a joint lambda-phase (elim.py), the longest phase, and the
recursive gap depth (depth.py).  Usage: sweep.py games nmin nmax seed"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT, elim as EL, depth as DP
pg = OT.pg
def rgame(rng, n):
    pr = rng.sample(range(n), n); ow = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    return pg.Game(pr, ow, succ)
if __name__ == "__main__":
    N, lo, hi, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
    stats = {}
    for t in range(N):
        n = rng.randint(lo, hi); g = rgame(rng, n)
        _, it, rows = EL.elim_g(g, None, 'n5')
        E, Ed, states, fbf, _ = OT.run_states(g, None)
        d = max(dd for _, dd in DP.depth_run(g, states, E, Ed, OT.Lex(E)))
        w = max(r["noelimrun"] for r in rows); w2 = max(r["noelimrun_st"] for r in rows); lp = max(r["trans"] for r in rows)
        s = stats.setdefault(n, [0, 0, 0, 0, 0, 0]); s[0] += 1; s[1] = max(s[1], w); s[5] = max(s[5], w2); s[2] = max(s[2], lp); s[3] = max(s[3], d); s[4] = max(s[4], it)
    for n in sorted(stats):
        c, w, lp, d, it, w2 = stats[n]
        print(f"n={n:3d} games={c:5d} max non-elim run (sigma)={w:3d} (sigma or tau)={w2:3d} max phase={lp:3d} max depth={d} max iterations={it}", flush=True)
