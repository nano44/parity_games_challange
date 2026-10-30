#!/usr/bin/env python3
"""L-NEW box 79 (P-N5-WCH §4 DATA): check the packet's sharpened Theorem RET-WCH and Corollary RUN-WCH on W-runs (R89: tau fixed, no S4c,
lambda_W fixed; as box78/retwch.py). For a return u of Even v to e with last leave k: if W(v) changes at k the return must be paid by a change
of W(e) at some transition s in [k, u]; otherwise it is a TT leave (W(v) unchanged at k). Checks per (F, v, e): RET <= WCH_F(e) + TT_F(v, e);
per (F, v): sum_e TT_F(v, e) <= TIE_F(v) (switches of v in F with W(v) unchanged); per F: |F| <= m_E + sum_e d_E(e) WCH_F(e) + TIE_F.
In N5-LZC (--lzc) TIE_F must be 0 (LZ-STRICT). Usage: wchpk.py GAME.pg [START] [--lzc]"""
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
mE = sum(len(g.succ[v]) for v in ev); dE = Counter(w for v in ev for w in g.succ[v])
Wc = {}
def eng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def Wv(k, tau): return eng(tau).evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = Counter(); worst = 0; maxratio = 0.0
for a, b in runs:
    tau = TAU[a]; W = {k: Wv(k, tau) for k in range(a, b + 1)}
    wch = {z: [s_ for s_ in range(a, b) if W[s_ + 1][z] != W[s_][z]] for z in range(n)}
    ret = Counter(); tt = Counter(); tie = Counter()
    for v in ev:
        held = {S[a][v]}; lastleave = {}
        for k in range(a, b):
            if S[k + 1][v] == S[k][v]: continue
            e_old, e = S[k][v], S[k + 1][v]
            lastleave[e_old] = k
            if W[k + 1][v] == W[k][v]: tie[v] += 1; tt[(v, e_old)] += 1
            if e in held:
                c['returns'] += 1; ret[(v, e)] += 1; kk = lastleave.get(e)
                if kk is None: c['no-leave-in-F'] += 1; continue
                if W[kk + 1][v] == W[kk][v]: c['TT'] += 1
                elif any(kk <= s_ <= k for s_ in wch[e]): c['paid-W'] += 1
                else: c['UNPAID'] += 1
            held.add(e)
    for (v, e), x in ret.items():
        if x > len(wch[e]) + tt[(v, e)]: c['per-edge-viol'] += 1
        worst = max(worst, x)
    tieF = sum(tie.values()); c['TIE'] += tieF
    bound = mE + sum(dE[z] * len(wch[z]) for z in range(n)) + tieF
    if b - a > bound: c['RUN-viol'] += 1
    maxratio = max(maxratio, (b - a) / bound)
print(f"WCHPK {os.path.basename(args[0])} n {n} wruns {len(runs)} {dict(c)} max-ret-per-edge {worst} max|F|/bound {maxratio:.3f}")
