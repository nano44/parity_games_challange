"""L-RED box 16 (produced on Opus 5.5): per transition at depth-0 position b, its type (G: same (rank, V), piece grew; O: (rank, V)
rose; N: the chain got longer/shorter at b) and the NEST* of the segment of positions > b that follows, up to the next transition
at a position <= b. Chains from L-ALG's unmodified b12_pot.run/chain + b12_core.states (via xscore). Histogram (type, segNEST*).
Usage: DTL_ORDER=.. segstat.py G.pg ..."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X
from comb.neststar import nest_star
B = X.B


def trans(g, order, C):
    d = B.run(g, order); q = 1 - C; phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(B.chain(calls, g.n)))
    for ph, L in phases.items():
        if ph[0] != q: continue
        T = []
        for x, y in zip(L, L[1:]):
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None: continue
            t = "N" if p0 >= len(x) or p0 >= len(y) else ("G" if (x[p0][1], x[p0][2]) == (y[p0][1], y[p0][2]) else "O")
            T.append((p0, t))
        yield ph, T


def segs(T):
    for i, (b, t) in enumerate(T):
        seg = []
        for p, _ in T[i + 1:]:
            if p <= b: break
            seg.append(p)
        yield b, t, nest_star(tuple(seg))


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); H = collections.Counter(); ex = {}
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        if C is None: continue
        try:
            for ph, T in trans(g, order, C):
                for b, t, s in segs(T):
                    H[(t, s)] += 1
                    if s >= 2: ex.setdefault((t, s), []).append((os.path.basename(f), b))
        except RecursionError:
            pass
    for k in sorted(H): print(k, H[k], ex.get(k, [])[:4])
