#!/usr/bin/env python3
"""T-L2 step 2 (BFS variant): level-by-level enumeration of the realisable profile partitions of the core, with
deduplication (only the partition into i-profiles matters for the future) and the sound pruning of prooftree.py.
Usage: prooftree2.py core.json k"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prooftree import refine_check, realisable
from coremin import struct_only

if __name__ == "__main__":
    core = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(sys.argv[1]))["games"]]
    k = int(sys.argv[2])
    S, W = struct_only(core)
    owner = [int(o) for o in S.owner]; p2 = [int(p == 2) for p in S.prio]
    succ = [[int(w) for w in S.indices[S.indptr[v]:S.indptr[v + 1]]] for v in range(S.N)]
    W = [bool(w) for w in W]
    prof0 = tuple(p2[v] * 2 + (1 - owner[v]) for v in range(S.N))
    print(f"core: {len(core)} games, {S.N} vertices; k = {k}; depth-k types separate W: {refine_check(prof0, owner, succ, W, k) is None}", flush=True)
    level = {prof0: None}
    for i in range(1, k + 1):
        t0 = time.time(); nxt = {}; dead = 0; raw = 0
        for prof in level:
            cases, nocc = realisable(prof, owner, succ, 10 ** 7)
            raw += len(cases)
            for s, fsel in cases:
                ids = {}
                newprof = tuple(ids.setdefault((prof[v], s[v]), len(ids)) for v in range(len(prof)))
                if newprof in nxt: continue
                pair = refine_check(newprof, owner, succ, W, k - i)
                if pair is not None: dead += 1; continue
                nxt[newprof] = (prof, fsel)
        print(f"level {i}: {raw} realisable choices from {len(level)} partitions -> {len(nxt)} new live partitions, {dead} dead [{time.time()-t0:.1f}s]", flush=True)
        if not nxt:
            print(f"RESULT: no {k}-gate program solves the core (tree exhausted at level {i})"); break
        level = nxt
    else:
        print(f"{len(level)} partitions survive all {k} levels: the pruning is too weak or the core is SAT")
