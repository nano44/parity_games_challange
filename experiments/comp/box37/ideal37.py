#!/usr/bin/env python3
"""L-COMP box 37 (Lead 09:25Z): MY IDEAL-CYC engine and the mover class height D_mov of L-NEW box 204 (claude/l-new 3a492186,
docs/new/N5-K1EQ-box204.md), written from TEXT:
  - Gamma(G): RESULTS R104 [DEF] as quoted in P-N5-QN §Scope (l-new 3a492186, docs/new/P-N5-QN.md l. 34-45): movers (Even, prio 0) ->
    gates (Odd, prio 1) -> {e_g, beta_g}; beta prio 6 + 2*br + bp, edges to the Xi-target and to u (u alone when the target is X); e even
    above every beta (Omega(e) = eb + 2i, i = position in (lev(owner), gate) order under [E-LEV], as own34.build), one edge to the
    W-target or to c_W; unused loop c_X prio 2; c_W top; K0 = u (Even, top + 2) -> {K1, K3}; K1 (Even, 5) -> {K0, K1}; K2 (Odd, 3) ->
    {K1, K2}; K3 (Even, top + 3) -> {K1, K2}. No Gamma3 pads (own34.build without pA, s, q, r, pe, pB, pb, m).
  - IDEAL-CYC(G): RESULTS R118 (a) «The game is Gamma(G) with every Even vertex that is not a mover frozen at its start successor. Odd is
    unrestricted (gates and K2).», start «sigma = the genome start at movers, beta -> its Xi-target (u when the target is X), K0 -> K3,
    K1 -> K1, K3 -> K2»; Howard steps at the movers (switch-best: every mover with a strictly better successor switches to its best).
    Values: VJ (Lambda, Pi, k) with Odd's optimal counterstrategy (n5b SpecSI.evaluate_choice), order = PGSolver port SI.nvo.
    MY TIE RULE (stated; not in the text): among equally best successors keep the current one if it is among them, else the larger index.
  - class_t(v) := (Lambda_t(v), E_t(v)), E_t(v) = e-vertices of Pi_t(v); D^tot(v) := the number of distinct classes of v over states
    0..T (P-N5-QN l. 71-72); D_mov := max over movers x of D^tot(x) (box 204 §0 Theorem EQ). Also D_face := max over gates of
    max(D^tot(e_g), D^tot(beta_g)), flips(g) := #{t >= 1 : sigma-bar_(t-1)(g) != sigma-bar_t(g)}.
Usage: ideal37.py G.json ...  -> T D_mov argmax-mover D_face maxflip (gate) Dminface."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg
from n5b import SpecSI
EVEN, ODD = 0, 1

def build(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; byg = sorted(O, key=lambda q: gate[q[0]][q[1]])
    V = {}; i = 0
    def add(key):
        nonlocal i; V[key] = i; i += 1
    for x in range(N): add(("x", x))
    for q in byg: add(("g", q))
    for q in O: add(("b", q))
    for q in byg: add(("e", q))
    add("cX"); add("cW")
    for j in range(4): add(("K", j))
    n = i; prio = [0] * n; own = [EVEN] * n; succ = [None] * n
    for q in O: prio[V[("b", q)]] = 6 + 2 * br[opts[q[0]][q[1]][2]] + bp[opts[q[0]][q[1]][2]]
    eb = max(prio[V[("b", q)]] for q in O) + 1; eb += eb % 2
    for j, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 * j
    prio[V["cX"]] = 2; top = max(prio) + 2; top += top % 2
    K = [V[("K", j)] for j in range(4)]
    prio[V["cW"]] = top; prio[K[0]] = top + 2; prio[K[1]] = 5; prio[K[2]] = 3; prio[K[3]] = top + 3; own[K[2]] = ODD
    st = [-1] * n
    for x in range(N): succ[V[("x", x)]] = [V[("g", (x, k))] for k in range(len(opts[x]))]; st[V[("x", x)]] = V[("g", (x, G["start"][x]))]
    for q in O:
        x, k = q; wt, xt, _ = opts[x][k]; g, b, e = V[("g", q)], V[("b", q)], V[("e", q)]
        own[g] = ODD; prio[g] = 1; succ[g] = [e, b]
        succ[b] = ([V[("x", xt)]] if xt >= 0 else []) + [K[0]]; st[b] = V[("x", xt)] if xt >= 0 else K[0]
        succ[e] = [V[("x", wt)] if wt >= 0 else V["cW"]]; st[e] = succ[e][0]
    succ[V["cX"]] = [V["cX"]]; succ[V["cW"]] = [V["cW"]]; st[V["cX"]] = V["cX"]; st[V["cW"]] = V["cW"]
    succ[K[0]] = [K[1], K[3]]; succ[K[1]] = [K[0], K[1]]; succ[K[2]] = [K[1], K[2]]; succ[K[3]] = [K[1], K[2]]
    st[K[0]] = K[3]; st[K[1]] = K[1]; st[K[3]] = K[2]
    return pg.Game(prio, own, [sorted(s) for s in succ]), V, st

def run(G, cap=20000):
    g, V, st = build(G); si = SpecSI(g); N = G["N"]; mv = [V[("x", x)] for x in range(N)]; H = []
    while True:
        val, ch = si.evaluate_choice(list(st)); H.append((val, ch, list(st)))
        new = list(st); changed = False
        for x in mv:
            cur = st[x]; best = cur
            for y in g.succ[x]:
                c = si.nvo(val[y], val[best])
                if c > 0 or (c == 0 and best != cur and y > best): best = y
            if si.nvo(val[best], val[cur]) > 0: new[x] = best; changed = True
        if not changed or len(H) > cap: break
        st = new
    return g, V, H

def heights(G, cap=20000):
    g, V, H = run(G, cap); T = len(H) - 1
    ev = {V[k] for k in V if isinstance(k, tuple) and k[0] == "e"}
    cl = lambda v, t: (H[t][0][v][0], frozenset(H[t][0][v][1] & ev))
    D = lambda v: len({cl(v, t) for t in range(T + 1)})
    dm = max(((D(V[("x", x)]), x) for x in range(G["N"])))
    gates = [k[1] for k in V if isinstance(k, tuple) and k[0] == "g"]
    df = dmin = 0; mf = (-1, (-1, -1))
    for q in gates:
        a, b, gv = V[("e", q)], V[("b", q)], V[("g", q)]; da, db = D(a), D(b); df = max(df, da, db); dmin = max(dmin, min(da, db))
        fl = sum(H[t - 1][1][gv] != H[t][1][gv] for t in range(1, T + 1)); mf = max(mf, (fl, q))
    return dict(T=T, Dmov=dm[0], Dmov_x=dm[1], Dface=df, Dminface=dmin, maxflip=mf[0], flipgate=list(mf[1]) if mf[1] else None,
                Dall={x: D(V[("x", x)]) for x in range(G["N"])})

if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); r = heights(G); r.pop("Dall")
        print(os.path.basename(f), "N+M", G["N"] + sum(map(len, G["opts"])), json.dumps(r), flush=True)
