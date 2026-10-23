#!/usr/bin/env python3
"""N9a (box 18, docs/new/N9-screen.md §1): Sherali-Adams level-k lift (SA+, see below) of the ACYC mixed 0-1 program for the query
"Even wins every vertex". Exact pseudocode in N9-screen.md §1(e).

ACYC(G): binary s_e for every edge e = (v, u) of an Even vertex v with >= 2 distinct successors, sum_u s_vu = 1 per such v
(single-successor Even edges and all Odd edges are always active). For every odd priority p, continuous f_p(x) in [0, n] for
every x with pr(x) <= p, and for every edge x -> y with pr(x), pr(y) <= p:
    f_p(x) - f_p(y) - [pr(x) = p] + M (1 - s_xy) >= 0      (M = n + 1; the M term only for variable edges).
Feasible iff Even wins every vertex (some positional sigma has no cycle whose max priority is odd).
SA_k: multiply every constraint (including 0 <= s <= 1 and 0 <= f <= n) by prod_{e in S} s_e prod_{e in T} (1 - s_e) for
disjoint S, T, |S| + |T| <= k; linearise s_e^2 = s_e, y_A = prod_{e in A} s_e (|A| <= k+1), q_{A,x} = y_A f(x) (|A| <= k).
Monomials y_A with two edges of the same Even vertex are set to 0 (SA derives this at level >= 1). Feasibility LP by HiGHS."""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def acyc(g):
    """Return (edges, cons, nf). edges: list of variable edges (v, u). cons: list of (const, {edge_idx: a}, {fvar: b}) meaning
    const + sum a s + sum b f >= 0, or ('eq', ...) for equalities. fvar = (p, x)."""
    n = g.n
    succ = [sorted(set(s)) for s in g.succ]
    edges, eidx = [], {}
    for v in range(n):
        if g.owner[v] == 0 and len(succ[v]) >= 2:
            for u in succ[v]:
                eidx[(v, u)] = len(edges); edges.append((v, u))
    cons = []
    for v in range(n):
        if g.owner[v] == 0 and len(succ[v]) >= 2:
            cons.append(("eq", -1.0, {eidx[(v, u)]: 1.0 for u in succ[v]}, {}))
    for e in range(len(edges)):
        cons.append(("ge", 0.0, {e: 1.0}, {}))
        cons.append(("ge", 1.0, {e: -1.0}, {}))
    M = n + 1.0
    for p in sorted({q for q in g.prio if q % 2 == 1}):
        low = [x for x in range(n) if g.prio[x] <= p]
        for x in low:
            cons.append(("ge", 0.0, {}, {(p, x): 1.0}))
            cons.append(("ge", float(n), {}, {(p, x): -1.0}))
        for x in low:
            for y in succ[x]:
                if g.prio[y] > p:
                    continue
                c = 1.0 if g.prio[x] == p else 0.0
                if (x, y) in eidx:
                    cons.append(("ge", -c + M, {eidx[(x, y)]: -M}, {(p, x): 1.0, (p, y): -1.0} if x != y else {}))
                else:
                    cons.append(("ge", -c, {}, {(p, x): 1.0, (p, y): -1.0} if x != y else {}))
    return edges, cons


def sa_feasible(g, k, return_x=False):
    edges, cons = acyc(g)
    owner_of = [v for (v, u) in edges]
    nE = len(edges)

    def ok(A):  # no two edges of one vertex
        vs = [owner_of[e] for e in A]
        return len(vs) == len(set(vs))

    deg = {}
    for v in owner_of:
        deg[v] = deg.get(v, 0) + 1
    deg2 = [deg[v] == 2 for v in owner_of]
    var = {}

    def vid(key):
        if key not in var:
            var[key] = len(var)
        return var[key]

    rows, cols, vals, rhs, kinds = [], [], [], [], []
    r = 0
    for size in range(k + 1):
        for ST in itertools.combinations(range(nE), size):
            for mask in range(1 << size):
                S = frozenset(ST[i] for i in range(size) if mask >> i & 1)
                T = [ST[i] for i in range(size) if not mask >> i & 1]
                # Pruning (equivalent LP): a multiplier with two edges of one vertex in S u T is 0 or equals a smaller
                # multiplier (sum_u s_vu = 1 is multiplied by every smaller multiplier); for an out-degree-2 vertex,
                # (1 - s_a) = s_b, so its edges appear in S only.
                if not ok(ST) or any(deg2[e] for e in T):
                    continue
                # multiplier = sum_{U subset T} (-1)^|U| y_{S cup U}
                mult = []
                for t in range(len(T) + 1):
                    for U in itertools.combinations(T, t):
                        A = S | frozenset(U)
                        if ok(A):
                            mult.append((A, (-1.0) ** t))
                for kind, c0, aS, bF in cons:
                    row = {}
                    const = 0.0
                    for A, sg in mult:
                        if c0:
                            if A:
                                key = ("y", A); row[key] = row.get(key, 0.0) + sg * c0
                            else:
                                const += sg * c0
                        for e, a in aS.items():
                            B = A | {e}
                            if not ok(B):
                                continue
                            key = ("y", B) if B else None
                            row[key] = row.get(key, 0.0) + sg * a
                        for fv, b in bF.items():
                            key = ("q", A, fv); row[key] = row.get(key, 0.0) + sg * b
                    row = {kk: vv for kk, vv in row.items() if abs(vv) > 1e-12}
                    if not row and abs(const) < 1e-12:
                        continue
                    for kk, vv in row.items():
                        rows.append(r); cols.append(vid(kk)); vals.append(vv)
                    rhs.append(-const); kinds.append(kind); r += 1
    # SA+ (N9-screen.md §1(e)): the choice equalities sum_u s_vu = 1 multiplied by q-monomials, i.e.
    # sum_u q_{A + vu, x} = q_{A, x} for |A| <= k - 1 (A without an edge of v). Valid for every integral point; it makes the
    # pruning above exact (without it, (1 - s_a) f and s_b f are different monomials).
    fvars = sorted({fv for _, _, _, bF in cons for fv in bF})
    byv = {}
    for e, v in enumerate(owner_of):
        byv.setdefault(v, []).append(e)
    for size in range(k):
        for A in itertools.combinations(range(nE), size):
            if not ok(A):
                continue
            A = frozenset(A)
            used = {owner_of[e] for e in A}
            for v, es in byv.items():
                if v in used:
                    continue
                for fv in fvars:
                    rows.append(r); cols.append(vid(("q", A, fv))); vals.append(-1.0)
                    for e in es:
                        rows.append(r); cols.append(vid(("q", A | {e}, fv))); vals.append(1.0)
                    rhs.append(0.0); kinds.append("eq"); r += 1
    if r == 0:
        return True
    nv = max(len(var), 1)
    A = coo_matrix((vals, (rows, cols)), shape=(r, nv)).tocsr()
    rhs = np.array(rhs)
    ge = np.array([kd == "ge" for kd in kinds]); eq = ~ge
    # row . x >= rhs  ->  -row . x <= -rhs
    for method in ("highs-ds", "highs-ipm", "highs"):  # retry on a HiGHS solve error (status 4)
        res = linprog(np.zeros(nv), A_ub=-A[ge] if ge.any() else None, b_ub=-rhs[ge] if ge.any() else None,
                      A_eq=A[eq] if eq.any() else None, b_eq=rhs[eq] if eq.any() else None,
                      bounds=[(None, None)] * nv, method=method)
        if res.status in (0, 2):
            break
    if res.status == 2:
        return (False, None) if return_x else False
    if res.status != 0:
        raise RuntimeError(f"LP status {res.status}: {res.message}")
    x = res.x
    viol = 0.0
    if ge.any():
        viol = max(viol, float(np.max(rhs[ge] - A[ge] @ x, initial=0.0)))
    if eq.any():
        viol = max(viol, float(np.max(np.abs(A[eq] @ x - rhs[eq]), initial=0.0)))
    if viol > 1e-6:
        raise RuntimeError(f"feasible point violates by {viol}")
    return (True, (var, x)) if return_x else True


def even_wins_all(g):
    import zielonka
    return all(w == 0 for w in zielonka.solve(g))


if __name__ == "__main__":
    import pg
    g = pg.read(sys.argv[1]); k = int(sys.argv[2])
    print(f"n={g.n} k={k} SA_feasible={sa_feasible(g, k)} even_wins_all={even_wins_all(g)}")
