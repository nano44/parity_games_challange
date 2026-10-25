#!/usr/bin/env python3
"""Box 32: classify the used-level RISES (L_{k+1} > L_k inside a phase; lrun.py) of N5 on C^1O. For a rise at transition k+1 -> k+2:
src = E (top level attained by an Even switch y -> z) or O (only by σ̄(o)); for src E: was (y, z) a gate edge at k (HIGH says yes), was
y in R_k, did the W-value of z change at k -> k+1 (W_{k+1}(z) vs W_k(z)), the state type at k+1 (route form of each frame: rf, U2, U3,
U23), fallback at k or k+1. Usage: rises.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def usedL(g, rows, ev, i):
    a, c = rows[i], rows[i + 1]; Xi = ev[i][0]; L = -2; top = []
    for y in range(g.n):
        if g.owner[y] == 0 and a["s"][y] != c["s"][y]:
            l = lev(Xi[a["s"][y]], Xi[c["s"][y]])
            if l > L: L, top = l, []
            if l == L: top.append(("E", y, c["s"][y]))
    for u in range(g.n):
        if g.owner[u] == 1 and ev[i][1][u] != ev[i + 1][1][u]:
            l = lev(Xi[ev[i][1][u]], Xi[ev[i + 1][1][u]])
            if l > L: L, top = l, []
            if l == L: top.append(("O", u, ev[i + 1][1][u]))
    return L, top

def run(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
    Is = [set(E.improving(tuple(r["s"]), ev[i][0])) for i, r in enumerate(rows)]
    prev = None
    for i in range(len(rows) - 1):
        if rows[i]["ph"] != rows[i + 1]["ph"]: prev = None; continue
        L, top = usedL(g, rows, ev, i)
        if prev is not None and L > prev[0]:
            k = i - 1; a = rows[i]
            st = "rf" if a["rfX"] and a["rfW"] else ("U2" if a["rfW"] else ("U3" if a["rfX"] else "U23"))
            fb = "fb" if (rows[k]["fb"] or rows[i]["fb"]) else "nofb"
            es = [t for t in top if t[0] == "E"]
            if not es: key = f"O_{st}_{fb}"
            else:
                _, y, z = es[0]
                wasgate = (y, z) in Is[k]; inR = y in rows[k]["R"] or y == o; wz = rows[k]["W"][z] != rows[i]["W"][z]
                key = f"E_{st}_{fb}_gate{int(wasgate)}_inR{int(inR)}_Wz{int(wz)}"
            acc[key] = acc.get(key, 0) + 1; acc.setdefault("ex_" + key, (name, i, prev[0], L))
        prev = (L,)

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
        run(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
