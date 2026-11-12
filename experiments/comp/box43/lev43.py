#!/usr/bin/env python3
"""L-COMP box 43 item 1: MY counters for L-NEW 72's box 208 (claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md, sha1 55e65381),
written from its TEXT; no code of level208.py / plat208.py is used. Two kinds of run:
  genome mode : IDEAL-CYC(G) on MY engine (box37/ideal37.py); classes, bounds and vertex kinds as in the text.
  game mode   : the LIFT to (plain parity game, Howard run): every Even vertex moves to a best successor (keeps its current one if it is
                among the best, else the largest index); «movers» CH := the Even vertices with >= 2 successors; «gates» := the Odd vertices
                with >= 2 successors; «e-vertices» W := for each gate its successor of largest even priority (L-LIT T66's «esc»).
                Values: n5b SpecSI.evaluate_choice (VJ (Lambda, Pi, len), Odd's optimal counterstrategy).
Quoted definitions (box 208):
  §1 «class_t(v) := (Λ_t(v), E_t(v))», «E_t(v) := the e-vertices of Π_t(v)»; ORDER ON CLASSES «(Λ, E) < (Λ′, E′) iff reward(Λ) <
     reward(Λ′), or Λ = Λ′ and E <lex E′ (the most relevant element of E Δ E′ lies in E′)».
  §2 (K1) «class_t(v) ≤ class_(t+1)(v)»; (K3) «(c) class_t(v) = class_t(s_t(v)) for every vertex v that is not an e-vertex; (d) for an
     e-vertex e whose successor w is a mover: class_t(e) = (Λ_t(w), {e} ∪ E_t(w)), e ∉ E_t(w), so class_t(e) > class_t(w)»; (K4)
     «class_t(g) = min(class_t(e_g), class_t(β_g))»; (K5) «For every mover x, step t and gate y of x: class_(t+1)(x) ≥ class_t(y).»
  §3 «LAG_t := {v : class_t(v) ≠ class_b(v)}», «m_t := min{class_t(v) : v ∈ LAG_t}; FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t :=
     (m_t, −|FRONT_t|)», STALL «if class_(t+1)(v) = class_t(v) for every v ∈ FRONT_t»; (L1) «LAG_(t+1) ⊆ LAG_t. If the step t → t + 1
     is a stall: LAG_(t+1) ≠ ∅, FRONT_(t+1) = FRONT_t and Φ_(t+1) = Φ_t. If it is not a stall: LAG_(t+1) = ∅ or Φ_(t+1) > Φ_t.»;
     (L2) «Every vertex of FRONT_t is a mover, a gate or a β-vertex whose frozen successor is a mover.»; (L3) «(α) some mover z ∈
     FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)); or (β) there is a play at t whose cycle consists of movers, their
     chosen gates and those gates' β-faces, all in FRONT_t, and then m_t = (c, ∅) for its cycle node c»; (L4) the stall cycle (map:
     mover → its gate at b, gate → its face at t, β → its Ξ-target); (L5) «Φ takes at most 2M·(N + 2M) values».
  §4 (C2) «b′ − a = q + Σ_i (v_i − u_i)»; (C4) «b − b′ ≤ N».
  Add. A: Lemma PLATEAU «v − u ≤ N + 2M + 5»; (P1) «{x : class_s(x) ≤ m} = Y, and class_s(x) = class_u(x) for x ∈ Y»; (P2) «s_s(x) ∈
     Y»; (P3) «class_s(y) ≤ class_s(x)» for a mover x ∈ Y and its gates y; (P4) «σ̄_s(g) is the same face for all s ∈ [u, v]»; (P6)
     «every step s → s + 1 with u ≤ s ≤ v changes σ at some mover of Y»; (P7) «v − u ≤ n_E(H)»; Theorem ALL-TCYC «T_CYC ≤ P·(N + 2M +
     6) + N, P = 2M(N + 2M)».
Reference state b := T (the last state), a := 0. Counters (must-0 if the statement holds; unit in brackets; scope: every vertex):
  mono [(vertex, step)] (K1); k3c [(non-e vertex, state)], k3d [(e-vertex, state)] (K3); k4 [(gate, state)] (K4); k5 [(mover, successor,
  step)] (K5); l1sub [step: LAG grows], l1phi [step: (L1)'s stall / non-stall statement fails], phifall [step: Φ_(t+1) < Φ_t];
  l2 [state: FRONT holds a vertex (L2) excludes; game mode: an e-vertex]; l3 [state: neither (α) nor (β)], l3val [state: (α) or (β)
  holds but m_t is not the stated class]; l4 [stall: no cycle of the stall map inside FRONT]; c2 [run: (C2)'s identity fails]; c4 [run:
  T − b′ above its bound]; qfail [run: #Φ-intervals q > P]; plat [plateau: v − u above its bound]; p1, p2, p3, p4, p6, p7 (Addendum A,
  units as there); tcyc [run: T above ALL-TCYC's bound].
  Bounds. Genome mode: the text's (P = 2M(N + 2M); plateau N + 2M + 5; tail N; T ≤ P(N + 2M + 6) + N). Game mode (the lift's analogue,
  stated here, not L-NEW's): P := (m_CH + n)·n with m_CH = #edges of movers (m_t would be the class at b of a mover's successor or
  (c, ∅) for a vertex c; |FRONT| ≤ n); plateau n_E = #Even vertices; tail |CH|; T ≤ P(n_E + 1) + |CH|.
Descriptive: T, q (maximal intervals of constant Φ), phivals (distinct Φ), stalls, plateaus, platmax, bprime, tail.
For every counter the FIRST failure (smallest state, then smallest vertex) is kept with names.
Usage: lev43.py genome G.json ... | lev43.py lmcs NMIN NMAX | lev43.py switchall NMIN NMAX   (env FIRST=1 prints first failures)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [os.path.join(H, "..", "box37"), os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"),
                os.path.join(R, "experiments", "harness")]
import pg
from n5b import SpecSI

CTRL = os.environ.get("LV43_CTRL", "0")    # controls: 1 = FRONT := the HIGHEST lagging class (l3 / l4 must fire); 2 = plateau set Y := FRONT (p2 / p3 / p6 must fire)
WMODE = os.environ.get("WMODE", "esc")     # game mode: esc = W := the escapes; up = W := every vertex at least as relevant as the least relevant escape
KEYS = ("mono", "k3c", "k3d", "k4", "k5", "l1sub", "l1phi", "phifall", "l2", "l3", "l3val", "l4", "c2", "c4", "qfail", "plat",
        "p1", "p2", "p3", "p4", "p6", "p7", "tcyc")
DESC = ("T", "q", "phivals", "stalls", "plateaus", "platmax", "bprime", "tail")


# ---------------------------------------------------------------- histories
def genome_hist(G):
    import ideal37
    g, V, Hs = ideal37.run(G); n, N = g.n, G["N"]; M = sum(len(o) for o in G["opts"]); T = len(Hs) - 1
    kind = [None] * n; name = [None] * n
    for k, v in V.items(): kind[v] = k[0] if isinstance(k, tuple) else k; name[v] = str(k)
    mv = [V[("x", x)] for x in range(N)]; ms = set(mv)
    ok2 = [kind[v] in ("x", "g") or (kind[v] == "b" and g.succ[v][0] in ms and len(g.succ[v]) == 2) for v in range(n)]
    P = 2 * M * (N + 2 * M)
    return dict(n=n, owner=g.owner, succ=g.succ, prio=g.prio, name=name, T=T, val=[h[0] for h in Hs],
                nxt=[[h[2][v] if g.owner[v] == 0 else h[1][v] for v in range(n)] for h in Hs],
                W={v for v in range(n) if kind[v] == "e"}, CH=mv, okfront=ok2, dmov={v for v in range(n) if kind[v] == "e" and g.succ[v][0] in ms},
                bP=P, bplat=N + 2 * M + 5, btail=N, bT=P * (N + 2 * M + 6) + N, mode="genome")


def howard(g, start, cap=200000):
    """all Even vertices; ties: keep the current successor if it is among the best, else the largest index (ideal37's rule)"""
    si = SpecSI(g); st = list(start); Hs = []
    while True:
        val, ch = si.evaluate_choice(list(st)); Hs.append((val, ch, list(st)))
        new = list(st); changed = False
        for x in range(g.n):
            if g.owner[x] != 0: continue
            cur = st[x]; best = cur
            for y in g.succ[x]:
                c = si.nvo(val[y], val[best])
                if c > 0 or (c == 0 and best != cur and y > best): best = y
            if si.nvo(val[best], val[cur]) > 0: new[x] = best; changed = True
        if not changed or len(Hs) > cap: break
        st = new
    return Hs


def escapes(g):
    W = set()
    for v in range(g.n):
        if g.owner[v] == 1 and len(set(g.succ[v])) >= 2:
            ev = [w for w in set(g.succ[v]) if g.prio[w] % 2 == 0]
            if ev: W.add(max(ev, key=lambda w: (g.prio[w], w)))
    return W


def game_hist(g, start, names, W=None):
    Hs = howard(g, start); n, T = g.n, len(Hs) - 1
    CH = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]; nE = sum(1 for v in range(n) if g.owner[v] == 0)
    mch = sum(len(set(g.succ[v])) for v in CH); P = (mch + n) * n
    W = escapes(g) if W is None else W
    if WMODE == "up" and W:
        lo = min((g.prio[v], v) for v in W); W = {v for v in range(n) if (g.prio[v], v) >= lo}
    return dict(n=n, owner=g.owner, succ=g.succ, prio=g.prio, name=list(names), T=T, val=[h[0] for h in Hs],
                nxt=[[h[2][v] if g.owner[v] == 0 else (h[1][v] if h[1][v] != -1 else g.succ[v][0]) for v in range(n)] for h in Hs],
                W=W, CH=CH, okfront=[v not in W for v in range(n)], dmov=set(W), bP=P, bplat=nE, btail=len(CH), bT=P * (nE + 1) + len(CH),
                mode="game")


def lmcs(n):
    """G_n of Friedmann, arXiv 1106.0778 v2 (LMCS 7(3:19)), Table 4, as quoted in claude/l-lit docs/lit/T66-deep3-lower-bound-families.md
    §3 («t_1: player 0, 4n + 3, {s, r, c}; t_(i>1): 0, 4n + 2i + 1, {s, r, t_(i−1)}; a_i: 1, 4n + 2i + 2, {t_i}; c: 0, 8n + 4, {s, r};
    d_i: 0, 4i + 1, {s, e_i, r} ∪ {a_j | j < 2i + 1}; e_i: 1, 4i + 2, {d_i, h_i}; g_i: 0, 4i + 4, {f_i, k_i}; k_i: 0, 8n + 4i + 7, {x} ∪
    {g_j | i < j ≤ n}; f_i: 1, 8n + 4i + 9, {e_i}; h_i: 1, 8n + 4i + 10, {k_i}; s: 0, 8n + 6, {f_j | j ≤ n} ∪ {x}; r: 0, 8n + 8, {g_j |
    j ≤ n} ∪ {x}; x: 1, 1, {x}»; t_i and a_i for i ≤ 2n) and its start («ι(t_1) = c, ι(g_i) = k_i, ι(* ∈ {t_(i>1), c, d_i}) = r,
    ι(* ∈ {k_i, s, r}) = x»). My transcription; compared with L-LIT's function lmcs by xgame43.py."""
    V = []
    def add(nm, pl, pr, su): V.append((nm, pl, pr, su))
    add("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1): add("t%d" % i, 0, 4 * n + 2 * i + 1, ["s", "r", "t%d" % (i - 1)])
    for i in range(1, 2 * n + 1): add("a%d" % i, 1, 4 * n + 2 * i + 2, ["t%d" % i])
    add("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        add("d%d" % i, 0, 4 * i + 1, ["s", "e%d" % i, "r"] + ["a%d" % j for j in range(1, 2 * i + 1)])
        add("e%d" % i, 1, 4 * i + 2, ["d%d" % i, "h%d" % i])
        add("g%d" % i, 0, 4 * i + 4, ["f%d" % i, "k%d" % i])
        add("k%d" % i, 0, 8 * n + 4 * i + 7, ["x"] + ["g%d" % j for j in range(i + 1, n + 1)])
        add("f%d" % i, 1, 8 * n + 4 * i + 9, ["e%d" % i])
        add("h%d" % i, 1, 8 * n + 4 * i + 10, ["k%d" % i])
    add("s", 0, 8 * n + 6, ["f%d" % j for j in range(1, n + 1)] + ["x"])
    add("r", 0, 8 * n + 8, ["g%d" % j for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    V.sort(); names = [v[0] for v in V]; idx = {nm: i for i, nm in enumerate(names)}      # vertices indexed by sorted name, as L-LIT's lmcs
    assert len(V) == 10 * n + 4     # Fact 6.1. NOTE: priorities are NOT pairwise distinct in this table: g_n and a_1 both have 4n + 4
    g = pg.Game([v[2] for v in V], [v[1] for v in V], [sorted(idx[w] for w in v[3]) for v in V], names)
    iota = {"t1": "c", "c": "r", "s": "x", "r": "x"}
    for i in range(2, 2 * n + 1): iota["t%d" % i] = "r"
    for i in range(1, n + 1): iota["g%d" % i] = "k%d" % i; iota["d%d" % i] = "r"; iota["k%d" % i] = "x"
    return g, [-1 if g.owner[v] == 1 else idx[iota[names[v]]] for v in range(g.n)], names


def switchall(n):
    """PGSolver's switchallexp n (trunk experiments/hard-families/pgsolver_port.py), start = best reward (PGSolver stratimpralgs
    initial_strategy_by_best_reward as experiments/si/si.py states it: successor of largest reward, ties to the largest index if the
    reward is even, the smallest if odd)."""
    import pgsolver_port
    g = pg.parse(pgsolver_port.switchallexp(n))
    names = list(g.labels) if getattr(g, "labels", None) else [str(v) for v in range(g.n)]
    def key(w):
        r = g.prio[w] if g.prio[w] % 2 == 0 else -g.prio[w]; return (r, w if r % 2 == 0 else -w)
    return g, [-1 if g.owner[v] == 1 else max(g.succ[v], key=key) for v in range(g.n)], names


# ---------------------------------------------------------------- counters
def census(P):
    n, T, val, nxt, owner, succ, prio, W, CH = P["n"], P["T"], P["val"], P["nxt"], P["owner"], P["succ"], P["prio"], P["W"], P["CH"]
    rk = lambda v: (prio[v], v); rew = lambda v: prio[v] if prio[v] % 2 == 0 else -prio[v]
    # E as a number: + 2^i for the i-th least relevant vertex of W if it is even, − 2^i if it is odd (odd ones only in the lift WMODE=up).
    # For even W this is a bitmask, and the integer order is «the most relevant element of E Δ E′ lies in E′»; with odd elements it is
    # the VJ order on Π ∩ W (the most relevant differing element z decides: better iff z is in the set and even, or out of it and odd).
    bit = {v: (1 << i) * (1 if prio[v] % 2 == 0 else -1) for i, v in enumerate(sorted(W, key=rk))}
    cls = [[(rew(val[t][v][0]), sum(bit[u] for u in val[t][v][1] if u in bit)) for v in range(n)] for t in range(T + 1)]
    c = dict.fromkeys(KEYS, 0); first = {}; nm = P["name"]
    def fail(k, t, info, cnt=1):
        c[k] += cnt
        if k not in first: first[k] = (t, info)
    gates = [v for v in range(n) if owner[v] == 1 and len(set(succ[v])) >= 2]; chs = set(CH)
    for t in range(T + 1):
        ct = cls[t]
        for v in range(n):
            w = nxt[t][v]
            if v in W:
                if v in P["dmov"] and not (ct[v] == (ct[w][0], ct[w][1] + bit[v]) and v not in val[t][w][1] and ct[v] > ct[w]):
                    fail("k3d", t, "%s -> %s: class %s vs successor's %s" % (nm[v], nm[w], ct[v], ct[w]))
            elif ct[v] != ct[w]: fail("k3c", t, "%s -> %s: class %s vs successor's %s" % (nm[v], nm[w], ct[v], ct[w]))
        for g in gates:
            lo = min(ct[y] for y in succ[g])
            if ct[g] != lo: fail("k4", t, "gate %s: class %s, faces %s" % (nm[g], ct[g], [(nm[y], ct[y]) for y in succ[g]]))
        if t < T:
            c1 = cls[t + 1]
            for v in range(n):
                if c1[v] < ct[v]: fail("mono", t, "%s: %s -> %s" % (nm[v], ct[v], c1[v]))
            for x in CH:
                for y in succ[x]:
                    if c1[x] < ct[y]: fail("k5", t, "mover %s: class at t+1 %s < class at t of successor %s %s" % (nm[x], c1[x], nm[y], ct[y]))
    # LEVEL, reference b = T
    b = T; fin = cls[b]
    def front(t):
        lag = {v for v in range(n) if cls[t][v] != fin[v]}
        if not lag: return None
        m = (max if CTRL == "1" else min)(cls[t][v] for v in lag); return lag, m, {v for v in lag if cls[t][v] == m}
    def cyc_inside(F, s):
        state = {}
        for v0 in sorted(F):
            path = []; v = v0
            while v in F and v not in state: state[v] = 1; path.append(v); v = s(v)
            if v in F and state.get(v) == 1: return path[path.index(v):]
            for u in path: state[u] = 2
        return None
    fr = [front(t) for t in range(T + 1)]
    bprime = next(t for t in range(T + 1) if fr[t] is None)
    stalls = 0; phis = []; isstall = []
    for t in range(T):
        if fr[t] is None:
            if fr[t + 1] is not None: fail("l1sub", t, "LAG empty at t, non-empty at t+1")
            phis.append(None); isstall.append(False); continue
        lag, m, F = fr[t]; phi = (m, -len(F)); phis.append(phi)
        bad = [v for v in F if not P["okfront"][v]]
        if bad: fail("l2", t, "FRONT holds %s (m %s)" % ([nm[v] for v in sorted(bad)[:4]], m))
        alpha = [z for z in F if z in chs and nxt[t][z] not in lag]
        betac = cyc_inside(F, lambda v: nxt[t][v])
        if not alpha and betac is None: fail("l3", t, "m %s, |FRONT| %d: %s" % (m, len(F), [nm[v] for v in sorted(F)[:6]]))
        else:
            if alpha and any(fin[nxt[t][z]] != m for z in alpha): fail("l3val", t, "(α) mover %s: m %s vs class_b(successor) %s" % (nm[alpha[0]], m, fin[nxt[t][alpha[0]]]))
            if not alpha and m[1] != 0: fail("l3val", t, "(β) m %s is not (c, ∅)" % (m,))
        st = all(cls[t + 1][v] == cls[t][v] for v in F); isstall.append(st); stalls += st
        nx = fr[t + 1]
        if nx is not None and not nx[0] <= lag: fail("l1sub", t, "LAG_(t+1) not inside LAG_t: %s" % [nm[v] for v in sorted(nx[0] - lag)[:4]])
        if st:
            if nx is None or nx[2] != F or (nx[1], -len(nx[2])) != phi: fail("l1phi", t, "stall, but LAG/FRONT/Φ changes: Φ %s -> %s" % (phi, None if nx is None else (nx[1], -len(nx[2]))))
            s = lambda v: nxt[b][v] if v in chs else nxt[t][v]
            if cyc_inside(F, s) is None: fail("l4", t, "stall, no cycle of the stall map inside FRONT (|FRONT| %d, m %s): %s" % (len(F), m, [nm[v] for v in sorted(F)[:6]]))
        elif nx is not None:
            phi1 = (nx[1], -len(nx[2]))
            if not phi1 > phi: fail("l1phi", t, "not a stall, but Φ %s -> %s" % (phi, phi1))
        if nx is not None and (nx[1], -len(nx[2])) < phi: fail("phifall", t, "Φ %s -> %s" % (phi, (nx[1], -len(nx[2]))))
    # intervals of constant Φ on the states with LAG non-empty (a = 0)
    ivs = []; t = 0
    while t < T and phis[t] is not None:
        u = t
        while t + 1 < T and phis[t + 1] == phis[u]: t += 1
        ivs.append((u, t)); t += 1
    q = len(ivs); lagstates = sum(1 for p in phis if p is not None)
    if bprime != q + sum(v - u for u, v in ivs) or lagstates != bprime: fail("c2", bprime, "b′ %d, q %d, Σ(v − u) %d, states with LAG %d" % (bprime, q, sum(v - u for u, v in ivs), lagstates))
    if T - bprime > P["btail"]: fail("c4", bprime, "T − b′ = %d > %d" % (T - bprime, P["btail"]))
    if q > P["bP"]: fail("qfail", 0, "q %d > P %d" % (q, P["bP"]))
    if T > P["bT"]: fail("tcyc", 0, "T %d > %d" % (T, P["bT"]))
    platmax = 0; nplat = 0
    for u, v in ivs:
        if v == u: continue
        nplat += 1; platmax = max(platmax, v - u); m = phis[u][0]
        if v - u > P["bplat"]: fail("plat", u, "plateau [%d, %d] of %d steps > %d" % (u, v, v - u, P["bplat"]))
        Y = set(fr[u][2]) if CTRL == "2" else {x for x in range(n) if cls[u][x] <= m}
        for s in range(u, v + 1):
            for x in range(n):
                if (x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x]): fail("p1", s, "plateau [%d, %d], vertex %s: class %s (at u %s), m %s" % (u, v, nm[x], cls[s][x], cls[u][x], m))
                if x in Y and nxt[s][x] not in Y: fail("p2", s, "plateau [%d, %d], %s ∈ Y -> %s ∉ Y" % (u, v, nm[x], nm[nxt[s][x]]))
            for x in CH:
                if x in Y:
                    for y in succ[x]:
                        if cls[s][y] > cls[s][x]: fail("p3", s, "plateau [%d, %d], mover %s ∈ Y, successor %s of higher class" % (u, v, nm[x], nm[y]))
        for s in range(u, v):
            for g in gates:
                if g in Y and nxt[s][g] != nxt[s + 1][g]: fail("p4", s, "plateau [%d, %d], gate %s ∈ Y flips" % (u, v, nm[g]))
        for s in range(u, v + 1):
            if s < T and not any(nxt[s][x] != nxt[s + 1][x] for x in CH if x in Y): fail("p6", s, "plateau [%d, %d]: no mover of Y switches at step %d" % (u, v, s))
        if v - u > sum(1 for x in Y if owner[x] == 0): fail("p7", u, "plateau [%d, %d] longer than #Even vertices of Y" % (u, v))
    d = dict(T=T, q=q, phivals=len(set(p for p in phis if p is not None)), stalls=stalls, plateaus=nplat, platmax=platmax, bprime=bprime, tail=T - bprime)
    return c, d, first


def line(tag, P, c, d):
    return "%s %s n %d | %s | %s | bounds P %d plat %d tail %d T %d" % (tag, P["mode"], P["n"], " ".join("%s %d" % (k, c[k]) for k in KEYS),
           " ".join("%s %d" % (k, d[k]) for k in DESC), P["bP"], P["bplat"], P["btail"], P["bT"])


if __name__ == "__main__":
    a = sys.argv[1:]; FIRST = os.environ.get("FIRST") == "1"
    def show(tag, P):
        c, d, first = census(P); print(line(tag, P, c, d), flush=True)
        if FIRST:
            for k in KEYS:
                if k in first: print("   FIRST %s at state %d: %s" % (k, first[k][0], first[k][1]), flush=True)
    if a[0] == "genome":
        for fn in a[1:]:
            G = json.load(open(fn)); G = G.get("genome", G); show(os.path.basename(fn), genome_hist(G))
    else:
        mk = lmcs if a[0] == "lmcs" else switchall
        for N in range(int(a[1]), int(a[2]) + 1):
            g, st, names = mk(N); show("%s N %d" % (a[0], N), game_hist(g, st, names))
