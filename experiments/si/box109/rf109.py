#!/usr/bin/env python3
"""L-SI box 109: candidate S8 = RF (ROOT-FIRST strategy improvement). ONE implementation, as docs/si/box109-design.md §4 states it.

Input: a parity game G (max-parity, TARGET.md §1; PGSolver format). Valuations: SPEC S1 = L-SI's experiments/si/si.py Engine
(Voege-Jurdzinski; Engine.evaluate(sigma) = (Xi_sigma, sigma-bar), sigma-bar = Odd's optimal counterstrategy; Engine.improving =
SPEC S2's I_sigma). Start: SPEC S3 for Even (Engine.initial("best")), or a given Even strategy.
Loop (one ITERATION = one pass with I_sigma non-empty):
  1. (Xi_sigma, sigma-bar) := S1(sigma); I_sigma := S2. If I_sigma is empty: STOP.
  2. Imp := {v Even : v has an improving edge}; T(v) := {w : (v, w) in I_sigma}.
  3. PLAY GRAPH: nxt(x) := sigma(x) if x is Even's, sigma-bar(x) if x is Odd's. pi(x) := the set of vertices on the play
     x, nxt(x), nxt(nxt(x)), ... (path and cycle).
  4. DEPENDENCY: for v in Imp, D(v) := ( pi(sigma(v)) + union of pi(w), w in T(v) ) intersected with Imp, minus {v}.
     Delta := the digraph on Imp with an edge v -> u for every u in D(v).
  5. S := the union of the SINK strongly connected components of Delta (components with no edge to another component).
  6. For every v in S: sigma(v) := the w in T(v) maximising (Xi_sigma(w), w) (best valuation; ties: larger index). Others keep sigma.
Output (SPEC S5): Even wins v iff the cycle node of Xi_sigma(v) has even priority; Even's strategy sigma on Even's region, Odd's
strategy sigma-bar (to the FINAL sigma) on Odd's region.
Every iteration applies a non-empty set of improving switches, at most one per vertex (Delta has a sink component whenever Imp is
non-empty), so the run is a Voege-Jurdzinski strategy-improvement run: RESULTS R15 (a), (c) give termination, and the stop
condition I_sigma = empty is optimality of sigma (classical).

Usage: rf109.py GAME.pg [OUT.sol] [--cap K] [--trace]     prints: RF n .. iterations .. switches .. capped .. maxsink .. secs ..
  iterations  unit: loop passes with I_sigma non-empty        switches  unit: (vertex, iteration) pairs with a changed successor
  maxsink     the largest |S| of the run (|S| = |Imp| in every iteration would be Howard's rule)"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import pg
from si import Engine


def sccs(n, succ):
    """Tarjan, iterative. Returns (component id per vertex, number of components)."""
    index = [None] * n; low = [0] * n; onst = [False] * n; comp = [None] * n; st = []; c = 0; nc = 0
    for r in range(n):
        if index[r] is not None: continue
        work = [(r, 0)]
        while work:
            v, i = work.pop()
            if i == 0:
                index[v] = low[v] = c; c += 1; st.append(v); onst[v] = True
            rec = False
            for j in range(i, len(succ[v])):
                w = succ[v][j]
                if index[w] is None:
                    work.append((v, j + 1)); work.append((w, 0)); rec = True; break
                if onst[w]: low[v] = min(low[v], index[w])
            if rec: continue
            if low[v] == index[v]:
                while True:
                    w = st.pop(); onst[w] = False; comp[w] = nc
                    if w == v: break
                nc += 1
            if work:
                u = work[-1][0]; low[u] = min(low[u], low[v])
    return comp, nc


def rf_select(n, owner, E, sigma, vs, sbar, Is):
    """Steps 2-6 for the 'Even' player of engine E (owner[v] == 0). Returns {v: new successor} for v in S."""
    T = {}
    for v, w in Is: T.setdefault(v, []).append(w)
    L = sorted(T); idx = {v: i for i, v in enumerate(L)}
    nxt = [sigma[v] if owner[v] == 0 else sbar[v] for v in range(n)]
    mask = [None] * n                       # mask[x] = bit set of the vertices of Imp on pi(x)
    for x in range(n):
        if mask[x] is not None: continue
        path = []; pos = {}; y = x
        while mask[y] is None and y not in pos:
            pos[y] = len(path); path.append(y); y = nxt[y]
        if mask[y] is None:                 # a new cycle: every vertex of it sees the cycle's improvable vertices
            cyc = path[pos[y]:]; m = 0
            for c in cyc:
                if c in idx: m |= 1 << idx[c]
            for c in cyc: mask[c] = m
            rest = path[:pos[y]]; base = m
        else:
            rest = path; base = mask[y]
        for z in reversed(rest):
            if z in idx: base |= 1 << idx[z]
            mask[z] = base
    dep = []
    for v in L:
        m = mask[sigma[v]]
        for w in T[v]: m |= mask[w]
        m &= ~(1 << idx[v])
        dep.append([i for i in range(len(L)) if m >> i & 1])
    comp, nc = sccs(len(L), dep)
    sink = [True] * nc
    for i in range(len(L)):
        for j in dep[i]:
            if comp[j] != comp[i]: sink[comp[i]] = False
    return {L[i]: max(T[L[i]], key=lambda w: (E.key(vs[w]), w)) for i in range(len(L)) if sink[comp[i]]}


def run(g, cap=10 ** 7, start=None, trace=None):
    E = Engine(g); sigma = list(start) if start is not None else list(E.initial("best")); its = sw = mx = 0
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if not Is or its >= cap: break
        sel = rf_select(g.n, g.owner, E, sigma, vs, sbar, Is)
        assert sel and all(sigma[v] != w for v, w in sel.items())
        if trace is not None: trace.append((len({v for v, _ in Is}), sorted(sel.items())))
        for v, w in sel.items(): sigma[v] = w
        its += 1; sw += len(sel); mx = max(mx, len(sel))
    win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    strat = [sigma[v] if g.owner[v] == 0 else sbar[v] for v in range(g.n)]
    return dict(its=its, sw=sw, win=win, strat=strat, capped=int(bool(Is)), maxsink=mx, sigma=sigma)


if __name__ == "__main__":
    av = [a for a in sys.argv[1:] if not a.startswith("--")]; cap = 10 ** 7
    if "--cap" in sys.argv: cap = int(sys.argv[sys.argv.index("--cap") + 1]); av.remove(str(cap))
    g = pg.parse("".join(l for l in open(av[0]) if not l.lstrip().startswith("%"))); tr = [] if "--trace" in sys.argv else None
    t0 = time.time(); r = run(g, cap, trace=tr)
    if tr is not None:
        for i, (ni, sel) in enumerate(tr, 1): print(i, "improvable", ni, "switch", " ".join(f"{v}>{w}" for v, w in sel))
    if len(av) > 1:
        pg.write_sol(r["win"], av[1], [r["strat"][v] if r["win"][v] == g.owner[v] else None for v in range(g.n)])
    print(f"RF n {g.n} m {sum(len(set(s)) for s in g.succ)} iterations {r['its']} switches {r['sw']} capped {r['capped']} maxsink {r['maxsink']} secs {time.time() - t0:.2f}")
