"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18l (β'): what happens to a BORN ORPHAN (dtl_bornorph.py)
in the NEXT search of its phase? For each born orphan t of search s with a next search s+1 in the same phase, classify by
the first event of s+1 among: (A) t is accepted by a tangle attractor (attractTangle returns true) before s+1's first
learned tangle (with the accepting caller: bv-reg / bv-thr = best_vertices regions / threshold loop, sptl, dom, tattr = the
-1 attractor of search_rec); (L) s+1 learns before any such acceptance; (N) neither (s+1 ends without either).
DTL_ORDER = oink | stable. Usage: dtl_bornnext.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_fdlcheck as FC
FD = FC.FD; tab = {}


class BN(FC.CK):
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth; r = FD.D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def sptl(s, V, R, p):
        s.ctxR = set(R); return FC.CK.sptl(s, V, R, p)
    def extractTangles(s, top, R):
        k = len(s.tv); r = FC.CK.extractTangles(s, top, R)
        for i in range(k, len(s.tv)):
            esc = [e for e in s.tout[i] if e in s.G]
            if esc and not any(e in s.ctxR for e in esc): s.born.append((i, s.dep))
        return r
    def search(s, p):
        s.born = []; r = FC.CK.search(s, p); s.trace[-1]["born"] = list(s.born); return r


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = FD.P.X.build(g); d = BN(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in FD.phase_rows(d):
            for a, b in zip(ph, ph[1:]):
                for t, dep in a.get("born", []):
                    cls = "N"
                    for e in b["log"]:
                        if e[0] == "extract": cls = "L"; break
                        if e[0] != "pass" and t in e[5]:
                            cls = "A"; w = f"accepted by {e[0]} at depth {e[1]}"; tab[w] = tab.get(w, 0) + 1; break
                    k = f"born at depth {'0' if dep == 0 else '>0'}: {cls}"; tab[k] = tab.get(k, 0) + 1
    print({k: tab[k] for k in sorted(tab)})
