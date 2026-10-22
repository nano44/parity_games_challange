#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): log of the pinned reference model (L-ALG dtl_pyref, UNMODIFIED, via subclass): per
search_rec call, best_vertices result and V, and per sptl top its region, closed flag and the tangles extracted. Input ids.
Usage: LALG_DIR=... DTL_ORDER=stable|oink sptltrace.py G.pg [max_searches]"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X
D = X.D; g = pg.read(sys.argv[1]); MAXS = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
d0 = X.build(g); I = d0.idx
class L(D.DTL):
    ns = 0
    def search(s, p):
        s.ns += 1
        if s.ns <= MAXS: print(f"=== search {s.ns - 1} p={p}")
        return D.DTL.search(s, p)
    def best_vertices(s, V, R, p):
        r = D.DTL.best_vertices(s, V, R, p)
        if s.ns <= MAXS: print(f"  bv |R|={len(R)} res={r} V={sorted(I[v] for v in V)}")
        return r
    def sptl(s, V, R, p):
        Rc = set(R); nt = len(s.tv); out = []
        for top in range(s.n - 1, -1, -1):
            if top not in V or top not in Rc: continue
            Z = {top}; s.str[top] = -1; s.Q = [top]; s.tattr(p, Z, Rc, Rc, s.pr[top], Rc)
            cl = (s.str[top] != -1) if s.ow[top] == p else not any(w in Rc for w in s.outs[top])
            out.append(f"{I[top]}:{{{','.join(str(I[v]) for v in sorted(Z, key=lambda v: I[v]))}}}{'C' if cl else ''}{'W' if top in s.W else ''}")
        r = D.DTL.sptl(s, V, R, p)
        if s.ns <= MAXS: print("   sptl", " ".join(out), "| new", " ".join("{%s}esc{%s}" % (",".join(str(I[v]) for v, _ in s.tv[t]), ",".join(str(I[e]) for e in s.tout[t])) for t in range(nt, len(s.tv))))
        return r
d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = I
sys.setrecursionlimit(100000); d.run(); print("iterations", d.iterations, "win", "".join(str(w) for w in d.win))
