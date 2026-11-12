#!/usr/bin/env python3
"""L-RED-B's own IDEAL-CYC engine. Written from the definitions only:
  - genome and game Gamma(G): docs/red/P-N5-REALIZE.md par. 2 and par. 3.1 (RESULTS R104's packet);
  - IDEAL-CYC, Howard step, values: docs/new/P-N5-XICYC.md par. 1 [VJ] and par. 2 (RESULTS R118 (a)).
No code of any other lane is imported or copied.

Genome (JSON, the data format of the fleet's frozen instances, read as data):
  N; lev[x]; opts[x] = list of [wt, xt, bid] (wt = -1 at level 0, xt = -1 for the exit X);
  gate[x][k] = gate index of option (x, k); br[bid], bp[bid] = rank and parity of the beta-id; start[x] (default: option 0).
  Optional key "eorder" (this lane's, for tests only): an arbitrary order of the e-priorities instead of the packet's.

Vertices of Gamma(G), n = N + 3M + 6 (P-N5-REALIZE par. 3.1):
  movers 0..N-1 (Even, 0); gates N + gate index (Odd, 1); beta N+M.. in (x, k) order (Even, 6 + 2 br + bp);
  e N+2M.. in gate-index order (Even, eb + 2 i, i = position by (lev(owner), gate index)); c_X (Even, 2);
  c_W (Even, top); K0 (Even, top+2); K1 (Even, 5); K2 (Odd, 3); K3 (Even, top+3).
IDEAL-CYC: every Even vertex that is not a mover has its start successor only: beta -> xt (K0 if X), e -> wt (c_W at
level 0), c_X, c_W self-loops, K0 -> K3, K1 -> K1, K3 -> K2. Odd: gate -> {e, beta}, K2 -> {K1, K2}.

Value of a vertex under a positional pair (R118's premise [VJ]): (Lambda, Pi, k), encoded as a tuple of integers
  (reward(Lambda), signed weight of Pi, -k if Lambda even else k), compared as tuples = the order "better for Even".
  reward(v) = +p'(v) for even priority, -p'(v) for odd, p'(v) = 2 rank(v) + parity, rank by (priority, index).
  signed weight of Pi = sum over u in Pi of +2^rank(u) (even priority) or -2^rank(u) (odd): the sign of the difference of
  two such sums is the sign of the most relevant element of the symmetric difference, as [VJ] asks.
"""
import json, sys, itertools, random

class Game:
    __slots__ = ("N", "M", "n", "lev", "opts", "gate_of", "owner", "prio", "succ", "rank", "rew", "bit", "kind",
                 "g_owner", "g_opt", "beta", "evx", "gatev", "cX", "cW", "K", "movers", "odd", "is_e", "emask",
                 "start", "xt", "wt", "oddmask", "name")

def build(G):
    """Gamma(G) with the IDEAL-CYC freezing. G is a genome dict."""
    g = Game()
    N = G["N"]; lev = G["lev"]; opts = G["opts"]; gate = G["gate"]; br = G["br"]; bp = G["bp"]
    M = sum(len(o) for o in opts)
    assert sorted(x for row in gate for x in row) == list(range(M)), "gate indices must be a bijection onto 0..M-1"
    assert sorted(br[o[2]] for row in opts for o in row) == list(range(M)), "beta ranks must be a bijection onto 0..M-1"
    n = N + 3 * M + 6
    g.N, g.M, g.n, g.lev, g.opts = N, M, n, lev, opts
    owner = [0] * n; prio = [0] * n; succ = [None] * n; kind = [""] * n
    cX, cW = N + 3 * M, N + 3 * M + 1
    K = [N + 3 * M + 2 + i for i in range(4)]
    # option order (x, k)
    olist = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    oidx = {o: i for i, o in enumerate(olist)}
    gatev = {}; beta = {}; evx = {}
    for (x, k) in olist:
        gatev[(x, k)] = N + gate[x][k]
        beta[(x, k)] = N + M + oidx[(x, k)]
        evx[(x, k)] = N + 2 * M + gate[x][k]
    bmax = 0
    for (x, k) in olist:
        wt, xt, bid = opts[x][k]
        if lev[x] == 0: assert wt == -1, "level-0 option must have no W-target"
        else: assert 0 <= wt < N and lev[wt] == lev[x] - 1, "W-target must be a mover one level below (GRADED)"
        assert xt == -1 or 0 <= xt < N
        v = gatev[(x, k)]; owner[v] = 1; prio[v] = 1; succ[v] = [evx[(x, k)], beta[(x, k)]]; kind[v] = "g"
        b = beta[(x, k)]; prio[b] = 6 + 2 * br[bid] + bp[bid]; succ[b] = [xt if xt >= 0 else K[0]]; kind[b] = "b"
        bmax = max(bmax, prio[b])
    eb = bmax + 1 if (bmax + 1) % 2 == 0 else bmax + 2
    order = sorted(olist, key=lambda o: (lev[o[0]], gate[o[0]][o[1]]))
    if "eorder" in G:
        # optional, NOT R104's packet order: an arbitrary order of the e-priorities (a permutation of the option list in
        # (x, k) order, lowest e-priority first). Used only to test that a statement does not depend on [E-LEV].
        assert sorted(G["eorder"]) == list(range(M))
        order = [olist[i] for i in G["eorder"]]
    mx = bmax
    for i, (x, k) in enumerate(order):
        e = evx[(x, k)]; prio[e] = eb + 2 * i; kind[e] = "e"; mx = max(mx, prio[e])
        wt = opts[x][k][0]
        succ[e] = [wt if lev[x] > 0 else cW]
    for x in range(N):
        prio[x] = 0; succ[x] = [gatev[(x, k)] for k in range(len(opts[x]))]; kind[x] = "m"
        assert len(succ[x]) >= 1
    prio[cX] = 2; succ[cX] = [cX]; kind[cX] = "cX"
    mx = max(mx, 5)
    top = mx + 2 if (mx + 2) % 2 == 0 else mx + 3
    prio[cW] = top; succ[cW] = [cW]; kind[cW] = "cW"
    K0, K1, K2, K3 = K
    prio[K0] = top + 2; succ[K0] = [K3]; kind[K0] = "K0"      # frozen: K0 -> K3 (full edges {K1, K3})
    prio[K1] = 5; succ[K1] = [K1]; kind[K1] = "K1"            # frozen: K1 -> K1 (full edges {K0, K1})
    prio[K2] = 3; owner[K2] = 1; succ[K2] = [K1, K2]; kind[K2] = "K2"
    prio[K3] = top + 3; succ[K3] = [K2]; kind[K3] = "K3"      # frozen: K3 -> K2 (full edges {K1, K2})
    g.owner, g.prio, g.succ, g.kind = owner, prio, succ, kind
    byrel = sorted(range(n), key=lambda v: (prio[v], v))
    rank = [0] * n
    for r, v in enumerate(byrel): rank[v] = r
    g.rank = rank
    g.rew = [(2 * rank[v]) if prio[v] % 2 == 0 else -(2 * rank[v] + 1) for v in range(n)]
    g.bit = [(1 << rank[v]) if prio[v] % 2 == 0 else -(1 << rank[v]) for v in range(n)]
    g.gate_of = {}; g.g_owner = {}; g.g_opt = {}
    for (x, k) in olist:
        v = gatev[(x, k)]; g.g_owner[v] = x; g.g_opt[v] = k
    g.beta = beta; g.evx = evx; g.gatev = gatev; g.cX = cX; g.cW = cW; g.K = K
    g.movers = list(range(N)); g.odd = [v for v in range(n) if owner[v] == 1]
    g.is_e = [kind[v] == "e" for v in range(n)]
    g.emask = sum((1 << rank[v]) for v in range(n) if kind[v] == "e")
    g.oddmask = sum((1 << rank[v]) for v in range(n) if prio[v] % 2 == 1)
    g.start = list(G.get("start", [0] * N))
    g.xt = {(x, k): opts[x][k][1] for (x, k) in olist}; g.wt = {(x, k): opts[x][k][0] for (x, k) in olist}
    g.name = G.get("name", "")
    return g

def play_values(g, nxt):
    """Values of the plays of the functional graph nxt (one successor per vertex).
    Returns (val, lam, pim, kk): val[v] the comparison tuple, lam[v] the cycle node, pim[v] the set Pi as a bitmask over
    ranks (unsigned), kk[v] the number of steps to the cycle node."""
    n = g.n; rank = g.rank
    lam = [-1] * n; state = [0] * n
    for s in range(n):
        if state[s]: continue
        path = []; v = s
        while state[v] == 0:
            state[v] = 1; path.append(v); v = nxt[v]
        if state[v] == 1:            # new cycle found, v is on it
            i = path.index(v); cyc = path[i:]
            c = max(cyc, key=lambda u: rank[u])
            for u in cyc: lam[u] = c
            for u in reversed(path[:i]): lam[u] = c
        else:
            c = lam[v]
            for u in path: lam[u] = c
        for u in path: state[u] = 2
    pim = [None] * n; kk = [None] * n
    for s in range(n):
        if pim[s] is not None: continue
        stack = []; v = s
        while pim[v] is None and v != lam[v]:
            stack.append(v); v = nxt[v]
        if pim[v] is None:           # v is its own cycle node
            pim[v] = 0; kk[v] = 0
        for u in reversed(stack):
            w = nxt[u]; c = lam[u]
            pim[u] = pim[w] | ((1 << rank[u]) if rank[u] > rank[c] else 0)
            kk[u] = kk[w] + 1
    val = [None] * n
    prio = g.prio; rew = g.rew
    # signed weight: even-priority vertices +2^rank, odd -2^rank
    oddmask = g.oddmask
    for v in range(n):
        p = pim[v]
        sw = (p & ~oddmask) - (p & oddmask)
        c = lam[v]
        val[v] = (rew[c], sw, -kk[v] if prio[c] % 2 == 0 else kk[v])
    return val, lam, pim, kk

def best_reply(g, sig, sbar0=None):
    """Odd's optimal counterstrategy against the mover choice sig (sig[x] = option index), by one-player strategy
    iteration for Odd from sbar0 (default: beta-face at every gate, K1 at K2). Returns (sbar, val, lam, pim, kk),
    sbar a dict Odd vertex -> successor."""
    n = g.n
    nxt = [None] * n
    for v in range(n):
        if g.owner[v] == 0:
            nxt[v] = g.succ[v][sig[v]] if v < g.N else g.succ[v][0]
    if sbar0 is None:
        sbar = {v: g.succ[v][1] for v in g.odd}
        sbar[g.K[2]] = g.K[1]
    else:
        sbar = dict(sbar0)
    while True:
        for v in g.odd: nxt[v] = sbar[v]
        val, lam, pim, kk = play_values(g, nxt)
        changed = False
        for v in g.odd:
            cur = sbar[v]
            for w in g.succ[v]:
                if w != cur and val[w] < val[cur]:
                    cur = w
            if cur != sbar[v]:
                sbar[v] = cur; changed = True
        if not changed:
            return sbar, val, lam, pim, kk

def brute_reply(g, sig):
    """Pointwise minimum over ALL positional Odd strategies of the play value (brute force). Returns val_min[v]."""
    n = g.n
    nxt = [None] * n
    for v in range(n):
        if g.owner[v] == 0:
            nxt[v] = g.succ[v][sig[v]] if v < g.N else g.succ[v][0]
    best = None
    for choice in itertools.product(*[g.succ[v] for v in g.odd]):
        for v, w in zip(g.odd, choice): nxt[v] = w
        val, _, _, _ = play_values(g, nxt)
        if best is None: best = list(val)
        else:
            for v in range(n):
                if val[v] < best[v]: best[v] = val[v]
    return best

def howard_run(g, tie="keep-low", cap=100000, rng=None, sig0=None):
    """The Howard run of IDEAL-CYC from the genome start. tie rule among several best successors when the current
    one is not best: "keep-low" lowest option index, "high" highest option index, "rand" random (rng).
    Returns a list of states; state = dict(sig, sbar, val, lam, pim, kk)."""
    sig = list(sig0 if sig0 is not None else g.start)
    hist = []
    sbar = None
    while True:
        sbar, val, lam, pim, kk = best_reply(g, sig, None)
        hist.append({"sig": list(sig), "sbar": dict(sbar), "val": val, "lam": lam, "pim": pim, "kk": kk})
        new = list(sig); ch = False
        for x in range(g.N):
            succ = g.succ[x]
            vals = [val[w] for w in succ]
            bestv = max(vals)
            if vals[sig[x]] == bestv: continue
            cands = [k for k in range(len(succ)) if vals[k] == bestv]
            if tie == "keep-low": k = cands[0]
            elif tie == "high": k = cands[-1]
            else: k = rng.choice(cands)
            new[x] = k; ch = True
        if not ch: return hist
        sig = new
        if len(hist) > cap: raise RuntimeError("cap")

def load(path):
    G = json.load(open(path))
    G.setdefault("name", path.split("/")[-1])
    return G

if __name__ == "__main__":
    G = load(sys.argv[1]); g = build(G)
    h = howard_run(g)
    print(g.name, "N", g.N, "M", g.M, "n", g.n, "T_CYC", len(h) - 1)
