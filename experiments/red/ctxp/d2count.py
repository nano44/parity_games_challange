#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): D2 cost counters on the reference model (dtl_pyref UNMODIFIED, subclass hooks):
search_rec calls and max depth, best_vertices calls, tattr calls, vertex pops (attractVertices calls), attractTangle calls and
tangle-vertex scans (sum of |tangle| over attractTangle calls past the parity check), extractTangles duplicate-key comparisons
(len(tkeys) per candidate SCC). Usage: d2count.py G.pg"""
import sys, os, time
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D; g = pg.read(sys.argv[1]); d0 = X_.build(g)
C = dict(searches=0, search_rec=0, maxdepth=0, bv=0, tattr=0, pops=0, attrT=0, tscan=0, dupcmp=0, sptl=0)
class K(D.DTL):
    def search(s, p): C["searches"] += 1; return D.DTL.search(s, p)
    def search_rec(s, R, p, depth): C["search_rec"] += 1; C["maxdepth"] = max(C["maxdepth"], depth); return D.DTL.search_rec(s, R, p, depth)
    def best_vertices(s, V, R, p): C["bv"] += 1; return D.DTL.best_vertices(s, V, R, p)
    def sptl(s, V, R, p): C["sptl"] += 1; return D.DTL.sptl(s, V, R, p)
    def tattr(s, *a): C["tattr"] += 1; return D.DTL.tattr(s, *a)
    def attractVertices(s, *a): C["pops"] += 1; return D.DTL.attractVertices(s, *a)
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        C["attrT"] += 1
        if s.tpr[t] != -1 and s.tpr[t] % 2 == p: C["tscan"] += len(s.tv[t])
        return D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
    def extractTangles(s, top, R): C["dupcmp"] += len(s.tkeys); return D.DTL.extractTangles(s, top, R)
d = K(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); sys.setrecursionlimit(100000)
t = time.time(); d.run(); C["tangles"] = len(d.tv); C["sec"] = round(time.time() - t, 1)
print(os.path.basename(sys.argv[1]), f"n {g.n}", " ".join(f"{k} {v}" for k, v in C.items()), flush=True)
