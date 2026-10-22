"""L-RED box 17 (produced on Opus 5.5): which of a climb's essential changes are needed? Changes = priority MOVES (vertices whose
rank moved by >= MINMOVE between SEED and RESULT) and EDGE-set changes. For every subset: start from SEED, apply the chosen edge sets,
relocate the chosen movers to their RESULT slot (others keep the SEED order), reassign priorities increasing with parity kept, and
report NEST* (stable and oink). Usage: subsets.py SEED.pg RESULT.pg [MINMOVE=10]"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000)
import xscore as X, nestclass as NC
from comb.neststar import nest_star
a = X.distinct(X.pg.read(sys.argv[1])); b = X.distinct(X.pg.read(sys.argv[2])); n = a.n; C = X.controller(b)
mm = int(sys.argv[3]) if len(sys.argv) > 3 else 10
ra = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: a.prio[v]))}; rb = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: b.prio[v]))}
movers = [v for v in range(n) if abs(rb[v] - ra[v]) >= mm]; edges = [v for v in range(n) if set(a.succ[v]) != set(b.succ[v])]
print("movers", movers, "edge changes", edges, flush=True)


def build(M, E):
    seq = [v for v in sorted(range(n), key=lambda v: a.prio[v]) if v not in M]
    for v in sorted(M, key=lambda v: rb[v]): seq.insert(min(rb[v], len(seq)), v)
    prio = [0] * n; last = -1
    for v in seq:
        p = last + 1
        if p % 2 != a.prio[v] % 2: p += 1
        prio[v] = p; last = p
    succ = [list(b.succ[v]) if v in E else list(a.succ[v]) for v in range(n)]
    return X.pg.Game(prio, list(a.owner), succ)


res = []
for k in range(len(movers) + len(edges) + 1):
    for S in itertools.combinations(movers + [("e", v) for v in edges], k):
        M = {x for x in S if not isinstance(x, tuple)}; E = {x[1] for x in S if isinstance(x, tuple)}
        h = build(M, E)
        if not X.inclass(h, C): continue
        try:
            ns = [max((nest_star(tuple(P)) for P in NC.positions(h, o, C)[0].values()), default=0) for o in ("stable", "oink")]
        except RecursionError:
            continue
        res.append((min(ns), sorted(M), sorted(E)))
        if min(ns) >= 6: print("NEST*", ns, "movers", sorted(M), "edges", sorted(E), flush=True)
print("max over subsets", max(res)[0] if res else None, "subsets", len(res))
