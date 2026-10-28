#!/usr/bin/env python3
"""Friedmann's H_n (O. Friedmann, LMCS 7(3:19) 2011, arXiv 1106.0778, §8.4, Table 7; start ι_{H_n} below Table 7).
Built from the paper's text (pdf sha256 46c96f44...), not from PGSolver (PGSolver's switchbestexp has 25N+10 vertices,
H_n has 21n: a different family).

Player 0 = Even (owner 0), player 1 = Odd (owner 1), max-parity: as pg.py.
Vertices: x, s, c, r; a_i, t_i (0 < i <= 6n-2); d1_i, d2_i, d3_i, e_i, f_i, h_i, g_i, y_i, k_i (0 < i <= n).
Edge sets exactly as Table 7, with j >= 0 in {a_{3j+3} | j <= 2i-2} etc. (this reading reproduces Fact 8.1's edge count
3.5n^2 + 40.5n - 4, checked below).

PRIORITIES. Table 7 as printed is NOT injective (§2 assumes Ω injective): gate n's d2_n = 8n+3 = Ω(t1), d3_n = 8n+5 = Ω(t2),
e_n = 8n+6 = Ω(a2), y_n = 8n+7 = Ω(t3), g_n = 8n+8 = Ω(a3). Figure 10 (H_3) and Figures 8, 9 (p'_1 = 3) put the gate
priorities 6 lower: d1_i = 8i-5, d2_i = 8i-3, d3_i = 8i-1, e_i = 8i, y_i = 8i+1, g_i = 8i+2 (Fig. 10: d^0_3:19, e3:24, g3:26
for i = 3), which is injective and below the lane (t1 = 8n+3). Mode 'fig' (DEFAULT) = Table 7 with these gate priorities
(Table 6 with p'_i = 8i-5, p_i = 20n+4i+3); everything else as Table 7. Mode 'table' = Table 7 verbatim (duplicates; ties are
broken by vertex index downstream). Figure 10's labels for s, r (30, 32) and k, f, h (20n+4i+1, +3, +4) are NOT used: they
contradict Table 7 and Fact 8.1's highest priority 24n+6; Table 7's values are.
Usage: hn.py N [--mode fig|table] [--out FILE.pg] [--start FILE.start]   (start = ι_{H_n} for Even, SIGMA0 lines only)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg

EVEN, ODD = 0, 1


def build(n, mode="fig"):
    m = 6 * n - 2
    names = ["x", "s", "c", "r"] + [f"a{i}" for i in range(1, m + 1)] + [f"t{i}" for i in range(1, m + 1)]
    for i in range(1, n + 1):
        names += [f"d1_{i}", f"d2_{i}", f"d3_{i}", f"e{i}", f"f{i}", f"h{i}", f"g{i}", f"y{i}", f"k{i}"]
    ix = {nm: v for v, nm in enumerate(names)}
    N = len(names)
    prio, own, succ = [None] * N, [None] * N, [None] * N

    def node(nm, pl, p, ss):
        v = ix[nm]
        own[v], prio[v], succ[v] = pl, p, sorted(ix[s] for s in ss)
    node("t1", EVEN, 8 * n + 3, ["s", "r", "c"])
    for i in range(2, m + 1):
        node(f"t{i}", EVEN, 8 * n + 2 * i + 1, ["s", "r", f"t{i-1}"])
    for i in range(1, m + 1):
        node(f"a{i}", ODD, 8 * n + 2 * i + 2, [f"t{i}"])
    node("c", ODD, 20 * n, ["r"])
    off = -6 if mode == "fig" else 0
    for i in range(1, n + 1):
        node(f"d1_{i}", EVEN, 8 * i + 1 + off, ["s", "c", f"d2_{i}"] + [f"a{3*j+3}" for j in range(0, 2 * i - 1)])
        node(f"d2_{i}", EVEN, 8 * i + 3 + off, [f"d3_{i}"] + [f"a{3*j+2}" for j in range(0, 2 * i - 1)])
        node(f"d3_{i}", EVEN, 8 * i + 5 + off, [f"e{i}"] + [f"a{3*j+1}" for j in range(0, 2 * i)])
        node(f"e{i}", ODD, 8 * i + 6 + off, [f"d1_{i}", f"h{i}"])
        node(f"y{i}", EVEN, 8 * i + 7 + off, [f"f{i}", f"k{i}"])
        node(f"g{i}", EVEN, 8 * i + 8 + off, [f"y{i}", f"k{i}"])
        node(f"k{i}", EVEN, 20 * n + 4 * i + 3, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        node(f"f{i}", ODD, 20 * n + 4 * i + 5, [f"e{i}"])
        node(f"h{i}", ODD, 20 * n + 4 * i + 6, [f"k{i}"])
    node("s", EVEN, 20 * n + 2, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    node("r", EVEN, 20 * n + 4, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    node("x", ODD, 1, ["x"])
    g = pg.Game(prio, own, succ, names)
    # Fact 8.1: 21n nodes, 3.5n^2 + 40.5n - 4 edges, highest priority 24n + 6
    assert g.n == 21 * n, g.n
    assert 2 * g.m == 7 * n * n + 81 * n - 8, (g.m, n)
    assert max(prio) == 24 * n + 6
    if mode == "fig":
        assert len(set(prio)) == g.n, "fig mode must be injective"
    return g, ix


def iota(n, ix):
    """ι_{H_n} (§8.4, below Table 7): Even's start strategy, as {vertex: successor}."""
    m = 6 * n - 2
    s = {ix["t1"]: ix["c"], ix["s"]: ix["x"], ix["r"]: ix["x"]}
    for i in range(2, m + 1):
        s[ix[f"t{i}"]] = ix[f"t{i-1}"] if i <= 3 else ix["r"]
    for i in range(1, n + 1):
        s[ix[f"d1_{i}"]] = ix[f"d2_{i}"]
        s[ix[f"d2_{i}"]] = ix["a2"]
        s[ix[f"d3_{i}"]] = ix["a1"]
        s[ix[f"g{i}"]] = ix[f"k{i}"]
        s[ix[f"y{i}"]] = ix[f"k{i}"]
        s[ix[f"k{i}"]] = ix["x"]
    return s   # ι(c) = r is Odd's only edge (c is a player 1 node in Table 7)


def main():
    a = sys.argv[1:]
    n = int(a[0])
    mode = a[a.index("--mode") + 1] if "--mode" in a else "fig"
    g, ix = build(n, mode)
    ev = [v for v in range(g.n) if g.owner[v] == EVEN]
    s = iota(n, ix)
    assert sorted(s) == ev and all(s[v] in g.succ[v] for v in s)
    if "--out" in a:
        pg.write(g, a[a.index("--out") + 1])
    else:
        sys.stdout.write(pg.dumps(g))
    if "--start" in a:
        with open(a[a.index("--start") + 1], "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in ev) + "\n")


if __name__ == "__main__":
    main()
