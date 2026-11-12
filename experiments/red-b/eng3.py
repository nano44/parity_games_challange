#!/usr/bin/env python3
"""L-RED-B's own Gamma3 builder and HOW3 run (successor 3; B2, box 209). Written from the definitions only:
  - Gamma(G): eng.py (this lane's session-1 builder, from docs/red/P-N5-REALIZE.md par. 2, 3.1 = RESULTS R104's packet);
  - the pads: docs/new/P-N5-REACH.md par. 3 (RESULTS R117's packet), quoted in docs/red-b/B2-box209.md par. 1:
      «appended after Γ's vertices in the order pA, s, q, r, pe (gate-index order), pβ (gate-index order), pb (option order),
       m (gate-index order)»; «pA (Ω 0) on K0 → K3; s (Ω 0) on the self-loop of K1 (K1 → s → K1); q (Ω 1) on K1 → K0;
       r (Ω 0) on K2 → K1»; «pe_g (Ω 1) on g → e_g, and pβ_g (Ω 0) on g → β_g»; «pb_g (Ω 1) on β_g → u (for every gate g,
       also when xt(g) = X)»; «m_(x,k) on x → g_(x,k), with Ω 2 if k = start(x) and Ω 0 otherwise».
  - the standard state (same par. 3): «σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if xt(g) is a mover, pb_g otherwise; σ(K0) = pA,
       σ(K1) = s, σ(K3) = K2; τ(g) = pe_g at every gate, τ(K2) = K2; forced choices elsewhere.»
  - HOW3 (RESULTS R125, quoted in box 209 par. 1): «every non-mover Even vertex frozen at the standard state's choice ...,
       Odd unrestricted at the gates and K2, every mover moving to a ⊴-best successor and keeping a best current one;
       T3 := the first state at which no mover has a strictly better successor».
Values: eng.play_values (R118's [VJ] as P-N5-REACH par. 0 states it: rank by (Ω(v), v); (c, P, ℓ); c odd: longer is better
for Even). Odd's reply: one-player strategy iteration for Odd (best_reply3), checked against brute force (brute3).
No code of any other lane is imported or copied.
"""
import itertools, json, sys
import eng

class G3:
    pass

def build3(G, frozen=True):
    """Gamma3(G) with HOW3's freezing (every non-mover Even vertex has its standard-state successor only)."""
    g0 = eng.build(G)
    N, M, n0 = g0.N, g0.M, g0.n
    n = n0 + 4 * M + 4
    g = G3()
    g.N, g.M, g.n, g.n0, g.name = N, M, n, n0, g0.name
    owner = list(g0.owner) + [0] * (4 * M + 4)
    prio = list(g0.prio) + [0] * (4 * M + 4)
    succ = [list(s) for s in g0.succ] + [None] * (4 * M + 4)
    kind = list(g0.kind) + [""] * (4 * M + 4)
    K0, K1, K2, K3 = g0.K
    pA, s, q, r = n0, n0 + 1, n0 + 2, n0 + 3
    olist = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    oidx = {o: i for i, o in enumerate(olist)}
    gate = G["gate"]; start = list(G.get("start", [0] * N))
    pe = {}; pbt = {}; pb = {}; mp = {}
    for (x, k) in olist:
        gi = gate[x][k]
        pe[(x, k)] = n0 + 4 + gi
        pbt[(x, k)] = n0 + 4 + M + gi
        pb[(x, k)] = n0 + 4 + 2 * M + oidx[(x, k)]
        mp[(x, k)] = n0 + 4 + 3 * M + gi
    # core pads
    prio[pA] = 0; kind[pA] = "pA"; succ[pA] = [K3]
    prio[s] = 0; kind[s] = "s"; succ[s] = [K1]
    prio[q] = 1; kind[q] = "q"; succ[q] = [K0]
    prio[r] = 0; kind[r] = "r"; succ[r] = [K1]
    succ[K0] = [pA]          # frozen: σ(K0) = pA (full edges {K1, pA})
    succ[K1] = [s]           # frozen: σ(K1) = s (full edges {q, s})
    succ[K2] = [r, K2]       # Odd, unrestricted
    succ[K3] = [K2]          # frozen: σ(K3) = K2 (full edges {K1, K2})
    for (x, k) in olist:
        gv = g0.gatev[(x, k)]; e = g0.evx[(x, k)]; b = g0.beta[(x, k)]
        a, c, d, m = pe[(x, k)], pbt[(x, k)], pb[(x, k)], mp[(x, k)]
        prio[a] = 1; kind[a] = "pe"; succ[a] = [e]
        prio[c] = 0; kind[c] = "pbeta"; succ[c] = [b]
        prio[d] = 1; kind[d] = "pb"; succ[d] = [K0]
        prio[m] = 2 if k == start[x] else 0; kind[m] = "mp"; succ[m] = [gv]
        succ[gv] = [a, c]    # Odd gate: [e-face pad, beta-face pad]
        xt = G["opts"][x][k][1]
        succ[b] = [xt] if xt >= 0 else [d]   # frozen standard choice of beta
    for x in range(N):
        succ[x] = [mp[(x, k)] for k in range(len(G["opts"][x]))]
    g.owner, g.prio, g.succ, g.kind = owner, prio, succ, kind
    byrel = sorted(range(n), key=lambda v: (prio[v], v))
    rank = [0] * n
    for rr, v in enumerate(byrel): rank[v] = rr
    g.rank = rank
    g.rew = [(2 * rank[v]) if prio[v] % 2 == 0 else -(2 * rank[v] + 1) for v in range(n)]
    g.oddmask = sum((1 << rank[v]) for v in range(n) if prio[v] % 2 == 1)
    g.emask = sum((1 << rank[v]) for v in range(n) if kind[v] == "e")
    g.K = g0.K; g.cX, g.cW = g0.cX, g0.cW; g.pA, g.s, g.q, g.r = pA, s, q, r
    g.pe, g.pbt, g.pb, g.mp = pe, pbt, pb, mp
    g.gatev, g.evx, g.beta = g0.gatev, g0.evx, g0.beta
    g.olist = olist; g.start = start
    g.odd = [v for v in range(n) if owner[v] == 1]
    g.gates = [v for v in range(n) if kind[v] == "g"]
    g.gate_of_vertex = {g0.gatev[o]: o for o in olist}
    g.nE = sum(1 for v in range(n) if owner[v] == 0)
    g.core = {K0, K1, K2, K3, pA, s, q, r}
    g.G = G
    return g

def nxt_of(g, sig, sbar):
    nx = [0] * g.n
    for v in range(g.n):
        if g.owner[v] == 1: nx[v] = sbar[v]
        elif v < g.N: nx[v] = g.succ[v][sig[v]]
        else: nx[v] = g.succ[v][0]
    return nx

def best_reply3(g, sig, sbar0=None):
    """Odd's optimal counterstrategy against sig by one-player strategy iteration for Odd (start: beta-face pads, K2 -> r)."""
    if sbar0 is None:
        sbar = {v: g.succ[v][1] for v in g.gates}
        sbar[g.K[2]] = g.r
    else:
        sbar = dict(sbar0)
    while True:
        nx = nxt_of(g, sig, sbar)
        val, lam, pim, kk = eng.play_values(g, nx)
        changed = False
        for v in g.odd:
            cur = sbar[v]
            for w in g.succ[v]:
                if w != cur and val[w] < val[cur]: cur = w
            if cur != sbar[v]: sbar[v] = cur; changed = True
        if not changed:
            return sbar, val, lam, pim, kk, nx

def brute3(g, sig):
    """Pointwise minimum of play values over ALL positional Odd strategies."""
    best = None
    for ch in itertools.product(*[g.succ[v] for v in g.odd]):
        sbar = dict(zip(g.odd, ch))
        val = eng.play_values(g, nxt_of(g, sig, sbar))[0]
        if best is None: best = list(val)
        else:
            for v in range(g.n):
                if val[v] < best[v]: best[v] = val[v]
    return best

def how3_run(g, tie="keep-low", cap=10 ** 6, rng=None, sig0=None, keep=True):
    """HOW3 from the standard state for the genome start. tie: rule among several best successors when the current one is
    not best ("keep-low", "high", "rand"). Returns the list of states dict(sig, sbar, val, lam, pim, kk, nx)."""
    sig = list(sig0 if sig0 is not None else g.start)
    hist = []; sbar = None
    while True:
        sbar, val, lam, pim, kk, nx = best_reply3(g, sig, None)
        hist.append({"sig": list(sig), "sbar": dict(sbar), "val": val, "lam": lam, "pim": pim, "kk": kk, "nx": nx})
        new = list(sig); ch = False
        for x in range(g.N):
            vals = [val[w] for w in g.succ[x]]
            bv = max(vals)
            if vals[sig[x]] == bv: continue
            cands = [k for k in range(len(vals)) if vals[k] == bv]
            if tie == "keep-low": k = cands[0]
            elif tie == "high": k = cands[-1]
            else: k = rng.choice(cands)
            new[x] = k; ch = True
        if not ch: return hist
        sig = new
        if len(hist) > cap: raise RuntimeError("cap")

if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = eng.load(p); g = build3(G)
        h = how3_run(g)
        print(g.name, "N", g.N, "M", g.M, "n3", g.n, "T3", len(h) - 1)
