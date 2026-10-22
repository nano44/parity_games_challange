#!/usr/bin/env python3
"""Box 8: check Lemma S (N5-K9-Pstrict-counter.md §5) by computer. One-player 1-sink games (random DAGs into a priority-0
self-loop sink, all vertices Even; plus CDAG_n). N5 on a one-player game makes Even arena-optimum steps only (Odd has no
vertices) = switch-best. From random starts, the iteration count must be ≤ h = max depth of the optimal tree (edges to the sink).
Usage: sb_sink_check.py games seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); worst = 0; viol = 0; runs = 0
for gi in range(games):
    n = rng.randint(2, nmax); pr = rng.sample(range(1, 3 * n), n)
    succ = [[0]] + [sorted(set(rng.randrange(v) for _ in range(rng.randint(1, min(v, 4))))) for v in range(1, n + 1)]
    g = pg.Game([0] + pr, [0] * (n + 1), succ)
    it, fb, win, ws, ev = n5.run(g, "n5"); opt = ws
    def depth(v):
        d = 0
        while v != 0: v = opt[v]; d += 1
        return d
    h = max(depth(v) for v in range(n + 1))
    for _ in range(5):
        st = {v: rng.choice(succ[v]) for v in range(1, n + 1)}
        it, fb, win, ws2, ev = n5.run(g, "n5", (st, {})); runs += 1
        worst = max(worst, it - h); viol += it > h
print(f"runs={runs} violations(it > h)={viol} max(it - h)={worst}")
