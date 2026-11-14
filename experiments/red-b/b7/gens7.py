#!/usr/bin/env python3
"""L-RED-B B7 generators.
lmcs(n, ver): Friedmann's G_n, arXiv 1106.0778v2 Table 4 (PDF p. 15) with the start strategy iota_{G_n} (same page, «As an
  initial strategy we select the following»).  ver = "fig4": the priorities of the paper's Figure 4 (G_3: d1 3, e1 4, g1 6,
  k1 33, f1 35, h1 36, ...), i.e. Table 4 with the six rows d, e, g, k, f, h lowered by 2; then the highest priority is
  12n + 8 as Fact 6.1 says and the priorities are injective.  ver = "table4": the table as printed (highest 12n + 10;
  pr(g_n) = pr(a_1) = 4n + 4).  Transcribed by this lane from the PDF (sha1 a63a9293...), not from another lane's file.
Usage: gens7.py lmcs N [fig4|table4] OUT.pg OUT.start"""
import sys
from si7 import Game, dump_pg


def lmcs(n, ver="fig4"):
    V = {}
    lo = 2 if ver == "fig4" else 0
    assert ver in ("fig4", "table4")
    def add(name, player, prio, succ):
        V[name] = (player, prio, succ)
    add("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1):
        add(f"t{i}", 0, 4 * n + 2 * i + 1, ["s", "r", f"t{i - 1}"])
    for i in range(1, 2 * n + 1):
        add(f"a{i}", 1, 4 * n + 2 * i + 2, [f"t{i}"])
    add("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        add(f"d{i}", 0, 4 * i + 1 - lo, ["s", f"e{i}", "r"] + [f"a{j}" for j in range(1, 2 * i + 1)])
        add(f"e{i}", 1, 4 * i + 2 - lo, [f"d{i}", f"h{i}"])
        add(f"g{i}", 0, 4 * i + 4 - lo, [f"f{i}", f"k{i}"])
        add(f"k{i}", 0, 8 * n + 4 * i + 7 - lo, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        add(f"f{i}", 1, 8 * n + 4 * i + 9 - lo, [f"e{i}"])
        add(f"h{i}", 1, 8 * n + 4 * i + 10 - lo, [f"k{i}"])
    add("s", 0, 8 * n + 6, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    add("r", 0, 8 * n + 8, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    names = list(V)
    idx = {nm: i for i, nm in enumerate(names)}
    g = Game([V[nm][1] for nm in names], [V[nm][0] for nm in names], [[idx[w] for w in V[nm][2]] for nm in names], names)
    iota = {"t1": "c", "c": "r", "s": "x", "r": "x"}
    for i in range(2, 2 * n + 1):
        iota[f"t{i}"] = "r"
    for i in range(1, n + 1):
        iota[f"g{i}"] = f"k{i}"; iota[f"d{i}"] = "r"; iota[f"k{i}"] = "x"
    start = [idx[iota[names[v]]] if g.owner[v] == 0 else -1 for v in range(g.n)]
    assert g.n == 10 * n + 4 and 2 * g.m == 3 * n * n + 41 * n + 10            # Fact 6.1
    assert max(g.prio) == (12 * n + 8 if ver == "fig4" else 12 * n + 10)
    return g, start


def write_start(path, g, start):
    with open(path, "w") as f:
        for v in range(g.n):
            if g.owner[v] == 0:
                f.write(f"{v} {start[v]}\n")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "lmcs":
        g, s = lmcs(int(a[1]), a[2])
        open(a[3], "w").write(dump_pg(g)); write_start(a[4], g, s)
