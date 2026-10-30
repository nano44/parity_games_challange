#!/usr/bin/env python3
"""L-NEW box 74: rho per W-run. W-run as in L-SI's tied.py / box72 txc.py (tau fixed, no S4c, sigma changing, W's cycle-node map fixed).
rho_F := pairs (transition s of F, Odd choice vertex q (out-degree >= 2)) with Xi_{s+1}(q) != Xi_s(q) (RESULTS R56's rho, per W-run).
Per W-run: len (transitions), wch (transitions changing W somewhere), wflat (len - wch), rho, max per q, sbar-changes at Q (pairs with
sbar_s(q) != sbar_{s+1}(q)), and sum_v WCH_F(v) (pairs (v, s) with W(v) strictly rising). Usage: rho.py GAME.pg [START] [--lzc]"""
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
T = len(S) - 1
EV = [E.evaluate(x) for x in S]; XI = [e[0] for e in EV]; SB = [e[1] for e in EV]
Q = [x for x in range(n) if g.owner[x] == 1 and len(set(g.succ[x])) >= 2]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    tau = TAU[k]
    ok = TAU[k + 1] == tau and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, tau)] == [x[0] for x in Wv(k + 1, tau)]
    if not ok: cur = None; continue
    if cur is None: cur = dict(start=k, len=0, wch=0, rho=0, perq=Counter(), sbq=0, wsum=0); runs.append(cur)
    w0, w1 = Wv(k, tau), Wv(k + 1, tau); Ek = Wc[tau]
    cur['len'] += 1; cur['wch'] += w0 != w1; cur['wsum'] += sum(1 for x in range(n) if Ek.key(w1[x]) > Ek.key(w0[x]))
    for q in Q:
        if XI[k][q] != XI[k + 1][q]: cur['rho'] += 1; cur['perq'][q] += 1
        if SB[k][q] != SB[k + 1][q]: cur['sbq'] += 1
best = max(runs, key=lambda r: r['rho']) if runs else None
mx = lambda key: max((r[key] for r in runs), default=0)
print(f"RHO {os.path.basename(args[0])} n {n} |Q| {len(Q)} iters {T} wruns {len(runs)} max-len {mx('len')} max-wflat {max((r['len'] - r['wch'] for r in runs), default=0)} "
      f"max-rho {mx('rho')} max-rho-per-q {max((max(r['perq'].values(), default=0) for r in runs), default=0)} max-sbq {mx('sbq')} "
      f"best-run {'none' if best is None else (best['len'], best['wch'], best['rho'], best['sbq'], best['wsum'])} total-rho {sum(r['rho'] for r in runs)}")
