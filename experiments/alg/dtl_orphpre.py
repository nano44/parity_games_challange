"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18l: (NO-ORPHAN-pre) — at every best_vertices call (any
depth) of a search made BEFORE the search's first newly learned tangle, no orphan exists: no stored, alive p-tangle t ⊆ R
all of whose escapes lie outside R. Orphans after the first learning are counted separately (they exist: gapb_dup_n20,
gapbW_dup_n20). DTL_ORDER = oink | stable. Usage: dtl_orphpre.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D
tab = {}


class OP(S5.S5):
    def search(s, p):
        s.T0 = len(s.tv); s.p_cur = p
        return S5.S5.search(s, p)

    def best_vertices(s, V, R, p):
        pre = len(s.tv) == s.T0
        orph = 0
        for i in range(len(s.tv)):
            if s.tpr[i] == -1 or s.tpr[i] % 2 != p: continue
            C = [v for v, _ in s.tv[i]]
            if all(v in R for v in C) and all(v in s.G for v in C) and not any(e in R for e in s.tout[i]): orph += 1
        k = "calls " + ("before" if pre else "after") + " the search's first learned tangle: " + ("orphan present" if orph else "no orphan")
        tab[k] = tab.get(k, 0) + 1
        if orph and pre and tab.get("shown", 0) < 3: tab["shown"] = tab.get("shown", 0) + 1; print("NO-ORPHAN-pre VIOLATION", s.fname, "p", p, "|R|", len(R), flush=True)
        return D.DTL.best_vertices(s, V, R, p)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = S5.build(g); d = OP(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
        d.trace = []; d.fname = f; d.T0 = 0; d.run()
    print(tab)
