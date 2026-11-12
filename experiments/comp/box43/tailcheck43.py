#!/usr/bin/env python3
"""L-COMP box 43 item 3: what TAIL_h does to a run (MY Γ3 engine own34, N5'-xi from S3, states 0..T3). For G and T := TAIL_h(G):
  T3 of both; seqdiff [unit (mover of G, state)]: σ_t differs; taudiff [unit (gate of G, state)]: Odd's face differs (both must be 0:
  the run on G's movers is the same run); per internal gate of G and step t ≥ t0: the charged depth d_G of a flip in G and d_T of the same
  flip in T; shift = min and max of d_T − d_G over the Λ-quiet charged flips whose face value has Λ = K1 (sink-ending plays);
  quietK1 / quietOther = Λ-quiet internal flips after t0 by the cycle node of the face left; Deep_c(T) for c = CMAX; the per-gate maximum.
Usage: tailcheck43.py G.json h   (env CMAX, default 3)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box41"), os.path.join(H, "..", "box34"), os.path.join(H, "..", "box40")]
import own34, scc40, deep41, tail43
from own34 import SpecSI


def flips(G):
    r = own34.run(G); g, V, vals, sigs, T = r["g"], r["V"], r["vals"], r["sigs"], r["T3"]
    SG = SpecSI(g); sbar = [SG.evaluate_choice(list(s))[1] for s in sigs]; rk = {v: (g.prio[v], v) for v in range(g.n)}; name = {v: k for k, v in V.items()}
    adj = scc40.dgraph(G); comp, comps = scc40.sccs(adj); K = len(comps); f = [0] * K
    for t in range(1, T + 1):
        for x in range(G["N"]):
            if sigs[t - 1][V[("x", x)]] != sigs[t][V[("x", x)]]: f[comp[x]] = t
    succ = [set() for _ in range(K)]
    for x in range(G["N"]):
        for y in adj[x]:
            if comp[y] != comp[x]: succ[comp[x]].add(comp[y])
    reach = {}
    def R(c):
        if c not in reach:
            s = set()
            for d in succ[c]: s.add(d); s |= R(d)
            reach[c] = s
        return reach[c]
    t0 = [max((f[d] for d in R(c)), default=0) for c in range(K)]; out = {}
    for x in range(G["N"]):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            if not (wt >= 0 and xt >= 0 and comp[wt] == comp[x] and comp[xt] == comp[x]): continue
            gv = V[("g", (x, k))]
            for t in range(T):
                if sbar[t][gv] == sbar[t + 1][gv] or t < t0[comp[x]]: continue
                a = sbar[t][gv]; va, vb = vals[t][a], vals[t + 1][a]
                if va == vb: continue
                out[(x, k, t)] = (deep41.depth(va, vb, rk), va[0] == vb[0], name[va[0]])
    seq = [[name[sigs[t][V[("x", x)]]][1][1] for x in range(G["N"])] for t in range(T + 1)]
    tau = [{q: name[sbar[t][V[("g", q)]]][0] for q in ((x, k) for x in range(G["N"]) for k in range(len(G["opts"][x])))} for t in range(T + 1)]
    return T, out, seq, tau


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); G = G.get("genome", G); h = int(sys.argv[2]); TG = tail43.tail(G, h); C = deep41.CMAX
    T1, F1, s1, u1 = flips(G); T2, F2, s2, u2 = flips(TG); N = G["N"]
    seqdiff = sum(1 for t in range(min(T1, T2) + 1) for x in range(N) if s1[t][x] != s2[t][x]) + abs(T1 - T2) * N
    taudiff = sum(1 for t in range(min(T1, T2) + 1) for q in u1[t] if u1[t][q] != u2[t][q])
    qk = [k for k, v in F1.items() if v[1] and v[2] == ("K", 1)]; qo = [k for k, v in F1.items() if v[1] and v[2] != ("K", 1)]
    sh = [F2[k][0] - F1[k][0] for k in qk if k in F2]; per = {}
    for (x, k, t), v in F2.items():
        if x < N and v[0] > C: per[(x, k)] = per.get((x, k), 0) + 1
    print(os.path.basename(sys.argv[1]), "h", h, "N+M", N + sum(map(len, G["opts"])), "->", TG["N"] + sum(map(len, TG["opts"])), "T3", T1, T2, "seqdiff", seqdiff, "taudiff", taudiff,
          "| G: internal flips after t0", len(F1), "quietK1", len(qk), "quietOther", len(qo), "deep(>%d)" % C, sum(1 for v in F1.values() if v[0] > C),
          "| TAIL: same flips", set(F1) == {k for k in F2 if k[0] < N}, "shift min", min(sh, default=None), "max", max(sh, default=None),
          "deep(>%d)" % C, sum(1 for k, v in F2.items() if k[0] < N and v[0] > C), "per-gate max", max(per.values(), default=0), "at gate", max(per, key=per.get) if per else None, flush=True)
