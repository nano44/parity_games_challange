#!/usr/bin/env python3
"""L-RED R182 route (C) scorer. Like r174 zclimb.zruns, but a CRUN is a maximal sequence of consecutive moves of an Even h in one
fallback-free stretch of a TWO-FIX window, all into options of class X (portalck cls), each W-strict at h, such that
  ZC: X's Xi-cycle node is the same at every state from the first move's j-1 to the last move's j-1, and
  NOTNR(h): at each move j, h lies on X's Xi-play (sigma_(j-1), sbar) or on X's W-play (sigma_j, tau)  [route (C)].
Only windows with ODIFF <= ODMAX (env, default 2). Also LAMW: whether the W-cycle node of h is constant over the run (one lambda_W
phase at h). Prints CRUN <game> moves span odiff h X lamw K.  Usage: cscore.py G START|-  or import cruns(g, st)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "r170"), os.path.join(HERE, "..", "..", "new", "box21")]
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen
ODMAX = int(os.environ.get("ODMAX", "2"))
def playset(succ1, x):
    s = []; seen = set(); v = x
    while v not in seen: seen.add(v); s.append(v); v = succ1[v]
    return seen
def cruns(g, st, cap=600, odmax=None):
    odmax = ODMAX if odmax is None else odmax
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); W, SB = windows(g, S, T, E)
    n, own, pr = g.n, g.owner, g.prio; best = dict(moves=0, span=0, odiff=0, h=None, X=None, lamw=0, K=len(S) - 1)
    for a, b in W:
        if b - a < 2: continue
        gf = frozen(g, SB[a], T[a]); tau, sb = T[a], SB[a]
        od = sum(1 for v in range(n) if own[v] == 1 and sb[v] != tau[v])
        if od > odmax: continue
        EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        EX = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [sb[v]] for v in range(n)]))
        wc, xc = {}, {}
        def wv(j):
            if j not in wc: wc[j] = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
            return wc[j]
        def xv(j):
            if j not in xc: xc[j] = EX.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
            return xc[j]
        def cls(h, x):
            v, seen = x, {h}
            while len(gf.succ[v]) == 1:
                if v in seen: return None
                seen.add(v); v = gf.succ[v][0]
            return None if v in seen else v
        sx = lambda j: [S[j][v] if own[v] == 0 else sb[v] for v in range(n)]
        sw = lambda j: [S[j][v] if own[v] == 0 else tau[v] for v in range(n)]
        for h in range(n):
            if own[h] != 0: continue
            mv = [(j, S[j - 1][h], S[j][h]) for j in range(a + 1, b + 1) if S[j][h] != S[j - 1][h]]
            cur = []
            def flush(cur):
                nonlocal best
                if len(cur) > best["moves"]:
                    lam = len({wv(j)[h][0] for j, _, _ in cur}) == 1
                    best = dict(moves=len(cur), span=cur[-1][0] - cur[0][0], odiff=od, h=h, X=cls(h, cur[0][2]), lamw=int(lam), K=len(S) - 1)
            for (j, o, nw) in mv:
                X = cls(h, nw); w = wv(j)
                ok = (X is not None and not F[j] and w[nw] is not None and EW.key(w[nw]) > EW.key(w[o])
                      and (h in playset(sx(j - 1), X) or h in playset(sw(j), X)))
                cont = ok and cur and cls(h, o) == X and cls(h, cur[-1][2]) == X and xv(j - 1)[X][0] == xv(cur[0][0] - 1)[X][0] and not any(F[cur[-1][0]:j + 1])
                if cont: cur.append((j, o, nw))
                else:
                    flush(cur); cur = [(j, o, nw)] if ok else []
            flush(cur)
    return best
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    r = cruns(g, st); print("CRUN " + os.path.basename(sys.argv[1]) + " " + " ".join(f"{k} {v}" for k, v in r.items()))
