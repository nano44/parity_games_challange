#!/usr/bin/env python3
"""L-COMP box 44 item 1: MY builder of L-SI 52's wrapper W(H, s0), written from the TEXT of claude/l-si 26704e01
docs/si/box104-map.md §3 (the Definition, quoted in README.md); wrap104.py was NOT opened before the comparison with the frozen files.
Quoted construction (box 104 §3):
  «the vertices of H with their owners and indices, and Ω(v) := pr(v) + 6;»
  «for every edge (v, w) with v ∈ V_E: a pad m_(v,w) (Ω 2 if w = s0(v), else 0), an Odd GATE g_(v,w) (Ω 1), pads pe_(v,w) (Ω 1) and
   pβ_(v,w) (Ω 0), with the edges v → m → g, g → pe → c_W and g → pβ → b_(v,w);»
  «for every edge (o, w) with o ∈ V_O: pads x1, x2, x3 (Ω 0), with the edges o → x1 → x2 → x3 → b_(o,w);»
  «for every edge (a, w) of H: a VALVE b_(a,w) (Even, Ω 0) and pads y_(a,w) (Ω 2), pb_(a,w) (Ω 1), with the edges b → y → w and
   b → pb → K0;»
  «for every o ∈ V_O: a pad pe_o (Ω 1), with the edges o → pe_o → c_W;»
  «c_W (Even, a self-loop, Ω top := the least even number ≥ max Ω(V) + 2), and R117's core with its pads: K0 (Even, top + 2) → {K1, pA},
   pA → K3, K1 (Even, 5) → {q, s}, s → K1, q → K0, K2 (Odd, 3) → {r, K2}, r → K1, K3 (Even, top + 3) → {K1, K2}; pA, s, r have Ω 0, q
   has Ω 1.»
  «Every pad is an Even vertex with one successor; the new vertices are indexed after V.» «|W| = n + 7·m_E + 6·m_O + n_O + 9.»
  STANDARD STATE «σ(v) = m_(v,s(v)) for v ∈ V_E; σ(b) = y at every valve; σ(K0) = pA, σ(K1) = s, σ(K3) = K2; τ0: τ(g) = pe at every
   gate, τ(o) = pe_o at every o ∈ V_O, τ(K2) = K2.»
Readings (mine, each stated): R1 the text fixes no order for the new vertices beyond «after V»: MY order is, edge by edge in (v, w)
order, the Even-edge gadgets (m, g, pe, pβ), then the Odd-edge pads (x1, x2, x3), then (b, y, pb) for every edge, then pe_o for every
o, then c_W, K0, K1, K2, K3, pA, s, q, r (ORDER=rev: the new vertices in the reverse of that order; ORDER=rand:<seed>: shuffled;
ORDER=lsi: the order of L-SI's frozen files, read off the isomorphism between my build and inst/W_2.pg: c_W, K0..K3, pA, s, q, r, then
vertex by vertex, edge by edge: pb, y, b, then pβ, pe, g, m (Even edge) or x3, x2, x1 (Odd edge), and pe_o after an Odd vertex's edges);
R2 «max Ω(V)» is over the vertices of H (= max pr + 6); R3 H's edges are a set (duplicates in a successor list count once).
Also here: canon() = a canonical relabelling by colour refinement with individualisation (exact signatures, no hashing), used to
compare two builds up to isomorphism (fixed = k individualises the first k vertices by index: «same H indices»).
Usage: wrap44.py pg H.pg S0.json OUT.pg | wrap44.py canon A.pg [fixed]   (prints the sha1 of the canonical text)"""
import sys, os, json, hashlib, random
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "harness")]
import pg
EVEN, ODD = 0, 1
ORDER = os.environ.get("ORDER", "mine")


def wrap(h, s0, eorder=None):
    """h: pg.Game; s0: list, s0[v] = a successor of v for v Even (anything at Odd vertices). Returns (game, V) with V: role key -> index.
    eorder[v] (optional): v's successors in the order in which their gadgets are indexed (default: increasing index)."""
    n = h.n; succ = [sorted(set(s)) for s in h.succ]
    if eorder is not None:
        assert all(sorted(eorder[v]) == succ[v] for v in range(n)); succ = [list(e) for e in eorder]
    for v in range(n):
        if h.owner[v] == EVEN: assert s0[v] in succ[v], "s0 is not a strategy at %d" % v
    keys = []
    for v in range(n):
        if h.owner[v] == EVEN:
            for w in succ[v]: keys += [("m", v, w), ("g", v, w), ("pe", v, w), ("pB", v, w)]
    for o in range(n):
        if h.owner[o] == ODD:
            for w in succ[o]: keys += [("x1", o, w), ("x2", o, w), ("x3", o, w)]
    for a in range(n):
        for w in succ[a]: keys += [("b", a, w), ("y", a, w), ("pb", a, w)]
    for o in range(n):
        if h.owner[o] == ODD: keys.append(("peo", o))
    keys += ["cW", "K0", "K1", "K2", "K3", "pA", "s", "q", "r"]
    if ORDER == "lsi":      # the order of L-SI's frozen files, READ OFF the isomorphism between my build and inst/W_2.pg (not from wrap104.py)
        keys = ["cW", "K0", "K1", "K2", "K3", "pA", "s", "q", "r"]
        for v in range(n):
            for w in succ[v]:
                keys += [("pb", v, w), ("y", v, w), ("b", v, w)]
                keys += [("pB", v, w), ("pe", v, w), ("g", v, w), ("m", v, w)] if h.owner[v] == EVEN else [("x3", v, w), ("x2", v, w), ("x1", v, w)]
            if h.owner[v] == ODD: keys.append(("peo", v))
    elif ORDER == "rev": keys.reverse()
    elif ORDER.startswith("rand:"): random.Random(int(ORDER[5:])).shuffle(keys)
    V = {("h", v): v for v in range(n)}
    for i, k in enumerate(keys): V[k] = n + i
    N = n + len(keys); prio = [0] * N; own = [EVEN] * N; S = [None] * N
    top = max(h.prio) + 6 + 2; top += top % 2
    def put(k, p, o, su): prio[V[k]] = p; own[V[k]] = o; S[V[k]] = [V[x] for x in su]
    for v in range(n):
        if h.owner[v] == EVEN:
            put(("h", v), h.prio[v] + 6, EVEN, [("m", v, w) for w in succ[v]])
            for w in succ[v]:
                put(("m", v, w), 2 if s0[v] == w else 0, EVEN, [("g", v, w)])
                put(("g", v, w), 1, ODD, [("pe", v, w), ("pB", v, w)])
                put(("pe", v, w), 1, EVEN, ["cW"])
                put(("pB", v, w), 0, EVEN, [("b", v, w)])
        else:
            put(("h", v), h.prio[v] + 6, ODD, [("x1", v, w) for w in succ[v]] + [("peo", v)])
            for w in succ[v]:
                put(("x1", v, w), 0, EVEN, [("x2", v, w)]); put(("x2", v, w), 0, EVEN, [("x3", v, w)]); put(("x3", v, w), 0, EVEN, [("b", v, w)])
            put(("peo", v), 1, EVEN, ["cW"])
        for w in succ[v]:
            put(("b", v, w), 0, EVEN, [("y", v, w), ("pb", v, w)])
            put(("y", v, w), 2, EVEN, [("h", w)])
            put(("pb", v, w), 1, EVEN, ["K0"])
    put("cW", top, EVEN, ["cW"])
    put("K0", top + 2, EVEN, ["K1", "pA"]); put("pA", 0, EVEN, ["K3"])
    put("K1", 5, EVEN, ["q", "s"]); put("s", 0, EVEN, ["K1"]); put("q", 1, EVEN, ["K0"])
    put("K2", 3, ODD, ["r", "K2"]); put("r", 0, EVEN, ["K1"])
    put("K3", top + 3, EVEN, ["K1", "K2"])
    g = pg.Game(prio, own, [sorted(s) for s in S])
    mE = sum(len(succ[v]) for v in range(n) if h.owner[v] == EVEN); mO = sum(len(succ[v]) for v in range(n) if h.owner[v] == ODD)
    assert g.n == n + 7 * mE + 6 * mO + sum(h.owner) + 9, "vertex count is not the text's"
    return g, V


def standard(h, s, g, V):
    """The standard state of the Even strategy s of H, as full-length lists (sigma: Even vertices, tau: Odd vertices; -1 elsewhere)."""
    sig = [-1] * g.n; tau = [-1] * g.n
    for u in range(g.n):
        if len(g.succ[u]) == 1: (sig if g.owner[u] == EVEN else tau)[u] = g.succ[u][0]
    for v in range(h.n):
        if h.owner[v] == EVEN: sig[v] = V[("m", v, s[v])]
        else: tau[v] = V[("peo", v)]
        for w in set(h.succ[v]):
            sig[V[("b", v, w)]] = V[("y", v, w)]
            if h.owner[v] == EVEN: tau[V[("g", v, w)]] = V[("pe", v, w)]
    sig[V["K0"]] = V["pA"]; sig[V["K1"]] = V["s"]; sig[V["K3"]] = V["K2"]; tau[V["K2"]] = V["K2"]
    return sig, tau


def hpart(h, sig, V):
    """H-part of a state: for v in V_E the w with sigma(v) = m_(v,w); None if sigma(v) is not one of v's m-pads."""
    inv = {V[("m", v, w)]: w for v in range(h.n) if h.owner[v] == EVEN for w in set(h.succ[v])}
    return [inv.get(sig[v]) if h.owner[v] == EVEN else -1 for v in range(h.n)]


# ------------------------------------------------------------------ canonical relabelling
def _refine(g, col):
    n = g.n
    while True:
        sig = [(col[v], tuple(sorted(col[w] for w in set(g.succ[v]))), tuple(sorted(col[u] for u in g.pred[v]))) for v in range(n)]
        rk = {s: i for i, s in enumerate(sorted(set(sig)))}
        new = [rk[s] for s in sig]
        if len(rk) == len(set(col)): return new
        col = new


def _text(g, col):
    """Game text with vertex v renamed col[v] (col a bijection onto 0..n-1)."""
    inv = [0] * g.n
    for v, c in enumerate(col): inv[c] = v
    return "".join("%d %d %d %s;\n" % (i, g.prio[inv[i]], g.owner[inv[i]], ",".join(map(str, sorted(col[w] for w in set(g.succ[inv[i]]))))) for i in range(g.n))


def canon(g, fixed=0, cap=20000):
    """Canonical relabelling of g up to isomorphism (owner, priority, edges); with fixed = k the first k vertices keep their identity.
    Returns (text, discrete, col): text = the game in canonical names; col[v] = canonical name of v; discrete = True if plain
    refinement already separated every vertex (no individualisation was needed)."""
    n = g.n
    init = [(0, v, 0) if v < fixed else (1, g.owner[v], g.prio[v]) for v in range(n)]
    rk = {s: i for i, s in enumerate(sorted(set(init)))}
    col = _refine(g, [rk[s] for s in init])
    if len(set(col)) == n: return _text(g, col), True, col
    budget = [cap]
    def search(col):
        if len(set(col)) == n: return _text(g, col), col
        budget[0] -= 1
        if budget[0] < 0: raise RuntimeError("canon: individualisation budget exceeded")
        cells = {}
        for v, c in enumerate(col): cells.setdefault(c, []).append(v)
        c0 = min(c for c, vs in cells.items() if len(vs) > 1); best = None
        for v in cells[c0]:
            c2 = [2 * c + 1 for c in col]; c2[v] = 2 * c0
            rk2 = {s: i for i, s in enumerate(sorted(set(c2)))}
            t = search(_refine(g, [rk2[s] for s in c2]))
            if best is None or t[0] < best[0]: best = t
        return best
    t, c = search(col)
    return t, False, c


def csha(g, fixed=0):
    t, d, _ = canon(g, fixed); return hashlib.sha1(t.encode()).hexdigest(), d


def iso(a, b, fixed=0):
    """An isomorphism a -> b as a list phi (phi[v of a] = vertex of b), or None. With fixed = k it is the identity on the first k vertices."""
    if a.n != b.n: return None
    ta, _, ca = canon(a, fixed); tb, _, cb = canon(b, fixed)
    if ta != tb: return None
    inv = [0] * b.n
    for v, c in enumerate(cb): inv[c] = v
    return [inv[ca[v]] for v in range(a.n)]


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "pg":
        h = pg.read(a[1]); s0 = json.load(open(a[2])); g, V = wrap(h, s0); pg.write(g, a[3]); print("W", g.n)
    elif a[0] == "canon":
        g = pg.read(a[1]); print(a[1], *csha(g, int(a[2]) if len(a) > 2 else 0))
