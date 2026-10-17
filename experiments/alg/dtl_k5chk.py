"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18n (C): dump V*, Reg and the rescue set A per level at the
first stable best_vertices call (REFEREE-2 G-c2, K5 (i)/(iii) counterexample). Usage: DTL_ORDER=oink|stable dtl_k5chk.py G.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5
g = pg.read(sys.argv[1]); d = S5.build(g)
print("idx", d.idx, "pr", d.pr, "ow", d.ow, "outs", d.outs)
orig = d.best_vertices
def bv(V, R, p, d=d):
    r = orig(V, R, p)
    if r == 1 and not hasattr(d, "done"):
        d.done = 1; Z = set(); CurR = set(R)
        for top in range(d.n - 1, -1, -1):
            if top not in V or top in Z: continue
            CurZ = {top}; d.Q = [top]; d.tattr(p, CurZ, CurR, CurR, d.pr[top], CurR); Z |= CurZ
        Reg = set(Z); print("p", p, "R", sorted(R), "V*", sorted(V), "Reg", sorted(Reg))
        for t in [0] + [q for q in d.prios if 0 < q <= d.maxpr]:
            d.Q = sorted(Z); d.tattr(p, Z, R, R, t, None); print("  level", t, "A", sorted(Z))
    return r
d.best_vertices = bv; sys.setrecursionlimit(10000); d.run(); print("win", d.win)
