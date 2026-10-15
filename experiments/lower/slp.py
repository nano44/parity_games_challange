#!/usr/bin/env python3
"""Straight-line symbolic programs (docs/lower/L1-statement.md, Def. 1.3) and their evaluation.

A program is a list of gates (tuples). Gate i refers to earlier gates by index.
  ('P', p)        base set P_p = {v : pr(v) = p}
  ('VE',)         V_E
  ('EMPTY',)      the empty set
  ('or', j, k)    X_j ∪ X_k
  ('and', j, k)   X_j ∩ X_k
  ('not', j)      V \\ X_j
  ('cpre', j)     Cpre_E(X_j) = {v ∈ V_E : E(v) ∩ X_j ≠ ∅} ∪ {v ∈ V_O : E(v) ⊆ X_j}
The output is the last gate. cost(prog) = number of 'cpre' gates; depth(prog) = nesting depth of 'cpre' gates.

Evaluation targets:
  eval_game(prog, g)        on a harness pg.Game (sets as int bitmasks over vertices); returns the final bitmask.
  eval_struct(prog, S)      on a Struct (any finite Kripke structure with owner/prio labels; numpy bool arrays).
Builders:
  buchi_unfold(n)           Lemma 2.3: n^2 Cpre gates for priorities {1,2}.
  anp_symmetric(n, d)       Transfer 2.4: ANP's ‖F‖_{U,V} with U = S_{n,h_mu}, V = S_{n,h_nu}, (d+1) Cpre gates per query.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))


def cost(prog):
    return sum(1 for g in prog if g[0] == "cpre")


def depth(prog):
    d = [0] * len(prog)
    for i, g in enumerate(prog):
        if g[0] in ("P", "VE", "EMPTY"):
            d[i] = 0
        elif g[0] == "not":
            d[i] = d[g[1]]
        elif g[0] in ("or", "and"):
            d[i] = max(d[g[1]], d[g[2]])
        elif g[0] == "cpre":
            d[i] = d[g[1]] + 1
        else:
            raise ValueError(g)
    return max(d) if d else 0


# ---------- evaluation on a pg.Game (bitmasks) ----------
def game_tables(g):
    """Per-game precomputation: succ bitmask per vertex, V_E mask, full mask, P_p masks."""
    succ = [0] * g.n
    for v in range(g.n):
        for w in g.succ[v]:
            succ[v] |= 1 << w
    ve = sum(1 << v for v in range(g.n) if g.owner[v] == 0)
    full = (1 << g.n) - 1
    P = {}
    for v in range(g.n):
        P[g.prio[v]] = P.get(g.prio[v], 0) | (1 << v)
    return succ, ve, full, P


def cpre_mask(X, succ, ve, full):
    out = 0
    for v in range(len(succ)):
        s = succ[v]
        if (ve >> v) & 1:
            if s & X:
                out |= 1 << v
        else:
            if s & X == s:
                out |= 1 << v
    return out


def eval_game(prog, g, tables=None):
    succ, ve, full, P = tables if tables is not None else game_tables(g)
    val = [0] * len(prog)
    for i, gate in enumerate(prog):
        k = gate[0]
        if k == "P":
            val[i] = P.get(gate[1], 0)
        elif k == "VE":
            val[i] = ve
        elif k == "EMPTY":
            val[i] = 0
        elif k == "or":
            val[i] = val[gate[1]] | val[gate[2]]
        elif k == "and":
            val[i] = val[gate[1]] & val[gate[2]]
        elif k == "not":
            val[i] = full & ~val[gate[1]]
        elif k == "cpre":
            val[i] = cpre_mask(val[gate[1]], succ, ve, full)
        else:
            raise ValueError(gate)
    return val[-1]


# ---------- evaluation on a Struct (numpy) ----------
class Struct:
    """Finite structure: N nodes, owner[i] in {0,1}, prio[i] int, successors as CSR (indptr, indices); every node has >= 1 successor."""

    def __init__(self, owner, prio, succ_lists):
        self.N = len(owner)
        self.owner = np.asarray(owner, dtype=np.int8)
        self.prio = np.asarray(prio, dtype=np.int16)
        lens = np.array([len(s) for s in succ_lists], dtype=np.int64)
        assert (lens >= 1).all(), "every node needs a successor"
        self.indptr = np.concatenate([[0], np.cumsum(lens)])
        self.indices = np.array([w for s in succ_lists for w in s], dtype=np.int64)
        self.is_even = self.owner == 0
        self.starts = self.indptr[:-1]

    def cpre(self, X):
        vals = X[self.indices]
        any_ = np.logical_or.reduceat(vals, self.starts)
        all_ = np.logical_and.reduceat(vals, self.starts)
        return np.where(self.is_even, any_, all_)


def eval_struct(prog, S, keep=False):
    val = [None] * len(prog)
    for i, gate in enumerate(prog):
        k = gate[0]
        if k == "P":
            val[i] = S.prio == gate[1]
        elif k == "VE":
            val[i] = S.is_even.copy()
        elif k == "EMPTY":
            val[i] = np.zeros(S.N, dtype=bool)
        elif k == "or":
            val[i] = val[gate[1]] | val[gate[2]]
        elif k == "and":
            val[i] = val[gate[1]] & val[gate[2]]
        elif k == "not":
            val[i] = ~val[gate[1]]
        elif k == "cpre":
            val[i] = S.cpre(val[gate[1]])
        else:
            raise ValueError(gate)
    return val if keep else val[-1]


# ---------- builders ----------
class Builder:
    def __init__(self):
        self.prog = []

    def add(self, gate):
        self.prog.append(gate)
        return len(self.prog) - 1

    def P(self, p): return self.add(("P", p))
    def VE(self): return self.add(("VE",))
    def empty(self): return self.add(("EMPTY",))
    def full(self): return self.add(("not", self.empty()))
    def or_(self, a, b): return self.add(("or", a, b))
    def and_(self, a, b): return self.add(("and", a, b))
    def not_(self, a): return self.add(("not", a))
    def cpre(self, a): return self.add(("cpre", a))


def buchi_unfold(n, inner=None, outer=None):
    """Lemma 2.3: Z_0 = V; Z_i = Y_n where Y_0 = ∅, Y_j = Cpre((P_2 ∩ Z_{i-1}) ∪ (P_1 ∩ Y_{j-1})). n*n Cpre gates."""
    inner = n if inner is None else inner
    outer = n if outer is None else outer
    b = Builder()
    p1, p2 = b.P(1), b.P(2)
    Z = b.full()
    for _ in range(outer):
        Y = b.empty()
        p2z = b.and_(p2, Z)
        for _ in range(inner):
            Y = b.cpre(b.or_(p2z, b.and_(p1, Y)))
        Z = Y
    return b.prog


def S_tree(n, h):
    """ANP Prop. 2.5 / p.9:5: S_{n,0} = S_{0,h} = <>, S_{n,h} = S_{n/2,h} . <S_{n,h-1}> . S_{n/2,h}. Trees as nested lists (leaf = [])."""
    if n == 0 or h == 0:
        return []
    side = S_tree(n // 2, h)
    return side + [S_tree(n, h - 1)] + side


def width(T):
    return 1 if not T else sum(width(c) for c in T)


def anp_symmetric(n, d, tree=S_tree):
    """ANP §3.1: value ‖(Θ, g, (0,1))‖_{U,V} with Θ = <θ_d, ..., θ_0>, θ_p = ν for even p, μ for odd p,
    g(x_0..x_d) = ∪_p (P_p ∩ Cpre_E(x_p)), U = tree(n, #μ), V = tree(n, #ν). Straight-line by construction.
    Variables are bound outermost first: case (2)/(3) instantiate the LAST free argument (x_d first)."""
    b = Builder()
    Pp = [b.P(p) for p in range(d + 1)]
    theta = ["nu" if p % 2 == 0 else "mu" for p in range(d, -1, -1)]  # Θ = <θ_d, ..., θ_0>
    h_mu, h_nu = theta.count("mu"), theta.count("nu")
    U, V = tree(n, h_mu), tree(n, h_nu)
    zero, one = b.empty(), b.full()
    queries = [0]

    def query(args):  # args: gate index per priority p = 0..d ; returns gate of g(args)
        queries[0] += 1
        acc = None
        for p in range(d + 1):
            t = b.and_(Pp[p], b.cpre(args[p]))
            acc = t if acc is None else b.or_(acc, t)
        return acc

    def value(k, inst, A, B, U, V):
        """‖(Θ[k:], g with x_{d-k+1..d} instantiated by inst (dict p -> gate), (A, B))‖_{U,V}; returns gate index."""
        if k == len(theta):
            q = query([inst[p] for p in range(d + 1)])
            return b.or_(A, b.and_(B, q))  # f_{A,B} = A + B * f
        p_var = d - k  # variable bound at this level
        if theta[k] == "nu":
            Bj = B
            for Vj in V:
                inst2 = dict(inst); inst2[p_var] = Bj
                Bj = value(k + 1, inst2, A, Bj, U, Vj)
            return Bj
        else:
            Aj = A
            for Uj in U:
                inst2 = dict(inst); inst2[p_var] = Aj
                Aj = value(k + 1, inst2, Aj, B, Uj, V)
            return Aj

    out = value(0, {}, zero, one, U, V)
    assert queries[0] == width(U) * width(V), (queries[0], width(U), width(V))
    b.prog.append(("or", out, out))  # output = last gate
    return b.prog


if __name__ == "__main__":
    for n in range(1, 6):
        p = buchi_unfold(n)
        print(f"buchi_unfold({n}): cost {cost(p)} depth {depth(p)}")
    for n, d in [(2, 2), (3, 2), (4, 2), (4, 3), (6, 4)]:
        p = anp_symmetric(n, d)
        print(f"anp_symmetric({n},{d}): cost {cost(p)} depth {depth(p)} gates {len(p)}")
