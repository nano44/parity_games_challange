#!/usr/bin/env python3
"""L-RED R182 check of Lemma C-STATIC. For every TWO-FIX window (any ODIFF), every Even h: a run = consecutive moves of h, no S4c
fallback at those transitions, all into options of class X (portalck cls), each W-strict at h (key W_j(new) > key W_j(old)), with h's
W-cycle node theta the same at every move (one lambda_W-phase at h) and NOPRE: no vertex of prefix(h, i) (i the old or new option)
on X's W-play (sigma_j, tau) at the move. C-STATIC predicts: the options visited are strictly increasing in a static order, so no
option is visited twice and the run has at most (#class-X options of h) - 1 moves. Prints CSTATIC <game> runs maxlen routeC viol
(routeC = runs with h on X's W- or Xi-play at some move). Usage: cstatic.py G START|-"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "r170"), os.path.join(HERE, "..", "..", "new", "box21")]
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen
def playset(succ1, x):
    seen = set(); v = x
    while v not in seen: seen.add(v); v = succ1[v]
    return seen
def check(g, st, cap=800):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); W, SB = windows(g, S, T, E); n, own, pr = g.n, g.owner, g.prio
    R = dict(runs=0, maxlen=0, routeC=0, viol=0)
    for a, b in W:
        if b - a < 1: continue
        gf = frozen(g, SB[a], T[a]); tau, sb = T[a], SB[a]
        EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        wc = {}
        def wv(j):
            if j not in wc: wc[j] = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
            return wc[j]
        def pref(h, x):
            v, seen, pre = x, {h}, []
            while len(gf.succ[v]) == 1:
                if v in seen: return None, None
                seen.add(v); pre.append(v); v = gf.succ[v][0]
            return (None, None) if v in seen else (v, pre)
        sw = lambda j: [S[j][v] if own[v] == 0 else tau[v] for v in range(n)]
        sx = lambda j: [S[j][v] if own[v] == 0 else sb[v] for v in range(n)]
        for h in range(n):
            if own[h] != 0: continue
            nopt = {}
            cur = []; theta = None; X0 = None; rc = False
            def flush():
                nonlocal cur, rc
                if len(cur) >= 1:
                    R["runs"] += 1; R["maxlen"] = max(R["maxlen"], len(cur)); R["routeC"] += rc
                    vis = [cur[0][1]] + [w for _, _, w in cur]
                    k = sum(1 for y in g.succ[h] if pref(h, y)[0] == X0)
                    if len(set(vis)) != len(vis) or len(cur) > k - 1: R["viol"] += 1
                cur = []; rc = False
            for j in range(a + 1, b + 1):
                o, w = S[j - 1][h], S[j][h]
                if o == w: continue
                X, pw = pref(h, w); Xo, po = pref(h, o); Wj = wv(j)
                ok = (not F[j] and X is not None and Xo == X and EW.key(Wj[w]) > EW.key(Wj[o]))
                if ok:
                    pl = playset(sw(j), X); ok = not any(u in pl for u in pw + po)
                th = Wj[h][0]
                if ok and cur and X == X0 and th == theta: cur.append((j, o, w))
                else:
                    flush()
                    if ok: cur = [(j, o, w)]; X0 = X; theta = th
                if ok and (h in playset(sw(j), X) or h in playset(sx(j - 1), X)): rc = True
            flush()
    return R
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R = check(g, st); print("CSTATIC " + os.path.basename(sys.argv[1]) + " " + " ".join(f"{k} {v}" for k, v in R.items()))
