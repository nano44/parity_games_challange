#!/usr/bin/env python3
"""T-L2 step 2: case tree for "no k-gate program solves the core" (n = 4, two-player Büchi).
A k-gate program of depth k is a chain s_i = Cpre_E(f_i(P2, VE, s_1..s_{i-1})); the i-profile of v is (P2, VE, s_1..s_i)(v).
At level i the only freedom is which (i-1)-profiles of successors f_i accepts; distinct choices with the same s_i-vector on the
core are the same case. Pruning (sound): with r levels left, vertices u, u' with the same i-profile, the same owner and the
same set of successor classes after r-1 further such refinement rounds get the same profiles at every later level; if
W(u) != W(u') the case is dead (fooling pair). Prints the tree size per level and the dead leaves' fooling pairs.
Usage: prooftree.py core.json k [maxcases]"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153
from coremin import struct_only, load

stats = {}


def refine_check(prof, owner, succ, W, rounds):
    """Refine profile ids `rounds` times by (owner, set of successor ids); then return a W-mixed pair (u, u') or None."""
    cls = list(prof)
    for _ in range(rounds):
        sig = [(cls[v], owner[v], tuple(sorted(set(cls[w] for w in succ[v])))) for v in range(len(cls))]
        ids = {}
        new = [ids.setdefault(sg, len(ids)) for sg in sig]
        if len(ids) == len(set(cls)): break   # stable
        cls = new
    seen = {}
    for v, c in enumerate(cls):
        if c in seen:
            if W[seen[c]] != W[v]: return (seen[c], v)
        else: seen[c] = v
    return None


def realisable(prof, owner, succ, limit):
    """Enumerate realisable s-vectors at the next level: choose f on occurring successor profiles."""
    occ = sorted(set(prof[w] for v in range(len(prof)) for w in succ[v]))
    fvar = {p: i + 1 for i, p in enumerate(occ)}
    svar = {v: len(occ) + 1 + v for v in range(len(prof))}
    cl = []
    for v in range(len(prof)):
        fs = sorted(set(fvar[prof[w]] for w in succ[v]))
        if owner[v] == 0:   # Even: s = OR
            cl.append([-svar[v]] + fs)
            for f in fs: cl.append([svar[v], -f])
        else:               # Odd: s = AND
            cl.append([svar[v]] + [-f for f in fs])
            for f in fs: cl.append([-svar[v], f])
    solver = Cadical153(bootstrap_with=cl); out = []
    while solver.solve():
        m = set(l for l in solver.get_model() if l > 0)
        s = tuple(int(svar[v] in m) for v in range(len(prof)))
        fsel = tuple(p for p in occ if fvar[p] in m)
        out.append((s, fsel))
        solver.add_clause([(-svar[v] if s[v] else svar[v]) for v in range(len(prof))])
        if len(out) >= limit: break
    solver.delete()
    return out, len(occ)


def search(prof, owner, succ, W, level, k, limit, path, out):
    cases, nocc = realisable(prof, owner, succ, limit)
    stats.setdefault(level + 1, [0, 0, 0])
    stats[level + 1][0] += len(cases)
    for s, fsel in cases:
        ids = {}
        newprof = [ids.setdefault((prof[v], s[v]), len(ids)) for v in range(len(prof))]
        pair = refine_check(newprof, owner, succ, W, k - (level + 1))
        if pair is not None:
            stats[level + 1][1] += 1
            out.append((path + [fsel], level + 1, pair))
            continue
        if level + 1 == k:
            stats[level + 1][2] += 1
            out.append((path + [fsel], level + 1, "SURVIVES"))
            continue
        search(newprof, owner, succ, W, level + 1, k, limit, path + [fsel], out)


if __name__ == "__main__":
    core = load(sys.argv[1]) if not sys.argv[1].endswith("core3.json") else [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(sys.argv[1]))["games"]]
    k = int(sys.argv[2]); limit = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    S, W = struct_only(core)
    owner = [int(o) for o in S.owner]; p2 = [int(p == 2) for p in S.prio]
    succ = [[int(w) for w in S.indices[S.indptr[v]:S.indptr[v + 1]]] for v in range(S.N)]
    W = [bool(w) for w in W]
    prof0 = [p2[v] * 2 + (1 - owner[v]) for v in range(S.N)]
    print(f"core: {len(core)} games, {S.N} vertices; k = {k}")
    pair = refine_check(prof0, owner, succ, W, k)
    print("depth-k types separate W:", pair is None)
    t0 = time.time(); out = []
    search(prof0, owner, succ, W, 0, k, limit, [], out)
    print(f"[{time.time()-t0:.1f}s] tree: level -> (cases, dead, survivors):")
    for lv in sorted(stats): print(f"  level {lv}: {stats[lv]}")
    surv = [o for o in out if o[2] == "SURVIVES"]
    print(f"dead leaves: {len(out) - len(surv)}, surviving leaves: {len(surv)}")
    json.dump([{"path": [list(map(int, f)) for f in p], "level": lv, "pair": pr} for p, lv, pr in out], open(f"prooftree_k{k}.json", "w"))
