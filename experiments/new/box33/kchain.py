#!/usr/bin/env python3
"""Box 33: explicit K-chain family (docs/new/N5-K-box33.md §11). One phase of N5 from the canonical start with K - 1 wakes at
consecutive transitions, wake levels rising. Construction (U3, length-only band: top vertex T on o's W-cycle, every route passes T):
  ladder L_1 -> T, L_j -> L_{j-1}; o (Odd) -> {t_1 -> ... -> t_6 -> T, x}; T -> o; x (Even) -> {o, r}; r -> {r_long -> L_8, r_short -> bad -> T}.
  gadget i: y_i -> {A_i -> L_{a_i}, Z_i -> h_i -> p_i}; p_i -> {Q_i -> g_i -> L_{q_i}} (+ y_{i-1} for i >= 2).
  a_1 = 5, q_1 = 0; for i >= 2: a_i = D_{i-1} + 3, q_i = D_{i-1}, D_i = D_{i-1} + 4, D_1 = 6.
Ranks: ladder, low structural vertices, t's, o < x < g's and h's (g_i < h_{i-1}, h increasing) < bad < T.
Usage: kchain.py K out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg

def build(K):
    D = [None, 6]; a = [None, 5]; q = [None, 0]
    for i in range(2, K + 1): a.append(D[i - 1] + 3); q.append(D[i - 1]); D.append(D[i - 1] + 4)
    LAD = max(max(a[1:]), max(q[1:]), 8)
    names = []; succ = {}; own = {}
    def add(nm, s, o=0): names.append(nm); succ[nm] = s; own[nm] = o
    add("T", ["o"])
    for j in range(1, LAD + 1): add(f"L{j}", ["T" if j == 1 else f"L{j-1}"])
    add("o", ["t1", "x"], 1)
    for j in range(1, 7): add(f"t{j}", [f"t{j+1}" if j < 6 else "T"])
    add("x", ["o", "r"]); add("r", ["rl", "rs"]); add("rl", ["L8"]); add("rs", ["bad"]); add("bad", ["T"])
    for i in range(1, K + 1):
        add(f"y{i}", [f"A{i}", f"Z{i}"]); add(f"A{i}", [f"L{a[i]}"]); add(f"Z{i}", [f"h{i}"]); add(f"h{i}", [f"p{i}"])
        add(f"p{i}", [f"Q{i}"] + ([f"y{i-1}"] if i >= 2 else [])); add(f"Q{i}", [f"g{i}"]); add(f"g{i}", [f"L{q[i]}" if q[i] > 0 else "T"])
    # priorities: build a rank order (low to high) and give parities
    even = lambda p: p if p % 2 == 0 else p + 1
    order = []   # (name, parity) from lowest rank up
    for j in range(1, LAD + 1): order.append((f"L{j}", 0))
    for i in range(1, K + 1): order += [(f"A{i}", 0), (f"Z{i}", 1), (f"Q{i}", 0), (f"y{i}", 1), (f"p{i}", 0)]
    order += [("rl", 0), ("rs", 1), ("r", 1)]
    for j in range(1, 7): order.append((f"t{j}", 1))
    order += [("o", 0), ("x", 2 % 2), ("g1", 0)]
    for i in range(2, K + 1): order += [(f"g{i}", 0), (f"h{i-1}", 0)]
    order += [(f"h{K}", 0), ("bad", 1), ("T", 0)]
    assert sorted(nm for nm, _ in order) == sorted(names), set(names) ^ set(nm for nm, _ in order)
    prio = {}; p = 0
    for nm, par in order:
        while p % 2 != par: p += 1
        prio[nm] = p; p += 1
    idx = {nm: k for k, nm in enumerate(names)}
    g = pg.Game([prio[nm] for nm in names], [own[nm] for nm in names], [[idx[s] for s in succ[nm]] for nm in names])
    return g, names

if __name__ == "__main__":
    K = int(sys.argv[1]); g, names = build(K); pg.write(g, sys.argv[2]); print("n", g.n)
