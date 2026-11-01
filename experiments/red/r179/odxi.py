#!/usr/bin/env python3
"""L-RED R179 ODXI: Xi-changes at ODIFF vertices inside N5's own FL runs.
FL transition j: no fallback at j, tau_j = tau_(j-1), sigma-bar_j = sigma-bar_(j-1), sigma_j != sigma_(j-1), and W_j = W_(j-1) everywhere
(W = valuation against tau_(j-1)). ODIFF vertex o: Odd, sigma-bar(o) != tau(o) (constant across j-1, j). XICH: Xi_j(o) != Xi_(j-1)(o).
Prints ODXI <game> n K fltrans odiff_max xich (number of (j, o) pairs) and one line per pair. Usage: odxi.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual, step
import pg

def analyse(g, st=None, cap=2000, verbose=False):
    n, own, pr = g.n, g.owner, g.prio; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    S, T, F = [list(s)], [list(t)], []
    while len(S) <= cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(list(r[0])); T.append(list(r[1])); F.append(r[4])
    V = []; SB = []
    for x in S:
        vs, sb = E.evaluate(tuple(x)); V.append(vs); SB.append(sb)
    K = len(S) - 1; fl = 0; xich = 0; odm = 0; pairs = []; flj = []
    for j in range(1, K + 1):
        if F[j - 1] or T[j] != T[j - 1] or SB[j] != SB[j - 1] or S[j] == S[j - 1]: continue
        tau = T[j - 1]; EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        Wj = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        Wp = EW.evaluate(tuple(S[j - 1][v] if own[v] == 0 else -1 for v in range(n)))[0]
        if Wj != Wp: continue
        fl += 1; flj.append(j); od = [o for o in range(n) if own[o] == 1 and SB[j][o] != tau[o]]; odm = max(odm, len(od))
        for o in od:
            if V[j][o] != V[j - 1][o]: xich += 1; pairs.append((j, o, V[j - 1][o], V[j][o]))
    return dict(n=n, K=K, fl=fl, odm=odm, xich=xich, pairs=pairs, flj=flj)

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R = analyse(g, st)
    print(f"ODXI {os.path.basename(sys.argv[1])} n {R['n']} K {R['K']} fltrans {R['fl']} odiff_max {R['odm']} xich {R['xich']}")
    for p in R["pairs"][:20]: print("  XICH j", p[0], "o", p[1], p[2], "->", p[3])
