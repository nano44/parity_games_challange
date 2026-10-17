"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): injective forms of "each search but the last settles
a vertex". LR_s = union of the regions Z_top of the sptl passes in which search s extracted a new tangle; LT_s = union of the
tangles learned in s. (LR-SETTLE): every non-last s has a vertex of LR_s in no LR_{s'}, s' > s. (LT-SETTLE): the same for LT.
Either gives S - 1 <= |G'|. DTL_ORDER=oink | stable. Usage: dtl_settle2.py G.pg ... (S2_V=1 verbose)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
D = P.X.D

class S2(P.PS):
    def search(s, p):
        s.LR = set(); s.LT = set(); r = P.PS.search(s, p); s.trace[-1]["LR"] = s.LR; s.trace[-1]["LT"] = s.LT; return r
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        if len(s.tv) > k:
            s.LR |= set(R)
            for t in range(k, len(s.tv)): s.LT |= {v for v, _ in s.tv[t]}
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = [0, 0, 0]
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.X.build(g); d = S2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            L = len(ph); f1 = []; f2 = []
            for s in range(L - 1):
                later_R = set().union(*[ph[q]["LR"] for q in range(s + 1, L)]); later_T = set().union(*[ph[q]["LT"] for q in range(s + 1, L)])
                if not ph[s]["LR"] - later_R: f1.append(s)
                if not ph[s]["LT"] - later_T: f2.append(s)
            tot[0] += L - 1; tot[1] += len(f1); tot[2] += len(f2)
            if os.environ.get("S2_V") and L > 3: print(os.path.relpath(f), f"p={ph[0]['p']} S={L} LR fails {f1} LT fails {f2}")
    print("non-last searches", tot[0], "LR-SETTLE fails", tot[1], "LT-SETTLE fails", tot[2])
