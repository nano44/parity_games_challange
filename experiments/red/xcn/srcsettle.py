#!/usr/bin/env python3
"""L-RED R147: data check of RUN-SETTLE with SOURCE heads (docs/red/R147-xcn.md §2) on n5b SPEC traces.
Per W-run F (tau fixed, C fixed): S_k := D_k u D_(k+1) u C (D_k = Odd o with sigmabar_k(o) != tau(o)).
EVENT^src at k -> k+1: (ii) sigma changes at some Even c in C, or (iii^src) Xi changes at some vertex of S_k.
Checks (S_j) of RUN-SETTLE with these events: in a block of event^src-free transitions starting at k0, every Even y switching at k has
ell_(k+1)(y) >= k - k0 + 1, and (X_j) every x with Xi change has ell_(k+1)(x) >= k - k0 + 1. Counts VIOL. Also reports E (R143 events:
sigmabar change, CN, Xi change on U_k u U_(k+1)), Esrc, CNO (CN switches at a c that is its own Xi-cycle node at k or k+1, and with
Xi(c) unchanged), FLIPONLY (transitions that are R143 events only through a sigmabar flip), max block length.
Variant S2 (no CN event): EVENT^S2 := (iii^src) only. Checks (S_j) for non-C switchers and (X_j) on S2-blocks (VIOL2), that an
S2-event-free C-only transition is followed only by C-only transitions inside its block (TAILV), and block length <= n - 1 + sum over Even
c in C of (|succ(c)| - 1) (BLKV); maxblk2 = longest S2-block, maxtail = longest C-only tail.
Usage: srcsettle.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import xcn
pg = xcn.pg; n5b = xcn.n5b
def check(g, tr, fb):
    runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g); X = {}
    def Xi(k):
        if k not in X: X[k] = SG.evaluate_choice(list(tr[k][0]))
        return X[k]
    odd = [v for v in range(g.n) if g.owner[v] == 1]
    tot = dict(VIOL=0, E=0, Esrc=0, CN=0, CNO=0, CNOX=0, FLIPONLY=0, maxblk=0, maxL=0, maxEsrc=0, maxE=0, maxHXS=0, VIOL2=0, TAILV=0, BLKV=0, maxblk2=0, maxtail=0, Es2=0)
    for F in runs:
        if len(F) < 2: continue
        t = tr[F[0]][1]; Wv = W(tr[F[0]][0], t); C = [v for v in range(g.n) if Wv[v][0] == v]
        Ce = [c for c in C if g.owner[c] == 0]
        E = Es = 0; k0 = F[0]; hxs = {}; b0 = F[0]; tail = 0; intail = False
        cap = g.n - 1 + sum(len(g.succ[c]) - 1 for c in Ce)
        for k in F[:-1]:
            s, s2 = tr[k][0], tr[k + 1][0]; (x1, b1), (x2, b2) = Xi(k), Xi(k + 1)
            D1 = {o for o in odd if b1[o] != t[o]}; D2 = {o for o in odd if b2[o] != t[o]}
            S = D1 | D2 | set(C)
            cn = [c for c in Ce if s[c] != s2[c]]
            hx = [v for v in S if x1[v] != x2[v]]
            for v in hx: hxs[v] = hxs.get(v, 0) + 1
            for c in cn:
                if x1[c] == x2[c]:
                    tot["CNO"] += 1
                    if not (x1[c][0] == c or x2[c][0] == c): tot["CNOX"] += 1   # Xi(c) unchanged but c not own: should be 0
            tot["CN"] += len(cn)
            U = lambda xb, sg: {xb[1][o] for o in odd if xb[1][o] != t[o]} | {(sg[c] if g.owner[c] == 0 else xb[1][c]) for c in C}
            Uk = U((x1, b1), s) | U((x2, b2), s2)
            flip = any(b1[o] != b2[o] for o in odd); xu = any(x1[u] != x2[u] for u in Uk)
            ev = flip or bool(cn) or xu; evs = bool(cn) or bool(hx)
            E += ev; Es += evs
            if flip and not cn and not xu: tot["FLIPONLY"] += 1
            if hx:
                b0 = k + 1; tail = 0; intail = False; tot["Es2"] += 1
            else:
                Wn2 = W(s2, t); j2 = k - b0; nonC = [y for y in range(g.n) if g.owner[y] == 0 and s[y] != s2[y] and y not in C]
                if intail and nonC: tot["TAILV"] += 1
                if not nonC: intail = True; tail += 1; tot["maxtail"] = max(tot["maxtail"], tail)
                for y in nonC:
                    if Wn2[y][2] < j2 + 1: tot["VIOL2"] += 1
                for y in range(g.n):
                    if x1[y] != x2[y] and Wn2[y][2] < j2 + 1: tot["VIOL2"] += 1
                tot["maxblk2"] = max(tot["maxblk2"], k + 1 - b0)
                if k + 1 - b0 > cap: tot["BLKV"] += 1
            if evs: k0 = k + 1; continue
            tot["maxblk"] = max(tot["maxblk"], k + 1 - k0)
            Wn = W(s2, t); j = k - k0
            for y in range(g.n):
                if g.owner[y] == 0 and s[y] != s2[y] and Wn[y][2] < j + 1: tot["VIOL"] += 1
                if x1[y] != x2[y] and Wn[y][2] < j + 1: tot["VIOL"] += 1
        tot["E"] += E; tot["Esrc"] += Es; tot["maxL"] = max(tot["maxL"], len(F) - 1); tot["maxEsrc"] = max(tot["maxEsrc"], Es)
        tot["maxE"] = max(tot["maxE"], E); tot["maxHXS"] = max([tot["maxHXS"]] + list(hxs.values()))
    return tot
if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    g = pg.read(a[0]); st = n5b.read_start(a[1], g) if len(a) > 1 else (None, None)
    try: tr, fb = xcn.trace(g, *st)
    except Exception as e: print(f"SRC {os.path.basename(a[0])} n {g.n} RUN-ERROR {e}"); sys.exit(0)
    r = check(g, tr, fb)
    print(f"SRC {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in r.items()))
