#!/usr/bin/env python3
"""L-NEW box 105 (docs/new/N5-O1-box105.md): Lemma O1 on W-runs. W-runs as box92/xirun.py. For every return of Even X to g (X leaves g at
j -> j + 1, re-enters at k -> k + 1, X not holding g on [j + 1, k]):
  O1W   W(X) changes at some transition of [j, k] (leave, inside or re-entry);
  O1IN  W(X) changes at some transition strictly inside, i.e. of [j + 1, k - 1];
  LEAVE_TIE / RET_TIE  the leave (re-entry) transition does not change W(X) (a tie switch in W).
Prints counts of returns violating O1W and O1IN, the tie counts, and the first violating return (state indices, X, g, W(X) along the window).
Usage: o1.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; EVN = [v for v in range(n) if own[v] == 0]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
tcls = {}
c = dict(returns=0, O1W=0, O1IN=0, LEAVE_TIE=0, RET_TIE=0, BOTH_TIE=0); wit = None
for a, b in runs:
    tau = TAU[a]; W = [Wv(k, tau) for k in range(a, b + 1)]
    lastleave = {}
    for k in range(a, b):
        for y in EVN:
            if S[k + 1][y] == S[k][y]: continue
            z = S[k + 1][y]
            if (y, z) in lastleave:
                j = lastleave[(y, z)]; c['returns'] += 1
                ch = [q for q in range(j, k + 1) if W[q + 1 - a][y] != W[q - a][y]]
                lt = W[j + 1 - a][y] == W[j - a][y]; rt = W[k + 1 - a][y] == W[k - a][y]
                c['LEAVE_TIE'] += lt; c['RET_TIE'] += rt; c['BOTH_TIE'] += lt and rt
                if lt:
                    cn = W[j - a][y][0]; par = E.par[cn]
                    inI = all(W[q + 1 - a] == W[q - a] for q in range(j, k + 1))
                    key = ('TIE', 'odd' if par == 1 else 'even', 'oneInterval' if inI else 'Wchanges', 'own' if cn == y else 'nonown')
                    tcls[key] = tcls.get(key, 0) + 1
                if not ch:
                    c['O1W'] += 1
                    if wit is None: wit = (a, b, j, k, y, z, [W[q - a][y] for q in range(j, k + 2)])
                if not [q for q in ch if j + 1 <= q <= k - 1]: c['O1IN'] += 1
            lastleave[(y, S[k][y])] = k
print(f"O1 {os.path.basename(sys.argv[1])} n {n} W-runs {len(runs)} " + " ".join(f"{k} {v}" for k, v in c.items()))
if tcls: print("  TIECLASS", sorted(tcls.items()))
if wit: print(f"  first O1W violation: W-run {wit[0]}-{wit[1]} X {wit[4]} leaves {wit[5]} at {wit[2]}, re-enters at {wit[3]}; W(X) on [j, k+1]: {wit[6]}")
