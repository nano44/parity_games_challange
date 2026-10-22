"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18l (β'): BORN ORPHANS. A tangle is a born orphan if, when
extractTangles creates it, none of its escapes inside G' lies in the sptl context R (all are in X or outside the
search_rec context). If search s creates one at point P and search s+1 runs identically up to P (First-Difference Lemma:
it does unless a tangle s learned at or after the first difference is attracted earlier), s+1 meets it as an orphan
before learning, i.e. (NO-ORPHAN-pre) fails. Counts born orphans, and for each whether the NEXT search of the same player
in the same phase re-finds it as a duplicate: not counted here (see dtl_orphpre.py for orphans before learning).
DTL_ORDER = oink | stable. Usage: dtl_bornorph.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D
tab = {}


class BO(S5.S5):
    def search_rec(s, R, p, depth):
        old = getattr(s, "dep", 0); s.dep = depth; r = S5.S5.search_rec(s, R, p, depth); s.dep = old; return r

    def sptl(s, V, R, p):
        s.ctxR = set(R); return S5.S5.sptl(s, V, R, p)

    def extractTangles(s, top, R):
        k = len(s.tv); r = S5.S5.extractTangles(s, top, R)
        for i in range(k, len(s.tv)):
            esc = [e for e in s.tout[i] if e in s.G]
            born = bool(esc) and not any(e in s.ctxR for e in esc)
            tab["tangles created"] = tab.get("tangles created", 0) + 1
            if born:
                tab["born orphans"] = tab.get("born orphans", 0) + 1
                kd = "born orphans at depth 0" if s.dep == 0 else "born orphans at depth > 0"
                tab[kd] = tab.get(kd, 0) + 1
                if tab.get("shown", 0) < 5:
                    tab["shown"] = tab.get("shown", 0) + 1
                    print("BORN ORPHAN", os.path.basename(s.fname), "tangle", sorted(s.idx[v] for v, _ in s.tv[i]), "in-G' escapes", sorted(s.idx[e] for e in esc), flush=True)
        return r


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = S5.build(g); d = BO(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
        d.trace = []; d.fname = f; d.ctxR = set(); d.run()
        if not all(w is not None for w in d.win): print("INCOMPLETE RUN", f, flush=True)
    tab.pop("shown", None); print(tab)
