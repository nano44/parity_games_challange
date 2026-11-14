#!/usr/bin/env python3
"""Box 208 (L-NEW successor 72): a SECOND ENGINE for level208.py's counters. Runs L-RED 54's independent IDEAL-CYC implementation
(claude/l-red experiments/red/r221q/own.py; its own builder of Gamma(G), its own VJ valuation, Odd's answer by its own one-player
strategy iteration; no code of si.py, idealcyc.py or gfc203.py) and writes its run in level208.py's --hist format. L-RED's file is
NOT copied into this lane: give the path of a checkout of it (e.g. `git show <l-red sha>:experiments/red/r221q/own.py > /tmp/own.py`).
Usage: ownhist208.py PATH/own.py G.json OUT.json   then   level208.py --hist OUT.json"""
import sys, os, json, importlib.util
spec = importlib.util.spec_from_file_location("lred_own", sys.argv[1]); own = importlib.util.module_from_spec(spec); spec.loader.exec_module(own)
G = json.load(open(sys.argv[2])); N = G["N"]
out, V, O, owner = own.run(G); n, prio, owner2, succ, V2, O2 = own.build(G); T = len(out) - 1
kind = [None] * n
for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k
evs = sorted((v for v in range(n) if kind[v] == "e"), key=lambda v: (prio[v], v)); ebit = {v: 1 << i for i, v in enumerate(evs)}
rew = lambda v: prio[v] if prio[v] % 2 == 0 else -prio[v]
nxt = []; cls = []
for (sigN, vals, tau) in out:
    row = [succ[v][0] if owner[v] == 0 else tau[v] for v in range(n)]
    for x in range(N): row[x] = sigN[x]
    nxt.append(row); cls.append([[rew(vals[v][0]), sum(ebit[u] for u in vals[v][1] if u in ebit)] for v in range(n)])
json.dump(dict(genome=G, g3=False, n=n, T=T, movers=[V[("x", x)] for x in range(N)], kind=kind, owner=list(owner), succ=[list(s) for s in succ],
               ebit={str(v): b for v, b in ebit.items()}, nxt=nxt, cls=cls), open(sys.argv[3], "w"))
print("own engine", os.path.basename(sys.argv[2]), "n", n, "T", T)
