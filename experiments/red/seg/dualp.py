#!/usr/bin/env python3
"""L-RED: why is an Odd edge tau-improving? For the state k of the n5b run and each Odd vertex with I_tau edges, print the dual valuations
(Odd's own frame, Even best-replying to tau) of tau(v) and of each improving successor: (cycle node, path set by label, length) and the
dual best-reply play. Usage: dualp.py GAME.pg START k"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second")); sys.path.insert(0, HERE)
import n5b
from segchk import play
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); k = int(sys.argv[3])
lab = {int(m.group(1)): m.group(2) for m in (re.match(r'\s*(\d+)\s.*"(.*)"', l) for l in open(sys.argv[1])) if m}
L = lambda v: lab.get(v, str(v))
N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []; N.run(s0, t0, trace=tr, fbtrace=fb)
S, T = tr[k]; T = list(T)
vt = N.ev(N.SD, T); tb = N.opt(N.SD, T)[1]   # dual valuations as the run computes them (evaluate); best reply only for the display
It = N.improving(N.SD, T, vt)
nx = [T[v] if g.owner[v] == 1 else tb[v] for v in range(g.n)]
for v, ws in It.items():
    for w in [T[v]] + ws:
        val = vt[w]
        print(f"{L(v)} -> {L(w)}{' (tau)' if w == T[v] else ''}: ({L(val[0])}, {sorted((L(x) for x in val[1]), key=lambda q: -g.prio[[i for i in lab if lab[i] == q][0]])}, {val[2]}) play {[L(x) for x in sum(play(nx, w), ())]}")
