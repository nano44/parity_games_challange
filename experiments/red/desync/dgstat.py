#!/usr/bin/env python3
"""L-RED R135: per-run counts for a game + start (n5b SPEC trace; W = val(sigma, tau) and Xi = val(sigma, sigma-bar) by the fleet Engine).
Prints: iterations, fallbacks, tau-changes, W-runs (maximal tau-constant stretches), distinct W(TOP) values, the largest number of
W-changes of one vertex inside one W-run, and the cycle nodes seen by W and by Xi (a Xi cycle node other than the sink = Odd closed a cycle).
Usage: dgstat.py GAME.pg START [TOPNAME]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "si", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b, pg
from si import Engine
gp, sp = sys.argv[1], sys.argv[2]; top = sys.argv[3] if len(sys.argv) > 3 else "T"
names = {}
for l in open(gp):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): names[int(a[0])] = a[4].strip('"')
g5 = n5b.pg.read(gp); s0, t0 = n5b.read_start(sp, g5)
N = n5b.N5(g5); N.mode = "spec"; tr, fbt = [], []; N.run(s0, t0, trace=tr, fbtrace=fbt)
g = pg.parse("".join(l for l in open(gp) if not l.lstrip().startswith("%"))); n = g.n
T = [v for v, x in names.items() if x == top][0]
E = Engine(g); WE = {}
def W(s, t):
    if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    return WE[t].evaluate(tuple(x if g.owner[v] == 0 else -1 for v, x in enumerate(s)))[0]
tch = runs = 0; best = (0, None); tv = []; lw, lx = set(), set(); cnt = {}; prevW = None; prevt = None
for s, t in tr:
    w = W(s, t); x = E.evaluate(tuple(v if g.owner[i] == 0 else -1 for i, v in enumerate(s)))[0]
    lw |= {names[y[0]] for y in w}; lx |= {names[y[0]] for y in x}
    if prevt is None or t != prevt:
        runs += 1; cnt = {}
        if prevt is not None: tch += 1
    elif prevW is not None:
        for v in range(n):
            if w[v] != prevW[v]:
                cnt[v] = cnt.get(v, 0) + 1
                if cnt[v] > best[0]: best = (cnt[v], names[v])
    if not tv or tv[-1] != w[T]: tv.append(w[T])
    prevW, prevt = w, t
print(f"DGSTAT {os.path.basename(gp)} n {n} iterations {len(tr) - 1} fallbacks {sum(fbt)} tau-changes {tch} W-runs {runs} "
      f"W({top})-values {len(tv)} max-WCH-in-a-W-run {best[0]} ({best[1]}) W-cycle-nodes {sorted(lw)} Xi-cycle-nodes {sorted(lx)}")
