#!/usr/bin/env python3
"""L-SI box 53 §6: own-cycle-node sbar-flips (XCN) per W-run. xcn.py GAME.pg [START]: XCN_TR (most XCN transitions in one W-run), XCN_V (most at one vertex), XCN_RUN_ALL (whole run). Whole-run transition counts: XA (an own-node flip where o is its own Xi-cycle node at exactly one of k, k+1), XB (own at both: a DFS re-order), LAMCH (transitions changing lambda_Xi; RESULTS R47 Lemma PHI bounds them by n(n-1)), XANL (XA transitions with lambda_Xi unchanged; impossible, a control). xcnrs.py SEED COUNT N DMAX BIAS: random search for the most XCN transitions in one W-run."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None)
S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
EV = [E.evaluate(x) for x in S]; ODD = [o for o in range(n) if own[o] == 1]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs, cur = [], None
for k in range(len(S) - 1):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
xt, xv, wr = 0, 0, 0
for p, q in runs:
    per = {}; tr = 0
    for k in range(p, q):
        f = [o for o in ODD if EV[k][1][o] != EV[k + 1][1][o] and (EV[k][0][o][0] == o or EV[k + 1][0][o][0] == o)]
        tr += bool(f)
        for o in f: per[o] = per.get(o, 0) + 1
    xt = max(xt, tr); xv = max(xv, max(per.values(), default=0)); wr = max(wr, q - p)
xa = sum(1 for k in range(len(S) - 1) for o in ODD if EV[k][1][o] != EV[k + 1][1][o] and (EV[k][0][o][0] == o or EV[k + 1][0][o][0] == o))
XB = sum(1 for k in range(len(S) - 1) if any(EV[k][1][o] != EV[k + 1][1][o] and EV[k][0][o][0] == o and EV[k + 1][0][o][0] == o for o in ODD))
XA = sum(1 for k in range(len(S) - 1) if any(EV[k][1][o] != EV[k + 1][1][o] and (EV[k][0][o][0] == o) != (EV[k + 1][0][o][0] == o) for o in ODD))
LAM = sum(1 for k in range(len(S) - 1) if [x[0] for x in EV[k][0]] != [x[0] for x in EV[k + 1][0]])
XANL = sum(1 for k in range(len(S) - 1) if any(EV[k][1][o] != EV[k + 1][1][o] and (EV[k][0][o][0] == o) != (EV[k + 1][0][o][0] == o) for o in ODD) and [x[0] for x in EV[k][0]] == [x[0] for x in EV[k + 1][0]])
print(os.path.basename(a[0]), "n", n, "T", len(S) - 1, "LMAX", wr, "XCN_TR", xt, "XCN_V", xv, "XCN_RUN_ALL", xa, "XA", XA, "XB", XB, "LAMCH", LAM, "XANL", XANL)
