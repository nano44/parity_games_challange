#!/usr/bin/env python3
"""Box 8: K9 segment statistics along N5's own run (n5_lock.step = n5.py's loop, as in n5_brchanges.py). A σ̄-segment is a maximal
run of iterations in which Odd's best reply σ̄_k (on Odd's vertices) is constant; within it Even's moves are an improvement sequence of
the one-player game G_c (K9). Reports the max number of Even moves in one σ̄-segment and of Odd moves in one τ̄-segment, plus the
largest number of vertices Even switched in one move. Usage: n5_segments.py game.pg [game2.pg ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
for path in sys.argv[1:]:
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); E, Ed = Engine(g), Engine(dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
    def br(): return tuple(E.evaluate(tuple(s))[1][v] for v in O), tuple(Ed.evaluate(tuple(t))[1][v] for v in V0)
    bs, bt = br(); segE = segO = maxE = maxO = it = 0; minsw = None
    while it < 100000:
        r = step(g, E, Ed, s, t)
        if r is None: break
        it += 1; de = sum(a != b for a, b in zip(r[0], s)); do = sum(a != b for a, b in zip(r[1], t))
        segE += de > 0; segO += do > 0; s, t = r[0], r[1]
        ns, nt = br()
        if ns != bs: segE = 0
        if nt != bt: segO = 0
        bs, bt = ns, nt; maxE = max(maxE, segE); maxO = max(maxO, segO)
    print(f"{os.path.basename(path)} n={g.n} iterations={it} maxEvenMovesPerSigmaBarSegment={maxE} maxOddMovesPerTauBarSegment={maxO}")
