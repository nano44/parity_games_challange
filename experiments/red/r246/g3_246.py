#!/usr/bin/env python3
"""L-RED 71 R246: OWN builder of Gamma3(G) for an R104 genome G, written from the texts: trunk docs/red/P-N5-REALIZE.md section 3.1 (the game
Gamma(G): movers, gates, beta, e, c_X, c_W, the core K) and RESULTS R117 / box 189's stated pads (4M + 4 single-successor Even pads of
priority <= 2: pA, s, q, r in the core; pe_g, pbeta_g on the two gate faces; pb_g on beta_g -> u; m_(x,k) on x -> gate (x, k), priority 2 for
the genome's start option). No code of another lane is imported. Vertex order (so that EMODE=r104 can be compared byte for byte with the
frozen .pg files of claude/l-red-b, data/b6b/pg/G_k_g3.pg): movers; gates in gate order; beta in (x, k) order; e in gate order; c_X; c_W;
K0..K3; pA, s, q, r; pe in gate order; pbeta in gate order; pb in (x, k) order; m in gate order.

EMODE (the priorities of the e-vertices and of c_W; everything else is R104's):
  r104  R104's: Omega(e_g) = eb + 2 i, i = position of g in the order by (level of the owner, gate index), eb = least even > bmax; c_W above
        every e (top). In S4a's arena every W-play to c_W carries the EMPTY P-set: every option of a mover is tied (Lemma W (iii)).
  top   TIE-FREE variant (this lane, R246): c_W gets the least even priority above every beta; every e is EVEN and ABOVE c_W, ordered
        ROOT-MAJOR: Omega(e_g) = cw + 2 + 2 j, j = position of g in the order by (-level of the owner, -gate index), so a lower level outranks a
        higher one and, inside a level, a smaller gate index outranks a larger one. In S4a's arena the W-play of an option then carries the
        P-set {e-vertices on it}, and the order on P-sets (most relevant vertex of the symmetric difference, even = good for Even) is exactly
        the root-first lexicographic key order: the key-least option is STRICTLY best.
  topodd  as top but every e ODD with the order inside a level reversed (larger gate index outranks): the same strict order by avoidance.
Usage: g3_246.py EMODE GENOME.json OUT.pg   (prints n, m, sha1 of the file)"""
import sys, json, hashlib

def build(G, emode="r104"):
    N, lev, opts, gate, br, bp, start = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"], G["start"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O)
    assert sorted(gate[x][k] for x, k in O) == list(range(M)), "gate indices must be a bijection onto 0..M-1 (R104)"
    GO = sorted(O, key=lambda q: gate[q[0]][q[1]])                                   # gate order
    V = {}; nxt = 0
    def new(key):
        nonlocal nxt
        V[key] = nxt; nxt += 1
    for x in range(N): new(("x", x))
    for q in GO: new(("g", q))
    for q in O: new(("b", q))
    for q in GO: new(("e", q))
    new("cX"); new("cW")
    for i in range(4): new(("K", i))
    for nm in ("pA", "s", "q", "r"): new(nm)
    for q in GO: new(("pe", q))
    for q in GO: new(("pbeta", q))
    for q in O: new(("pb", q))
    for q in GO: new(("m", q))
    n = nxt; assert n == N + 7 * M + 10
    prio = [0] * n; own = [0] * n; succ = [None] * n
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4)); u = K0; cW = V["cW"]
    bmax = max(6 + 2 * br[b] + bp[b] for b in range(M)); eb = bmax + 1 + (bmax + 1) % 2
    if emode == "r104":
        for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 * i
    elif emode == "top":
        for j, q in enumerate(sorted(O, key=lambda q: (-lev[q[0]], -gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 + 2 * j
    elif emode == "topodd":
        for j, q in enumerate(sorted(O, key=lambda q: (-lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 3 + 2 * j
    else: raise SystemExit("EMODE?")
    for x in range(N): succ[x] = sorted(V[("m", (x, k))] for k in range(len(opts[x])))
    for q in O:
        x, k = q; wt, xt, b = opts[x][k]; g, bv, e = V[("g", q)], V[("b", q)], V[("e", q)]
        prio[g] = 1; own[g] = 1; succ[g] = sorted([V[("pe", q)], V[("pbeta", q)]])
        prio[bv] = 6 + 2 * br[b] + bp[b]
        succ[bv] = sorted([xt, V[("pb", q)]]) if xt >= 0 else [V[("pb", q)]]
        succ[e] = [cW if wt < 0 else wt]
        prio[V[("pe", q)]] = 1; succ[V[("pe", q)]] = [e]
        prio[V[("pbeta", q)]] = 0; succ[V[("pbeta", q)]] = [bv]
        prio[V[("pb", q)]] = 1; succ[V[("pb", q)]] = [u]
        prio[V[("m", q)]] = 2 if start[x] == k else 0; succ[V[("m", q)]] = [g]
    prio[V["cX"]] = 2; succ[V["cX"]] = [V["cX"]]
    if emode == "r104":
        top = max(prio) + 2; top += top % 2; prio[cW] = top
    else:
        prio[cW] = eb; top = max(prio) + 2; top += top % 2                            # K0 = top + 2, K3 = top + 3 stay above every e
    succ[cW] = [cW]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0] = sorted([K1, V["pA"]]); succ[K1] = sorted([V["q"], V["s"]]); succ[K2] = sorted([V["r"], K2]); succ[K3] = sorted([K1, K2])
    prio[V["pA"]] = 0; succ[V["pA"]] = [K3]; prio[V["s"]] = 0; succ[V["s"]] = [K1]
    prio[V["q"]] = 1; succ[V["q"]] = [K0]; prio[V["r"]] = 0; succ[V["r"]] = [K1]
    return prio, own, succ, V

def dumps(prio, own, succ):
    n = len(prio)
    return f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n))

def mover_state(G, V, sigma):
    inv = {V[("m", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    return tuple(inv.get(sigma[x], -1) for x in range(G["N"]))

if __name__ == "__main__":
    emode, fn, out = sys.argv[1:4]
    G = json.load(open(fn)); prio, own, succ, V = build(G, emode); s = dumps(prio, own, succ)
    open(out, "w").write(s)
    print("G3_246", emode, fn.split("/")[-1], "n", len(prio), "m", sum(len(x) for x in succ), "sha1", hashlib.sha1(s.encode()).hexdigest(), flush=True)
