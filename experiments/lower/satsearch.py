#!/usr/bin/env python3
"""Exact minimum number of Cpre gates for one-player Büchi on <= n vertices (B_1(n), L1-statement Def. 1.4), by SAT on
the bisimulation quotient Q_n (quotient.py). Unknowns for a program with k Cpre gates: for gate i (1..k) a truth table
t_i over the i input bits (P_2(q), s_1(q), ..., s_{i-1}(q)) giving the argument y_i(q) (this is exactly "any Boolean
combination of the base sets and earlier Cpre outputs", R4), s_i(q) = OR over successors r of y_i(r) (one-player: Cpre = Pre),
and an output truth table over (P_2, s_1..s_k) that must equal W. CEGAR: solve on a successor-closed subset of Q_n,
verify the decoded program on all of Q_n, add the classes where it fails, repeat. UNSAT on a subset is UNSAT on Q_n.
Usage: satsearch.py n [kmax]   -> prints B_1(n) with the witness program (also saved as JSON)."""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import build
from slp import eval_struct, cost, depth


def encode(q, nodes, k):
    """Return (solver, decode) for k gates on the node subset `nodes` (list of class ids, successor-closed)."""
    S, lab = q.S, (q.S.prio == 2)
    nodes = list(nodes)
    pos = {c: j for j, c in enumerate(nodes)}
    nv = [0]

    def new():
        nv[0] += 1
        return nv[0]
    s = {}   # (i, c) -> var for s_i(c)
    y = {}   # (i, c) -> var
    t = {}   # (i, e) -> var, e in range(2^i); i = k+1 is the output table
    cl = []
    for i in range(1, k + 2):
        for e in range(2 ** i):
            t[(i, e)] = new()
    for i in range(1, k + 1):
        for c in nodes:
            s[(i, c)] = new(); y[(i, c)] = new()

    def inputs(i, c):  # literals of the i input bits of node c for table i: bit0 = P_2(c), bit j = s_j(c)
        lits = [None] + [s[(j, c)] for j in range(1, i)]
        return lits  # None marks the constant label bit

    for c in nodes:
        for i in range(1, k + 2):
            target = y[(i, c)] if i <= k else None
            lits = inputs(i, c)
            lb = 1 if lab[c] else 0
            for e in range(2 ** i):
                if (e & 1) != lb:
                    continue  # table entries with the wrong label bit are irrelevant for this node
                # match(c, e) := AND_j (s_j(c) == bit_j(e)); clause: ¬match ∨ (target ↔ t[i,e])
                neg = []
                for j in range(1, i):
                    bit = (e >> j) & 1
                    neg.append(-lits[j] if bit else lits[j])
                tv = t[(i, e)]
                if i <= k:
                    cl.append(neg + [-target, tv]); cl.append(neg + [target, -tv])
                else:
                    cl.append(neg + ([tv] if q.W[c] else [-tv]))
    for i in range(1, k + 1):
        for c in nodes:
            succ = [int(r) for r in S.indices[S.indptr[c]:S.indptr[c + 1]]]
            ys = [y[(i, r)] for r in succ]
            cl.append([-s[(i, c)]] + ys)
            for yr in ys:
                cl.append([s[(i, c)], -yr])
    solver = Cadical153(bootstrap_with=cl)

    def decode(model):
        m = set(v for v in model if v > 0)
        tables = [[int(t[(i, e)] in m) for e in range(2 ** i)] for i in range(1, k + 2)]
        return tables
    return solver, decode, len(cl)


def program_from_tables(tables, k):
    """Build an slp program: gates P_2, then for each i the argument as a DNF over the inputs, Cpre, finally the output."""
    prog = [("P", 2), ("not", 0)]  # 0: P_2 ; 1: P_1 = complement (one-player Büchi, priorities {1,2})
    s_gate = {}
    empty = len(prog); prog.append(("EMPTY",))

    def lit_gate(j, bit):  # gate for literal: j = 0 label, else s_j
        base = 0 if j == 0 else s_gate[j]
        if bit:
            return base
        prog.append(("not", base)); return len(prog) - 1

    def table_gate(i, tab):
        acc = empty
        for e in range(2 ** i):
            if not tab[e]:
                continue
            term = None
            for j in range(i):
                g = lit_gate(j, (e >> j) & 1)
                if term is None:
                    term = g
                else:
                    prog.append(("and", term, g)); term = len(prog) - 1
            prog.append(("or", acc, term)); acc = len(prog) - 1
        return acc
    for i in range(1, k + 1):
        a = table_gate(i, tables[i - 1])
        prog.append(("cpre", a)); s_gate[i] = len(prog) - 1
    out = table_gate(k + 1, tables[k])
    prog.append(("or", out, out))
    return prog


def solve_k(q, k, seed_nodes, verbose=True):
    nodes = set(seed_nodes)
    rounds = 0
    while True:
        rounds += 1
        t0 = time.time()
        solver, decode, ncl = encode(q, sorted(nodes), k)
        ok = solver.solve()
        if verbose:
            print(f"  k={k} round {rounds}: subset {len(nodes)} classes, {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if not ok:
            return None
        prog = program_from_tables(decode(solver.get_model()), k)
        out = eval_struct(prog, q.S)
        bad = np.nonzero(out != q.W)[0]
        if len(bad) == 0:
            return prog
        # add failing classes and their successor closure
        add = set(int(b) for b in bad[:200])
        stack = list(add)
        while stack:
            c = stack.pop()
            for r in q.S.indices[q.S.indptr[c]:q.S.indptr[c + 1]]:
                r = int(r)
                if r not in nodes and r not in add:
                    add.add(r); stack.append(r)
        nodes |= add


def minimum(q, kmax=12, verbose=True):
    # seed: all classes realizable with <= min(n,3) vertices (small, successor-closed)
    seed = [c for c in range(q.N) if q.size[c] <= min(q.n, 3)]
    for k in range(0, kmax + 1):
        prog = solve_k(q, k, seed, verbose)
        if prog is not None:
            return k, prog
    return None, None


if __name__ == "__main__":
    n = int(sys.argv[1]); kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    q = build(n, verbose=True)
    k, prog = minimum(q, kmax)
    print(f"B_1({n}) = {k}; witness cost {cost(prog)} depth {depth(prog)} gates {len(prog)}")
    json.dump({"n": n, "B1": k, "program": prog}, open(f"min_b1_n{n}.json", "w"))
