#!/usr/bin/env python3
"""Box 189 (L-NEW successor 58): an independent builder of R104's Gamma(G) (packet P-N5-REALIZE §3.1) and of the S3-PADDED variant
Gamma3(G). Every edge of R104's stated start that S3 (SPEC FIX 1, best reward) would not pick is made S3's pick by single-successor
EVEN pads of priority <= 2 (rank below K2 and below every cycle node that can occur, so a pad is never in a P-set and never a cycle
node; it adds 1 to lengths and its index to vertex sequences):
  core ("K"): pA (Om 0) on K0 -> K3; s (Om 0) on the K1 self-loop (K1 -> s -> K1); q (Om 1) on K1 -> K0; r (Om 0) on K2 -> K1.
     S3: K0 {K1 odd 5, pA even} -> pA; K1 {q odd, s even} -> s; K3 {K1 5, K2 3} -> K2 (lowest odd); Odd K2 {r even, K2 odd 3}
     -> K2 (highest odd).                                             [= R104 start K0 -> K3, K1 -> K1, K3 -> K2, K2 -> K2]
  gate faces ("pe"): pe_g (Om 1) on gate -> e_g and pbeta_g (Om 0) on gate -> beta_g; S3 at Odd gate: highest odd = pe_g [tau = e]
  escapes ("pb"): pb_g (Om 1) on beta_g -> u; S3 at beta: the even mover xt (Om 0) beats the odd pad          [beta -> xt]
  movers ("m"): m_(x,k) (Om 2 for the genome start option, Om 0 otherwise; indices in gate-index order) on x -> gate (x,k);
     S3 at x: highest even = the start's pad                                                    [sigma(x) = start]
build(G, pads subset of {"K","pe","pb","m"}) -> (game, sigma0, tau0, V). With pads = {} the game equals L-RED's r187
stab.build(G, 0, kgad=True, esc=True) (selftest: python3 gamma3.py GENOME LREDROOT)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/harness"), os.path.join(ROOT, "experiments/new")]
import pg

def build(G, pads=()):
    pads = set(pads); N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O)
    V = {}; nxt = 0
    for x in range(N): V[("x", x)] = nxt; nxt += 1
    for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("g", q)] = nxt; nxt += 1
    for q in O: V[("b", q)] = nxt; nxt += 1
    for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("e", q)] = nxt; nxt += 1
    V["cX"] = nxt; V["cW"] = nxt + 1; nxt += 2
    for i in range(4): V[("K", i)] = nxt; nxt += 1
    if "K" in pads:
        for nm in ("pA", "s", "q", "r"): V[nm] = nxt; nxt += 1
    if "pe" in pads:
        for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("pe", q)] = nxt; nxt += 1
        for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("pbeta", q)] = nxt; nxt += 1
    if "pb" in pads:
        for q in O: V[("pb", q)] = nxt; nxt += 1
    if "m" in pads:
        for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("m", q)] = nxt; nxt += 1
    n = nxt; prio = [0] * n; own = [0] * n; succ = [None] * n
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4)); u = K0
    bmax = max(6 + 2 * br[b] + bp[b] for b in range(M))
    eb = bmax + 1 + (bmax + 1) % 2
    for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 * i
    for x in range(N):
        succ[x] = sorted((V[("m", (x, k))] if "m" in pads else V[("g", (x, k))]) for k in range(len(opts[x])))
    for q in O:
        x, k = q; wt, xt, b = opts[x][k]; g, bv, e = V[("g", q)], V[("b", q)], V[("e", q)]
        prio[g] = 1; own[g] = 1; succ[g] = sorted([V[("pe", q)], V[("pbeta", q)]] if "pe" in pads else [e, bv])
        prio[bv] = 6 + 2 * br[b] + bp[b]
        esc = V[("pb", q)] if "pb" in pads else u
        succ[bv] = sorted([xt, esc]) if xt >= 0 else [esc]
        succ[e] = [V["cW"] if wt < 0 else wt]
        if "pe" in pads:
            prio[V[("pe", q)]] = 1; succ[V[("pe", q)]] = [e]; prio[V[("pbeta", q)]] = 0; succ[V[("pbeta", q)]] = [bv]
        if "pb" in pads: prio[V[("pb", q)]] = 1; succ[V[("pb", q)]] = [u]
        if "m" in pads: prio[V[("m", q)]] = 2 if G["start"][x] == k else 0; succ[V[("m", q)]] = [g]
    prio[V["cX"]] = 2; succ[V["cX"]] = [V["cX"]]
    top = max(prio) + 2; top += top % 2; cW = V["cW"]; prio[cW] = top; succ[cW] = [cW]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0] = sorted([K1, V["pA"] if "K" in pads else K3]); succ[K1] = sorted([V["q"], V["s"]] if "K" in pads else [K0, K1])
    succ[K2] = sorted([V["r"] if "K" in pads else K1, K2]); succ[K3] = [K1, K2]
    if "K" in pads:
        prio[V["pA"]] = 0; succ[V["pA"]] = [K3]; prio[V["s"]] = 0; succ[V["s"]] = [K1]
        prio[V["q"]] = 1; succ[V["q"]] = [K0]; prio[V["r"]] = 0; succ[V["r"]] = [K1]
    gm = pg.Game(prio, own, succ)
    # R104's stated start, transported through the pads
    sig = {v: succ[v][0] for v in range(n) if own[v] == 0}
    for q in O:
        if opts[q[0]][q[1]][1] >= 0: sig[V[("b", q)]] = opts[q[0]][q[1]][1]
    sig[K0] = V["pA"] if "K" in pads else K3; sig[K1] = V["s"] if "K" in pads else K1; sig[K3] = K2
    for x in range(N): q = (x, G["start"][x]); sig[x] = V[("m", q)] if "m" in pads else V[("g", q)]
    tau = {V[("g", q)]: (V[("pe", q)] if "pe" in pads else V[("e", q)]) for q in O}; tau[K2] = K2
    return gm, sig, tau, V

def mover_state(G, V, sigma, pads):
    """option index per mover read from sigma (through the mover pad if present); -1 if sigma(x) is not a (pad of a) gate."""
    N = G["N"]; inv = {}
    for (kind, *rest), v in ((k if isinstance(k, tuple) else (k,), v) for k, v in V.items()):
        if kind == ("m" if "m" in pads else "g"): inv[v] = rest[0][1]
    return tuple(inv.get(sigma[x], -1) for x in range(N))

if __name__ == "__main__":   # selftest against L-RED's builder: python3 gamma3.py GENOME LREDROOT
    sys.path[:0] = [os.path.join(sys.argv[2], "experiments/red/r187"), os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/si")]
    import stab
    G = json.load(open(sys.argv[1])); a, sa, ta, _ = build(G); b, sb, tb, *_ = stab.build(G, 0, kgad=True, esc=True)
    assert (a.prio, a.owner, a.succ) == (b.prio, b.owner, [sorted(s) for s in b.succ]) or (a.prio, a.owner) == (b.prio, b.owner), "games differ"
    assert [sorted(s) for s in a.succ] == [sorted(s) for s in b.succ], "edges differ"
    assert sa == sb and ta == tb, "starts differ"
    print("SELFTEST gamma3.build(G, {}) == stab.build(G, 0, kgad, esc): game and start identical, n", a.n)
