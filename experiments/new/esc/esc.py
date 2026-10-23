#!/usr/bin/env python3
"""N10a (box 19, docs/new/N10-screen.md §1): ACYC (level 0, s relaxed to [0,1]) plus ESCAPE cuts, by exact separation.
Query: "Even wins every vertex". Exact pseudocode in N10-screen.md §1(e).
U0 = V minus every vertex that lies on an even-max cycle of G (same SCC of G[pr <= p] as a vertex of even priority p, the SCC
containing a cycle). ESCAPE(U), for nonempty U subset of U0 closed under Odd successors (Odd v in U => succ(v) subset of U):
    sum_{v in U Even} sum_{u not in U} s_vu >= 1        (single-successor Even edges count as the constant 1).
Valid: if sigma keeps every Even vertex of U inside U, G_sigma[U] has out-degree >= 1, so it has a cycle, and every cycle of
G[U] is odd-max; Odd wins there. Separation: for each w in U0, a minimum s-t cut with w forced into U, vertices outside U0
forced out, infinite arcs v -> u for Odd v, capacity s_vu on Even arcs v -> u. Loop: LP, separate, add cuts, until none < 1."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sa"))
import numpy as np
import networkx as nx
from scipy.optimize import linprog
from sa import acyc


def sccs(nodes, succ):
    G = nx.DiGraph(); G.add_nodes_from(nodes)
    for v in nodes:
        for u in succ[v]:
            if u in nodes:
                G.add_edge(v, u)
    return [c for c in nx.strongly_connected_components(G)
            if len(c) > 1 or any(v in succ[v] for v in c)]


def u0(g):
    succ = [set(s) for s in g.succ]; B = set()
    for p in sorted({q for q in g.prio if q % 2 == 0}):
        low = {x for x in range(g.n) if g.prio[x] <= p}
        for c in sccs(low, succ):
            if any(g.prio[x] == p for x in c):
                B |= c
    return set(range(g.n)) - B


def u0_tau(g, tau):
    """U0 for a fixed Odd strategy tau: V minus vertices on an even-max cycle of G_tau (Odd v -> tau[v] only, Even all edges)."""
    succ = [set(s) if g.owner[v] == 0 else {tau[v]} for v, s in enumerate(g.succ)]
    B = set()
    for p in sorted({q for q in g.prio if q % 2 == 0}):
        low = {x for x in range(g.n) if g.prio[x] <= p}
        for c in sccs(low, succ):
            if any(g.prio[x] == p for x in c):
                B |= c
    return set(range(g.n)) - B


def families(g, taus=()):
    """ESC1: (U0, Odd closure = all successors). ESC-tau (N10b): (U0(tau), Odd closure = {tau(v)}) per given tau."""
    fam = [(u0(g), [sorted(set(s)) for s in g.succ])]
    for tau in taus:
        fam.append((u0_tau(g, tau), [sorted(set(s)) if g.owner[v] == 0 else [tau[v]] for v, s in enumerate(g.succ)]))
    return fam


def esc_feasible(g, max_iter=500, tol=1e-7, taus=(), return_s=False):
    """Return (feasible, n_cuts, iterations). taus: Odd strategies (dict v -> successor) for the ESC-tau families."""
    edges, cons = acyc(g)
    eidx = {e: i for i, e in enumerate(edges)}
    nE = len(edges)
    fvars = sorted({fv for _, _, _, bF in cons for fv in bF})
    fid = {fv: nE + i for i, fv in enumerate(fvars)}
    nv = nE + len(fvars) + 1  # one dummy column keeps the LP non-empty
    A_ub, b_ub, A_eq, b_eq = [], [], [], []
    for kind, c0, aS, bF in cons:
        row = np.zeros(nv)
        for e, a in aS.items():
            row[e] += a
        for fv, b in bF.items():
            row[fid[fv]] += b
        if kind == "eq":
            A_eq.append(row); b_eq.append(-c0)
        else:
            A_ub.append(-row); b_ub.append(c0)   # row.x + c0 >= 0
    fams = families(g, taus)
    succ = [sorted(set(s)) for s in g.succ]
    cuts = 0
    for it in range(max_iter):
        res = None
        for method in ("highs-ds", "highs-ipm", "highs"):
            res = linprog(np.zeros(nv), A_ub=np.array(A_ub) if A_ub else None, b_ub=b_ub or None,
                          A_eq=np.array(A_eq) if A_eq else None, b_eq=b_eq or None, bounds=[(None, None)] * nv, method=method)
            if res.status in (0, 2):
                break
        if res.status == 2:
            return (False, cuts, it + 1, None) if return_s else (False, cuts, it + 1)
        if res.status != 0:
            raise RuntimeError(f"LP status {res.status}")
        s = res.x[:nE]
        sval = lambda v, u: (s[eidx[(v, u)]] if (v, u) in eidx else 1.0)
        found = False
        for U0, clo in fams:
          for w in sorted(U0):
              H = nx.DiGraph(); S, T = "S", "T"
              H.add_edge(S, w, capacity=float("inf"))
              for v in range(g.n):
                  if v not in U0:
                      H.add_edge(v, T, capacity=float("inf"))
                  for u in (clo[v] if g.owner[v] == 1 else succ[v]):
                      if u == v:
                          continue
                      cap = float("inf") if g.owner[v] == 1 else max(0.0, float(sval(v, u)))
                      if H.has_edge(v, u):
                          H[v][u]["capacity"] += cap
                      else:
                          H.add_edge(v, u, capacity=cap)
              if not H.has_node(T):
                  H.add_node(T)
              try:
                  val, (side, _) = nx.minimum_cut(H, S, T)
              except nx.NetworkXUnbounded:
                  continue  # w cannot be in such a U (Odd-closure leaves U0)
              if val < 1 - 1e-6:
                  U = set(side) - {S}
                  row = np.zeros(nv); const = 0.0
                  for v in U:
                      if g.owner[v] == 0:
                          for u in succ[v]:
                              if u not in U:
                                  if (v, u) in eidx:
                                      row[eidx[(v, u)]] += 1.0
                                  else:
                                      const += 1.0
                  A_ub.append(-row); b_ub.append(const - 1.0)   # row.s + const >= 1
                  cuts += 1; found = True
        if not found:
            if return_s:
                return True, cuts, it + 1, {e: float(s[i]) for i, e in enumerate(edges)}
            return True, cuts, it + 1
    raise RuntimeError("cut loop did not converge")


if __name__ == "__main__":
    import pg, zielonka
    g = pg.read(sys.argv[1])
    print(esc_feasible(g), "truth:", all(w == 0 for w in zielonka.solve(g)))
