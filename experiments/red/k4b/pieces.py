#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): piece-level trace of every search of A_DTL (L-ALG's dtl_pyref via dtl_kin.KI,
unmodified, LALG5_DIR): per search p, |G'|, W_p(G'); per piece (depth, kind = STABLE / DOM-1 (−1, Q empty) / THR-1 (−1,
threshold t)), the removed set with its W_p part, and tangles learned (inside / outside W_p). DTL_ORDER = oink | stable.
Usage: pieces.py G.pg"""
import sys, os
ld = os.path.join(os.environ["LALG5_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_kin as K
D = K.D

class Dup(list):
    """pyref's duplicate check is `if key in self.tkeys: continue` (dtl.cpp 385-424); count the hits."""
    def __contains__(self, x):
        r = list.__contains__(self, x)
        if r: self.hits.append(frozenset(x))
        return r

class PT(K.KI):
    @property
    def tkeys(s): return s._tk
    @tkeys.setter
    def tkeys(s, v): s._tk = Dup(v); s._tk.hits = []
    def search(s, p):
        s.log = []; s.depth = 0; h0 = len(s.tkeys.hits); r = K.KI.search(s, p)
        s.trace[-1]["log"] = s.log; s.trace[-1]["dups"] = s.tkeys.hits[h0:]; return r
    def search_rec(s, R, p, depth):
        # same body as dtl_pyref.DTL.search_rec, with log lines
        s.depth = depth; X = set()
        while True:
            V = set(); Rin = set(R); res = s.best_vertices(V, R, p)
            if res == 0: return
            if res == 1:
                k = len(s.tv)
                while s.sptl(V, set(R), p): pass
                before = set(X); s.dom(V, R, X, p)
                s.log.append((depth, "STABLE", sorted(V), X - before, [frozenset(v for v, _ in s.tv[t]) for t in range(k, len(s.tv))], Rin))
                continue
            t = 0; Z = set(); s.Q = []
            for v in range(s.n):
                if v not in R: continue
                if s.pr[v] > t:
                    if s.Q: break
                    t = s.pr[v]
                if s.attracts(p, v, X, R): Z.add(v); s.str[v] = -1; s.Q.append(v)
            if s.Q:
                s.tattr(p, Z, R, R, t, R)
                before = set(X)
                for u in range(s.n - 1, -1, -1):
                    if s.pr[u] < t: break
                    if u in Z and s.pr[u] == t: X.add(u); s.Q.append(u)
                while s.Q:
                    u = s.Q.pop(); Z.discard(u); s.attractVertices(1 - p, u, Z, X, Z, t)
                X |= Z
                s.log.append((depth, f"THR-1 t={t}", sorted(V), X - before - Z, [], Rin))   # Z itself is searched at depth + 1
                s.search_rec(Z, p, depth + 1); s.depth = depth
            else:
                before = set(X); s.dom(V, R, X, p)
                s.log.append((depth, "DOM-1", sorted(V), X - before, [], Rin))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    g = pg.read(sys.argv[1]); d0 = K.P.build(g); d = PT(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
    lab = lambda v: str(d0.idx[v]) if hasattr(d0, "idx") else str(v)
    for i, tr in enumerate(d.trace):
        W = tr["Wp"]; print(f"search {i} dups={[('IN' if C <= W else 'OUT') + str(sorted(map(int, map(lab, C)))) for C in tr['dups']]} p={tr['p']} |G'|={len(tr['G'])} |W_p|={len(W)} dominion={tr['d1'] > tr['dom']} W_p={sorted(map(int, map(lab, W)))}")
        for dep, kind, V, rem, newt, Rin in tr["log"]:
            nt = " ".join(("IN" if C <= W else "MEET" if C & W else "OUT") + str(sorted(map(int, map(lab, C)))) for C in newt)
            print(f"  {'  ' * dep}d{dep} {kind:10s} V*={sorted(map(int, map(lab, V)))} removed={sorted(map(int, map(lab, rem)))} (W_p part {len(rem & W)}) {nt}")
    print("unsolved at end:", sorted(map(int, map(lab, d.G))))
