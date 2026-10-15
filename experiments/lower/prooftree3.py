#!/usr/bin/env python3
"""T-L2 step 2 (exact pruning): BFS over the realisable profile partitions of the core, level by level, deduplicated;
a partition at level i is LIVE iff the remaining k - i gates can still solve the core from it (exact, by SAT with the
profiles as base labels). Records the tree: live partitions per level and, for each dead partition, that it is dead.
Usage: prooftree3.py core.json k [out.json]"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from prooftree import realisable
from coremin import struct_only


def solvable_from(prof, owner, succ, W, r):
    """Can r more Cpre gates (any DAG over the profiles and the new gates) make W a function of the final profile?"""
    P = sorted(set(prof)); pid = {p: i for i, p in enumerate(P)}
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    t, s, y = {}, {}, {}
    for i in range(1, r + 2):
        for p in range(len(P)):
            for e in range(2 ** (i - 1)):
                t[(i, p, e)] = new()
    for i in range(1, r + 1):
        for c in range(len(prof)):
            s[(i, c)] = new(); y[(i, c)] = new()
    cl = []
    for c in range(len(prof)):
        p = pid[prof[c]]
        for i in range(1, r + 2):
            for e in range(2 ** (i - 1)):
                neg = []
                for j in range(1, i):
                    bit = (e >> (j - 1)) & 1
                    neg.append(-s[(j, c)] if bit else s[(j, c)])
                tv = t[(i, p, e)]
                if i <= r:
                    cl.append(neg + [-y[(i, c)], tv]); cl.append(neg + [y[(i, c)], -tv])
                else:
                    cl.append(neg + ([tv] if W[c] else [-tv]))
        for i in range(1, r + 1):
            ys = [y[(i, w)] for w in succ[c]]
            if owner[c] == 0:
                cl.append([-s[(i, c)]] + ys); [cl.append([s[(i, c)], -yr]) for yr in ys]
            else:
                cl.append([s[(i, c)]] + [-yr for yr in ys]); [cl.append([-s[(i, c)], yr]) for yr in ys]
    solver = Cadical153(bootstrap_with=cl); ok = solver.solve(); solver.delete(); return ok


if __name__ == "__main__":
    core = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(sys.argv[1]))["games"]]
    k = int(sys.argv[2]); fout = sys.argv[3] if len(sys.argv) > 3 else f"prooftree3_k{k}.json"
    S, W = struct_only(core)
    owner = [int(o) for o in S.owner]; p2 = [int(p == 2) for p in S.prio]
    succ = [[int(w) for w in S.indices[S.indptr[v]:S.indptr[v + 1]]] for v in range(S.N)]
    W = [bool(w) for w in W]
    prof0 = tuple(p2[v] * 2 + (1 - owner[v]) for v in range(S.N))
    print(f"core: {len(core)} games, {S.N} vertices; k = {k}", flush=True)
    t0 = time.time(); print(f"level 0: solvable with {k} gates: {solvable_from(prof0, owner, succ, W, k)} [{time.time()-t0:.1f}s]", flush=True)
    level = {prof0: None}; tree = {0: [{"prof": prof0, "parent": None, "f": None}]}
    for i in range(1, k + 1):
        t0 = time.time(); nxt = {}; dead = []; raw = 0
        for pi, prof in enumerate(level):
            cases, nocc = realisable(prof, owner, succ, 10 ** 7)
            raw += len(cases)
            for s, fsel in cases:
                ids = {}
                newprof = tuple(ids.setdefault((prof[v], s[v]), len(ids)) for v in range(len(prof)))
                if newprof in nxt or newprof in dead: continue
                if solvable_from(newprof, owner, succ, W, k - i): nxt[newprof] = (pi, fsel)
                else: dead.append(newprof)
        print(f"level {i}: {raw} realisable choices from {len(level)} partitions -> {len(nxt)} live, {len(dead)} dead (distinct partitions) [{time.time()-t0:.1f}s]", flush=True)
        tree[i] = [{"prof": p, "parent": v[0], "f": [int(x) for x in v[1]]} for p, v in nxt.items()]
        tree[f"dead{i}"] = len(dead)
        if not nxt:
            print(f"RESULT: no {k}-gate program solves the core (tree exhausted at level {i})"); break
        level = nxt
    json.dump({str(a): b for a, b in tree.items()}, open(fout, "w"))
