#!/usr/bin/env python3
"""Box 10: for each mask LIFT (gate (y,w) closed -> open with tau(y) unchanged) along N5's run, report the Odd switches of the previous
iteration and where they sit: on the current tau/taubar-play from w, from t = tau(y), downstream of y, or elsewhere. Usage: lifttrace.py game.pg [maxlifts]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step, play_val
from n5 import pg, Engine, dual
p = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 12
g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
O = [v for v in range(g.n) if g.owner[v] == 1]
def play(start, sig, ta, tbar=None):
    """vertices on the play from start under (Even: tbar if given else sig; Odd: ta)"""
    x, seen = start, []
    while x not in seen:
        seen.append(x); x = (tbar if tbar is not None else sig)[x] if g.owner[x] == 0 else ta[x]
    return seen
hist = []
while True:
    vt, tbar = Ed.evaluate(tuple(t)); It = set(Ed.improving(tuple(t), vt)); Vd = play_val(Ed, dual(g), t, s)
    gates = {(y, w): (y, w) in It for y in O for w in g.succ[y] if w != t[y] and Ed.key(Vd[w]) > Ed.key(Vd[t[y]])}
    r = step(g, E, Ed, s, t)
    if r is None: break
    hist.append((list(s), list(t), gates, list(tbar), r[0] != s)); s, t = r[0], r[1]
cnt = 0
for i in range(1, len(hist)):
    s0, t0, g0, tb0, _ = hist[i - 1]; s1, t1, g1, tb1, _ = hist[i]
    moved = [z for z in O if t1[z] != t0[z]]
    for (y, w), op in g1.items():
        if t1[y] == t0[y] and (y, w) in g0 and not g0[(y, w)] and op:
            cnt += 1
            if cnt > mx: break
            Pw0 = play(w, s0, t0, tb0); Pt0 = play(t0[y], s0, t0, tb0); Pw1 = play(w, s1, t1, tb1)
            rel = []
            for z in moved:
                tags = []
                if z in Pw0: tags.append("on taubar-play from w")
                if z in Pt0: tags.append("on taubar-play from t")
                if z in play(y, s0, t0): tags.append("downstream of y (sigma,tau)")
                if not tags: tags.append("elsewhere")
                rel.append((z, t0[z], t1[z], "; ".join(tags)))
            fires = t1[y] != w and i + 1 < len(hist) and hist[i + 1][1][y] == w
            tbchg = [v for v in range(g.n) if g.owner[v] == 0 and tb0[v] != tb1[v]]
            print(f"iter {i}: lift ({y},{w}) t={t0[y]}; fires next: {fires}; prev-step Odd moves {rel}; taubar changed at {len(tbchg)} Even vertices; exploit on w-play before: {[v for v in Pw0 if g.owner[v]==0 and tb0[v]!=s0[v]]} after: {[v for v in Pw1 if g.owner[v]==0 and tb1[v]!=s1[v]]}")
print("lifts shown", min(cnt, mx), "of", cnt)
