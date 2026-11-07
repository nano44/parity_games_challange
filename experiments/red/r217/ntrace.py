#!/usr/bin/env python3
"""L-RED 54 R217: named trace of an IDEAL-CYC run (box191 idealcyc + si Engine): per state, each mover's chosen target name, the
cycle node of selected movers, and the faces of level-1 gates. Usage: ntrace.py G.json names.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, gamma3
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); inv = {v: k for k, v in nm.items()}
h, s0, movers, _ = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G); _, _, _, V = gamma3.build(G, set()); rv = {v: k for k, v in V.items()}
def vname(v):
    k = rv[v]
    if k[0] == "x": return inv[k[1]]
    if isinstance(k, tuple) and len(k) == 2 and isinstance(k[1], tuple): return f"{k[0]}:{inv[k[1][0]]}.{k[1][1]}"
    return str(k)
for t, s in enumerate(st):
    cur = list(s0)
    for x in range(G["N"]): cur[movers[x]] = V[("g", (x, s[x]))]
    vs, sb = E.evaluate(tuple(cur))
    ch = " ".join(f"{inv[x]}>{(inv[G['opts'][x][s[x]][1]] if G['opts'][x][s[x]][1] >= 0 else 'u')}" for x in range(G["N"]) if len(G["opts"][x]) > 1)
    faces = "".join("e" if sb[V[("g", (x, k))]] == V[("e", (x, k))] else "b" for x in range(G["N"]) if G["lev"][x] == 1 for k in range(len(G["opts"][x])))
    lam = sorted(set(vname(vs[movers[x]][0]) for x in range(G["N"])))
    print(t, ch, "| faces", faces, "| Lambdas", lam)
