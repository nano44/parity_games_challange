#!/usr/bin/env python3
"""L-NEW box 65: R56's rho per phase (phase = maximal run with lambda_Xi and tau constant, RESULTS R38 (a)): the number of
(Odd choice vertex, transition) pairs at which Xi of that vertex changes, and the in-phase fallbacks; checks R56 FB-RED
(fb <= 1 + (n-1)(2+rho)) as a control. Plain N5, S3 start (--start: GAME.start). Usage: rho.py GAME.pg [--start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
p = sys.argv[1]; g = load(p); n = g.n
start = readstart(p[:-3] + ".start") if "--start" in sys.argv and os.path.exists(p[:-3] + ".start") else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
OC = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
def xi(s): return E.evaluate(tuple(s))[0]
cur = xi(s); ph = dict(rho=0, fb=0, len=0); worst = dict(rho=0, fb=0, len=0); viol = 0; nph = 1
def close():
    global viol
    if ph["fb"] > 1 + (n - 1) * (2 + ph["rho"]): viol += 1
    for k in ph: worst[k] = max(worst[k], ph[k])
while True:
    r = step(g, E, Ed, s, t)
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; nxt = xi(ns)
    if nt != t or any(nxt[x][0] != cur[x][0] for x in range(n)):
        close(); nph += 1; ph = dict(rho=0, fb=0, len=0)
    else:
        ph["len"] += 1; ph["fb"] += fb; ph["rho"] += sum(1 for o in OC if nxt[o] != cur[o])
    s, t, cur = ns, nt, nxt
close()
print(f"RHO {os.path.basename(p)} n {n} phases {nph} worst {worst} FBRED-viol {viol}")
