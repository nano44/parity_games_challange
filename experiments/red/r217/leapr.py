#!/usr/bin/env python3
"""L-RED 54 R217: LEAP with self-triggered rounds (experimental). k taps per side, W rounds. Usage: leapr.py k W variant [out]"""
import sys, json
from gdsl import Gen
def build(k, W, var):
    g = Gen(); L = 2 * k
    c = [g.mv(f"c{i}", 0) for i in range(L)]; H = g.mv("H", 0); s = g.mv("s", 0)
    TOP = [g.mv(f"TOP{w}", 1) for w in range(W)]; Q = [g.mv(f"Q{w}", 0) for w in range(W)]
    T = [g.mv(f"T{j}", 1) for j in range(2 * k)]; Y = g.mv("Y", 0); X = g.mv("X", 0); Z = g.mv("Z", 1)
    g.opt(s, None, None, (0, "sink"), 1)
    g.opt(H, None, s, (1, "H", 0), 1)
    for i in range(L):
        g.opt(c[i], None, H, (2, "exit", i), 1)
        if i + 1 < L: g.opt(c[i], None, c[i + 1], (8, "chain", i), 1)
    for w in range(W):
        g.opt(c[L - 1], None, TOP[w], (3, "end", w), 0)
        g.opt(TOP[w], Q[w], TOP[w], (6, "top", w), 0, gkey=(3, w))
        g.opt(Q[w], None, s, (1, "Qs", w), 1)
        g.opt(Q[w], None, c[0], (7 if var == 0 else 5, "Qc", w), 0)
        if var >= 1: g.opt(H, None, TOP[w], (4, "HT", w), 0)
    for j in range(2 * k):
        g.opt(T[j], c[L - 1 - j], T[j], (5, "bit", j), 0, gkey=(2, j))
        g.opt(Y if j % 2 == 0 else X, None, T[j], (1, "tap", j), 0)
    g.opt(Z, Y, X, (1, "g"), 0, gkey=(1,))
    return g.genome()
if __name__ == "__main__":
    k, W, var = map(int, sys.argv[1:4]); G, ix = build(k, W, var)
    out = sys.argv[4] if len(sys.argv) > 4 else f"out/leapr_k{k}_W{W}_v{var}.json"; json.dump(G, open(out, "w")); print(out, "Z", ix["Z"])
