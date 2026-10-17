#!/usr/bin/env python3
"""BFS over window-1 chain programs (gate i reads P2, VE, s_{i-1}) on a core: realisable partitions per level with
deduplication and the weak (refinement) pruning. Measures how big an enumerated chain-only proof would be.
Usage: chainbfs.py core.json k"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prooftree import refine_check
from levels import load_core
from coremin import struct_only

def realisable_w1(prof, last, owner, succ):
    """choices F over the 8 window profiles (P2, VE, s_{i-1}); returns distinct s-vectors."""
    keyv = [(prof[v] & 3) | (last[v] << 2) for v in range(len(prof))]   # prof&3 = (P2, VE) bits of the vertex itself
    out = {}
    for F in range(256):
        s = tuple((any((F >> keyv[w]) & 1 for w in succ[v]) if owner[v] == 0 else all((F >> keyv[w]) & 1 for w in succ[v])) for v in range(len(prof)))
        out.setdefault(s, F)
    return out

if __name__ == "__main__":
    core = load_core(sys.argv[1]); k = int(sys.argv[2])
    S, W = struct_only(core); owner=[int(o) for o in S.owner]; p2=[int(p==2) for p in S.prio]
    succ=[[int(w) for w in S.indices[S.indptr[v]:S.indptr[v+1]]] for v in range(S.N)]; W=[bool(w) for w in W]
    base = tuple(p2[v] | ((1 - owner[v]) << 1) for v in range(S.N))
    level = {base: tuple(0 for _ in range(S.N))}   # partition -> last s-vector
    for i in range(1, k + 1):
        t0 = time.time(); nxt = {}; dead = 0; raw = 0
        for prof, last in level.items():
            cases = realisable_w1(prof, last, owner, succ); raw += len(cases)
            for s in cases:
                ids = {}; newprof = tuple(ids.setdefault((prof[v], s[v]), len(ids)) for v in range(S.N))
                if newprof in nxt: continue
                if refine_check(newprof, owner, succ, W, k - i) is not None: dead += 1; continue
                nxt[newprof] = s
        print(f"level {i}: {raw} choices from {len(level)} -> {len(nxt)} live partitions, {dead} dead [{time.time()-t0:.1f}s]", flush=True)
        if not nxt: print("RESULT: no window-1 chain of", k, "gates solves the core"); break
        level = nxt
