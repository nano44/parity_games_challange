#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5): greedy edge removal, then vertex deletion, keeping a (MEET) failure in BOTH orders on a complete run
(screen meet/meetfit.py; the result is re-judged by L-ALG dtl_meetd.py and pinned Oink). Usage: shrink.py IN.pg OUT.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meetfit, pg
sys.setrecursionlimit(100000)


def bad(g):
    try:
        return all((lambda m: m["meetfail"] and not m["incomplete"])(meetfit.measure_game(g, o)) for o in ("oink", "stable"))
    except RecursionError:
        return False


g = pg.read(sys.argv[1]); assert bad(g)
changed = True
while changed:
    changed = False
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) < 2: break
            succ = [list(s) for s in g.succ]; succ[v] = [x for x in succ[v] if x != w]
            h = pg.Game(list(g.prio), list(g.owner), succ)
            if bad(h): g = h; changed = True
def drop(g, v):
    keep = [u for u in range(g.n) if u != v]; ren = {u: i for i, u in enumerate(keep)}
    succ = [[ren[w] for w in g.succ[u] if w != v] for u in keep]
    if any(not s for s in succ): return None
    return pg.Game([g.prio[u] for u in keep], [g.owner[u] for u in keep], succ)


changed = True
while changed:                                      # then vertex deletion (ids compacted in their old relative order)
    changed = False
    for v in reversed(range(g.n)):
        h = drop(g, v)
        if h is not None and bad(h): g = h; changed = True; break
open(sys.argv[2], "w").write(pg.dumps(g)); print("n", g.n, "edges", sum(len(s) for s in g.succ))
