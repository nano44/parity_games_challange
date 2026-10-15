#!/usr/bin/env python3
"""Backward analysis on a core: depth-j types of its vertices, the W-mixed pairs first separated at depth j (M_j), and
the last-gate constraint: F_6 subset of depth-5 types with Cpre_E(F_6) separating every pair of M_6 (all solutions)."""
import sys, os, json, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from coremin import struct_only


def load_core(f):
    return [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(f))["games"]]


def types(owner, p2, succ, k):
    """types[j][v] = canonical id of the depth-j type of v (ids consistent across vertices, not across levels)."""
    T = [[p2[v] * 2 + owner[v] for v in range(len(owner))]]
    for j in range(1, k + 1):
        ids = {}
        T.append([ids.setdefault((T[-1][v], tuple(sorted(set(T[-1][w] for w in succ[v])))), len(ids)) for v in range(len(owner))])
    return T


def mixed_pairs(T, W, j):
    """pairs (u, u') with same depth-(j-1) type, different depth-j type, different W; one pair per (type_{j}(u), type_j(u'))."""
    by = collections.defaultdict(list)
    for v in range(len(W)): by[T[j - 1][v]].append(v)
    pairs = {}
    for c, vs in by.items():
        for u in vs:
            for u2 in vs:
                if W[u] and not W[u2] and T[j][u] != T[j][u2]:
                    pairs.setdefault((T[j][u], T[j][u2]), (u, u2))
    return list(pairs.values())


def last_gate_solutions(T, owner, succ, W, pairs, j, limit=1000):
    """All F subset of depth-(j-1) types (occurring as successor types) such that Cpre_E(F) separates every pair."""
    occ = sorted(set(T[j - 1][w] for v in range(len(W)) for w in succ[v]))
    var = {t: i + 1 for i, t in enumerate(occ)}
    sv = {}
    cl = []
    def s_of(v):
        if v in sv: return sv[v]
        x = len(occ) + 1 + len(sv); sv[v] = x
        fs = sorted(set(var[T[j - 1][w]] for w in succ[v]))
        if owner[v] == 0:
            cl.append([-x] + fs); [cl.append([x, -f]) for f in fs]
        else:
            cl.append([x] + [-f for f in fs]); [cl.append([-x, f]) for f in fs]
        return x
    for u, u2 in pairs:
        a, b = s_of(u), s_of(u2); cl.append([a, b]); cl.append([-a, -b])
    solver = Cadical153(bootstrap_with=cl); sols = []
    while solver.solve() and len(sols) < limit:
        m = set(l for l in solver.get_model() if l > 0)
        F = tuple(t for t in occ if var[t] in m); sols.append(F)
        solver.add_clause([(-var[t] if var[t] in m else var[t]) for t in occ])
    return sols, occ


if __name__ == "__main__":
    core = load_core(sys.argv[1]); k = int(sys.argv[2])
    S, W = struct_only(core)
    owner = [int(o) for o in S.owner]; p2 = [int(p == 2) for p in S.prio]
    succ = [[int(w) for w in S.indices[S.indptr[v]:S.indptr[v + 1]]] for v in range(S.N)]; W = [bool(w) for w in W]
    T = types(owner, p2, succ, k)
    print("vertices:", S.N, "; distinct depth-j types for j = 0..k:", [len(set(t)) for t in T])
    for j in range(1, k + 1):
        P = mixed_pairs(T, W, j)
        print(f"M_{j}: {len(P)} type-pairs first separated at depth {j}")
    P = mixed_pairs(T, W, k)
    sols, occ = last_gate_solutions(T, owner, succ, W, P, k)
    print(f"last gate: {len(occ)} occurring depth-{k-1} successor types; F_{k} solutions: {len(sols)}")
    for F in sols[:20]: print("  F =", F)
