#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): trace search_rec structure (reference model dtl_pyref UNMODIFIED, via subclass hooks
on best_vertices / dom / search_rec entry): depth, R, best_vertices result and V, X after dom. Input ids.
Usage: srtrace.py G.pg [max_searches]"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D; g = pg.read(sys.argv[1]); MAXS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
d0 = X_.build(g); I = d0.idx
nm = lambda S_: "{" + ",".join(str(I[v]) for v in sorted(S_, key=lambda v: I[v])) + "}"
class L(D.DTL):
    ns = 0
    def search(s, p): s.ns += 1; s.out = s.ns <= MAXS; (print(f"=== search {s.ns-1} p={p}") if s.out else None); return D.DTL.search(s, p)
    def search_rec(s, R, p, depth):
        if s.out: print("  " * depth + f"search_rec depth {depth} R={nm(R)}")
        s.dep = depth; return D.DTL.search_rec(s, R, p, depth)
    def best_vertices(s, V, R, p):
        r = D.DTL.best_vertices(s, V, R, p)
        if s.out: print("  " * s.dep + f"  bv R={nm(R)} -> {r} V={nm(V)}")
        return r
    def dom(s, V, R, X, p):
        D.DTL.dom(s, V, R, X, p)
        if s.out: print("  " * s.dep + f"  dom -> X={nm(X)} R={nm(R)}")
d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = I
sys.setrecursionlimit(100000); d.run()
