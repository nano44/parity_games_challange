#!/usr/bin/env python3
"""Box 192: VCYC data. For gate g at state t, VCYC_t(g) := the most relevant vertex of the cycle closed by the play from beta_g when g is
forced to beta (sigma-bar elsewhere), or None if that play does not return to g. Counts, over all steps: max changes of VCYC per gate,
max sigma-bar changes per gate, total sigma-bar changes at gates, and those changes with VCYC(g) unchanged. Usage: vcyc192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, idealcyc
def vtop(h, cur, sb, g, b, E):
    # follow beta_g's play with g forced to beta; return top-rank vertex of the closed cycle if it closes through g, else None
    seen = []; s = set(); v = b
    while v not in s:
        seen.append(v); s.add(v); v = (cur[v] if h.owner[v] == 0 else (b if v == g else sb[v]))
    cyc = seen[seen.index(v):]
    return max(cyc, key=lambda u: E.rank[u]) if g in cyc else None
def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    hh, s0, mv, inv = idealcyc.build(G); st = idealcyc.run(G); gi = {}
    for x in range(G["N"]):
        for v in hh.succ[mv[x]]: gi[(x, inv[v])] = v
    gates = [v for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    prev = None; ch = {g: 0 for g in gates}; fl = {g: 0 for g in gates}; flnoch = 0
    for t in range(len(ev)):
        vs, sb = ev[t]; cur = list(s0)
        for x in range(G["N"]): cur[mv[x]] = gi[(x, st[t][x])]
        top = {g: vtop(h, cur, sb, g, V[("b", name[g][1])], E) for g in gates}
        if prev is not None:
            ptop, psb = prev
            for g in gates:
                c = top[g] != ptop[g]; f = psb[g] != sb[g]
                ch[g] += c; fl[g] += f; flnoch += f and not c
        prev = (top, sb)
    return max(ch.values()), max(fl.values()), sum(fl.values()), flnoch
for f in sys.argv[1:]:
    a = analyse(json.load(open(f)))
    print(os.path.basename(f), "max VCYC-top changes per gate", a[0], "max flips per gate", a[1], "flips", a[2], "flips without VCYC change", a[3])
