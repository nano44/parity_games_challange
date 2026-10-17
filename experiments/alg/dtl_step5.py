"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C Step 5 tracer: every piece of every search_rec call.
Piece types (C5 §2, dtl.cpp 834-991): S = stable, Dom(V*, R) after sptl (878-890); T = -1 with Q nonempty, threshold
attractor + recursion (899-954); P = -1 with Q EMPTY, Dom(prevV, R) (962-991); E = result 0 (R has no p-priority vertex).
For each piece: depth, |R|, the removed set, its split over W_p(G') / W_{1-p}(G') (Zielonka on G'), the new tangles it
learned (S only) and whether they lie inside W_p. Order datum: DTL_ORDER = oink | stable (dtl_deficit.build).
Usage: dtl_step5.py [-v] G.pg ...   (-v prints every piece of every search with W_p != {} and no dominion)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_deficit as X, dtl_orphan as O
D = X.D


class S5(D.DTL):
    """dtl_pyref.DTL with search_rec copied verbatim and instrumented (no change to the computation)."""
    def search(s, p):
        s.Wp = O.winning(s, set(s.G), p) if s.G else set(); s.pieces = []; s.newt = []; s.G0 = set(s.G); s.cur_new = []; s.cur_top = []
        d0 = s.dominions; r = D.DTL.search(s, p)
        s.trace.append(dict(p=p, G=s.G0, Wp=s.Wp, pieces=s.pieces, newt=s.newt, dom=s.dominions > d0))
        return r

    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)):
            s.newt.append(frozenset(v for v, _ in s.tv[t])); s.cur_new.append(frozenset(v for v, _ in s.tv[t]))
            s.cur_top.append((top, frozenset(v for v, _ in s.tv[t])))
        return r

    def search_rec(s, R, p, depth):
        X_ = set()
        while True:
            V = set(); R0 = frozenset(R); X0 = frozenset(X_); s.cur_nt = len(s.tv)
            res = s.best_vertices(V, R, p)
            if res == 0:
                s.pieces.append(dict(kind="E", depth=depth, nt=s.cur_nt, R=R0, X=X0, rem=frozenset(), V=frozenset())); return
            if res == 1:
                s.cur_new = []; s.cur_top = []
                while s.sptl(V, set(R), p): pass
                s.dom(V, R, X_, p)
                s.pieces.append(dict(kind="S", depth=depth, nt=s.cur_nt, R=R0, X=X0, rem=R0 - frozenset(R), V=frozenset(V), new=list(s.cur_new), tops=list(s.cur_top)))
                continue
            t = 0; Z = set(); s.Q = []
            for v in range(s.n):
                if v not in R: continue
                if s.pr[v] > t:
                    if s.Q: break
                    t = s.pr[v]
                if s.attracts(p, v, X_, R):
                    Z.add(v); s.str[v] = -1; s.Q.append(v)
            if s.Q:
                seeds = frozenset(Z)
                s.tattr(p, Z, R, R, t, R)
                Zall = frozenset(Z); Xb = set(X_)
                for u in range(s.n - 1, -1, -1):
                    if s.pr[u] < t: break
                    if u in Z and s.pr[u] == t: X_.add(u); s.Q.append(u)
                while s.Q:
                    u = s.Q.pop(); Z.discard(u)
                    s.attractVertices(1 - p, u, Z, X_, Z, t)
                X_ |= Z
                s.pieces.append(dict(kind="T", depth=depth, nt=s.cur_nt, R=R0, X=X0, rem=Zall, V=frozenset(V), t=t, seeds=seeds, rest=frozenset(Z)))
                s.search_rec(Z, p, depth + 1)
            else:
                s.dom(V, R, X_, p)
                s.pieces.append(dict(kind="P", depth=depth, nt=s.cur_nt, R=R0, X=X0, rem=R0 - frozenset(R), V=frozenset(V)))


def build(g):
    d0 = X.build(g); d = S5(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []; return d


def show(d, tr, f):
    W = tr["Wp"]; p = tr["p"]
    lab = lambda S: "{" + " ".join(f"{d.idx[v]}" + ("*" if v in W else "") for v in sorted(S)) + "}"
    print(f"== {os.path.basename(f)} search p={p} |G'|={len(tr['G'])} |W_p|={len(W)} dominion={tr['dom']}  (* = in W_p; original ids)")
    for pc in tr["pieces"]:
        extra = ""
        if pc["kind"] == "S": extra = " new=" + ",".join(lab(C) + ("[in W_p]" if C <= W else "") for C in pc["new"])
        if pc["kind"] == "T": extra = f" t={pc['t']} seeds={lab(pc['seeds'])} rest={lab(pc['rest'])}"
        print(f"  {'  ' * pc['depth']}{pc['kind']} d={pc['depth']} |R|={len(pc['R'])} V={lab(pc['V'])} rem={lab(pc['rem'])}{extra}")


if __name__ == "__main__":
    sys.setrecursionlimit(100000); verbose = "-v" in sys.argv
    for f in [a for a in sys.argv[1:] if a != "-v"]:
        d = build(pg.read(f)); d.run()
        for tr in d.trace:
            if verbose and tr["Wp"] and not tr["dom"]: show(d, tr, f)
