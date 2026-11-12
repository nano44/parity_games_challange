#!/usr/bin/env python3
"""L-RED 64 R230 item 6: the mover dependency graph D(G) and the SCC-CHAIN bound for N5'-xi's T3 on Gamma3(G).
D(G): node per mover; edge x -> wt and x -> xt for every option (x, k) (wt, xt >= 0), self-loops included.
SCC-CHAIN (lane claim, checked here): with C ranging over the SCCs of D and h(C) := 1 if C is one mover without a self-loop,
deg(x) if C = {x} with a Xi self-loop, and UNKNOWN for |C| >= 2,
  T3 <= Hc := max over source-to-sink chains of SCCs of sum h(C)   (whenever every SCC is a singleton).
Counters per genome: N, M, U, T3, nscc (#SCCs with >= 2 movers), maxscc (largest SCC), Hc (None if nscc > 0), viol (T3 > Hc).
Usage: scc230.py G.json ... | scc230.py rand SEED COUNT [acyc]"""
import sys, os, json, random
from elev230 import measure, U
from bonly3_230 import rgen
def sccs(G):
    N = G["N"]; adj = [sorted({y for o in G["opts"][x] for y in (o[0], o[1]) if y >= 0}) for x in range(N)]
    idx = {}; low = {}; st = []; on = set(); comp = [None] * N; out = []; c = [0]
    def dfs(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in idx: dfs(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            C = []
            while True:
                w = st.pop(); on.discard(w); comp[w] = len(out); C.append(w)
                if w == v: break
            out.append(C)
    sys.setrecursionlimit(10000)
    for v in range(N):
        if v not in idx: dfs(v)
    return adj, comp, out
def chain(G):
    adj, comp, C = sccs(G); big = [c for c in C if len(c) > 1]
    if big: return None, len(big), max(map(len, big))
    h = [1] * len(C)
    for i, c in enumerate(C):
        x = c[0]
        if x in adj[x]: h[i] = len(G["opts"][x])
    best = {}
    for i in range(len(C)):                     # Tarjan emits SCCs in reverse topological order (sinks first)
        x = C[i][0]; best[i] = h[i] + max([best[comp[y]] for y in adj[x] if comp[y] != i] or [0])
    return max(best.values()), 0, 1
def acyc(G, rng):          # force D acyclic: xt only to strictly lower levels or -1
    for x in range(G["N"]):
        for o in G["opts"][x]:
            if o[1] >= 0 and G["lev"][o[1]] >= G["lev"][x]: o[1] = rng.choice([y for y in range(G["N"]) if G["lev"][y] < G["lev"][x]] + [-1])
    return G
def one(tag, G, tot, verbose):
    Hc, nscc, mx = chain(G); m = measure(G); v = Hc is not None and m["T3"] > Hc
    tot["genomes"] += 1; tot["viol"] += v; tot["trivial"] += Hc is not None
    if Hc is not None: tot["maxT3_triv"] = max(tot["maxT3_triv"], m["T3"]); tot["max_ratio_triv"] = max(tot["max_ratio_triv"], m["T3"] / Hc)
    else: tot["maxT3_big"] = max(tot["maxT3_big"], m["T3"])
    if verbose or v: print(tag, dict(N=m["N"], M=m["M"], U=m["U"], T3=m["T3"], nscc=nscc, maxscc=mx, Hc=Hc, viol=v), flush=True)
if __name__ == "__main__":
    tot = dict(genomes=0, trivial=0, viol=0, maxT3_triv=0, max_ratio_triv=0.0, maxT3_big=0)
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); ac = len(sys.argv) > 4
        for i in range(int(sys.argv[3])):
            G = rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.choice([2, 3]))
            if ac: G = acyc(G, rng)
            one(f"r{i}", G, tot, False)
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); G.pop("_evals", None)
            if isinstance(G, dict) and "opts" in G: one(os.path.basename(f), G, tot, True)
    print("TOTAL", tot, flush=True)
