#!/usr/bin/env python3
"""T-L2 step 1c: game-based minimal UNSAT core (k gates, n = 4, two-player Büchi): units are whole games
(representative games of the needed Q_3 classes from coremin2 + the 4-vertex games). Several deletion orders; smallest kept.
Usage: coremin3.py k core2.json out.json [orders]"""
import sys, os, time, json, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from quotient import build
from sat2 import encode2
from coremin import struct_only, load
from coremin2 import encode_sel


def canon(raw):
    return (tuple(raw[0]), tuple(raw[1]), tuple(tuple(x) for x in raw[2]))


def minimise(games, k, order, verbose=False):
    S, W = struct_only(games)
    unit_of = [g for g, raw in enumerate(games) for _ in raw[0]]
    a, cl = encode_sel(S, W, k, unit_of)
    solver = Cadical153(bootstrap_with=cl)
    ok = solver.solve(assumptions=[a[u] for u in range(len(games))]); assert not ok
    keep = set(u for u in range(len(games)) if a[u] in set(abs(l) for l in solver.get_core()))
    for u in order:
        if u not in keep: continue
        trial = [v for v in keep if v != u]
        ok = solver.solve(assumptions=[a[v] for v in trial])
        if not ok:
            core_u = set(abs(l) for l in solver.get_core()); keep = set(v for v in trial if a[v] in core_u)
    solver.delete()
    return sorted(keep)


if __name__ == "__main__":
    k = int(sys.argv[1]); d = json.load(open(sys.argv[2])); fout = sys.argv[3]; norders = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    games4 = [canon(g) for g in d["games"]]
    small = sorted(set(canon(c[0]) for c in d["q3_classes"]), key=lambda r: (len(r[0]), r))
    games = games4 + small
    print(f"units: {len(games4)} four-vertex games + {len(small)} representative small games", flush=True)
    best = None
    for o in range(norders):
        rng = random.Random(o)
        order = list(range(len(games)))
        if o == 0: order = list(range(len(games4))) + list(range(len(games4), len(games)))[::-1]   # drop big games first, then small ones largest-first
        elif o == 1: order = list(range(len(games)))[::-1]
        else: rng.shuffle(order)
        t0 = time.time(); keep = minimise(games, k, order)
        sizes = [len(games[u][0]) for u in keep]
        print(f"order {o}: {len(keep)} games, {sum(sizes)} vertices, by size {dict((s, sizes.count(s)) for s in sorted(set(sizes)))} [{time.time()-t0:.1f}s]", flush=True)
        if best is None or (sum(sizes), len(keep)) < best[0]:
            best = ((sum(sizes), len(keep)), keep)
    keep = best[1]; core = [games[u] for u in keep]
    S, W = struct_only(core); solver, decode, ncl = encode2(S, W, list(range(S.N)), k)
    ok = solver.solve(); print(f"fresh verification: {len(core)} games, {S.N} nodes, {ncl} clauses -> {'SAT (BUG)' if ok else 'UNSAT (confirmed)'}")
    json.dump({"k": k, "n": 4, "games": core, "note": "successor-closed set of whole games; UNSAT at k gates => B_2(4) > k"}, open(fout, "w"))
