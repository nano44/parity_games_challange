"""Deterministic, exhaustive versions of shrink34.py's deletion moves (box 35 exact neighbourhood): all_deletions(G) yields every genome
obtained by ONE deletion: one option of a mover with >= 2 options, or one mover y with every assignment of y's in-pointing W-targets to
the other movers of y's level (one fixed choice for all of them per assignment: each such option independently, all combinations)."""
import itertools
from shrink34_core import normalise, unpack, size

def all_deletions(G):
    N = G["N"]
    for x in range(N):
        if len(G["opts"][x]) < 2: continue
        for k in range(len(G["opts"][x])):
            opts, gate, br, bp = unpack(G); del opts[x][k]; del gate[x][k]
            st = list(G["start"]); s = st[x]; st[x] = 0 if s == k else (s - 1 if s > k else s)
            yield normalise(N, list(G["lev"]), opts, gate, br, bp, st)
    lev = G["lev"]
    for y in range(N):
        if N == 1: continue
        same = [z for z in range(N) if z != y and lev[z] == lev[y]]
        ptr = [(x, i) for x in range(N) if x != y for i, o in enumerate(G["opts"][x]) if o[0] == y]
        if ptr and not same: continue
        for choice in itertools.product(same, repeat=len(ptr)) if ptr else [()]:
            opts, gate, br, bp = unpack(G)
            for (x, i), z in zip(ptr, choice): opts[x][i][0] = z
            for x in range(N):
                if x == y: continue
                for o in opts[x]:
                    if o[1] == y: o[1] = -1
            ren = lambda z: z if z < 0 else (z - 1 if z > y else z)
            opts2 = [[[ren(o[0]), ren(o[1]), o[2]] for o in opts[x]] for x in range(N) if x != y]
            gate2 = [gate[x] for x in range(N) if x != y]
            yield normalise(N - 1, [lev[x] for x in range(N) if x != y], opts2, gate2, br, bp, [G["start"][x] for x in range(N) if x != y])
