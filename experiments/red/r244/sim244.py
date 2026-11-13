#!/usr/bin/env python3
"""L-RED 70 (R244) own engine for the one-player key model 1P(G) (box 217 §1 / §6.1) on Ξ-acyclic genomes.
Genome: N, lev[x], opts[x] = [[wt, xt, b], ...], gate[x][k] (ε order), br[b], bp[b], start[x].
Values: V(x) = ω(b(x,s x)) + V(xt), ω = +2^(2 br + bp) if bp = 0 else -2^(2 br + bp); A(x) = {s x} ∪ {k: face(x,k) > face(x, s x)};
key step: by increasing level, s'(x) = argmin over A(x) of key'(wt(x,k)) ++ (gate[x][k])."""
import json, sys
def load(f):
    G = json.load(open(f)); return G.get("genome", G)
def prep(G):
    N, opts = G["N"], G["opts"]
    # topological order of the Ξ-DAG, targets first
    seen = [0] * N; topo = []
    def dfs(x):
        st = [(x, 0)]; seen[x] = 1
        while st:
            v, i = st[-1]; tg = [o[1] for o in opts[v] if o[1] >= 0]
            if i < len(tg):
                st[-1] = (v, i + 1); w = tg[i]
                if seen[w] == 1: raise ValueError("Xi-cycle")
                if seen[w] == 0: seen[w] = 1; st.append((w, 0))
            else: seen[v] = 2; topo.append(v); st.pop()
    for x in range(N):
        if not seen[x]: dfs(x)
    om = [[(1 << (2 * G["br"][o[2]] + G["bp"][o[2]])) * (1 if G["bp"][o[2]] == 0 else -1) for o in opts[x]] for x in range(N)]
    lord = sorted(range(N), key=lambda v: (G["lev"][v], v))
    return topo, om, lord
def run(G, cap=10**7, trace=False, hook=None):
    N, opts, gate = G["N"], G["opts"], G["gate"]; topo, om, lord = prep(G)
    s = list(G["start"]); sw = [0] * N; T = 0; S = [tuple(s)] if trace else None
    V = [0] * (N + 1)   # V[-1] = V[N] = 0 (exit)
    while T < cap:
        for x in topo:
            V[x] = om[x][s[x]] + V[opts[x][s[x]][1]]
        key = [None] * N; ns = s[:]; ch = False
        for x in lord:
            cur = V[x]; bk = None; bo = -1
            for k, o in enumerate(opts[x]):
                if k == s[x] or om[x][k] + V[o[1]] > cur:
                    kk = (key[o[0]] + (gate[x][k],)) if o[0] >= 0 else (gate[x][k],)
                    if bk is None or kk < bk: bk, bo = kk, k
            key[x] = bk
            if bo != s[x]: ns[x] = bo; sw[x] += 1; ch = True
        if hook: hook(T, s, ns, V, key)
        if not ch: break
        s = ns; T += 1
        if trace: S.append(tuple(s))
    return T, sw, S
def kdepth(G, sw):
    L = max(G["lev"]) + 1; N = G["N"]
    best = [max(sw[x] for x in range(N) if G["lev"][x] == l) for l in range(L)]
    K = (0, 0.0)
    for b in range(L):
        k = 0
        while b + k < L and best[b + k] == 2 ** (k + 1) - 1: k += 1
        frac = best[b + k] / (2 ** (k + 1) - 1) if b + k < L else 1.0
        K = max(K, (k, round(frac, 4)))
    return K, best
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = load(f); T, sw, _ = run(G); K, best = kdepth(G, sw)
        print(f"{f.split('/')[-1]}: N {G['N']} d {max(G['lev'])+1} T {T} k {K} best/level {best}")
