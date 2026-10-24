#!/usr/bin/env python3
"""m_r: θ-changes per level r in the longest joint λ-phase (Lead 16:45Z, from L-SI box 3). Level of a θ-change k -> k+1 = rank of the
most relevant vertex of P(θ_k) Δ P(θ_{k+1}) (VJ ranks, si.py), 'len' if only the length changes, 'cyc' if the cycle node changes.
Usage: LNEW_BOX25=... levels.py game.pg ..."""
import sys, os
sys.path.insert(0, os.environ["LNEW_BOX25"])
from common import *
from collections import Counter
for p in sys.argv[1:]:
    g = load(p); E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []; k = 0
    while k < 2000:
        Xi, _ = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t))
        rows.append(((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), Xi[o]))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1]); k += 1
    ph = []; st = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i][0] != rows[st][0]: ph.append((st, i)); st = i
    best = None
    for a, b in ph:
        m = Counter()
        for i in range(a + 1, b):
            x, y = rows[i - 1][1], rows[i][1]
            if x == y: continue
            if x[0] != y[0]: m["cyc"] += 1
            elif x[1] != y[1]: m[(x[1] ^ y[1]).bit_length() - 1] += 1
            else: m["len"] += 1
        if best is None or sum(m.values()) > sum(best[2].values()): best = (a, b, m)
    a, b, m = best
    lv = sorted(((r, c) for r, c in m.items() if isinstance(r, int)), reverse=True)
    print(f"{os.path.basename(p)} n={g.n} phase {a}..{b}: θ-changes={sum(m.values())} levels used={len(lv)} max m_r={max(m.values()) if m else 0} "
          f"m_r (rank:count, top first)={lv} other={ {k: v for k, v in m.items() if not isinstance(k, int)} }", flush=True)
