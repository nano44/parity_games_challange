#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): per search, the result of each depth-0 best_vertices call and the labels of the
p-vertices it pruned (initial V minus returned V; for a -1 result the returned V is the last round's V, also printed)
(reference model dtl_pyref UNMODIFIED via a subclass hook). Usage: prunes.py G.pg [max_calls_per_search]"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D; g = pg.read(sys.argv[1]); d0 = X_.build(g); MC = int(sys.argv[2]) if len(sys.argv) > 2 else 3
lab = lambda v: (g.labels[d0.idx[v]] if g.labels else str(d0.idx[v]))
class L(D.DTL):
    dep = 0; k = 0
    def search(s, p): s.k = 0; print(f"=== search p={p}"); return D.DTL.search(s, p)
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth; r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def best_vertices(s, V, R, p):
        V0 = {v for v in R if s.pr[v] % 2 == p}; r = D.DTL.best_vertices(s, V, R, p)
        if s.dep == 0 and s.k < MC:
            s.k += 1; print(f"  |R| {len(R)} -> {r}; kept {sorted(lab(v) for v in V)}; pruned {sorted(lab(v) for v in V0 - V)}")
        return r
d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); sys.setrecursionlimit(100000); d.run()
