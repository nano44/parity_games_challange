#!/usr/bin/env python3
"""L-NEW box 76: Odd DECISIONS per W-run (rho.py's W-run). SBQ_F = sbar-changes at Odd choice vertices = NEW_F + RET_F, where a change of
sbar(q) to e is NEW if q has not held e earlier in F (counting F's first state), else a RETURN. NEW_F <= sum_q (deg q - 1) always.
Also Even's side, same split, for sigma (NEWE / RETE). Usage: sbqrun.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
import pg
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; SB = [E.evaluate(x)[1] for x in S]
Q = [x for x in range(n) if g.owner[x] == 1 and len(set(g.succ[x])) >= 2]; ev = [v for v in range(n) if g.owner[v] == 0]
Wc = {}
def lw(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return [x[0] for x in Wc[tau].evaluate(S[k])[0]]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and lw(k, TAU[k]) == lw(k + 1, TAU[k])
    if not ok: cur = None; continue
    if cur is None:
        cur = dict(len=0, new=0, ret=0, newe=0, rete=0, hq={q: {SB[k][q]} for q in Q}, he={v: {S[k][v]} for v in ev}); runs.append(cur)
    cur['len'] += 1
    for q in Q:
        e = SB[k + 1][q]
        if e != SB[k][q]:
            if e in cur['hq'][q]: cur['ret'] += 1
            else: cur['new'] += 1; cur['hq'][q].add(e)
    for v in ev:
        e = S[k + 1][v]
        if e != S[k][v]:
            if e in cur['he'][v]: cur['rete'] += 1
            else: cur['newe'] += 1; cur['he'][v].add(e)
mO = sum(len(set(g.succ[q])) - 1 for q in Q); mE = sum(len(set(g.succ[v])) - 1 for v in ev)
mx = lambda k: max((r[k] for r in runs), default=0)
print(f"SBQRUN {os.path.basename(args[0])} n {n} mO {mO} mE {mE} wruns {len(runs)} max-len {mx('len')} max-sbq {max((r['new'] + r['ret'] for r in runs), default=0)} "
      f"max-new {mx('new')} max-ret {mx('ret')} max-newE {mx('newe')} max-retE {mx('rete')} tot-ret {sum(r['ret'] for r in runs)} tot-retE {sum(r['rete'] for r in runs)}")
