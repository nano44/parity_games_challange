#!/usr/bin/env python3
"""Box 192: hill-climb IDEAL-CYC genomes for R (steps that change sigma-bar without changing a cycle node), or F (max flips at one
gate), or D (max R-depth, depth192). Mutation = box191 climb191.mut (imported by exec of its def; unmodified file).
Resumable: keeps the best genome in OUT.json. Usage: climb192.py SCORE d w D seed iters OUT"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); B191 = os.path.join(HERE, "..", "box191"); sys.path[:0] = [HERE, B191]
import idealcyc, rand191, rpot192, depth192
sc, d, w, D, seed, iters, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
rng = random.Random(seed)
src = open(os.path.join(B191, "climb191.py")).read(); i0 = src.index("def mut(G):"); i1 = src.index("\ncur = ")
exec(src[i0:i1])          # defines mut(G) using the global rng

def flipcount(G):
    h, E, V, name, movers, ev = rpot192.states(G); gates = [v for v in range(h.n) if h.owner[v] == 1]; cnt = {}
    for t in range(1, len(ev)):
        for g in gates:
            if ev[t - 1][1][g] != ev[t][1][g]: cnt[g] = cnt.get(g, 0) + 1
    return max(cnt.values() or [0])

def score(G):
    a = rpot192.analyse(G)
    if sc == "R": main = a["R"]
    elif sc == "F": main = flipcount(G)
    else: main = max([dd for l, dd in depth192.depths(G) if l == "R"] or [0])
    return (main, a["R"], a["T"])

cur = json.load(open(out + ".json")) if os.path.exists(out + ".json") else rand191.rgen(rng, d, w, D)
best = score(cur); print(f"start {best} N {cur['N']}", flush=True)
for it in range(iters):
    G = mut(cur)
    if rng.random() < 0.5: G = mut(G)
    s = score(G)
    if s >= best:
        if s > best: print(f"it {it} score {s}", flush=True); json.dump(G, open(out + ".json", "w"))
        cur, best = G, s
print("final", best, flush=True)
