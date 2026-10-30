#!/usr/bin/env python3
"""L-NEW box 78: check Theorem RET-WCH. In a W-run F (rho.py's), an Even RETURN of v to e at transition u (sigma_{u+1}(v) = e != sigma_u(v),
v held e earlier in F) with v's last leave of e at k (sigma_k(v) = e != sigma_{k+1}(v), k < u) is PAID if W(e) changes at some transition
s in [k+1, u] (W read with F's tau), or if the leave was a TIE-LEAVE (e still W_{k+1}-consistent at v, consistent() below: both forms of Lemma TIE).
Counters: returns, paid-by-W(e), paid-by-tie-leave, UNPAID (must be 0), and per (F, v, e) the check RET <= WCH_F(e) + TIELEAVE_F(v, e).
Usage: retwch.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
import pg
from collections import Counter
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]
Wc = {}
def eng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def Wv(k, tau): return eng(tau).evaluate(S[k])[0]
def consistent(Ek, v, Wk, e):
    """e is W_k-consistent at v: off-cycle form v (+) W(e) = W(v), or (Lemma TIE (b)) cycle-node form W(v) = (v, empty, 0) and W(e) has
    cycle node v and empty path set."""
    if Wk[v][2] >= 1: return Ek.extend(v, Wk[e]) == Wk[v]
    return Wk[v] == (v, 0, 0) and Wk[e][0] == v and Wk[e][1] == 0
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = Counter(); worst = 0
for a, b in runs:
    tau = TAU[a]; Ek = eng(tau); W = {k: Wv(k, tau) for k in range(a, b + 1)}
    wch = {z: [s for s in range(a, b) if W[s + 1][z] != W[s][z]] for z in range(n)}
    ret = Counter(); tl = Counter()
    for v in ev:
        held = {S[a][v]}; lastleave = {}
        for k in range(a, b):
            if S[k + 1][v] == S[k][v]: continue
            e_old, e = S[k][v], S[k + 1][v]
            lastleave[e_old] = k
            if consistent(Ek, v, W[k + 1], e_old): tl[(v, e_old)] += 1
            if e in held:
                c['returns'] += 1; ret[(v, e)] += 1; kk = lastleave.get(e)
                if kk is None: c['no-leave-in-F'] += 1; continue
                if any(kk + 1 <= s_ <= k for s_ in wch[e]): c['paid-W'] += 1
                elif consistent(Ek, v, W[kk + 1], e): c['paid-tie'] += 1
                else: c['UNPAID'] += 1
            held.add(e)
    for (v, e), x in ret.items():
        if x > len(wch[e]) + tl[(v, e)]: c['per-edge-viol'] += 1
        worst = max(worst, x)
print(f"RETWCH {os.path.basename(args[0])} n {n} wruns {len(runs)} {dict(c)} max-ret-per-edge {worst}")
