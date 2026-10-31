#!/usr/bin/env python3
"""L-RED R160: independent re-implementation of L-NEW box 107 hier.py's level hierarchy on n5b SPEC traces (W via xcn.wruns).
CS(W(v)) = (cycle node, then for every vertex u in decreasing (priority, index) order: +1/-1 if u is in the path set (by parity of its
priority), else 0, then the signed length (+l if the cycle node's priority is odd, else -l)). Per W-run: level-1 block = its W-changing
transitions with reference W at the block end; P = sum_v lcp(CS W_k v, CS ref v); a transition with P rising is paid at this level;
maximal P-flat stretches recurse with their own end reference. Prints WT, DEPTH, NLEV, and per level the max width of one stretch
(transitions paid at that level inside one parent stretch). Usage: hierx.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
def analyse(g, tr, fb):
    runs, W = xcn.wruns(g, tr, fb)
    order = sorted(range(g.n), key=lambda u: (g.prio[u], u), reverse=True)
    def cs(val):
        c, P, l = val
        return (c,) + tuple(((1 if g.prio[u] % 2 == 0 else -1) if u in P else 0) for u in order) + ((l if g.prio[c] % 2 == 1 else -l),)
    def lcp(a, b):
        i = 0
        while i < len(a) and a[i] == b[i]: i += 1
        return i
    NL, WID = {}, {}; st = {"D": 0, "WT": 0}
    for F in runs:
        if len(F) < 2: continue
        t = tr[F[0]][1]; Ws = {k: W(tr[k][0], t) for k in F}; CS = {k: [cs(x) for x in Ws[k]] for k in F}
        ks = [k for k in F[:-1] if Ws[k] != Ws[k + 1]]; st["WT"] += len(F) - 1
        def block(ks, lev):
            if not ks: return
            ref = CS[ks[-1] + 1]
            P = lambda j: sum(lcp(CS[j][v], ref[v]) for v in range(g.n))
            sub, subs, paid = [], [], 0
            for k in ks:
                if P(k + 1) > P(k):
                    paid += 1; NL[lev] = NL.get(lev, 0) + 1; st["D"] = max(st["D"], lev)
                    if sub: subs.append(sub); sub = []
                else: sub.append(k)
            if sub: subs.append(sub)
            WID[lev] = max(WID.get(lev, 0), paid)
            for sb in subs: block(sb, lev + 1)
        block(ks, 1)
    return st["WT"], st["D"], NL, WID
if __name__ == "__main__":
    g = xcn.pg.read(sys.argv[1]); s = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    tr, fb = xcn.trace(g, *s); WT, D, NL, WID = analyse(g, tr, fb)
    print(f"HIERX {os.path.basename(sys.argv[1])} n {g.n} WT {WT} DEPTH {D} " + " ".join(f"NLEV{d} {NL[d]}" for d in sorted(NL)) + " | width " + " ".join(f"W{d} {WID[d]}" for d in sorted(WID)))
