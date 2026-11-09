#!/usr/bin/env python3
"""L-RED 62 R228: independent re-measure for L-NEW 67 BOX 201 (claude/l-new 47b325f6) on R221 own.py (pad-free Γ, the genome's start,
cap 3000), plus the Ξ feedback number k for the Lead. No L-NEW code.
  gateR  = max over (gate g, face b, w) of #flips of Odd at g into b with Λ_(t-1)(g) = Λ_t(g) = w (per-tuple maximum), with its gate id
  movR   = the same over movers (out-degree in brackets)
  F      = #steps t at which σ̄ (Odd's choice at some gate) changes (a TOTAL)
  seg    = longest run of consecutive steps with σ̄ and every Λ_t(v) constant (in steps; SEG-H says <= N + 1); segfail = seg > N + 1
  k      = minimum feedback vertex set of the Ξ-graph (mover -> Ξ-target mover; self-loops count) — exact by branch and bound after
           forced self-loops and source / sink pruning; printed as '>=lo,<=hi' if the search budget is exhausted.
Usage: seg228.py G.json ..."""
import sys, os, json, collections, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
def fvs(G):
    N = G["N"]; adj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}
    forced = {x for x in range(N) if x in adj[x]}
    def prune(nodes):
        nodes = set(nodes)
        while True:
            rm = {x for x in nodes if not (adj[x] & nodes) or not any(x in adj[y] for y in nodes)}
            if not rm: return nodes
            nodes -= rm
    def acyclic(nodes):
        return not prune(nodes)
    rest = prune(set(range(N)) - forced)
    if not rest: return str(len(forced))
    cand = sorted(rest)
    for k in range(0, 5):
        if (len(cand) > 40 and k >= 3) or (len(cand) > 150 and k >= 2): break
        for S in itertools.combinations(cand, k):
            if acyclic(rest - set(S)): return str(len(forced) + k)
    # greedy upper bound
    r = set(rest); g = 0
    while prune(r):
        r2 = prune(r); x = max(r2, key=lambda v: len(adj[v] & r2) + sum(1 for y in r2 if v in adj[y])); r.discard(x); g += 1
    return f">={len(forced) + k},<={len(forced) + g}"
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]; T = len(out) - 1
    gates = sorted({V[("g", q)] for q in O})
    nx = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    lam = lambda t, v: out[t][1][v][0]
    cnt = collections.Counter()
    for u in list(range(N)) + gates:
        for t in range(1, T + 1):
            if nx[t][u] != nx[t - 1][u] and lam(t - 1, u) == lam(t, u): cnt[(u, nx[t][u], lam(t, u))] += 1
    g = max(((v, k) for k, v in cnt.items() if k[0] >= N), default=(0, None)); m = max(((v, k) for k, v in cnt.items() if k[0] < N), default=(0, None))
    sb = [tuple(nx[t][q] for q in gates) for t in range(T + 1)]; lv = [tuple(lam(t, v) for v in range(n)) for t in range(T + 1)]
    F = sum(1 for t in range(1, T + 1) if sb[t] != sb[t - 1])
    seg = cur = 0
    for t in range(1, T + 1):
        cur = cur + 1 if (sb[t] == sb[t - 1] and lv[t] == lv[t - 1]) else 0; seg = max(seg, cur)
    md = len(G["opts"][m[1][0]]) if m[1] else 0
    return dict(T=T, gateR=g[0], gate=(g[1][0] if g[1] else None), movR=m[0], movdeg=md, F=F, seg=seg, segfail=int(seg > N + 1), N=N, k=fvs(G))
if __name__ == "__main__":
    print("instance N+M T gateR(gate) movR(deg) F seg N segfail k")
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), c["T"], f"{c['gateR']}({c['gate']})", f"{c['movR']}({c['movdeg']})", c["F"], c["seg"], c["N"], c["segfail"], c["k"], flush=True)
