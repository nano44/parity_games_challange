#!/usr/bin/env python3
"""L-RED R199 OFFS: three-level stacks with UNIFORM late offsets. Base level 0 (u0 moves at B + 1 if NPER 2; at B + 1 and 2B + 1 if
NPER 3), level 1 prompt at every level-0 carry (and step 1), late at offset o1; level 2 prompt at every level-1 carry, late o2 after;
level 3 prompt at every level-2 carry, late o3 after (a late move is kept only if it falls strictly before the next carry of the level
below and within 1..L). Enumerates B, o1, o2, o3; keeps W-feasible targets (r199/build.py) with 3 doubling levels in the weak sense
F_l >= 2F_(l-1) - c; writes them. Usage: offs.py nper Bmax c outdir"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build, schedof
NP, Bmax, c, od = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(od, exist_ok=True)
idx = []
for B in range(4, Bmax + 1):
    L = NP * B
    for o1 in range(1, B):
        for o2 in range(1, B):
            for o3 in range(1, 3):
                m = {0: {B + 1}, 1: ({2 * B + 1} if NP == 3 else set())}
                carries = sorted([1] + [B * i + 1 for i in range(1, NP)])   # level-0 carries plus a virtual one at step 1
                def level(l, cs, o):
                    pr, la = set(), set()
                    for i, cst in enumerate(cs):
                        nxt = cs[i + 1] if i + 1 < len(cs) else L + 1
                        pr.add(cst)
                        if cst + o < nxt and cst + o <= L: la.add(cst + o)
                    m[2 * l] = pr; m[2 * l + 1] = la
                    return sorted(pr | la)
                c1 = level(1, carries, o1); c2 = level(2, c1, o2); level(3, c2, o3)
                T = build.build(L, 4, m)
                if T["bad"]: continue
                F = T["F"]
                if not all(F[l] >= 2 * F[l - 1] - c for l in (1, 2, 3)): continue
                name = f"of_p{NP}_B{B}_{o1}_{o2}_{o3}"; json.dump(T, open(os.path.join(od, name + ".json"), "w")); idx.append((name, F, L))
print("OFFS nper", NP, "c", c, "targets", len(idx))
for n, F, L in idx: print(" ", n, "L", L, "F", F)
