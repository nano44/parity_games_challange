#!/usr/bin/env python3
"""L-SI box 83: named step trace of IDEAL-CYC Howard (runner = box81/ref idealcyc byte copy). Per step: label C/R/p, the movers that
moved (name: old -> new option label), Odd's face changes at gates (option label: e/b), and for each WATCH mover its play's e-sequence
(option labels of the gates whose e-face the play takes) and its cycle node kind.
Usage: trace83.py GENOME.json BOX81DIR [WATCH,names]"""
import sys, os, json
sys.path[:0] = [sys.argv[2], os.path.join(sys.argv[2], "ref", "experiments", "new", "box191"), os.path.join(sys.argv[2], "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[1][:-5] + ".names.json")); N = G["N"]
watch = [nm["movers"].index(w) for w in sys.argv[3].split(",")] if len(sys.argv) > 3 and sys.argv[3] else []
h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
_, _, _, V = gamma3.build(G, set()); RV = {}
for k, v in V.items(): RV[v] = k
def lab(x, k): return f'{nm["movers"][x]}.{nm["opts"][x][k]}'
def name(v):
    k = RV[v]
    if isinstance(k, tuple):
        if k[0] == "x": return nm["movers"][k[1]]
        if k[0] == "K": return f"K{k[1]}"
        return k[0] + ":" + lab(*k[1])
    return str(k)
def play(v, cur, sb):
    seen = []; es = []
    while v not in seen:
        seen.append(v); k = RV[v]
        if isinstance(k, tuple) and k[0] == "e": es.append(lab(*k[1]))
        v = cur[v] if h.owner[v] == 0 else sb[v]
    return es, name(v)
prev = None
for t, s in enumerate(st):
    cur = list(s0)
    for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
    vs, sb = E.evaluate(tuple(cur)); lam = [vs[v][0] for v in range(h.n)]
    faces = {(x, k): ("e" if sb[V[("g", (x, k))]] == V[("e", (x, k))] else "b") for x in range(N) for k in range(len(G["opts"][x]))}
    if prev is None:
        L = "start"; mv = [lab(x, s[x]) for x in range(N)]; fc = [f"{lab(*q)}:{f}" for q, f in faces.items() if f == "e"]
    else:
        pl, pf, ps = prev
        L = "C" if lam != pl else ("R" if faces != pf else "p")
        mv = [f'{nm["movers"][x]}:{nm["opts"][x][ps[x]]}->{nm["opts"][x][s[x]]}' for x in range(N) if s[x] != ps[x]]
        fc = [f"{lab(*q)}:{pf[q]}->{f}" for q, f in faces.items() if f != pf[q]]
    w = "; ".join(f'{nm["movers"][x]}={"/".join(play(movers[x], cur, sb)[0])}@{play(movers[x], cur, sb)[1]}' for x in watch)
    print(f"t {t} {L} | moves {' '.join(mv)} | faces {' '.join(fc)} | {w}")
    prev = (lam, faces, s)
print("T", len(st) - 1)
