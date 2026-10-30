#!/usr/bin/env python3
"""L-RED R136: route-pattern counter (n5b SPEC run; Lemma WAIT-CYCLE's triples).
Self-routed block of (X, g) at state s: X Even, g a successor != sigma(X), g not offered at X, and the sigma-bar-play from g passes X (X not
on its own play's cycle). Its PATTERN is the tuple of Even choices on pi (the play from g up to X).
Per W-run (tau constant) and per (X, g): PAT = distinct patterns; SERVED = switches X -> g made after a self-routed block of (X, g) in the same W-run (an upward wait served; one per block
episode: the flag clears at the switch).
Prints the totals and the max PAT / SERVED over all (X, g) and W-runs. WAIT-CYCLE: a served wait's pattern never recurs while sigma(X) = g.
Usage: patcount.py GAME.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
g = n5b.pg.read(sys.argv[1]); n = g.n
names = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(';').split()
    if len(a) >= 5 and a[0].isdigit(): names[int(a[0])] = a[4].strip('"'); s0, t0 = n5b.read_start(sys.argv[2], g)
N = n5b.N5(g); N.mode = "spec"; tr = []; N.run(s0, t0, trace=tr)
blocks = 0; mpat = (0, None); mserv = (0, None); served_tot = 0; prevt = None; worst = (0, 0, None); pats = {}; inblk = {}; serv = {}
for si, (sig, tau) in enumerate(tr):
    if tau != prevt: pats, inblk, serv, rv, swc = {}, {}, {}, {}, {}; prevt = tau; wstart = si
    elif si > 0:
        for v in range(n):
            if g.owner[v] == 0 and sig[v] != tr[si - 1][0][v]: swc[v] = swc.get(v, 0) + 1
    vs, sbar = N.opt(N.SG, list(sig)); Is = N.improving(N.SG, sig, N.ev(N.SG, list(sig)))
    nxt = lambda v: sig[v] if g.owner[v] == 0 else sbar[v]
    now = set()
    for X in range(n):
        if g.owner[X] != 0: continue
        if inblk.get((X, sig[X])):                       # the switch X -> g ended a block interval: a served wait
            serv[X, sig[X]] = serv.get((X, sig[X]), 0) + 1; served_tot += 1
            if serv[X, sig[X]] > mserv[0]: mserv = (serv[X, sig[X]], (X, sig[X]))
            inblk[X, sig[X]] = False
        seen, y = set(), sig[X]
        while y not in seen and y != X: seen.add(y); y = nxt(y)
        if y == X: continue
        for gg in g.succ[X]:
            if gg == sig[X] or gg in Is.get(X, []): continue
            path, y, ok = [], gg, False
            while y not in path:
                if y == X: ok = True; break
                path.append(y); y = nxt(y)
            if ok:
                blocks += 1; now.add((X, gg))
                pats.setdefault((X, gg), set()).add(tuple((v, sig[v]) for v in path if g.owner[v] == 0))
                rv.setdefault((X, gg), set()).update(v for v in path if g.owner[v] == 0)
                if len(pats[X, gg]) > mpat[0]: mpat = (len(pats[X, gg]), (X, gg))
                bound = 1 + sum(swc.get(v, 0) for v in rv[X, gg])                   # PAT <= 1 + switches on route vertices so far
                if len(pats[X, gg]) > bound: print("PAT-BOUND VIOLATION", X, gg, si)
                top = max(rv[X, gg], key=lambda v: swc.get(v, 0)) if rv[X, gg] else None
                if len(pats[X, gg]) >= worst[0]: worst = (len(pats[X, gg]), swc.get(top, 0), top)
    for key in now: inblk[key] = True                    # pending until X switches to g inside this W-run
print(f"PATCOUNT {os.path.basename(sys.argv[1])} n {n} iterations {len(tr) - 1} self-routed-blocks {blocks} served-waits {served_tot} "
      f"max-PAT {mpat[0]} max-SERVED {mserv[0]} at-max-PAT: busiest route vertex {names.get(worst[2], worst[2])} with {worst[1]} switches")
