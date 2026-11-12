#!/usr/bin/env python3
"""L-COMP box 44: (1) an INDEPENDENT Voege-Jurdzinski valuation of a parity game under an Even strategy and Odd's optimal counterstrategy,
written from the definition (no code of pgsolver_si / n5b / si.py): the value of v under a positional pair is (Λ, Π, k) with Λ the most
relevant vertex of the cycle of v's play, Π the vertices more relevant than Λ on the path from v before Λ, k the number of steps to Λ
(box 209 §1 [VJ] as used: «Λ(v) is the most relevant vertex of the cycle of v's play; Π(v) is the set of vertices on the path from v to
Λ(v), before Λ(v), that are more relevant than Λ(v); (VJ-1) if Λ ≠ Λ′, Ω ◁ Ω′ iff reward(Λ) < reward(Λ′); (VJ-2) if Λ = Λ′ and Π ≠ Π′,
with z the most relevant vertex of Π Δ Π′: Ω ◁ Ω′ iff (z ∈ Π′ and z even) or (z ∈ Π and z odd)»; third component, VJ00 §4.2 / Friedmann
arXiv 1106.0778 §3: for equal Λ and Π the SHORTER path is better for Even iff Λ is even). Relevance = (priority, index); reward(v) =
+relevance if the priority is even, −relevance if odd.
Odd's optimal counterstrategy: one-player strategy improvement for Odd from an arbitrary start (every Odd vertex moves to a successor of
⊴-least value, keeping its current one if that is least) until no Odd vertex has a strictly smaller successor; the values at that fixed
point are the pointwise minimum (VJ00: no improving switch <=> optimal). This is slower than PGSolver's evaluation and shares nothing
with it.
(2) howard(): Howard's rule on a game H from s0 (every Even vertex to a ⊴-best successor, keeping its current one if it is best, else
the LARGEST index among the best), values by n5b's SpecSI or by (1); tie events counted as L-SI box 104 §5.2 does («the (state, Even
vertex) pairs of that run at which the current successor is not best and two or more successors are best»)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
EVEN, ODD = 0, 1


def cmpval(g, a, b):
    """-1 if a ◁ b (b better for Even), 0 if equal, 1 if a ▷ b."""
    La, Pa, ka = a; Lb, Pb, kb = b
    if La != Lb:
        ra = (g.prio[La], La) if g.prio[La] % 2 == 0 else (-g.prio[La], -La)
        rb = (g.prio[Lb], Lb) if g.prio[Lb] % 2 == 0 else (-g.prio[Lb], -Lb)
        return -1 if ra < rb else 1
    if Pa != Pb:
        z = max(Pa ^ Pb, key=lambda u: (g.prio[u], u)); even = g.prio[z] % 2 == 0
        return (1 if even else -1) if z in Pa else (-1 if even else 1)
    if ka == kb: return 0
    if g.prio[La] % 2 == 0: return 1 if ka < kb else -1
    return 1 if ka > kb else -1


def playvalues(g, f):
    """Values of every vertex in the functional graph f (f[v] = the successor taken at v)."""
    n = g.n; val = [None] * n; rel = lambda u: (g.prio[u], u)
    state = [0] * n
    for v0 in range(n):
        if val[v0] is not None: continue
        path = []; v = v0
        while state[v] == 0: state[v] = 1; path.append(v); v = f[v]
        if state[v] == 1:                       # a new cycle, through v
            i = path.index(v); cyc = path[i:]; L = max(cyc, key=rel); j = cyc.index(L); m = len(cyc)
            for t, u in enumerate(cyc):         # steps from u to L along the cycle; no vertex of the cycle is above L
                val[u] = (L, frozenset(), (j - t) % m); state[u] = 2
            path = path[:i]
        for u in reversed(path):                # tree vertices: prepend u to the successor's path
            L, P, k = val[f[u]]
            val[u] = (L, P | {u} if rel(u) > rel(L) else P, k + 1); state[u] = 2
    return val


def evaluate(g, sigma):
    """(values, Odd's optimal counterstrategy) against the Even strategy sigma (sigma[v] for Even v; ignored elsewhere)."""
    n = g.n; f = [sigma[v] if g.owner[v] == EVEN else min(g.succ[v]) for v in range(n)]
    while True:
        val = playvalues(g, f); changed = False
        for v in range(n):
            if g.owner[v] != ODD: continue
            best = f[v]
            for w in sorted(set(g.succ[v])):
                if cmpval(g, val[w], val[best]) < 0: best = w
            if best != f[v]: f[v] = best; changed = True
        if not changed: return val, f


def howard(g, s0, valfn=None, ctrl=0, cap=10 ** 6):
    """Returns (states, T, ties, switches): states[t] = the Even strategy at state t (-1 at Odd vertices); T = len(states) - 1.
    valfn(g, s) -> list of values; default: n5b's SpecSI. ctrl 1: «best» := worst (a control)."""
    if valfn is None:
        from n5b import SpecSI
        si = SpecSI(g); valfn = lambda g_, s: si.evaluate(list(s))
    s = [s0[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]; states = [list(s)]; ties = sw = 0
    while True:
        val = valfn(g, s); new = list(s)
        for v in range(g.n):
            if g.owner[v] != EVEN: continue
            ws = sorted(set(g.succ[v])); top = ws[0]
            for w in ws[1:]:
                c = cmpval(g, val[w], val[top])
                if (c > 0) if not ctrl else (c < 0): top = w
            bests = [w for w in ws if cmpval(g, val[w], val[top]) == 0]
            if s[v] in bests: continue
            if len(bests) > 1: ties += 1
            new[v] = max(bests); sw += 1
        if new == s: return states, len(states) - 1, ties, sw
        s = new; states.append(list(s))
        if len(states) > cap: raise RuntimeError("howard cap")


def bestset(g, val, v):
    ws = sorted(set(g.succ[v])); top = ws[0]
    for w in ws[1:]:
        if cmpval(g, val[w], val[top]) > 0: top = w
    return [w for w in ws if cmpval(g, val[w], val[top]) == 0]
