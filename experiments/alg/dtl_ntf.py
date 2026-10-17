"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18h: (NT-f) the final pruning round of a best_vertices
call that returns −1 attracts no stored tangle in its region loop (690-708); also counts tangle firings inside
Dom(prevV) at P pieces (961-976) that use a vertex of old X or of an earlier top's part (the (YZ-read) exception).
DTL_ORDER = oink | stable. Usage: dtl_ntf.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D
tab = {}
class NT(S5.S5):
    def dom(s, V, R, X, p):
        for top in range(s.n - 1, -1, -1):
            if top not in V or top in X: continue
            s.x_before = set(X)
            X.add(top); s.str[top] = -1; s.Q = [top]
            s.tattr(p, X, R, R, s.pr[top], R)
    def search_rec(s, R, p, depth):
        X_ = set()
        while True:
            V = set()
            res = s.best_vertices(V, R, p)
            if res == 0: return
            if res == 1:
                while s.sptl(V, set(R), p): pass
                s.dom(V, R, X_, p); continue
            t = 0; Z = set(); s.Q = []
            for v in range(s.n):
                if v not in R: continue
                if s.pr[v] > t:
                    if s.Q: break
                    t = s.pr[v]
                if s.attracts(p, v, X_, R): Z.add(v); s.str[v] = -1; s.Q.append(v)
            if s.Q:
                s.tattr(p, Z, R, R, t, R)
                for u in range(s.n - 1, -1, -1):
                    if s.pr[u] < t: break
                    if u in Z and s.pr[u] == t: X_.add(u); s.Q.append(u)
                while s.Q:
                    u = s.Q.pop(); Z.discard(u); s.attractVertices(1 - p, u, Z, X_, Z, t)
                X_ |= Z
                s.search_rec(Z, p, depth + 1)
            else:
                s.in_dom = True; s.dom(V, R, X_, p); s.in_dom = False
                tab["P pieces"] = tab.get("P pieces", 0) + 1
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        r = D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
        if r and getattr(s, "in_regions", False):
            s.round_tangles += 1
            pv = [w for w, _ in s.tv[t] if s.pr[w] % 2 == p]
            k = "INV-T: a region accepts a tangle with " + ("a p-priority vertex in V_r" if any(w in s.cur_V for w in pv) else "NO p-priority vertex in V_r (VIOLATION)")
            tab[k] = tab.get(k, 0) + 1
            if "VIOL" in k and tab.get("shownT", 0) < 3: tab["shownT"] = tab.get("shownT", 0) + 1; print("INV-T VIOLATION", s.fname, sorted(s.idx[w] for w, _ in s.tv[t]), flush=True)
        if r and getattr(s, "in_dom", False):
            strad = any(w in s.x_before for w, _ in s.tv[t])
            k = "Dom(prevV) at a P piece fires a tangle" + (" with a vertex in old X or an earlier top's part (straddle)" if strad else " (no such vertex)")
            tab[k] = tab.get(k, 0) + 1
            if strad: print("DOMSTRADDLE", s.fname, "tangle", sorted(s.idx[w] for w, _ in s.tv[t]), flush=True)
        return r
    def best_vertices(s, V, R, p):
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        if not V: return 0
        tl = []
        while True:
            prevV = set(V); Z = set(); CurR = set(R); s.in_regions = True; s.round_tangles = 0; s.cur_V = set(V)
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]; s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR); Z |= CurZ
            s.in_regions = False; tl.append(s.round_tangles)
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand: return 1
            for t in [0] + [q for q in s.prios if 0 < q <= s.maxpr]:
                s.Q = sorted(Z); s.tattr(p, Z, R, R, t, None); keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t: keep += cand[i:]; break
                    if not s.attracts(p, u, Z, R): keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand: return 1
            if not V:
                V.clear(); V.update(prevV)
                k = "-1 call: final round's regions attract " + ("no tangle" if tl[-1] == 0 else "a tangle")
                tab[k] = tab.get(k, 0) + 1
                k2 = "-1 call: some earlier round's regions attract a tangle"
                if any(tl[:-1]): tab[k2] = tab.get(k2, 0) + 1
                if tl[-1] and tab.get("shown", 0) < 3: tab["shown"] = tab.get("shown", 0) + 1; print("FINAL TANGLE", s.fname, flush=True)
                return -1
files = sys.argv[1:]
for fn in files:
    g = pg.read(fn); d0 = S5.build(g); d = NT(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.fname = fn; d.in_regions = False; d.round_tangles = 0
    sys.setrecursionlimit(100000); d.run()
print(tab)
