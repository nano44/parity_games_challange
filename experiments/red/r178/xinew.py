#!/usr/bin/env python3
"""L-RED R178 XINEW (real game): Lemma XI-NEW in N5's own FL runs. An FL run = consecutive fallback-free transitions with tau and
sigma-bar constant and W_j = W_(j-1) (W = valuation against tau), sigma changing. At every transition j of an FL run except its first,
among the movers of least W-length (if one is non-corner), a non-corner one has a new option w that was NOT in the previous arena A_(j-2)(h)
(= {sigma_(j-2)(h)} u I_sigma at state j-2). Prints XINEW <game> fltrans checked viol nocand (nocand = all least movers are corners).
Usage: xinew.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual, step
import pg
def play(succ1, x):
    seq = [x]; seen = {x}; v = x
    while True:
        v = succ1[v]
        if v in seen: return seq
        seen.add(v); seq.append(v)
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n, own, pr = g.n, g.owner, g.prio; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
S, T, SB, A, F = [list(s)], [list(t)], [], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    vs, sb = E.evaluate(tuple(S[-1])); SB.append(sb)
    if r is None: A.append(None); break
    ns, nt, Is, It, fb, _, _ = r
    av = {v: {S[-1][v]} for v in range(n) if own[v] == 0}
    for v, w in Is: av[v].add(w)
    A.append(av); F.append(fb); S.append(ns); T.append(nt)
K = len(S) - 1; fl = 0; chk = 0; viol = 0; nocand = 0; prev_fl = False
for j in range(1, K + 1):
    ok = not F[j - 1] and T[j] == T[j - 1] and SB[j] == SB[j - 1] and S[j] != S[j - 1]
    if ok:
        tau = T[j - 1]; EW = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        Wj = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        Wp = EW.evaluate(tuple(S[j - 1][v] if own[v] == 0 else -1 for v in range(n)))[0]
        ok = Wj == Wp
    if not ok: prev_fl = False; continue
    fl += 1
    if prev_fl and j >= 2 and T[j - 2] == T[j - 1] and SB[j - 2] == SB[j - 1]:
        succ1 = [S[j][v] if own[v] == 0 else T[j - 1][v] for v in range(n)]
        mv = [h for h in range(n) if own[h] == 0 and S[j][h] != S[j - 1][h]]
        nc = [h for h in mv if h not in play(succ1, S[j - 1][h]) and h not in play(succ1, S[j][h]) and h != Wj[h][0]]
        m = min(Wj[h][2] for h in mv); low = [h for h in mv if Wj[h][2] == m]
        if not any(h in nc for h in low): nocand += 1
        else:
            chk += 1
            if not any(S[j][h] not in A[j - 2][h] for h in low if h in nc): viol += 1; print("XIVIOL", j, low)
    prev_fl = True
print(f"XINEW {os.path.basename(sys.argv[1])} n {n} K {K} fltrans {fl} checked {chk} viol {viol} nocand {nocand}")
