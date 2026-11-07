#!/usr/bin/env python3
"""L-RED 54 R217: RESET gadget under E-DOM (d 2). A fuse (LEAP style, k taps) keeps bit B1 busy: B1 follows the newest activated tap
(each carries a higher tap e), then SETS (its SET gate: beta back to B1, escape e1 -> sink). Lower bit B0: SET0 (escape e0) or ACC1
(a level-1 access mover whose copy gate of B1: beta -> B1, escape e1' -> sink). e-order (E-DOM respected; no odd penalty anywhere):
taps < e_top < e0 < e1' < e1. Prediction: B0 sets at step 1 (no premature access: B1's hidden route carries at most e_top < e0) and
RESETS (B0 -> ACC1) exactly one step after B1 sets. Usage: rsg.py k OUT.json"""
import sys, json
from gdsl import Gen
def build(k):
    g = Gen(); L = k
    c = [g.mv(f"c{i}", 0) for i in range(L)]; TOP = g.mv("TOP", 1); s = g.mv("s", 0)
    T = [g.mv(f"T{j}", 1) for j in range(k)]; B1 = g.mv("B1", 1); B0 = g.mv("B0", 1); A1 = g.mv("A1", 1); D = g.mv("DUMMY", 0)
    g.opt(s, None, None, (0, "sink"), 1); g.opt(D, None, D, (9, "dummy"), 0)
    for i in range(L):
        g.opt(c[i], None, None, (1, "exit", i), 1)
        g.opt(c[i], None, c[i + 1] if i + 1 < L else TOP, (8, "chain", i), 1)
    g.opt(TOP, s, TOP, (6, "top"), 0, gkey=(5, 0))
    for j in range(k): g.opt(T[j], c[L - 1 - j], T[j], (6, "tap", j), 0, gkey=(4, j))
    for j in range(k): g.opt(B1, D, T[j], (2, "b1tap", j), 0, gkey=(0, j))      # B1's tap options (Odd never escapes: DUMMY)
    g.opt(B1, s, B1, (7, "set1"), 0, gkey=(9, 0))                                # SET1: escape e1 (top)
    g.opt(B0, s, B0, (7, "set0"), 0, gkey=(6, 0))                                # SET0: escape e0
    g.opt(B0, D, A1, (2, "acc"), 0, gkey=(0, 99))                                # ACC1 -> access mover
    g.opt(A1, s, B1, (7, "copy1"), 0, gkey=(8, 0))                               # copy gate of B1: beta -> B1, escape e1'
    G, ix = g.genome({"B0": 1}); return G, ix
if __name__ == "__main__":
    G, ix = build(int(sys.argv[1])); json.dump(G, open(sys.argv[2], "w")); json.dump(ix, open(sys.argv[2][:-5] + ".names.json", "w"))
