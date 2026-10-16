#!/usr/bin/env python3
"""Minimal set of (winning, losing) vertex pairs that no k-gate program can separate simultaneously on a given
successor-closed structure (the structure is fixed; only the output requirement is weakened to 'the k-profiles of u and u'
differ'). Usage: pairmin.py qcore.json k [orders]"""
import sys, os, json, time, random, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153


def encode_pairs(owner, prio, succ, k):
    N = len(owner); lab2 = [p == 2 for p in prio]; labE = [o == 0 for o in owner]
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    t, s, y = {}, {}, {}
    for i in range(1, k + 1):
        for e in range(2 ** (i + 1)): t[(i, e)] = new()
    for i in range(1, k + 1):
        for c in range(N): s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in range(N):
        base = (1 if lab2[c] else 0) | (2 if labE[c] else 0)
        for i in range(1, k + 1):
            for e in range(2 ** (i + 1)):
                if (e & 3) != base: continue
                neg = []
                for j in range(1, i):
                    bit = (e >> (j + 1)) & 1; neg.append(-s[(j, c)] if bit else s[(j, c)])
                cl.append(neg + [-y[(i, c)], t[(i, e)]]); cl.append(neg + [y[(i, c)], -t[(i, e)]])
        for i in range(1, k + 1):
            ys = [y[(i, r)] for r in succ[c]]
            if labE[c]:
                cl.append([-s[(i, c)]] + ys); [cl.append([s[(i, c)], -yr]) for yr in ys]
            else:
                cl.append([s[(i, c)]] + [-yr for yr in ys]); [cl.append([-s[(i, c)], yr]) for yr in ys]
    return cl, s, new


if __name__ == "__main__":
    d = json.load(open(sys.argv[1])); k = int(sys.argv[2]); norders = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    owner, prio, succ, W = d["owner"], d["prio"], d["succ"], d["W"]; N = len(owner)
    cl, s, new = encode_pairs(owner, prio, succ, k)
    pairs = [(u, u2) for u in range(N) for u2 in range(N) if W[u] and not W[u2] and prio[u] == prio[u2] and owner[u] == owner[u2]]
    a = {}
    for (u, u2) in pairs:
        a[(u, u2)] = new()
        # a -> OR_i (s_i(u) xor s_i(u2)); d_i <-> xor
        ds = []
        for i in range(1, k + 1):
            dv = new(); ds.append(dv)
            x, z = s[(i, u)], s[(i, u2)]
            cl.append([-dv, x, z]); cl.append([-dv, -x, -z])
        cl.append([-a[(u, u2)]] + ds)
    solver = Cadical153(bootstrap_with=cl)
    ok = solver.solve(assumptions=[a[p] for p in pairs]); print(f"{N} vertices, {len(pairs)} W-pairs, k = {k}: {'SAT' if ok else 'UNSAT'}", flush=True); assert not ok
    best = None
    for o in range(norders):
        keep = [p for p in pairs if a[p] in set(abs(l) for l in solver.get_core())] if o == 0 else list(best)
        order = list(keep); random.Random(o).shuffle(order)
        for p in order:
            if p not in keep: continue
            trial = [q for q in keep if q != p]
            if not solver.solve(assumptions=[a[q] for q in trial]):
                core_a = set(abs(l) for l in solver.get_core()); keep = [q for q in trial if a[q] in core_a]
        print(f"order {o}: {len(keep)} pairs", flush=True)
        if best is None or len(keep) < len(best): best = keep
    print("minimal pair set:", best)
    json.dump({"k": k, "pairs": best, "source": sys.argv[1]}, open(sys.argv[1].replace(".json", f"_pairs_k{k}.json"), "w"))
