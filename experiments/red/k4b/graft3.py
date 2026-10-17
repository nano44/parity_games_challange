#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): grafts x (Even-owned, even P) -> y; y (Odd-owned, odd q) -> x, z; z (Even-owned,
priority r) -> base vertex b; optionally y -> base vertex c. Scored with carry/klow.py in both orders.
Usage: graft3.py BASE.pg OUTDIR"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import klow, pg
B = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); n = B.n; mp = max(B.prio) + 3; best = None; cnt = 0
for P in range(0, mp + 1, 2):
    for q in range(1, mp + 1, 2):
        for r in range(0, mp + 1):
            for b in range(n):
                for c in [None] + list(range(n)):
                    X, Y, Zv = n, n + 1, n + 2
                    succ = [list(s) for s in B.succ] + [[Y], [X, Zv] + ([c] if c is not None else []), [b]]
                    g = pg.Game(list(B.prio) + [P, q, r], list(B.owner) + [0, 1, 0], succ); cnt += 1
                    for order in ("oink", "stable"):
                        m = klow.measure_game(g, order)
                        if m["wsearch"] == 0: continue
                        key = (m["incomplete"], m["kin"], -m["minprod"], m["dupmin"], m["eaten"])
                        if m["incomplete"] or m["kin"]:
                            fn = os.path.join(out, f"g3_{P}_{q}_{r}_{b}_{c}_{order}.pg"); open(fn, "w").write(pg.dumps(g)); print("HIT", order, m, fn, flush=True)
                        if best is None or key > best[0]: best = (key, P, q, r, b, c, order)
print("games", cnt, "best", best)
