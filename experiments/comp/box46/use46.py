#!/usr/bin/env python3
"""L-COMP box 46 item 2: is a Ξ-cycle USED by N5's key-rule run (mode «spec», from S3 on Γ3(G), states 0..T_key before the first
fallback; my engine box44/n5xi44 on own34.build, as win46)? Descriptive counters (unit; scope states 0..T_key):
 offbeta [(gate, state)]: σ̄ takes the e-face (pe) of the gate, i.e. Ω(pe) ◁ Ω(pB) (R122 BETA-ACYC: 0 on every Ξ-acyclic genome);
 cycopt [(mover, state)]: σ_t(x) is an option (x, k) whose Ξ-edge x → xt(x, k) lies on a cycle of R104's Ξ-graph (xt in x's Ξ-SCC);
 cycgates: gates whose option's Ξ-edge lies on a Ξ-cycle. T_key as win46.
Usage: use46.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box34"), os.path.join(H, "..", "box44")]
import own34, n5xi44, val44


def sccs(N, adj):
    idx, low, on, stk, comp, cnt = {}, {}, set(), [], {}, [0]
    sys.setrecursionlimit(max(10000, 4 * N))
    def sc(v):
        idx[v] = low[v] = cnt[0]; cnt[0] += 1; stk.append(v); on.add(v)
        for w in adj[v]:
            if w not in idx: sc(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            while True:
                w = stk.pop(); on.discard(w); comp[w] = v
                if w == v: break
    for v in range(N):
        if v not in idx: sc(v)
    return comp


def use(G):
    g, V = own34.build(G, True); N = G["N"]; mv = [V[("x", x)] for x in range(N)]
    adj = [sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)]; comp = sccs(N, adj)
    cyc = {(x, k) for x in range(N) for k, o in enumerate(G["opts"][x]) if o[1] >= 0 and (o[1] == x or comp[o[1]] == comp[x])}
    cpad = {V[("m", q)]: q for q in cyc}; c = dict(Tkey=-1, offbeta=0, cycopt=0, cycgates=len(cyc))
    def hook(t, sigma, tau, vs, Is, It, F):
        if F > 0: return
        c["Tkey"] = t
        for x in range(N):
            if sigma[mv[x]] in cpad: c["cycopt"] += 1
            for k in range(len(G["opts"][x])):
                if val44.cmpval(g, vs[V[("pe", (x, k))]], vs[V[("pB", (x, k))]]) < 0: c["offbeta"] += 1
    n5xi44.run(g, "spec", hook=hook); return c


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G)
        print(os.path.basename(fn), "N+M", G["N"] + sum(map(len, G["opts"])), json.dumps(use(G)), flush=True)
