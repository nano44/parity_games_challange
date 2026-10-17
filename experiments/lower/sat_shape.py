#!/usr/bin/env python3
"""Exact SAT on ALL games of a small 4-vertex class (owner mask, P_2 masks, FILTER as in cegar_owner.py) with a prescribed
READING SHAPE: gate i may read P_2, V_E and the gates in reads[i]. Shapes: 'full' (every earlier gate), 'chain' (only
s_{i-1}), 'chain+j' (a 6-chain s_1..s_6 plus an extra gate x at level j reading s_{j-1} (and earlier chain gates); chain
gates at levels >= j may read x as well). Usage: sat_shape.py mask p2masks shape [k]   (FILTER env as in cegar_owner.py)"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
import vec2
from coremin import struct_only


def class_games(mask, p2masks):
    S4, ve4, p24 = vec2.all_games(4); keep = (ve4 == mask) & np.isin(p24, p2masks)
    if os.environ.get("FILTER"):
        deg = lambda v: np.array([bin(int(x)).count("1") for x in S4[:, v]])
        loop = lambda v: ((S4[:, v] >> v) & 1).astype(bool)
        keep &= eval(os.environ["FILTER"])
    idx = np.nonzero(keep)[0]
    return [vec2.game_at(S4, ve4, p24, int(g), 4) for g in idx]


def encode_shape(S, W, k, reads):
    """reads[i] (i = 1..k) = sorted list of earlier gate indices gate i may read; the output reads everything."""
    lab2 = S.prio == 2; labE = S.owner == 0
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    t, s, y = {}, {}, {}
    rd = {i: list(reads[i]) for i in range(1, k + 1)}; rd[k + 1] = list(range(1, k + 1))
    for i in range(1, k + 2):
        for e in range(2 ** (len(rd[i]) + 2)):
            t[(i, e)] = new()
    for i in range(1, k + 1):
        for c in range(S.N):
            s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in range(S.N):
        base = (1 if lab2[c] else 0) | (2 if labE[c] else 0)
        for i in range(1, k + 2):
            for e in range(2 ** (len(rd[i]) + 2)):
                if (e & 3) != base: continue
                neg = []
                for pos, j in enumerate(rd[i]):
                    bit = (e >> (pos + 2)) & 1
                    neg.append(-s[(j, c)] if bit else s[(j, c)])
                tv = t[(i, e)]
                if i <= k:
                    cl.append(neg + [-y[(i, c)], tv]); cl.append(neg + [y[(i, c)], -tv])
                else:
                    cl.append(neg + ([tv] if W[c] else [-tv]))
        for i in range(1, k + 1):
            succ = [int(r) for r in S.indices[S.indptr[c]:S.indptr[c + 1]]]
            ys = [y[(i, r)] for r in succ]
            if labE[c]:
                cl.append([-s[(i, c)]] + ys); [cl.append([s[(i, c)], -yr]) for yr in ys]
            else:
                cl.append([s[(i, c)]] + [-yr for yr in ys]); [cl.append([-s[(i, c)], yr]) for yr in ys]
    return Cadical153(bootstrap_with=cl), len(cl)


def shape_reads(shape, k):
    if shape == "full": return {i: list(range(1, i)) for i in range(1, k + 1)}
    if shape == "chain": return {i: ([i - 1] if i > 1 else []) for i in range(1, k + 1)}
    if shape.startswith("chain+"):   # k = 7: gates 1..j-1 chain, gate j = extra x (reads chain gates < j), gates j+1..7 = chain levels j..6
        j = int(shape[6:]); assert k == 7
        reads = {}
        for i in range(1, j): reads[i] = list(range(1, i))          # chain gates may read all earlier chain gates (depth i)
        reads[j] = list(range(1, j))                                 # extra gate at level j
        for i in range(j + 1, 8): reads[i] = list(range(1, i))       # chain gates after it read everything earlier
        return reads
    if shape.startswith("wchain+"):  # window-1 chain plus extra gate at level j, chain gates may read x
        j = int(shape[7:]); assert k == 7
        reads = {}
        for i in range(1, j): reads[i] = [i - 1] if i > 1 else []
        reads[j] = [j - 1] if j > 1 else []
        for i in range(j + 1, 8): reads[i] = sorted(set([i - 1, j] + ([j - 1] if i == j + 1 else [])))
        return reads
    raise ValueError(shape)


if __name__ == "__main__":
    mask = int(sys.argv[1]); p2masks = [int(m) for m in sys.argv[2].split(",")]; shape = sys.argv[3]; k = int(sys.argv[4]) if len(sys.argv) > 4 else 7
    games = class_games(mask, p2masks); S, W = struct_only(games)
    reads = shape_reads(shape, k)
    t0 = time.time(); solver, ncl = encode_shape(S, W, k, reads); ok = solver.solve()
    print(f"class: {len(games)} games ({S.N} nodes); shape {shape}, k = {k}, reads {reads}: {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]")
