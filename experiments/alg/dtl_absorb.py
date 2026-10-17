"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): the ABSORPTION step. For consecutive searches
s, s+1 of a phase whose first piece-level difference (dtl_piecediff.py) is SHRINK at piece position k (same tree position,
R' strict subset of R): let L = union of the tangles learned by search s inside the subtree of piece k. Checks
 (a) R minus R' = L exactly, (b) R minus R' within L, (c) L within R minus R', (c1) some single tangle learned in piece k lies in R minus R', (d) search s learned its tangles only in piece k's
 subtree. DTL_ORDER=oink | stable. Usage: dtl_absorb.py G.pg ... (AB_V=1 prints the non-(a) cases)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL, dtl_piecediff as PD
D = SL.P.X.D

class AB(SL.SL):
    def best_vertices(s, V, R, p):
        s.curpos = tuple(s.cnt[1:]); return SL.SL.best_vertices(s, V, R, p)
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.trace[-1].setdefault("learn", []).append((s.curpos, frozenset(v for v, _ in s.tv[t])))
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); st = {"shrink": 0, "a": 0, "b": 0, "c": 0, "c1": 0, "d": 0}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g)
        d = AB(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            for a, b in zip(ph, ph[1:]):
                key, k = PD.classify(a["calls"], b["calls"])
                if key[0] != "SHRINK": continue
                pos, R = a["calls"][k][0], a["calls"][k][1]; R2 = b["calls"][k][1]
                L = set().union(*[C for (q, C) in a.get("learn", []) if q[:len(pos)] == pos]) if a.get("learn") else set()
                only = all(q[:len(pos)] == pos for (q, C) in a.get("learn", []))
                lost = set(R) - set(R2)
                st["shrink"] += 1; st["a"] += lost == L; st["b"] += lost <= L; st["c"] += L <= lost; st["d"] += only
                st["c1"] += any(C <= lost for (q, C) in a.get("learn", []) if q[:len(pos)] == pos)
                if os.environ.get("AB_V") and (lost != L if os.environ.get("AB_V") == "1" else not L <= lost):
                    o = lambda S: sorted(d.idx[v] for v in S)
                    print(os.path.relpath(f), f"p={a['p']} pos {pos} |R| {len(R)}->{len(R2)} lost {o(lost)} learned-in-piece {o(L)} only-here {only}")
    print(st)
