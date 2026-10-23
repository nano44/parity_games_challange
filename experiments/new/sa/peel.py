#!/usr/bin/env python3
"""N9b (box 18, docs/new/N9-screen.md §2): LP-guided certified peeling. Exact pseudocode in N9-screen.md §2(e).
REGION(G) mixed 0-1 program: r_v (v in an Even dominion D), s_e for Even edges, f_p(x) in [0, n] for odd p, pr(x) <= p:
  Odd v:  r_v <= r_u (u in succ v);   Even v:  sum_u s_vu = r_v,  s_vu <= r_u;
  edge x -> y, pr(x), pr(y) <= p:  f_p(x) - f_p(y) >= [pr(x) = p] - M (1 - a_xy),  a_xy = s_xy (Even x) or r_x (Odd x);
  maximise sum_v r_v.  Its optimum is |W_E| (W_E is the largest Even dominion).
Round: solve the level-1 Sherali-Adams lift (multipliers 1, b, 1 - b for every binary b), sigma(v) = argmax_u s_vu
(ties: lowest index); certify: S = vertices where sigma wins in G (one-player solve), an Even dominion. Same on the dual game
for Odd. Remove the attractors of the certified dominions; repeat. STUCK if both certified sets are empty.
Sound by certification (every removed vertex is decided correctly); at most n rounds."""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import zielonka


def region_lp_sigma(prio, owner, succ, level=1):
    n = len(prio); M = n + 1.0
    bins = []  # ('r', v) or ('s', v, u)
    bid = {}
    for v in range(n):
        bid[("r", v)] = len(bins); bins.append(("r", v))
    for v in range(n):
        if owner[v] == 0:
            for u in succ[v]:
                bid[("s", v, u)] = len(bins); bins.append(("s", v, u))
    cons = []  # (kind, const, {bin: a}, {cont: b}) const + a.b + b.c (>= 0 | == 0)
    for i in range(len(bins)):
        cons.append(("ge", 0.0, {i: 1.0}, {})); cons.append(("ge", 1.0, {i: -1.0}, {}))
    for v in range(n):
        if owner[v] == 1:
            for u in succ[v]:
                if u != v:  # (a self-loop gives r_v <= r_v; a dict literal with one key twice would drop the +1)
                    cons.append(("ge", 0.0, {bid[("r", u)]: 1.0, bid[("r", v)]: -1.0}, {}))
        else:
            d = {bid[("s", v, u)]: 1.0 for u in succ[v]}; d[bid[("r", v)]] = -1.0
            cons.append(("eq", 0.0, d, {}))
            for u in succ[v]:
                cons.append(("ge", 0.0, {bid[("r", u)]: 1.0, bid[("s", v, u)]: -1.0}, {}))
    for p in sorted({q for q in prio if q % 2 == 1}):
        low = [x for x in range(n) if prio[x] <= p]
        for x in low:
            cons.append(("ge", 0.0, {}, {(p, x): 1.0})); cons.append(("ge", float(n), {}, {(p, x): -1.0}))
            for y in succ[x]:
                if prio[y] > p:
                    continue
                c = 1.0 if prio[x] == p else 0.0
                a = bid[("s", x, y)] if owner[x] == 0 else bid[("r", x)]
                cons.append(("ge", -c + M, {a: -M}, {(p, x): 1.0, (p, y): -1.0} if x != y else {}))
    var = {}
    vid = lambda key: var.setdefault(key, len(var))
    rows, cols, vals, rhs, kinds = [], [], [], [], []
    r = 0
    mults = [((), ())] + [((i,), ()) for i in range(len(bins))] + [((), (i,)) for i in range(len(bins))] if level >= 1 else [((), ())]
    for S, T in mults:
        terms = [(frozenset(S), 1.0)] + ([(frozenset(T), -1.0)] if T else [])
        if T:
            terms = [(frozenset(), 1.0), (frozenset(T), -1.0)]
        for kind, c0, aB, bC in cons:
            row, const = {}, 0.0
            for A, sg in terms:
                if c0:
                    if A:
                        row[("y", A)] = row.get(("y", A), 0.0) + sg * c0
                    else:
                        const += sg * c0
                for i, a in aB.items():
                    B = A | {i}
                    row[("y", B)] = row.get(("y", B), 0.0) + sg * a
                for cv, b in bC.items():
                    row[("q", A, cv)] = row.get(("q", A, cv), 0.0) + sg * b
            row = {k: v for k, v in row.items() if abs(v) > 1e-12}
            if not row:
                continue
            for k, v in row.items():
                rows.append(r); cols.append(vid(k)); vals.append(v)
            rhs.append(-const); kinds.append(kind); r += 1
    nv = len(var)
    A = coo_matrix((vals, (rows, cols)), shape=(r, nv)).tocsr(); rhs = np.array(rhs)
    ge = np.array([k == "ge" for k in kinds]); eq = ~ge
    obj = np.zeros(nv)
    for v in range(n):
        obj[vid(("y", frozenset([bid[("r", v)]])))] = -1.0 if ("y", frozenset([bid[("r", v)]])) in var else 0.0
    if len(obj) < len(var):
        obj = np.concatenate([obj, np.zeros(len(var) - len(obj))])
        A.resize((r, len(var)))
    for method in ("highs-ds", "highs-ipm", "highs"):
        res = linprog(obj, A_ub=-A[ge], b_ub=-rhs[ge], A_eq=A[eq] if eq.any() else None, b_eq=rhs[eq] if eq.any() else None,
                      bounds=[(None, None)] * len(var), method=method)
        if res.status == 0:
            break
    if res.status != 0:
        raise RuntimeError(f"LP status {res.status}")
    x = res.x
    val = lambda key: x[var[key]] if key in var else 0.0
    sigma = {}
    for v in range(n):
        if owner[v] == 0:
            sigma[v] = max(succ[v], key=lambda u: (val(("y", frozenset([bid[("s", v, u)]]))), -u))
    return sigma, -res.fun


def wins_with(prio, owner, succ, sigma):
    """Vertices from which Even's positional sigma wins (Odd one-player on G_sigma)."""
    n = len(prio)
    s = [[sigma[v]] if owner[v] == 0 else list(succ[v]) for v in range(n)]
    return set(range(n)) - zielonka._odd_wins_one_player(n, s, prio)


def attractor(owner, succ, alive, target, player):
    A = set(target); changed = True
    while changed:
        changed = False
        for v in alive - A:
            ss = [u for u in succ[v] if u in alive]
            if (owner[v] == player and any(u in A for u in ss)) or (owner[v] != player and all(u in A for u in ss)):
                A.add(v); changed = True
    return A


def peel(g, level=1):
    alive = set(range(g.n)); win = {}; rounds = 0
    while alive:
        rounds += 1
        keep = sorted(alive); ix = {v: i for i, v in enumerate(keep)}
        prio = [g.prio[v] for v in keep]; owner = [g.owner[v] for v in keep]
        succ = [sorted({ix[w] for w in g.succ[v] if w in ix}) for v in keep]
        progress = False
        for player in (0, 1):
            pr = prio if player == 0 else [p + 1 for p in prio]
            ow = owner if player == 0 else [1 - o for o in owner]
            sigma, _ = region_lp_sigma(pr, ow, succ, level)
            S = wins_with(pr, ow, succ, sigma)
            if S:
                Sg = {keep[i] for i in S}
                A = attractor(g.owner, [set(x) for x in g.succ], alive, Sg, player)
                for v in A:
                    win[v] = player
                alive -= A; progress = True
                break
        if not progress:
            return None, rounds, alive
    return [win[v] for v in range(g.n)], rounds, set()


if __name__ == "__main__":
    import pg
    g = pg.read(sys.argv[1])
    w, rounds, stuck = peel(g)
    if w is None:
        print(f"STUCK after {rounds} rounds, {len(stuck)} vertices left")
    else:
        print(f"solved in {rounds} rounds; agrees with Zielonka: {w == zielonka.solve(g)}")
