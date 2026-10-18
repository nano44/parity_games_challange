"""Greedy vertex deletion keeping a (TREE-PIECE⁺) violation in BOTH orders (b12_ident.tp_score with PLUS=1, unmodified).
A vertex is deleted with its edges; a deletion that leaves some vertex without a successor is skipped. Edge deletions follow.
Usage: shrink.py IN.pg OUT.pg"""
import sys, os
os.environ["PLUS"] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpclimb as T
I, pg = T.I, T.pg


def bad(g):
    try:
        return all(I.tp_score(g, o)[0] >= 1 for o in ("stable", "oink"))
    except RecursionError:
        return False


def delete(g, v):
    keep = [u for u in range(g.n) if u != v]; m = {u: i for i, u in enumerate(keep)}
    succ = [[m[w] for w in g.succ[u] if w != v] for u in keep]
    if any(not s for s in succ): return None
    return pg.Game([g.prio[u] for u in keep], [g.owner[u] for u in keep], succ)


sys.setrecursionlimit(100000); g = pg.read(sys.argv[1]); assert bad(g)
changed = True
while changed:
    changed = False
    for v in reversed(range(g.n)):
        h = delete(g, v)
        if h is not None and bad(h): g = h; changed = True; print("n", g.n, flush=True)
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) < 2: break
            succ = [list(s) for s in g.succ]; succ[v].remove(w); h = pg.Game(g.prio, g.owner, succ)
            if bad(h): g = h; changed = True
pg.write(g, sys.argv[2]); print("final n", g.n, "edges", sum(len(s) for s in g.succ))
