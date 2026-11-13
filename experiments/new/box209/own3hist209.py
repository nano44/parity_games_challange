#!/usr/bin/env python3
"""Box 209 (L-NEW successor 72): a SECOND ENGINE for the Gamma3 counters. Runs L-RED 65's own HOW3 engine (claude/l-red
experiments/red/r232/how3_232.py: Gamma3 graph from gamma3.build, values and Odd's optimal counterstrategy by L-RED's r221q/own.py, its
own tie rule: keep the current successor if best, else the larger vertex index) and writes the run in level208.py's --hist format.
L-RED's files are NOT copied into this lane: give the directory of a checkout of experiments/red (from the repository root: git archive <l-red sha> experiments/red/r230 experiments/red/r221q experiments/red/r232).
Env LNEW = this repository's root (bonly3_230.py reads it).
Usage: own3hist209.py RED_DIR G.json OUT.json   then   level208.py --hist OUT.json"""
import sys, os, json
RED = sys.argv[1]
sys.path[:0] = [os.path.join(RED, "r232"), os.path.join(RED, "r230"), os.path.join(RED, "r221q")]
import how3_232
G = json.load(open(sys.argv[2])); N = G["N"]
full = []; seq = how3_232.how3(G, full=full); gm, sig0, tau0, V, O = how3_232.build(G); n = gm.n; ow = list(gm.owner); T = len(seq) - 1
kind = [None] * n
for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
evs = sorted((v for v in range(n) if kind[v] == "e"), key=lambda v: (gm.prio[v], v)); ebit = {v: 1 << i for i, v in enumerate(evs)}
rew = lambda v: gm.prio[v] if gm.prio[v] % 2 == 0 else -gm.prio[v]
base = [sig0[v] if (ow[v] == 0 and v in sig0) else (gm.succ[v][0] if ow[v] == 0 else None) for v in range(n)]
nxt = []; cls = []
for t, (vals, tb, _) in enumerate(full):
    row = list(base)
    for x in range(N): row[x] = V[("m", (x, seq[t][x]))]
    for v in range(n):
        if ow[v] == 1: row[v] = tb[v]
    nxt.append(row); cls.append([[rew(vals[v][0]), sum(ebit[u] for u in vals[v][1] if u in ebit)] for v in range(n)])
json.dump(dict(genome=G, g3=True, n=n, T=T, movers=[V[("x", x)] for x in range(N)], kind=kind, owner=ow, succ=[list(s) for s in gm.succ],
               ebit={str(v): b for v, b in ebit.items()}, nxt=nxt, cls=cls), open(sys.argv[3], "w"))
print("own HOW3 engine", os.path.basename(sys.argv[2]), "n", n, "T3", T)
