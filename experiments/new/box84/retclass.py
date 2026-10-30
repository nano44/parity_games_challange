#!/usr/bin/env python3
"""L-NEW box 84 (Theorem TRIPLE-RED, docs/new/N5-WAIT-box84.md §4): classify every RETURN in every W-run F of N5 (R89 W-runs, as
box83/wchmax.py). A return of Even X to g at transition t2 - 1 -> t2 in F, with last leave s -> s + 1 of g in F (s >= a), is
  REG  if some state in [s + 1, t2 - 1] has a REG self-routed block of (X, g) (waits.py), else
  E0   if some state there has an E0 block of (X, g), else
  FREE (g never self-route-blocked at X while X was away).
Prints per game: |F| max, max_e WCH_F(e), and per (F, X, g) maxima of REG / E0 / FREE returns, plus totals; checks |F| <= #switch events
<= m_E + returns (NEW-BOUND form) and E0 returns <= n - 1 per (X, g). Usage: retclass.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; mE = sum(len(g.succ[v]) for v in ev)
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
blk = {}
def blocks(k):
    if k in blk: return blk[k]
    sig = S[k]; vs, sbar = E.evaluate(sig); Is = set(E.improving(sig, vs)); nxt = lambda v: sig[v] if g.owner[v] == 0 else sbar[v]; out = {}
    for X in ev:
        for gg in g.succ[X]:
            if gg == sig[X] or (X, gg) in Is: continue
            path, y, ok = [], gg, False
            while y not in path:
                if y == X: ok = True; break
                path.append(y); y = nxt(y)
            if not ok: continue
            cyc, y = [X], sig[X]
            while y != X and y not in cyc and len(cyc) <= n: cyc.append(y); y = nxt(y)
            if y == X and any(v in cyc for v in path): continue
            e0 = vs[X][0] == X and all(E.rank[v] < E.rank[X] for v in path)
            out[(X, gg)] = 'REG' if not e0 or out.get((X, gg)) == 'REG' else 'E0'
    blk[k] = out; return out
tot = dict(REG=0, E0=0, FREE=0, sw=0, bound_viol=0); mx = dict(REG=0, E0=0, FREE=0, F=0, wch=0)
for a, b in runs:
    mx['F'] = max(mx['F'], b - a); W = [Wv(x, TAU[a]) for x in range(a, b + 1)]
    mx['wch'] = max([mx['wch']] + [sum(1 for i in range(b - a) if W[i + 1][e] != W[i][e]) for e in range(n)])
    per = {}; sw = 0
    for X in ev:
        held = {S[a][X]}; last = {}
        for k in range(a, b):
            if S[k + 1][X] == S[k][X]: continue
            sw += 1; old, new = S[k][X], S[k + 1][X]; last[old] = k
            if new in held and new in last:
                cls = 'FREE'
                for q in range(last[new] + 1, k + 1):
                    c = blocks(q).get((X, new))
                    if c == 'REG': cls = 'REG'; break
                    if c == 'E0': cls = 'E0'
                per[(X, new, cls)] = per.get((X, new, cls), 0) + 1; tot[cls] += 1
            held.add(new)
    tot['sw'] += sw
    if b - a > sw or sw > mE + sum(per.values()): tot["bound_viol"] += 1
    for (X, gg, cls), v in per.items(): mx[cls] = max(mx[cls], v)
print(f"RETCLASS n {n} mE {mE} runs {len(runs)} totals {tot} maxima {mx}")
