r"""REFEREE throwaway: my own SAT encoding (pysat) for 'is there a deterministic weak/strong (n,d)-separator with k states',
convention V or S, graphs = all inclusion-maximal even/odd graphs with 1..n vertices computed by brute force (wsepref.py).
Usage: python3 -I wsepsat.py n d conv weak|strong k"""
import sys, itertools
sys.path.insert(0, '/home/user/parity_games_challange/docs/referee/scratch')
import wsepref as W
from pysat.solvers import Cadical153
from pysat.card import CardEnc

def maximal_graphs(n, d, conv, cls):
    """All inclusion-maximal graphs of class cls ('even'/'odd') among graphs with exactly m vertices, m = 1..n (V: per labelling)."""
    out = []
    for m in range(1, n + 1):
        gen = W.graphs_V(m, d) if conv == 'V' else W.graphs_S(m, d)
        groups = {}
        for e in gen:
            if conv == 'V':   # vertex symmetry: one representative labelling per orbit (non-decreasing labels); sound and complete
                lab = [None] * m
                for (u, p, w) in e: lab[u] = p
                if any(lab[i] > lab[i + 1] for i in range(m - 1)): continue
            if W.cycle_class(m, e) != cls: continue
            key = tuple(sorted({(u, p) for (u, p, w) in e})) if conv == 'V' else ()
            groups.setdefault(key, []).append(frozenset(e))
        for key, gs in groups.items():
            for g in gs:
                if not any(g < h for h in gs): out.append((m, sorted(g)))
    return out

def solve(n, d, conv, strong, k):
    evens = maximal_graphs(n, d, conv, 'even'); odds = [] if strong else maximal_graphs(n, d, conv, 'odd')
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    SINK = k
    t = [[[new() for q2 in range(k + 1)] for p in range(d)] for q in range(k)]
    cls = []
    for q in range(k):
        for p in range(d):
            cls += CardEnc.equals([t[q][p][q2] for q2 in range(k + 1)], 1, vpool=None, top_id=nv[0]).clauses
            nv[0] = max(nv[0], max(abs(l) for c in cls[-50:] for l in c))
    def add_graph(m, edges, odd):
        alive = W.prune(m, edges); E = [(u, p, w) for (u, p, w) in edges if u in alive and w in alive]
        verts = sorted(alive); idx = {v: i for i, v in enumerate(verts)}
        r = [[new() for q in range(k)] for v in verts]
        for v in verts: cls.append([r[idx[v]][0]])
        N = len(verts) * k
        ge = [[[new() for j in range(N + 1)] for q in range(k)] for v in verts] if odd else None   # ge[v][q][j]: rank >= j
        if odd:
            for v in verts:
                for q in range(k):
                    cls.append([ge[idx[v]][q][0]]); cls.append([-ge[idx[v]][q][N]])
                    for j in range(N): cls.append([-ge[idx[v]][q][j + 1], ge[idx[v]][q][j]])
        for (u, p, w) in E:
            iu, iw = idx[u], idx[w]
            for q in range(k):
                if not odd: cls.append([-r[iu][q], -t[q][p - 1][SINK]])        # W1: never the sink
                for q2 in range(k):
                    cls.append([-r[iu][q], -t[q][p - 1][q2], r[iw][q2]])          # closure
                    if odd:                                                         # W2: rank(u,q) > rank(w,q2)
                        for j in range(N):
                            cls.append([-r[iu][q], -t[q][p - 1][q2], -ge[iw][q2][j], ge[iu][q][j + 1]])
    for m, e in evens: add_graph(m, e, False)
    for m, e in odds: add_graph(m, e, True)
    if strong:   # S2 on all states: for each odd p, rank_p with <= on letters < p and < on letter p
        for p in range(1, d + 1, 2):
            ge = [[new() for j in range(k + 1)] for q in range(k)]
            for q in range(k):
                cls.append([ge[q][0]]); cls.append([-ge[q][k]])
                for j in range(k): cls.append([-ge[q][j + 1], ge[q][j]])
            for q in range(k):
                for l in range(1, p + 1):
                    for q2 in range(k):
                        for j in range(k + 1):
                            if l < p:
                                if j <= k: cls.append([-t[q][l - 1][q2], -ge[q2][j], ge[q][j]])
                            else:
                                if j < k: cls.append([-t[q][l - 1][q2], -ge[q2][j], ge[q][j + 1]])
    s = Cadical153(bootstrap_with=cls); sat = s.solve()
    delta = None
    if sat:
        model = set(l for l in s.get_model() if l > 0)
        delta = [[next(q2 for q2 in range(k + 1) if t[q][p][q2] in model) for p in range(d)] for q in range(k)]
        delta = [[None if q2 == SINK else q2 for q2 in row] for row in delta]
    return sat, delta, len(evens), len(odds), len(cls)

if __name__ == "__main__":
    n, d, conv, mode, k = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], int(sys.argv[5])
    import time; t0 = time.time()
    sat, delta, ne, no, ncl = solve(n, d, conv, mode == 'strong', k)
    print(f"{mode} conv {conv} n<={n} d={d} k={k}: {'SAT' if sat else 'UNSAT'} (maximal graphs even={ne} odd={no}, clauses={ncl}, {time.time()-t0:.0f}s)" + (f" delta={delta}" if sat else ""), flush=True)
    if sat:   # independent re-check against ALL graphs
        for m, (cnt, bad) in W.sub_n(n, d, conv, mode == 'strong', delta).items():
            print(f"  re-check n={m}: violations {bad if bad else 'none'}")
