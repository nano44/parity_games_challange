#!/usr/bin/env python3
"""Find a window-1 chain program of k gates on a 4-vertex class (as sat_shape.py) and print it as modal formulas over
P2, VE and s_{i-1}; the output as a minimised DNF over (P2, VE, s_1..s_k). Usage: chainshow.py mask p2masks k"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from sat_shape import class_games, shape_reads
from coremin import struct_only
from show import minimise


def encode_chain_tables(S, W, k):
    lab2 = S.prio == 2; labE = S.owner == 0
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    t, s, y = {}, {}, {}
    for i in range(1, k + 1):
        for e in range(8): t[(i, e)] = new()
    for e in range(2 ** (k + 2)): t[(k + 1, e)] = new()
    for i in range(1, k + 1):
        for c in range(S.N): s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in range(S.N):
        base = (1 if lab2[c] else 0) | (2 if labE[c] else 0)
        for i in range(1, k + 1):
            for b in (0, 1):
                e = base | (b << 2); neg = [] if i == 1 else [(-s[(i - 1, c)] if b else s[(i - 1, c)])]
                if i == 1 and b == 1: continue
                cl.append(neg + [-y[(i, c)], t[(i, e)]]); cl.append(neg + [y[(i, c)], -t[(i, e)]])
        for e in range(2 ** (k + 2)):
            if (e & 3) != base: continue
            neg = [(-s[(j, c)] if (e >> (j + 1)) & 1 else s[(j, c)]) for j in range(1, k + 1)]
            cl.append(neg + ([t[(k + 1, e)]] if W[c] else [-t[(k + 1, e)]]))
        for i in range(1, k + 1):
            succ = [int(r) for r in S.indices[S.indptr[c]:S.indptr[c + 1]]]; ys = [y[(i, r)] for r in succ]
            if labE[c]: cl.append([-s[(i, c)]] + ys); [cl.append([s[(i, c)], -yr]) for yr in ys]
            else: cl.append([s[(i, c)]] + [-yr for yr in ys]); [cl.append([-s[(i, c)], yr]) for yr in ys]
    solver = Cadical153(bootstrap_with=cl)
    def decode(m):
        m = set(v for v in m if v > 0)
        gates = [[int(t[(i, e)] in m) for e in range(8)] for i in range(1, k + 1)]
        out = [int(t[(k + 1, e)] in m) for e in range(2 ** (k + 2))]
        return gates, out
    return solver, decode


def fmt_gate(tab, i):
    names = ["P2", "VE", f"s{i-1}"]; keys = [0, 1, 2] if i > 1 else [0, 1]
    rows = {}
    for bits in itertools.product((0, 1), repeat=len(keys)):
        e = sum(b << kk for b, kk in zip(bits, keys)); rows[bits] = tab[e]
    return minimise(keys, rows, {0: "P2", 1: "VE", 2: f"s{i-1}"})


if __name__ == "__main__":
    mask = int(sys.argv[1]); p2masks = [int(m) for m in sys.argv[2].split(",")]; k = int(sys.argv[3])
    games = class_games(mask, p2masks); S, W = struct_only(games)
    solver, decode = encode_chain_tables(S, W, k); ok = solver.solve()
    print(f"class {len(games)} games, window-1 chain, k = {k}: {'SAT' if ok else 'UNSAT'}")
    if ok:
        gates, out = decode(solver.get_model())
        for i, tab in enumerate(gates, 1): print(f"  s{i} = Cpre( {fmt_gate(tab, i)} )")
        keys = list(range(k + 2)); names = {0: "P2", 1: "VE", **{j + 1: f"s{j}" for j in range(1, k + 1)}}
        rows = {bits: out[sum(b << kk for b, kk in zip(bits, keys))] for bits in itertools.product((0, 1), repeat=k + 2)}
        print("  out =", minimise(keys, rows, names))
