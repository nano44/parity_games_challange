#!/usr/bin/env python3
"""L-RED (box 5): GAP-C attack (L-ALG docs/alg/GAP-C.md, Lead 01:40Z). On A_DTL (L-ALG dtl_pyref via dtl_deficit.build,
read-only via LALG_DIR; order from DTL_ORDER) count hits of the duplicate-tangle check (dtl.cpp 385-424 = pyref
`if key in self.tkeys: continue`), and check completeness (no vertex left unsolved) and correctness (winners equal
Zielonka's, experiments/harness/zielonka.py). Usage: dupcheck.py G.pg ..."""
import sys, os

class Counting(list):
    hits = 0; inW = 0; Wcur = set()
    def __contains__(self, x):
        r = list.__contains__(self, x)
        if r:
            Counting.hits += 1
            if set(x) <= Counting.Wcur: Counting.inW += 1      # duplicate tangle inside W_p(G') of the searching player
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
        def search(s, p):                     # barren duplicate: a search whose only find was a duplicate (returns false)
            alive = {s.idx[v] for v in s.G}; st = [0]; W0, W1 = Z.solve_sub(g, alive, st, {})
            inv = {s.idx[v]: v for v in range(s.n)}; s.Wp = {inv[v] for v in (W0 if p == 0 else W1)}; Counting.Wcur = s.Wp
            s.wsearch += bool(s.Wp)
            h0 = Counting.hits; t0 = len(s.tv); d0_ = s.dominions; r = super().search(p)
            if s.Wp:                          # (K-in) and (TW), L-ALG GAP-C.md §8-§9
                new = [{w for w, _ in s.tv[t]} for t in range(t0, len(s.tv))]
                if s.dominions == d0_ and not any(C <= s.Wp for C in new): s.kin += 1
                s.straddle += sum(1 for C in new if (C & s.Wp) and not C <= s.Wp)
            if not r and Counting.hits > h0: s.barren += 1
            return r
        def best_vertices(s, V, R, p):        # GAP-beta precondition: stored p-tangles inside R with ALL escapes outside R
            Rs = set(R)
            for t in range(len(s.tv)):
                if s.tpr[t] == -1 or s.tpr[t] % 2 != p: continue
                C = [w for w, _ in s.tv[t]]
                if all(w in Rs for w in C) and s.tout[t] and not any(e in Rs for e in s.tout[t]):
                    s.orph += 1
                    if set(C) <= s.Wp: s.orphW += 1
            return super().best_vertices(V, R, p)
    d0 = X.build(g)
    d = T2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    Counting.hits = 0; Counting.inW = 0; d.orph = 0; d.orphW = 0; d.barren = 0; d.wsearch = 0; d.kin = 0; d.straddle = 0; d.Wp = set(); d.run()
    unsolved = len(d.G)
    zw = Z.solve(g)
    win = {d.idx[i]: d.win[i] for i in range(g.n)}
    wrong = sum(1 for v in range(g.n) if win[v] is not None and win[v] != (zw[v] if not isinstance(zw, tuple) else zw[0][v]))
    return dict(dup=Counting.hits, unsolved=unsolved, wrong=wrong, searches=d.iterations, orphans=d.orph, barren=d.barren, dupW=Counting.inW, orphW=d.orphW, searchesWithWp=d.wsearch, kin_viol=d.kin, tw_straddle=d.straddle)

def score(path):
    m = measure(path)
    return 10 ** 6 * (m["unsolved"] + m["wrong"]) + 1000 * m["dup"] + 100 * min(m["orphans"], 50) + m["searches"]

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        m = measure(f); print(f"{os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} {m}" + ("  ** INCOMPLETE/WRONG **" if m["unsolved"] or m["wrong"] else "") + ("  ** DUPLICATE CHECK FIRED **" if m["dup"] else ""))
