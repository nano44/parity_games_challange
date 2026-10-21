#!/usr/bin/env python3
"""Box 10: mask dynamics along N5's run (n5_lock.step = n5.py's loop, best-reward start). At each iteration, for every Odd vertex y and
successor w != tau(y) that is a G_sigma-improvement for Odd (V_{sigma,tau}(w) better for Odd than V_{sigma,tau}(tau(y)); V = profile
valuation, Odd one-player in G_sigma), record whether the gate is CLOSED (masked: (y,w) not in Itau, Odd's honest improvements against
Even's best reply) or OPEN. Between consecutive iterations with tau(y) unchanged, count LIFTS (closed -> open) and CLOSURES (open ->
closed). gen(m) emulation needs lifts: the bottom vertex waits with (2,1) masked and later fires it. Also reports tail length and
whether sigma was optimal in the tail. Usage: masklift.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step, play_val
from n5 import pg, Engine, dual
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(g.n) if g.owner[v] == 1]
    hist = []; k = 0
    while True:
        vt, _ = Ed.evaluate(tuple(t)); It = set(Ed.improving(tuple(t), vt))
        Vd = play_val(Ed, dual(g), t, s)            # Odd's profile valuation in G_sigma (dual: Odd is the improver)
        gates = {}
        for y in O:
            for w in g.succ[y]:
                if w != t[y] and Ed.key(Vd[w]) > Ed.key(Vd[t[y]]): gates[(y, w)] = (y, w) in It   # True = open
        r = step(g, E, Ed, s, t)
        if r is None: break
        hist.append((list(s), list(t), gates, r[0] != s)); s, t = r[0], r[1]; k += 1
    last = max([i for i, h in enumerate(hist) if h[3]], default=-1)
    lifts = closures = lifts_tail = fired_after_lift = 0; lifted = set()
    for i in range(1, len(hist)):
        s0, t0, g0, _ = hist[i - 1]; s1, t1, g1, _ = hist[i]
        for (y, w), op in g1.items():
            if t1[y] == t0[y] and (y, w) in g0:
                if not g0[(y, w)] and op:
                    lifts += 1; lifted.add((i, y, w))
                    if i > last: lifts_tail += 1
                elif g0[(y, w)] and not op: closures += 1
    # did a lifted edge fire at that iteration (y switched to w)?
    for (i, y, w) in lifted:
        if i + 1 < len(hist) and hist[i + 1][1][y] == w: fired_after_lift += 1
        elif i + 1 == len(hist): pass
    nimp = sum(len(h[2]) for h in hist); nclosed = sum(sum(1 for v in h[2].values() if not v) for h in hist)
    print(f"{os.path.basename(p)} n={g.n} iterations={k} tail={k - last - 1} (Even's last move {last}); G_sigma-improving Odd edges summed over iterations {nimp}, of which masked {nclosed}; "
          f"LIFTS (closed->open, tau(y) unchanged) {lifts} (in tail {lifts_tail}), of which fired next step {fired_after_lift}; closures {closures}")
