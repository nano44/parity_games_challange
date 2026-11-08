#!/usr/bin/env python3
"""L-RED 58 R223 item 5: my own builder of Gamma3(G), written from the text: RESULTS R104 [DEF] (Gamma(G): priorities, owners, edges,
vertex indices «movers, gates in gate-index order, beta-vertices, e-vertices in the order of their gates' gate indices, the unused loop,
c_W, K0 to K3») and P-N5-REACH §3 (pads appended «in the order pA, s, q, r, pe (gate-index order), pbeta (gate-index order), pb (option
order), m (gate-index order)», with their priorities). Choices the text leaves open, taken from [E-LEV] / P-N5-XICYC: beta-vertices in
option order; e-priorities = the least even number above every beta, + 2 per e in (level, gate index) order. Successor lists sorted.
build3(G) -> (prio, owner, succ, start_sigma (dict), tau0 (dict), V)."""
def build3(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; byg = sorted(O, key=lambda q: gate[q[0]][q[1]]); V = {}
    order = [("x", x) for x in range(N)] + [("g", q) for q in byg] + [("b", q) for q in O] + [("e", q) for q in byg] + ["cX", "cW"] \
        + [("K", i) for i in range(4)] + ["pA", "s", "q", "r"] + [("pe", q) for q in byg] + [("pbeta", q) for q in byg] \
        + [("pb", q) for q in O] + [("m", q) for q in byg]
    for i, k in enumerate(order): V[k] = i
    n = len(order); prio = [0] * n; own = [0] * n; succ = [[] for _ in range(n)]
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4))
    for q in O:
        b = opts[q[0]][q[1]][2]; prio[V[("b", q)]] = 6 + 2 * br[b] + bp[b]
    bmax = max(prio[V[("b", q)]] for q in O); e0 = bmax + 1 if (bmax + 1) % 2 == 0 else bmax + 2
    for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = e0 + 2 * i
    for x in range(N): succ[x] = [V[("m", (x, k))] for k in range(len(opts[x]))]
    for q in O:
        x, k = q; wt, xt, _ = opts[x][k]
        g = V[("g", q)]; prio[g] = 1; own[g] = 1; succ[g] = [V[("pe", q)], V[("pbeta", q)]]
        succ[V[("b", q)]] = ([xt] if xt >= 0 else []) + [V[("pb", q)]]
        succ[V[("e", q)]] = [V["cW"] if wt < 0 else wt]
        prio[V[("pe", q)]] = 1; succ[V[("pe", q)]] = [V[("e", q)]]
        prio[V[("pbeta", q)]] = 0; succ[V[("pbeta", q)]] = [V[("b", q)]]
        prio[V[("pb", q)]] = 1; succ[V[("pb", q)]] = [K0]
        prio[V[("m", q)]] = 2 if G["start"][x] == k else 0; succ[V[("m", q)]] = [g]
    prio[V["cX"]] = 2; succ[V["cX"]] = [V["cX"]]
    top = max(prio) + 2; top += top % 2; prio[V["cW"]] = top; succ[V["cW"]] = [V["cW"]]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0] = [K1, V["pA"]]; succ[K1] = [V["q"], V["s"]]; succ[K2] = [V["r"], K2]; succ[K3] = [K1, K2]
    for nm, p, t in (("pA", 0, K3), ("s", 0, K1), ("q", 1, K0), ("r", 0, K1)): prio[V[nm]] = p; succ[V[nm]] = [t]
    succ = [sorted(s) for s in succ]
    sig = {v: succ[v][0] for v in range(n) if own[v] == 0}
    for q in O:
        xt = opts[q[0]][q[1]][1]
        if xt >= 0: sig[V[("b", q)]] = xt
    sig[K0] = V["pA"]; sig[K1] = V["s"]; sig[K3] = K2
    for x in range(N): sig[x] = V[("m", (x, G["start"][x]))]
    tau = {V[("g", q)]: V[("pe", q)] for q in O}; tau[K2] = K2
    return prio, own, succ, sig, tau, V
