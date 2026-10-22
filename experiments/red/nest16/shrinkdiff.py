"""L-RED box 17 (produced on Opus 5.5): greedy shrink of a climb's changes. Given SEED and RESULT on the same vertex ids (RESULT may
have extra vertices, which are kept), revert, one at a time: (1) the whole priority order on the common vertices; (2) each owner
change; (3) each vertex's successor set. Keep a revert iff the game stays in class and NEST* (stable order) stays >= TARGET. Writes
OUT and prints the surviving changes. Usage: shrinkdiff.py SEED.pg RESULT.pg TARGET OUT.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000)
import xscore as X, nestclass as NC
from comb.neststar import nest_star
a = X.distinct(X.pg.read(sys.argv[1])); b = X.distinct(X.pg.read(sys.argv[2])); T = int(sys.argv[3]); out = sys.argv[4]; n = a.n
C = X.controller(b)
cur = {"prio": list(b.prio), "owner": list(b.owner), "succ": [list(s) for s in b.succ]}


def game(c): return X.distinct(X.pg.Game(list(c["prio"]), list(c["owner"]), [list(s) for s in c["succ"]]))


def ok(c):
    h = game(c)
    if not X.inclass(h, C): return False
    try:
        Ps, _ = NC.positions(h, "stable", C)
    except RecursionError:
        return False
    return max((nest_star(tuple(P)) for P in Ps.values()), default=0) >= T


def tryrev(field, v, val, label):
    old = cur[field][v] if field != "prio" else None
    if field == "prio":
        save = list(cur["prio"]); prio = list(cur["prio"])
        # common vertices take the seed's order; extra vertices keep their slot relative to the result order
        order = sorted(range(len(prio)), key=lambda u: (a.prio[u] if u < n else None) or 0)
        ranks = sorted(prio[:n]); seedorder = sorted(range(n), key=lambda u: a.prio[u])
        for r, u in zip(ranks, seedorder): prio[u] = r
        cur["prio"] = prio
        if ok(cur): print("REVERTED", label, flush=True); return
        cur["prio"] = save; print("KEPT", label, flush=True); return
    cur[field][v] = val
    if ok(cur): print("REVERTED", label, flush=True)
    else: cur[field][v] = old; print("KEPT", label, flush=True)


assert ok(cur), "result does not reach target"
tryrev("prio", None, None, "priority order")
for v in range(n):
    if a.owner[v] != b.owner[v]:
        save = (cur["owner"][v], list(cur["succ"][v])); cur["owner"][v] = a.owner[v]; cur["succ"][v] = list(a.succ[v])
        if ok(cur): print("REVERTED owner+succ", v, flush=True)
        else: cur["owner"][v], cur["succ"][v] = save[0], save[1]; print("KEPT owner", v, flush=True)
for v in range(n):
    if set(a.succ[v]) != set(cur["succ"][v]) and a.owner[v] == cur["owner"][v]:
        tryrev("succ", v, list(a.succ[v]), f"succ {v}")
X.pg.write(game(cur), out); print("wrote", out)
