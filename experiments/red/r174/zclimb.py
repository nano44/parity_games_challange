#!/usr/bin/env python3
"""L-RED R174 (route (Z) of R173 §2): longest W-strict same-portal climbs.
For an N5 run, every fallback-free stretch of every TWO-FIX window (freeze.windows), every Even h and branching vertex X of G_F:
a ZRUN is a maximal sequence of consecutive moves of h, all into options of class X (R173 portalck.cls), each W-strict at h
(key(W_j(new)) > key(W_j(old))). Reports the longest ZRUN (moves), its span (transitions from first to last move), ODIFF, and how many
of its steps change X's Xi-cycle node (ZCH) and X's W-cycle node (WCH). Lemma PORTAL predicts ZCH >= moves - 1 when NR holds.
Usage: zclimb.py G START  -> one line;  or import zruns(g, st, cap)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run, windows, frozen

def zruns(g, st, cap=10 ** 6):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); W, SB = windows(g, S, T, E)
    n, own, pr = g.n, g.owner, g.prio; best = dict(moves=0, span=0, odiff=0, zch=0, wch=0, h=None, X=None, K=len(S) - 1)
    for a, b in W:
        if b - a < 2: continue
        gf = frozen(g, SB[a], T[a]); tau, sb = T[a], SB[a]
        od = sum(1 for v in range(n) if own[v] == 1 and sb[v] != tau[v])
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
        for h in range(n):
            if own[h] != 0: continue
            mv = [(j, S[j - 1][h], S[j][h]) for j in range(a + 1, b + 1) if S[j][h] != S[j - 1][h]]
            cur = []
            def flush(cur):
                nonlocal best
                if len(cur) > best["moves"]:
                    X = cls(h, cur[0][2])
                    zch = sum(1 for (j1, _, _), (j2, _, _) in zip(cur, cur[1:]) if xv(j1 - 1)[X][0] != xv(j2 - 1)[X][0])
                    wch = sum(1 for (j1, _, _), (j2, _, _) in zip(cur, cur[1:]) if wv(j1)[X][0] != wv(j2)[X][0])
                    best = dict(moves=len(cur), span=cur[-1][0] - cur[0][0], odiff=od, zch=zch, wch=wch, h=h, X=X, K=len(S) - 1)
            for (j, o, nw) in mv:
                w = wv(j); X = cls(h, nw)
                ok = X is not None and w[nw] is not None and EW.key(w[nw]) > EW.key(w[o]) and not any(F[a + 1:j + 1][-1:]) and not F[j]
                if ok and cur and cls(h, cur[-1][2]) == X and cls(h, o) == X and not any(F[cur[-1][0]:j + 1]): cur.append((j, o, nw))
                else:
                    flush(cur); cur = [(j, o, nw)] if ok else []
            flush(cur)
    return best

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    r = zruns(g, st); print("ZRUN " + os.path.basename(sys.argv[1]) + " " + " ".join(f"{k} {v}" for k, v in r.items()))
