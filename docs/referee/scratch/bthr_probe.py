"""REFEREE probe (R-PROVED2, Lemma B-thr branch (b)): at every T piece (-1 with Q nonempty, dtl.cpp 914-954) check whether a
live stored p-tangle t lies wholly in the recursion context Z' while one of its escapes lies in the part B = Z_T minus Z'
that 936-950 moves to X (the shape of B-thr (b)).
Usage: DTL_ORDER=oink|stable bthr_probe.py G.pg ..."""
import sys, os
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "experiments", "alg")
sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_step5 as S5
D = S5.D
C = dict(T=0, b_shape=0, contained=0)
cur = [None]

class B(S5.S5):
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
                if s.attracts(p, v, X_, R):
                    Z.add(v); s.str[v] = -1; s.Q.append(v)
            if s.Q:
                s.tattr(p, Z, R, R, t, R)
                Zall = set(Z)
                for u in range(s.n - 1, -1, -1):
                    if s.pr[u] < t: break
                    if u in Z and s.pr[u] == t: X_.add(u); s.Q.append(u)
                while s.Q:
                    u = s.Q.pop(); Z.discard(u)
                    s.attractVertices(1 - p, u, Z, X_, Z, t)
                X_ |= Z
                C["T"] += 1
                Bset = Zall - Z
                for k in range(len(s.tv)):
                    if s.tpr[k] == -1 or s.tpr[k] % 2 != p: continue
                    tv = {w for w, _ in s.tv[k]}
                    if tv <= Zall:
                        C["contained"] += 1
                        if tv <= Z and any(e in Bset for e in s.tout[k]): C["b_shape"] += 1
                s.search_rec(Z, p, depth + 1)
            else:
                s.dom(V, R, X_, p)


for f in sys.argv[1:]:
    try: g = pg.read(f)
    except Exception: continue
    if g.n > 80: continue
    d0 = S5.X.build(g); d = B(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []
    d.run()
print(os.environ.get("DTL_ORDER", "stable"), C)
