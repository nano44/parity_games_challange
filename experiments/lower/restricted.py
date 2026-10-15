#!/usr/bin/env python3
"""Restricted SAT searches on Q_n (same encoding as satsearch.py, plus structural constraints on the truth tables):
  window w : the argument of gate i depends only on P_2 and s_{i-w}..s_{i-1} (chain programs, L-LIT T7 §b);
  monotone : every argument and the output are monotone in all inputs (no complement; P_1 = ~P_2 still allowed? no: monotone in P_2 too).
Reports the minimum cost under each restriction, or '> kmax'.  Usage: restricted.py n kmax"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import build
from slp import eval_struct, cost, depth
import satsearch


def encode_restricted(q, nodes, k, window=None, monotone=False):
    solver, decode, ncl = satsearch.encode(q, nodes, k)
    # we need access to the table variables: re-derive their numbering (tables are allocated first in encode)
    tvar = {}
    v = 0
    for i in range(1, k + 2):
        for e in range(2 ** i):
            v += 1; tvar[(i, e)] = v
    extra = []
    for i in range(1, k + 2):
        nb = i  # bits: 0 = P2, j = s_j
        if window is not None and i <= k + 1:
            allowed = {0} | {j for j in range(max(1, i - window), i)}
            if i == k + 1:
                allowed = set(range(i))  # output may read everything
            for e in range(2 ** i):
                for j in range(nb):
                    if j not in allowed and not (e >> j) & 1:
                        extra.append([-tvar[(i, e)], tvar[(i, e | (1 << j))]])
                        extra.append([tvar[(i, e)], -tvar[(i, e | (1 << j))]])
        if monotone:
            for e in range(2 ** i):
                for j in range(nb):
                    if not (e >> j) & 1:
                        extra.append([-tvar[(i, e)], tvar[(i, e | (1 << j))]])
    for c in extra:
        solver.add_clause(c)
    return solver, decode, ncl + len(extra)


def solve_k(q, k, seed, **kw):
    nodes = set(seed)
    while True:
        solver, decode, ncl = encode_restricted(q, sorted(nodes), k, **kw)
        if not solver.solve():
            return None
        prog = satsearch.program_from_tables(decode(solver.get_model()), k)
        out = eval_struct(prog, q.S)
        bad = np.nonzero(out != q.W)[0]
        if len(bad) == 0:
            return prog
        add = set(int(b) for b in bad[:200]); stack = list(add)
        while stack:
            c = stack.pop()
            for r in q.S.indices[q.S.indptr[c]:q.S.indptr[c + 1]]:
                r = int(r)
                if r not in nodes and r not in add:
                    add.add(r); stack.append(r)
        nodes |= add


if __name__ == "__main__":
    n = int(sys.argv[1]); kmax = int(sys.argv[2])
    q = build(n, verbose=True)
    seed = [c for c in range(q.N) if q.size[c] <= min(q.n, 3)]
    for name, kw in [("window1", dict(window=1)), ("window2", dict(window=2)), ("monotone", dict(monotone=True)),
                     ("window2+monotone", dict(window=2, monotone=True))]:
        t0 = time.time(); res = None
        for k in range(0, kmax + 1):
            prog = solve_k(q, k, seed, **kw)
            if prog is not None:
                res = (k, prog); break
        if res:
            print(f"n={n} {name}: min cost {res[0]} (depth {depth(res[1])}) [{time.time()-t0:.1f}s]", flush=True)
            json.dump({"n": n, "restriction": name, "cost": res[0], "program": res[1]}, open(f"min_{name}_n{n}.json", "w"))
        else:
            print(f"n={n} {name}: > {kmax} [{time.time()-t0:.1f}s]", flush=True)
