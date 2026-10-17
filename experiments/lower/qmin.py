#!/usr/bin/env python3
"""Smallest successor-closed UNSAT core in VERTICES: bisimulation quotient of a game list (class_exact.json or a core),
then assumption-based minimisation over quotient classes (closure a_c -> a_succ), several orders.
Usage: qmin.py games.json k out.json [orders]"""
import sys, os, json, time, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import refine
from slp import Struct
from sat2 import encode2
from coremin import struct_only
from coremin2 import encode_sel
from levels import load_core


def quotient(games):
    S, W = struct_only(games)
    cls, _ = refine(S, max(np.diff(S.indptr)))
    C = int(cls.max()) + 1
    first = np.full(C, S.N, dtype=np.int64); np.minimum.at(first, cls, np.arange(S.N))
    owner = S.owner[first]; prio = S.prio[first]
    succ = [sorted(set(int(cls[w]) for w in S.indices[S.indptr[f]:S.indptr[f + 1]])) for f in first]
    Wq = W[first]
    for v in range(S.N): assert W[v] == Wq[cls[v]]
    return Struct(owner, prio, succ), np.array(Wq, dtype=bool), cls, first


def minimise(S, W, k, order):
    a, cl = encode_sel(S, W, k, list(range(S.N)))
    for c in range(S.N):
        for r in S.indices[S.indptr[c]:S.indptr[c + 1]]: cl.append([-a[c], a[int(r)]])
    solver = Cadical153(bootstrap_with=cl)
    ok = solver.solve(assumptions=[a[u] for u in range(S.N)]); assert not ok
    keep = set(u for u in range(S.N) if a[u] in set(abs(l) for l in solver.get_core()))
    for u in order:
        if u not in keep: continue
        trial = [v for v in keep if v != u]
        if not solver.solve(assumptions=[a[v] for v in trial]):
            core_u = set(abs(l) for l in solver.get_core()); keep = set(v for v in trial if a[v] in core_u)
    solver.delete()
    # closure
    cls = set(keep); stack = list(cls)
    while stack:
        c = stack.pop()
        for r in S.indices[S.indptr[c]:S.indptr[c + 1]]:
            if int(r) not in cls: cls.add(int(r)); stack.append(int(r))
    return sorted(cls)


if __name__ == "__main__":
    games = load_core(sys.argv[1]); k = int(sys.argv[2]); fout = sys.argv[3]; norders = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    S, W, cls, first = quotient(games)
    print(f"{len(games)} games -> quotient with {S.N} classes", flush=True)
    best = None
    for o in range(norders):
        order = list(range(S.N))
        if o == 1: order = order[::-1]
        elif o >= 2: random.Random(o).shuffle(order)
        t0 = time.time(); keep = minimise(S, W, k, order)
        print(f"order {o}: {len(keep)} classes (closed) [{time.time()-t0:.1f}s]", flush=True)
        if best is None or len(keep) < len(best): best = keep
    remap = {c: i for i, c in enumerate(best)}
    owner = [int(S.owner[c]) for c in best]; prio = [int(S.prio[c]) for c in best]
    succ = [[remap[int(r)] for r in S.indices[S.indptr[c]:S.indptr[c + 1]]] for c in best]
    S2 = Struct(owner, prio, succ); W2 = np.array([W[c] for c in best], dtype=bool)
    solver, decode, ncl = encode2(S2, W2, list(range(S2.N)), k); ok = solver.solve()
    print(f"fresh verification: {S2.N} vertices, {ncl} clauses -> {'SAT (BUG)' if ok else 'UNSAT (confirmed)'}")
    json.dump({"k": k, "vertices": S2.N, "owner": owner, "prio": prio, "succ": succ, "W": [bool(w) for w in W2],
               "note": "successor-closed pointed structure (bisimulation classes); every vertex of a two-player Büchi game with <= 4 vertices"}, open(fout, "w"))
