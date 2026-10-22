"""L-RED box 17 (produced on Opus 5.5): shrink a priority-order change. For each common vertex u (most inversions first), move u back
to the slot the SEED order gives it among the other common vertices (parity of u kept), keep iff in class and NEST* (stable) >= TARGET.
Usage: shrinkprio.py SEED.pg RESULT.pg TARGET OUT.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000)
import xscore as X, nestclass as NC
from comb.neststar import nest_star
a = X.distinct(X.pg.read(sys.argv[1])); b = X.distinct(X.pg.read(sys.argv[2])); T = int(sys.argv[3]); out = sys.argv[4]; n = a.n
C = X.controller(b); prio = [4 * p for p in b.prio]


def ok(pr):
    h = X.distinct(X.pg.Game(pr, list(b.owner), [list(s) for s in b.succ]))
    try:
        Ps, _ = NC.positions(h, "stable", C)
    except RecursionError:
        return False
    return max((nest_star(tuple(P)) for P in Ps.values()), default=0) >= T


def inv(u, pr): return sum(1 for v in range(n) if v != u and (a.prio[u] < a.prio[v]) != (pr[u] < pr[v]))


movers = sorted((u for u in range(n) if inv(u, prio) > 0), key=lambda u: -inv(u, prio)); kept = 0
for u in movers:
    if inv(u, prio) == 0: continue
    below = [v for v in range(n) if v != u and a.prio[v] < a.prio[u]]
    lo = max((prio[v] for v in below), default=-4)       # just above the highest seed-lower vertex
    new = lo + (1 if (b.prio[u] % 2) != (lo % 2 == 0 and 0 or 1) else 2)
    new = lo + 1 if (lo + 1) % 2 == b.prio[u] % 2 else lo + 2
    if any(prio[v] == new for v in range(len(prio)) if v != u): new = lo + 3 if (lo + 3) % 2 == b.prio[u] % 2 else lo + 2
    trial = list(prio); trial[u] = new
    if ok(trial): prio = trial; print("REVERTED rank of", u, flush=True)
    else: kept += 1; print("KEPT rank of", u, "inversions", inv(u, prio), flush=True)
h = X.distinct(X.pg.Game(prio, list(b.owner), [list(s) for s in b.succ])); X.pg.write(h, out)
print("wrote", out, "remaining inversions", sum(1 for u in range(n) for v in range(u + 1, n) if (a.prio[u] < a.prio[v]) != (h.prio[u] < h.prio[v])))
