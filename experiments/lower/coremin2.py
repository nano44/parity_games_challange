#!/usr/bin/env python3
"""T-L2 step 1b: assumption-based minimal UNSAT core for k gates, n=4 two-player Büchi.
Units: every class of Q_3 (successor-closed via hard implications a_c -> a_r) and every game of the 4-vertex core.
Output: <out>.json with the needed Q_3 classes (closed) and the needed 4-vertex games; verified UNSAT by a fresh solve."""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import build
from sat2 import Sub, encode2
from coremin import load, with_q3
from slp import Struct


def encode_sel(S, W, k, unit_of):
    """Like sat2.encode2 but every node clause carries -a[unit_of[c]]; closure a_c -> a_succ for Q3 classes is added by caller."""
    lab2 = S.prio == 2; labE = S.owner == 0
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    nunits = max(unit_of) + 1
    a = [new() for _ in range(nunits)]
    t, s, y = {}, {}, {}
    for i in range(1, k + 2):
        for e in range(2 ** (i + 1)):
            t[(i, e)] = new()
    for i in range(1, k + 1):
        for c in range(S.N):
            s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in range(S.N):
        sel = -a[unit_of[c]]
        base = (1 if lab2[c] else 0) | (2 if labE[c] else 0)
        for i in range(1, k + 2):
            for e in range(2 ** (i + 1)):
                if (e & 3) != base: continue
                neg = [sel]
                for j in range(1, i):
                    bit = (e >> (j + 1)) & 1
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
                cl.append([sel, -s[(i, c)]] + ys)
                for yr in ys: cl.append([sel, s[(i, c)], -yr])
            else:
                cl.append([sel, s[(i, c)]] + [-yr for yr in ys])
                for yr in ys: cl.append([sel, -s[(i, c)], yr])
    return a, cl


if __name__ == "__main__":
    k = int(sys.argv[1]); fin = sys.argv[2]; fout = sys.argv[3]
    q3 = build(3, owners_set=(0, 1), verbose=True)
    core = load(fin)
    S, W = with_q3(q3, core)
    # units: Q3 class c -> unit c; 4-vertex game g -> unit q3.N + g
    unit_of = list(range(q3.N)) + [q3.N + g for g in range(len(core)) for _ in range(4)]
    assert len(unit_of) == S.N
    a, cl = encode_sel(S, W, k, unit_of)
    # closure on Q3 classes
    for c in range(q3.N):
        for r in q3.S.indices[q3.S.indptr[c]:q3.S.indptr[c + 1]]:
            cl.append([-a[c], a[int(r)]])
    solver = Cadical153(bootstrap_with=cl)
    units = list(range(len(a)))
    t0 = time.time(); ok = solver.solve(assumptions=[a[u] for u in units])
    print(f"all units: {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True); assert not ok
    core_u = sorted(set(abs(l) for l in solver.get_core()))
    units = [u for u in units if a[u] in core_u]
    print(f"solver core: {len(units)} units ({sum(u < q3.N for u in units)} Q3 classes, {sum(u >= q3.N for u in units)} 4-vertex games)", flush=True)
    # greedy deletion, 4-vertex games first (they are the expensive part of the story), then classes
    order = [u for u in units if u >= q3.N] + [u for u in units if u < q3.N]
    keep = set(units)
    for u in order:
        if u not in keep: continue
        trial = [v for v in keep if v != u]
        t0 = time.time(); ok = solver.solve(assumptions=[a[v] for v in trial])
        if not ok:
            core_u = set(abs(l) for l in solver.get_core()); keep = set(v for v in trial if a[v] in core_u)
        print(f"unit {u} ({'game' if u >= q3.N else 'class'}): {'needed' if ok else 'dropped'} -> {len(keep)} units [{time.time()-t0:.1f}s]", flush=True)
    games = [core[u - q3.N] for u in sorted(keep) if u >= q3.N]
    # closure of kept classes
    cls = set(u for u in keep if u < q3.N); stack = list(cls)
    while stack:
        c = stack.pop()
        for r in q3.S.indices[q3.S.indptr[c]:q3.S.indptr[c + 1]]:
            if int(r) not in cls: cls.add(int(r)); stack.append(int(r))
    cls = sorted(cls)
    print(f"minimal core: {len(games)} 4-vertex games + {len(cls)} Q3 classes (closed)")
    # verification by a fresh solver on exactly this subset
    sub_nodes = cls + [q3.N + 4 * (u - q3.N) + v for u in sorted(keep) if u >= q3.N for v in range(4)]
    # rebuild a struct with only these nodes
    remap = {c: i for i, c in enumerate(sub_nodes)}
    owner = [S.owner[c] for c in sub_nodes]; prio = [S.prio[c] for c in sub_nodes]
    succ = [[remap[int(r)] for r in S.indices[S.indptr[c]:S.indptr[c + 1]]] for c in sub_nodes]
    S2 = Struct(owner, prio, succ); W2 = np.array([W[c] for c in sub_nodes], dtype=bool)
    solver2, decode, ncl = encode2(S2, W2, list(range(S2.N)), k)
    ok = solver2.solve(); print(f"fresh verification: {S2.N} nodes, {ncl} clauses -> {'SAT (BUG)' if ok else 'UNSAT (confirmed)'}")
    json.dump({"k": k, "games": games, "q3_classes": [[q3.rep[c][0], q3.rep[c][1]] for c in cls], "q3_class_ids": cls,
               "sizes": {"games": len(games), "classes": len(cls)}}, open(fout, "w"))
