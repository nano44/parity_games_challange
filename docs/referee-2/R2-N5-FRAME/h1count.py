#!/usr/bin/env python3
"""REFEREE-2 succ. 21: on one game (S3 start), count ODD-FREEZE hits with box 63's (H1) (sigma_e = taubar, P_e = the (tau, taubar)-play
from e up to o) per state, and print the per-state (H1) and (H1') counts (H1' from frame_check.odd_freeze, uncapped). Usage: h1count.py GAME"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OFNODE", "2000000")
import frame_check as F
g = F.pg.read(sys.argv[1]); n = g.n; E = F.Engine(g); Ed = F.Engine(F.dual(g))
states, fbs = F.DC.Runner(g).run(list(E.initial("best")), list(Ed.initial("best")))
st = F.St(); h1 = h1p = 0; h1_040 = h1p_040 = 0
for k, (sg, tu) in enumerate(states):
    ue, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
    nxU = [tb[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    I = dict(tu=tu, nxU=nxU, U=[tuple(z) for z in ue])
    for o in range(n):
        if g.owner[o] != 1: continue
        for e in set(g.succ[o]):
            if e == tu[o]: continue
            r, w = F.odd_freeze(g, E, Ed, I, o, e, st)
            pe, _ = F.play(nxU, e)
            a = 0
            if o in pe:
                pe = pe[:pe.index(o) + 1]; B = set(F.play(nxU, tu[o])[0])
                top = max(pe, key=lambda x: E.rank[x])
                a = int(not (set(pe) & B) and g.prio[top] % 2 == 0 and E.rank[top] > E.rank[w])
            h1 += a; h1p += r["prot"]
            if k <= len(states) - 2: h1_040 += a; h1p_040 += r["prot"]
print(f"states {len(states)} H1 all {h1} H1 0..T-1 {h1_040} | H1' all {h1p} H1' 0..T-1 {h1p_040}")
