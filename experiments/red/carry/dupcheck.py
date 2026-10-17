#!/usr/bin/env python3
"""L-RED (box 5): GAP-C attack (L-ALG docs/alg/GAP-C.md, Lead 01:40Z). On A_DTL (L-ALG dtl_pyref via dtl_deficit.build,
read-only via LALG_DIR; order from DTL_ORDER) count hits of the duplicate-tangle check (dtl.cpp 385-424 = pyref
`if key in self.tkeys: continue`), and check completeness (no vertex left unsolved) and correctness (winners equal
Zielonka's, experiments/harness/zielonka.py). Usage: dupcheck.py G.pg ..."""
import sys, os

class Counting(list):
    hits = 0
    def __contains__(self, x):
        r = list.__contains__(self, x)
        if r: Counting.hits += 1
        return r

def _mods():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_deficit as X, pg, zielonka as Z
    return X, pg, Z

def measure(path):
    X, pg, Z = _mods(); g = pg.read(path)
    class T2(X.T):
        @property
        def tkeys(s): return s._tk
        @tkeys.setter
        def tkeys(s, v): s._tk = Counting(v)
        def best_vertices(s, V, R, p):        # GAP-beta precondition: stored p-tangles inside R with ALL escapes outside R
            Rs = set(R)
            for t in range(len(s.tv)):
                if s.tpr[t] == -1 or s.tpr[t] % 2 != p: continue
                C = [w for w, _ in s.tv[t]]
                if all(w in Rs for w in C) and s.tout[t] and not any(e in Rs for e in s.tout[t]): s.orph += 1
            return super().best_vertices(V, R, p)
    d0 = X.build(g)
    d = T2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    Counting.hits = 0; d.orph = 0; d.run()
    unsolved = len(d.G)
    zw = Z.solve(g)
    win = {d.idx[i]: d.win[i] for i in range(g.n)}
    wrong = sum(1 for v in range(g.n) if win[v] is not None and win[v] != (zw[v] if not isinstance(zw, tuple) else zw[0][v]))
    return dict(dup=Counting.hits, unsolved=unsolved, wrong=wrong, searches=d.iterations, orphans=d.orph)

def score(path):
    m = measure(path)
    return 10 ** 6 * (m["unsolved"] + m["wrong"]) + 1000 * m["dup"] + 10 * min(m["orphans"], 50) + m["searches"]

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        m = measure(f); print(f"{os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} {m}" + ("  ** INCOMPLETE/WRONG **" if m["unsolved"] or m["wrong"] else "") + ("  ** DUPLICATE CHECK FIRED **" if m["dup"] else ""))
