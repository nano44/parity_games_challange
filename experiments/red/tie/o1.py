#!/usr/bin/env python3
"""L-RED R152: test O1 on n5b SPEC traces. O1 (R151 §3, L-NEW 41 brief): in one W-run, an Even X that re-enters a target g it left changes
W(X) between the two entries. For every W-run F, every Even X and every re-entry (X leaves g at k -> k+1, first returns to g at j -> j+1,
k < j, all in F) compare W(X) at state k (last state on g) with W(X) at state j + 1 (back on g). A VIOLATION is a re-entry with
W(X) equal at both (W-MON: then W(X) is constant on [k, j + 1]). W(s, t) = n5b SpecSI valuation of the play under (s, t) (xcn.wruns).
A violation with W(X) = (X, {}, 0) has X a W-cycle node (X in C, W(X) fixed on F by definition); offC counts the others; nonflat counts offC violations with some W-change (anywhere) inside [k, j + 1].\nPrints totals and every violation. Usage: o1.py GAME.pg [START] [--quiet]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
def o1(g, tr, fb):
    runs, W = xcn.wruns(g, tr, fb); viol = []; reent = 0; maxL = 0
    for F in runs:
        if len(F) < 3: continue
        maxL = max(maxL, len(F) - 1); t = tr[F[0]][1]
        for X in range(g.n):
            if g.owner[X] != 0 or len(g.succ[X]) < 2: continue
            left = {}  # target -> state k where X was last on it before leaving
            for i in range(len(F) - 1):
                k = F[i]; a, b = tr[k][0][X], tr[k + 1][0][X]
                if a == b: continue
                left[a] = k
                if b in left:
                    reent += 1; k0 = left.pop(b); w0, w1 = W(tr[k0][0], t)[X], W(tr[k + 1][0], t)[X]
                    if w0 == w1: viol.append((F[0], F[-1], X, b, k0, k + 1, w0))
    o1.W = W
    return reent, viol, maxL
if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    g = pg.read(a[0]); st = n5b.read_start(a[1], g) if len(a) > 1 else (None, None)
    try: tr, fb = xcn.trace(g, *st)
    except Exception as e: print(f"O1 {os.path.basename(a[0])} n {g.n} RUN-ERROR {e}"); sys.exit(0)
    reent, viol, maxL = o1(g, tr, fb); W_ = o1.W
    if "--quiet" not in sys.argv:
        for (f0, f1, X, b, k0, k1, w) in viol: print(f"  VIOL run {f0}-{f1} X {X} target {b} left@{k0} back@{k1} W(X) {(w[0], sorted(w[1]), w[2])}")
    nc = [v for v in viol if v[6][0] != v[2]]; per = {}
    for v in nc: per[(v[0], v[2])] = per.get((v[0], v[2]), 0) + 1
    nonflat = sum(1 for (f0, f1, X, b, k0, k1, w) in nc if any(W_(tr[k][0], tr[f0][1]) != W_(tr[k0][0], tr[f0][1]) for k in range(k0, k1 + 1)))
    mx = max(per.items(), key=lambda x: x[1], default=((None, None), 0))
    print(f"O1 {os.path.basename(a[0])} n {g.n} iters {len(tr)-1} maxL {maxL} reentries {reent} violations {len(viol)} offC {len(nc)} "
          f"maxX {mx[1]} (X {mx[0][1]}) nonflat {nonflat}")
