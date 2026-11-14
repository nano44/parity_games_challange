#!/usr/bin/env python3
"""L-SI box 109 Addendum A: the STALE-OPTION counter on RF's run on K^s_n (ks109.build).
For every iteration of RF and every vertex v it switches: v is STALE-BLIND if some improvable vertex u != v lies on the play from a
successor of v that is neither sigma(v) nor an improving target (RF does not wait for u; RFA would). Counters per n: iterations,
switches, blind (unit: (iteration, switched vertex) pairs that are stale-blind), and how many of the blind vertices switch AGAIN later.
Usage: stale109.py n.."""
import sys, os
av = sys.argv[1:]; sys.argv = [sys.argv[0]]
import ks109, rf109
from si import Engine
for n in map(int, av):
    g, st, names = ks109.build(n); E = Engine(g); sigma = list(st); its = sw = blind = 0; last_blind = {}; again = 0
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if not Is: break
        T = {}
        for v, w in Is: T.setdefault(v, set()).add(w)
        nxt = [sigma[v] if g.owner[v] == 0 else sbar[v] for v in range(g.n)]
        def play(x):
            seen = set()
            while x not in seen: seen.add(x); x = nxt[x]
            return seen
        sel = rf109.rf_select(g.n, g.owner, E, sigma, vs, sbar, Is); its += 1
        for v, w in sel.items():
            sw += 1
            if v in last_blind: again += 1; del last_blind[v]
            others = [u for u in E.succ[v] if u != sigma[v] and u not in T[v]]
            if any((play(u) & set(T)) - {v} for u in others): blind += 1; last_blind[v] = its
        for v, w in sel.items(): sigma[v] = w
    print(f"STALE109 K^s_{n}: iterations {its} switches {sw} blind {blind} blind vertices that switch again later {again}", flush=True)
