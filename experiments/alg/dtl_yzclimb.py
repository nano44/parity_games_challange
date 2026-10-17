"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18k (YZ): hill-climb on real A_DTL runs for a P piece
whose Dom(prevV) removal Y_0 exceeds the final round's region union Z_f (possible only through a stored tangle that Dom
accepts using a vertex of old X or of an earlier top's part). Fitness (lexicographic): (max |Y_0 \\ Z_f| over P pieces,
number of such straddling acceptances in Dom). On a hit the game is saved and P-KT is evaluated there (dtl_pnl.py).
DTL_ORDER = oink | stable. Usage: dtl_yzclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_pyref as D, dtl_fmclimb as FC


class Y(S5.S5):
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        r = D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
        if r and s.in_dom and any(w in s.x_before for w, _ in s.tv[t]): s.strad += 1
        return r

    def best_vertices(s, V, R, p):
        res = D.DTL.best_vertices(s, V, R, p)
        if res == -1:                                   # recompute the final round's union with V = prevV (690-708)
            sv = list(s.str); Z = set(); CurR = set(R)
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]; s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR); Z |= CurZ
            s.str = sv; s.zf = frozenset(Z)
        return res

    def dom(s, V, R, X, p):
        for top in range(s.n - 1, -1, -1):
            if top not in V or top in X: continue
            s.x_before = set(X)
            X.add(top); s.str[top] = -1; s.Q = [top]
            s.tattr(p, X, R, R, s.pr[top], R)

    def search_rec(s, R, p, depth):
        X_ = set()
        while True:
            V = set(); res = s.best_vertices(V, R, p)
            if res == 0: return
            if res == 1:
                while s.sptl(V, set(R), p): pass
                s.in_dom = False; s.dom(V, R, X_, p); continue
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
                X_ |= Z; s.search_rec(Z, p, depth + 1)
            else:
                R0 = frozenset(R); s.in_dom = True; s.dom(V, R, X_, p); s.in_dom = False
                s.excess = max(s.excess, len((R0 - frozenset(R)) - s.zf))


def fitness(g):
    d0 = S5.build(g); d = Y(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.in_dom = False; d.strad = 0; d.excess = 0; d.x_before = set(); d.zf = frozenset()
    sys.setrecursionlimit(100000)
    try:
        d.run()
    except Exception:
        return (-1, 0)
    if not all(w is not None for w in d.win): return (99, 0)
    return (d.excess, d.strad)


if __name__ == "__main__":
    start, seed, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = pg.read(start); fg = fitness(g); os.makedirs(out, exist_ok=True); print("start", fg, flush=True)
    for it in range(steps):
        h = FC.mutate(g, rnd); fh = fitness(h)
        if fh[0] >= 99: pg.write(h, os.path.join(out, f"incomplete_yz_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg: print("step", it, "fitness", fh, flush=True)
            g, fg = h, fh
            if fg[0] >= 1: pg.write(g, os.path.join(out, f"yz_viol_{seed}_{it}.pg")); print("YZ FAILS", it, fg, flush=True); break
    pg.write(g, os.path.join(out, f"yz_last_{seed}.pg")); print("end", fg, flush=True)
