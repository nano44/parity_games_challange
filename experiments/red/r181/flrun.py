#!/usr/bin/env python3
"""L-RED R181 FLRUN: N5's own FL runs and their gating changes. FL transition j as in R179 odxi (no fallback; tau, sigma-bar unchanged;
sigma changes; W unchanged everywhere). A maximal run of consecutive FL transitions has length L. Gating changes inside the run
(FL-ANCHOR's gating data, L-NEW 46 box 132): Xi-changes at ODIFF vertices plus Xi-changes at W-cycle nodes (vertices c with
W(c)'s cycle node = c), counted over the run's transitions. Prints FLRUN <game> n m K LFL gate (for the longest run; ties: more gating)
and GATEMAX (max gating changes in any run). Usage: flrun.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual, step
import pg
def analyse(g, st=None, cap=3000):
    n, own, pr = g.n, g.owner, g.prio; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    S, T, F = [list(s)], [list(t)], []
    while len(S) <= cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(list(r[0])); T.append(list(r[1])); F.append(r[4])
    V, SB = [], []
    for x in S:
        vs, sb = E.evaluate(tuple(x)); V.append(vs); SB.append(sb)
    K = len(S) - 1; runs = []; cur = None
    for j in range(1, K + 1):
        ok = not F[j - 1] and T[j] == T[j - 1] and SB[j] == SB[j - 1] and S[j] != S[j - 1]
        if ok:
            tau = T[j - 1]; EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
            Wj = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
            Wp = EW.evaluate(tuple(S[j - 1][v] if own[v] == 0 else -1 for v in range(n)))[0]
            ok = Wj == Wp
        if not ok: cur = None; continue
        gate = sum(1 for o in range(n) if own[o] == 1 and SB[j][o] != tau[o] and V[j][o] != V[j - 1][o])
        gate += sum(1 for c in range(n) if Wj[c][0] == c and V[j][c] != V[j - 1][c])
        if cur is None or cur[1] != j - 1: cur = [j, j, 0]; runs.append(cur)
        cur[1] = j; cur[2] += gate
    best = max(runs, key=lambda r: (r[1] - r[0] + 1, r[2]), default=[0, -1, 0])
    return dict(n=n, m=sum(len(x) for x in g.succ), K=K, LFL=best[1] - best[0] + 1, gate=best[2], gatemax=max((r[2] for r in runs), default=0), runs=runs)
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None; R = analyse(g, st)
    print(f"FLRUN {os.path.basename(sys.argv[1])} n {R['n']} m {R['m']} K {R['K']} LFL {R['LFL']} gate {R['gate']} GATEMAX {R['gatemax']}")
