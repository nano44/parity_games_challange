#!/usr/bin/env python3
"""Box 192: CHARGE-RET data. For every RET R-flip at gate g at step t -> t+1 (after the flip the beta-play from beta_g runs back through
g; mtype192's RET), test: some mover on the return segment B' (beta_g ... g, state t+1) switched at step t (CHARGE-RET). Also the max
number of RET flips charged to one (step, mover) switch and to one mover over the run. Usage: charge192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, idealcyc
from mtype192 import play

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    hh, s0, mv, inv = idealcyc.build(G); st = idealcyc.run(G); gi = {}
    for x in range(G["N"]):
        for v in hh.succ[mv[x]]: gi[(x, inv[v])] = v
    ret = ok = 0; per_sw = {}; per_mover = {}
    for t in range(1, len(ev)):
        (pv, ps), (vs, sb) = ev[t - 1], ev[t]
        if any(pv[v][0] != vs[v][0] for v in range(h.n)): continue
        cur = list(s0)
        for x in range(G["N"]): cur[mv[x]] = gi[(x, st[t][x])]
        sw = {mv[x] for x in range(G["N"]) if st[t][x] != st[t - 1][x]}
        for g in range(h.n):
            if h.owner[g] != 1 or name[g][0] != "g" or ps[g] == sb[g]: continue
            q = name[g][1]; e, b = V[("e", q)], V[("b", q)]; PB = play(h, cur, sb, b)
            if e not in PB: continue
            ret += 1; seg = PB[:PB.index(g)]; ch = [v for v in seg if v in sw]
            if ch:
                ok += 1
                for v in ch: per_sw[(t, v)] = per_sw.get((t, v), 0) + 1; per_mover[v] = per_mover.get(v, 0) + 1
    return ret, ok, max(per_sw.values() or [0]), max(per_mover.values() or [0])

if __name__ == "__main__":
    T = [0, 0]
    for f in sys.argv[1:]:
        r, o, ms, mm = analyse(json.load(open(f))); T[0] += r; T[1] += o
        print(f"{os.path.basename(f)} RET flips {r} charged {o}; max per switch {ms}; max per mover {mm}")
    print("TOTAL RET", T[0], "charged", T[1])
