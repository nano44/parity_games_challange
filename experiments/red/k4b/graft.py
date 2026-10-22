#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): exhaustive small grafts onto a base game: new vertices tau (Even-owned, even P) and
y (Odd-owned, odd q) with tau -> y, y -> tau and y -> a set S of base vertices (|S| <= 2), optional base vertex -> tau.
Scores each with carry/klow.py in both orders; prints any (K-in) violation / incomplete run, and the best minprod/eaten.
GR_S=k: only |S| = k; GR_NOINTO=1: no base -> tau edge (the gapbW run used GR_S=1 GR_NOINTO=1). Usage: graft.py BASE.pg OUTDIR"""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import klow, pg
b = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); n = b.n; best = None; cnt = 0
maxp = max(b.prio) + 3
for P in range(0, maxp + 1, 2):
    for q in range(1, maxp + 1, 2):
        for S in (itertools.combinations(range(n), int(os.environ["GR_S"])) if os.environ.get("GR_S") else itertools.chain(itertools.combinations(range(n), 1), itertools.combinations(range(n), 2))):
            for into in ([None] if os.environ.get("GR_NOINTO") else [None] + list(range(n))):
                if into is not None and b.owner[into] == 1: continue      # only Even base vertices get an extra edge to tau
                succ = [list(s) for s in b.succ] + [[n + 1], [n] + list(S)]
                if into is not None: succ[into] = sorted(set(succ[into]) | {n})
                g = pg.Game(list(b.prio) + [P, q], list(b.owner) + [0, 1], succ); cnt += 1
                for order in ("oink", "stable"):
                    m = klow.measure_game(g, order)
                    if m["wsearch"] == 0: continue
                    key = (m["incomplete"], m["kin"], -m["minprod"], m["eaten"])
                    if m["incomplete"] or m["kin"]:
                        fn = os.path.join(out, f"graft_{P}_{q}_{'_'.join(map(str, S))}_{into}_{order}.pg"); open(fn, "w").write(pg.dumps(g))
                        print("HIT", order, m, fn, flush=True)
                    if best is None or key > best[0]: best = (key, P, q, S, into, order)
print("games", cnt, "best", best)
