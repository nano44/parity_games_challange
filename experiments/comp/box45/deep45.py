#!/usr/bin/env python3
"""L-COMP box 45 item (a): a depth notion that TAIL (box43/tail43.py) cannot inflate, counted on MY Γ3 engine (box34/own34.py: N5'-xi from
S3 on Γ3, [E-LEV], states 0..T3 before the first fallback), next to L-SI box 100's depth (box41/deep41.py, unchanged reading).
DEFINITIONS (mine; stated here, not taken from any lane):
  A flip of gate g at t -> t+1 (σ̄_t(g) = a ≠ σ̄_(t+1)(g)) is charged to the change Ω_t(a) -> Ω_(t+1)(a) (box 100 §2 TWO-CROSS, as deep41).
  P_t(a) := the play from a under (σ_t, σ̄_t), as a vertex list a = p_0, p_1, ..., p_L = λ (stopped at the FIRST visit of λ = Λ_t(a)).
  Self-check (counter pimis, must be 0): Π_t(a) ⊆ {p_0, ..., p_(L-1)} and the play reaches λ without repeating a vertex.
  For a Λ-quiet change (Λ_t(a) = Λ_(t+1)(a)) let pre := the longest common prefix of P_t(a), P_(t+1)(a) and suf := their longest common
  suffix (both end at λ), suf cut so that pre + suf <= min length. ABOVE := {u ∈ Π_t(a) : rk(u) > rk(z)}, z the most relevant element of
  Π_t Δ Π_(t+1) (rk = (priority, index), as deep41); ABOVE := Π_t(a) for a length-only change (Π_t = Π_(t+1)), as box 100 §3.
  depth100 := |ABOVE| (= deep41's depth); depthNS := |ABOVE minus the vertices of P_t(a) in its common suffix| (depth with the shared
  end of the two plays removed); depthMID := |ABOVE minus prefix and suffix|. Λ changes: all three = −1.
  Why TAIL cannot inflate depthNS (argument sketch, checked by tail mode below): TAIL_h appends the same chain to the END of every
  sink-ending play; on a Λ-quiet sink-ending change both plays end with that chain, so the chain lies in the common suffix.
Counters (unit = flip; scope as deep41): WHOLE RUN every gate states 0..T3: deep100 / deepNS / deepMID [flips with depth > C], dmax100 /
dmaxNS / dmaxMID; PER SCC after t0 at internal gates: Int100 / IntNS / IntMID (Σ_C Deep_C(C)), gmax100 / gmaxNS / gmaxMID (per-gate max of
those), dmaxIntNS; qflip [Λ-quiet flips], qmax [max Λ-quiet flips of one gate, whole run], unm and pimis (must be 0), and T3.
Usage: deep45.py G.json ...          one JSON line per genome (env CMAX, default 3; CTRL=1 control: suffix not removed, depthNS := depth100
                                     on the tail pair, so tail mode must report differences)
       deep45.py --tail G.json TG.json   flip-by-flip comparison of depthNS on G's gates (x < N_G) between G and TG = TAIL_h(G)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box34"), os.path.join(H, "..", "box40")]
import own34, scc40
from own34 import SpecSI
CMAX = int(os.environ.get("CMAX", "3")); CTRL = os.environ.get("CTRL") == "1"


def play(a, strat, choice, lam):
    P, seen, u = [a], {a}, a
    while u != lam:
        u = strat[u] if strat[u] != -1 else choice[u]
        if u in seen: return None
        P.append(u); seen.add(u)
    return P


def depths(va, vb, Pa, Pb, rk):
    if va[0] != vb[0]: return -1, -1, -1
    D = va[1] ^ vb[1]
    if D: z = max(D, key=lambda u: rk[u]); A = {u for u in va[1] if rk[u] > rk[z]}
    else: A = set(va[1])
    m = min(len(Pa), len(Pb)); pre = 0
    while pre < m and Pa[pre] == Pb[pre]: pre += 1
    suf = 0
    while suf < m - pre and Pa[-1 - suf] == Pb[-1 - suf]: suf += 1
    S = set(Pa[len(Pa) - suf:]); Pr = set(Pa[:pre])
    ns = len(A) if CTRL else len(A - S)
    return len(A), ns, len(A - S - Pr)


def census(G, keep=False):
    r = own34.run(G); g, V, vals, sigs, T = r["g"], r["V"], r["vals"], r["sigs"], r["T3"]
    SG = SpecSI(g); ch = [SG.evaluate_choice(list(s))[1] for s in sigs]
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
    c = dict(T3=T, flips=0, qflip=0, qmax=0, unm=0, pimis=0)
    for k in ("100", "NS", "MID"): c.update({"deep" + k: 0, "dmax" + k: -1, "Int" + k: 0, "gmax" + k: 0})
    c["dmaxIntNS"] = -1; rows = []
    for x in range(G["N"]):
        for kk, (wt, xt, _) in enumerate(G["opts"][x]):
            gv = V[("g", (x, kk))]
            internal = wt >= 0 and xt >= 0 and comp[wt] == comp[x] and comp[xt] == comp[x]
            gd = {"100": 0, "NS": 0, "MID": 0}; q = 0
            for t in range(T):
                if ch[t][gv] == ch[t + 1][gv]: continue
                a = ch[t][gv]; va, vb = vals[t][a], vals[t + 1][a]; c["flips"] += 1
                if va == vb: c["unm"] += 1; continue
                Pa = play(a, sigs[t], ch[t], va[0]); Pb = play(a, sigs[t + 1], ch[t + 1], vb[0])
                if Pa is None or Pb is None or not va[1] <= set(Pa[:-1]) or not vb[1] <= set(Pb[:-1]): c["pimis"] += 1; continue
                d = dict(zip(("100", "NS", "MID"), depths(va, vb, Pa, Pb, rk)))
                if va[0] == vb[0]: c["qflip"] += 1; q += 1
                if keep: rows.append((x, kk, t, d["100"], d["NS"], d["MID"]))
                for k in d:
                    c["dmax" + k] = max(c["dmax" + k], d[k]); c["deep" + k] += d[k] > CMAX
                    if internal and t >= t0[comp[x]] and d[k] > CMAX: c["Int" + k] += 1; gd[k] += 1
                if internal and t >= t0[comp[x]]: c["dmaxIntNS"] = max(c["dmaxIntNS"], d["NS"])
            c["qmax"] = max(c["qmax"], q)
            for k in gd: c["gmax" + k] = max(c["gmax" + k], gd[k])
    return (c, rows) if keep else c


def load(fn):
    G = json.load(open(fn)); return G.get("genome", G)


if __name__ == "__main__":
    if sys.argv[1] == "--tail":
        G, TG = load(sys.argv[2]), load(sys.argv[3]); N = G["N"]
        (c1, r1), (c2, r2) = census(G, True), census(TG, True)
        r2 = [r for r in r2 if r[0] < N]
        k1 = {(x, k, t): (d, ns, mid) for x, k, t, d, ns, mid in r1}; k2 = {(x, k, t): (d, ns, mid) for x, k, t, d, ns, mid in r2}
        same_flips = set(k1) == set(k2); common = set(k1) & set(k2)
        dNS = sum(k1[q][1] != k2[q][1] for q in common); dMID = sum(k1[q][2] != k2[q][2] for q in common); d100 = sum(k1[q][0] != k2[q][0] for q in common)
        print("TAIL45 %s -> %s | T3 %d / %d | flips on G's gates %d / %d, same flip set %s | flips with depth100 changed %d, depthNS changed %d, depthMID changed %d | deepNS %d / %d, IntNS %d / %d, gmaxNS %d / %d | deep100 %d / %d | pimis %d / %d | ctrl %d" % (
            os.path.basename(sys.argv[2]), os.path.basename(sys.argv[3]), c1["T3"], c2["T3"], len(r1), len(r2), same_flips, d100, dNS, dMID,
            c1["deepNS"], c2["deepNS"], c1["IntNS"], c2["IntNS"], c1["gmaxNS"], c2["gmaxNS"], c1["deep100"], c2["deep100"], c1["pimis"], c2["pimis"], CTRL), flush=True)
        sys.exit(0)
    for fn in sys.argv[1:]:
        G = load(fn)
        print(os.path.basename(fn), "N+M", G["N"] + sum(map(len, G["opts"])), "C", CMAX, json.dumps(census(G)), flush=True)
