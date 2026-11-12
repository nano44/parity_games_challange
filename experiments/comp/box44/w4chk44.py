#!/usr/bin/env python3
"""L-COMP box 44 item 1, beyond L-SI's six counters: the statements INSIDE Lemma WRAP (claude/l-si 26704e01 docs/si/box104-map.md §3) that
its proof rests on, measured on my builder (wrap44) and my engine (n5xi44), against H's own valuation (n5b SpecSI on H).
Quoted: (ii) «At every state of the N5′-xi run (and of the N5 run) from S3: τ = τ0 and Iτ = ∅.»
        (W4) «(a) σ̄(g) = pβ at every gate and σ̄(o) ≠ pe_o at every o ∈ V_O; (b) for v ∈ V, Ξσ(v) = (c, P, 6ℓ) where (c, P, ℓ) = Ω^H_s(v);
        (c) Ξσ(m_(v,w)) = (c, P, 6ℓ + 5) where (c, P, ℓ) = Ω^H_s(w)».
        (W1) «no pad, gate or valve is ever a cycle node or in a P-set».
Counters (must-0):
  tauch  [state, ALL states of the run, after the fallback too]: τ ≠ τ0;
  itau   [state, all states]: Iτ ≠ ∅;
  w4a    [(Odd vertex of W with two or more successors other than K2, state before the first fallback)]: Odd's reply, read off the values
         (a successor u with Ξσ(vertex) = ext(vertex, Ξσ(u))), can be pe (at a gate) or pe_o (at o ∈ V_O), or there is none;
         descriptive oddties [same unit]: two or more such successors (Odd's optimal reply is not unique; not a failure);
  w4b    [(vertex of H, state before the first fallback)]: Ξσ(v) ≠ (c, P, 6ℓ);
  w4c    [(pad m_(v,w), state before the first fallback)]: Ξσ(m) ≠ (c, P, 6ℓ + 5);
  w1     [(vertex of W, state before the first fallback)]: the cycle node of Ξσ, or an element of its P-set, is a pad, a gate or a valve.
Control W4CTRL=1: the factor 6 is replaced by 5 (w4b, w4c must fire where ℓ > 0).
Usage: w4chk44.py json RAND300.json | w4chk44.py fam switchall|lmcs|lmcst4 N   (env MODE=xi|spec) -> one line"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import wrap44, n5xi44, wchk44
from wchk44 import pg, SpecSI
EVEN, ODD = 0, 1
MODE = os.environ.get("MODE", "xi"); FAC = 5 if os.environ.get("W4CTRL") == "1" else 6
KEYS = ("tauch", "itau", "w4a", "w4b", "w4c", "w1"); DESC = ("oddties",)


def one(h, s0, c):
    g, V = wrap44.wrap(h, s0); n = h.n; siH = SpecSI(h)
    _, tau0 = wrap44.standard(h, s0, g, V)
    low = {v for k, v in V.items() if not (isinstance(k, tuple) and k[0] == "h") and k not in ("cW", "K0", "K1", "K2", "K3")}
    pes = {V[k] for k in V if isinstance(k, tuple) and k[0] in ("pe", "peo")}
    odds = [u for u in range(g.n) if g.owner[u] == ODD and len(g.succ[u]) > 1 and u != V["K2"]]
    mpad = [(V[("m", v, w)], w) for v in range(n) if h.owner[v] == EVEN for w in set(h.succ[v])]
    def hook(t, sigma, tau, vs, Is, It, F):
        if tau != tau0: c["tauch"] += 1
        if It: c["itau"] += 1
        if F > 0: return
        s = wrap44.hpart(h, sigma, V)
        if None in s: return
        vh = siH.evaluate(list(s))
        for v in range(n):
            L, P, k = vh[v]
            if (vs[v][0], vs[v][1], vs[v][2]) != (L, P, FAC * k): c["w4b"] += 1
        for m, w in mpad:
            L, P, k = vh[w]
            if (vs[m][0], vs[m][1], vs[m][2]) != (L, P, FAC * k + 5): c["w4c"] += 1
        for u in odds:
            L, P, k = vs[u]
            cands = [x for x in g.succ[u] if (vs[x][0], vs[x][1], vs[x][2]) == (L, P - {u}, k - 1)] if not (L == u and k == 0) else [x for x in g.succ[u] if vs[x][0] == u]
            if not cands or any(x in pes for x in cands): c["w4a"] += 1
            elif len(cands) > 1: c["oddties"] += 1
        for u in range(g.n):
            if vs[u][0] in low or any(x in low for x in vs[u][1]): c["w1"] += 1
    r = n5xi44.run(g, MODE, hook=hook)
    return r


if __name__ == "__main__":
    a = sys.argv[1:]; c = dict.fromkeys(KEYS + DESC, 0)
    if a[0] == "json":
        D = json.load(open(a[1])); it = 0
        for G in D["games"]:
            r = one(pg.Game(G["prio"], G["owner"], G["succ"]), G["s0"], c); it += r["Ttot"]
        print("W4CHK44 json %s games %d alg %s factor %d | %s | iterations (sum) %d" % (os.path.basename(a[1]), len(D["games"]), MODE, FAC, " ".join("%s %d" % (k, c[k]) for k in KEYS + DESC), it))
    else:
        fam, n = a[1], int(a[2])
        if fam == "switchall": h, s0 = wchk44.switchall(n)
        else: h, s0, _, _ = wchk44.lmcs(n, "table4" if fam == "lmcst4" else "fig4")
        r = one(h, s0, c)
        print("W4CHK44 fam %s n %d alg %s factor %d | %s | iterations %d fallbacks %d" % (fam, n, MODE, FAC, " ".join("%s %d" % (k, c[k]) for k in KEYS + DESC), r["Ttot"], r["F"]))
