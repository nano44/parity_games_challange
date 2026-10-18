#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): per search, the sequence of depth-0 best_vertices calls as |R|:result (reference model
dtl_pyref UNMODIFIED via a subclass hook). Usage: d0calls.py G.pg"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D; g = pg.read(sys.argv[1]); d0 = X_.build(g)
class L(D.DTL):
    dep = 0
    def search(s, p): s.row = []; r = D.DTL.search(s, p); print(f"search p={p}: " + " ".join(s.row), flush=True); return r
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth; r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def best_vertices(s, V, R, p):
        n = len(R); r = D.DTL.best_vertices(s, V, R, p)
        if s.dep == 0: s.row.append(f"{n}:{r}")
        return r
d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); sys.setrecursionlimit(100000); d.run()
