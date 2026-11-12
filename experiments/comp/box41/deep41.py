#!/usr/bin/env python3
"""L-COMP box 41 item 1: DEEP3 counters on MY Γ3 engine (box34/own34.py: N5'-xi from S3 on Γ3, [E-LEV], states 0..T3 before the first
fallback; its mover parts are a HOW3 run, R125 REACH3-ALL), written from L-SI box 100's TEXT (claude/l-si 3b6ae726 / 23d39400,
docs/si/box100-scclin.md §2 Lemma TWO-CROSS, §3 depth, §4 Deep_c, §5.2 counters), not from cross100.py. Quoted:
  §2 (i) «If σ̄_t(g) = a and σ̄_(t+1)(g) = b ≠ a, then Ω_t(a) ◁ Ω_(t+1)(a).» (a flip away from face a is charged to the change of Ω(a)).
  §3 «Depth of a change Ω_t(v) ≠ Ω_(t+1)(v): −1 if Λ changes; else the number of elements of Π_t (equivalently of Π_(t+1)) more relevant
      than z, the most relevant element of Π_t Δ Π_(t+1); |Π_t| if Π_t = Π_(t+1) (a length-only change).»
  §4 «Deep_c(C): #flips of internal gates of C after t0 that TWO-CROSS charges to a change of depth > c.»; «E_C: #ext gates» (ext = a
      target outside C or −1, §1), internal = both targets in C; t0(C) = box 99's e(C) (max f over SCCs reachable from C).
  §5.2 «The counter covers EVERY gate over the WHOLE run (states 0..T3), so it is an upper bound on Σ_C Deep_3(C)».
Relevance: n5b's injective rank (priority, vertex index) (n5b A1). σ̄_t := Odd's optimal counterstrategy at state t (n5b evaluate_choice).
Lead reading (stated): the «D1 note» (length-only changes on short paths count as shallow) is §3's «|Π_t| if Π_t = Π_(t+1)»: a
length-only change has depth |Π_t|, so it is shallow (<= c) exactly when |Π_t| <= c. No other rule is applied.
Counters (unit; scope):
  WHOLE RUN, every gate, states 0..T3 (= box 100's): deep [flip: charged depth > C], dmax [max charged depth], unm [flip: Ω(a) unchanged,
  must be 0], qflip [flip: Λ(a) unchanged], qint [qflip at an internal gate of its mover's SCC], gates, multi [gates with >= 2 flips],
  maxfl [max flips of one gate].
  PER SCC after t0 (box 100 §4): DeepInt = Σ_C Deep_c(C); DeepBig = Deep_c(C_max) (largest SCC); dmaxInt = max charged depth at internal
  gates after t0; gmaxInt = per-gate maximum of those deep internal flips (box 42); Iint = internal gates in total.
Usage: deep41.py G.json ...   (env CMAX, default 3; env CTRL=1: charge to the face Odd moves TO: unm must fire)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box34"), os.path.join(H, "..", "box40")]
import own34, scc40
from own34 import SpecSI
CMAX = int(os.environ.get("CMAX", "3")); CTRL = os.environ.get("CTRL") == "1"


def depth(a, b, rk):
    if a[0] != b[0]: return -1
    D = a[1] ^ b[1]
    if not D: return len(a[1])
    z = max(D, key=lambda u: rk[u]); return sum(1 for u in a[1] if rk[u] > rk[z])


def census(G):
    r = own34.run(G); g, V, vals, sigs, T = r["g"], r["V"], r["vals"], r["sigs"], r["T3"]
    SG = SpecSI(g); sbar = [SG.evaluate_choice(list(s))[1] for s in sigs]
    rk = {v: (g.prio[v], v) for v in range(g.n)}
    adj = scc40.dgraph(G); comp, comps = scc40.sccs(adj); K = len(comps)
    f = [0] * K
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
    t0 = [max((f[d] for d in R(c)), default=0) for c in range(K)]
    big = max(range(K), key=lambda c: (len(comps[c]), sum(len(G["opts"][x]) for x in comps[c])))
    c = dict(T3=T, deep=0, dmax=-1, unm=0, qflip=0, qint=0, gates=0, multi=0, maxfl=0, DeepInt=0, DeepBig=0, dmaxInt=-1, Iint=0,
             nscc=K, big=len(comps[big]), gmaxInt=0)
    for x in range(G["N"]):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            q = (x, k); gv, pe, pb = V[("g", q)], V[("pe", q)], V[("pB", q)]; gd = 0
            internal = wt >= 0 and xt >= 0 and comp[wt] == comp[x] and comp[xt] == comp[x]
            c["gates"] += 1; c["Iint"] += internal; fl = 0
            for t in range(T):
                if sbar[t][gv] == sbar[t + 1][gv]: continue
                fl += 1; a = sbar[t + 1][gv] if CTRL else sbar[t][gv]
                va, vb = vals[t][a], vals[t + 1][a]
                if va == vb: c["unm"] += 1; continue
                d = depth(va, vb, rk); c["dmax"] = max(c["dmax"], d); c["deep"] += d > CMAX
                if va[0] == vb[0]: c["qflip"] += 1; c["qint"] += internal
                if internal and t >= t0[comp[x]]:
                    c["dmaxInt"] = max(c["dmaxInt"], d)
                    if d > CMAX: c["DeepInt"] += 1; c["DeepBig"] += comp[x] == big; gd += 1
            c["multi"] += fl >= 2; c["maxfl"] = max(c["maxfl"], fl); c["gmaxInt"] = max(c["gmaxInt"], gd)
    return c


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G)
        print(os.path.basename(fn), "N+M", G["N"] + sum(map(len, G["opts"])), json.dumps(census(G)), flush=True)
