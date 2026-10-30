#!/usr/bin/env python3
"""L-NEW box 94 (docs/new/N5-KO-box94.md): N5 on random games of the class C^kO (at most k Odd vertices with out-degree >= 2).
Per game: iterations T, tau-changes, S4c fallbacks, W-runs (as box85/xirise.py), max |F|; per W-run the events of L-SI box 52 / L-RED R143:
(i) sbar changes (only at Odd choice vertices on C^kO), (ii) CN switches, (iii) Xi changes at upward heads, split into D-heads
(sbar(g), g in D) and C-heads (Xi-successors of W-cycle nodes); max per-vertex counts SBV (sbar flips of one vertex), HXD (Xi changes of a
D-head while it is one), HXC (same for C-heads). Usage: kodata.py n k deg trials seed [MAXN]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
n, k, deg, trials, seed = map(int, sys.argv[1:6]); rng = random.Random(seed)
def game():
    own = [rng.randint(0, 1) for _ in range(n)]
    odd = [v for v in range(n) if own[v] == 1]; ch = set(rng.sample(odd, min(k, len(odd))))
    succ = []
    for v in range(n):
        d = rng.randint(2, deg) if (own[v] == 0 or v in ch) else 1
        succ.append(sorted(rng.sample(range(n), min(d, n))))
    pr = list(range(n)); rng.shuffle(pr)
    return pg.Game(pr, own, succ)
tot = dict(T=0, runs=0); mx = dict(T=0, taus=0, fb=0, runs=0, F=0, E=0, EI=0, EII=0, EIIID=0, EIIIC=0, SBV=0, HXD=0, HXC=0, Fn=0.0); arg = {}
for it in range(trials):
    g = game(); own = g.owner
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
    while len(S) < 20000:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    T = len(S) - 1; EV = [E.evaluate(x) for x in S]; XK = [[E.key(y) for y in e[0]] for e in EV]
    Wc = {}
    def Wv(j, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[j])[0]
    runs, cur = [], None
    for j in range(T):
        ok = TAU[j + 1] == TAU[j] and not FB[j] and [x[0] for x in Wv(j, TAU[j])] == [x[0] for x in Wv(j + 1, TAU[j])]
        if not ok: cur = None; continue
        if cur is None: cur = [j, j]; runs.append(cur)
        cur[1] = j + 1
    loc = dict(T=T, taus=sum(1 for j in range(T) if TAU[j + 1] != TAU[j]), fb=sum(1 for x in FB if x), runs=len(runs))
    for p, q in runs:
        tau = TAU[p]; C = {x for x in range(n) if Wv(p, tau)[x][0] == x}
        def UD(j):
            sb = EV[j][1]; return {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]}
        def UC(j):
            sb = EV[j][1]; return {(S[j][x] if own[x] == 0 else sb[x]) for x in C}
        ev = ei = eii = eiiid = eiiic = 0; sbv = {}; hxd = {}; hxc = {}
        for j in range(p, q):
            fl = [o for o in range(n) if own[o] == 1 and EV[j][1][o] != EV[j + 1][1][o]]
            for o in fl: sbv[o] = sbv.get(o, 0) + 1
            e2 = any(S[j][x] != S[j + 1][x] for x in C if own[x] == 0)
            chd = [u for u in UD(j) | UD(j + 1) if XK[j][u] != XK[j + 1][u]]
            chc = [u for u in UC(j) | UC(j + 1) if XK[j][u] != XK[j + 1][u]]
            for u in chd: hxd[u] = hxd.get(u, 0) + 1
            for u in chc: hxc[u] = hxc.get(u, 0) + 1
            ei += bool(fl); eii += e2; eiiid += bool(chd); eiiic += bool(chc); ev += bool(fl or e2 or chd or chc)
        F = q - p
        for key_, val in (('F', F), ('E', ev), ('EI', ei), ('EII', eii), ('EIIID', eiiid), ('EIIIC', eiiic), ('SBV', max(sbv.values(), default=0)),
                          ('HXD', max(hxd.values(), default=0)), ('HXC', max(hxc.values(), default=0))):
            if val > mx[key_]: mx[key_] = val; arg[key_] = (seed, it)
    for key_ in ('T', 'taus', 'fb', 'runs'):
        if loc[key_] > mx[key_]: mx[key_] = loc[key_]; arg[key_] = (seed, it)
    tot['T'] += T; tot['runs'] += len(runs)
mx['Fn'] = round(mx['F'] / n, 3)
print(f"KODATA n {n} k {k} deg {deg} trials {trials} seed {seed} totals {tot} maxima {mx} argmax {arg}")
