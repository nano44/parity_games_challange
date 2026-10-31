#!/usr/bin/env python3
"""L-NEW box 111: trade-down root switches of W-runs (box 110 RESET-ROOT). Per transition k: every switched Even y with a RANK-bit reset in
W(y): old -> new target, q = first differing CS position (rank index: vertex u<v>(p<prio>) or len), the reset positions (rank bits),
and the Xi- and W-values' first difference between the two targets at k (who overtook whom). Summary TDROOT per selector.
Usage: tdtrace.py GAME.pg [START] [MAXLINES]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].endswith(".start") else None
ML = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 60
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Wraw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
byrank = {E.rank[v]: v for v in range(n)}
def rbits(x):
    c, m, l = x
    return tuple((1 if (m >> r) & 1 else 0) if E.rankpar[r] == 0 else (0 if (m >> r) & 1 else 1) for r in range(n - 1, -1, -1))
def nm(i): return f"u{byrank[n - 1 - i]}"
def fd(a, b):
    A, B = rbits(a), rbits(b)
    for i in range(n):
        if A[i] != B[i]: return nm(i)
    return "len" if a != b else "="
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wraw(k, TAU[k])] != [x[0] for x in Wraw(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
cnt = {}; lines = 0
for run in runs:
    tau = TAU[run[0]]
    for k in run:
        W0, W1 = Wraw(k, tau), Wraw(k + 1, tau); X0 = E.evaluate(S[k])[0]
        for y in range(n):
            if own[y] != 0 or S[k][y] == S[k + 1][y]: continue
            A, B = rbits(W0[y]), rbits(W1[y])
            res = [nm(i) for i in range(n) if A[i] > B[i]]
            if not res: continue
            a, b = S[k][y], S[k + 1][y]; cnt[y] = cnt.get(y, 0) + 1
            if lines < ML:
                lines += 1
                print(f"k {k} y {y}: {a}->{b} q {fd(W0[y], W1[y])} resets {res[:4]}{'...' if len(res) > 4 else ''} ({len(res)}) "
                      f"| W(b) vs W(a) at k: {fd(W0[a], W0[b])}; Xi(b) vs Xi(a): {fd(X0[a], X0[b])}")
print("TDROOT", os.path.basename(sys.argv[1]), sorted(cnt.items(), key=lambda x: -x[1])[:8])
