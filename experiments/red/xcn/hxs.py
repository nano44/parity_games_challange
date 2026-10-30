#!/usr/bin/env python3
"""L-RED R148: per W-run, Xi-changes at SOURCES (HXS_F(v), v in S_k = D_k u D_(k+1) u C; P-N5-SRC). Prints, for the W-run with the largest
max_v HXS_F(v): |F|, E^S_F, the top vertex v, its owner, out-degree, role (C / D), and the next two vertices.
Usage: hxs.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import xcn
pg = xcn.pg; n5b = xcn.n5b
def hxs(g, tr, fb):
    runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g); X = {}
    def Xi(k):
        if k not in X: X[k] = SG.evaluate_choice(list(tr[k][0]))
        return X[k]
    odd = [v for v in range(g.n) if g.owner[v] == 1]; best = None
    for F in runs:
        if len(F) < 2: continue
        t = tr[F[0]][1]; Wv = W(tr[F[0]][0], t); C = {v for v in range(g.n) if Wv[v][0] == v}
        cnt = {}; Es = 0
        for k in F[:-1]:
            (x1, b1), (x2, b2) = Xi(k), Xi(k + 1)
            S = {o for o in odd if b1[o] != t[o] or b2[o] != t[o]} | C
            hx = [v for v in S if x1[v] != x2[v]]
            Es += bool(hx)
            for v in hx: cnt[v] = cnt.get(v, 0) + 1
        top = sorted(cnt.items(), key=lambda kv: -kv[1])[:3]
        r = (top[0][1] if top else 0, len(F) - 1, Es, top, C)
        if best is None or r[:2] > best[:2]: best = r
    return best
if __name__ == "__main__":
    a = sys.argv[1:]; g = pg.read(a[0]); st = n5b.read_start(a[1], g) if len(a) > 1 else (None, None)
    tr, fb = xcn.trace(g, *st)
    m, L, Es, top, C = hxs(g, tr, fb)
    desc = " ".join(f"{v}({'C' if v in C else 'D'},{'E' if g.owner[v]==0 else 'O'},deg{len(g.succ[v])}):{c}" for v, c in top)
    print(f"HXS {os.path.basename(a[0])} n {g.n} iters {len(tr)-1} F {L} ES {Es} maxHXS {m} top {desc}")
