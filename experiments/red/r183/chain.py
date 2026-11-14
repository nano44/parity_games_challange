#!/usr/bin/env python3
"""L-RED R183 CHAIN: iterated odxi_n37 gadget. Core = vertices 0..31 of L-NEW's odxi_n37 (box133) plus its sink 32 (Even self-loop,
priority 8). Gadget i = 1..k: Even mover x_i (priority 0) -> {A_i, B_i}; Odd gates A_i -> {32, a_i}, B_i -> {32, b_i} (priority 0 or
the given one). a_i, b_i are core vertices or earlier movers x_j (spec string). Writes a .pg.
Spec: list of (a, b, pa, pb) with a/b = 'c<v>' (core vertex v) or 'x<j>' (mover j, j < i, or any j: feedback), pa/pb gate priorities.
Usage (library): build(spec) -> pg.Game."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load
import pg
CORE = os.path.join(HERE, "instances", "odxi_n37.pg")
def build(spec, core=CORE):
    g = load(core); P, O, S = list(g.prio[:33]), list(g.owner[:33]), [list(x) for x in g.succ[:33]]
    k = len(spec); X = [33 + 3 * i for i in range(k)]
    ref = lambda t: int(t[1:]) if t[0] == "c" else X[int(t[1:])]
    for i, (a, b, pa, pb) in enumerate(spec):
        x = X[i]; P += [0, pa, pb]; O += [0, 1, 1]
        S += [[x + 1, x + 2], sorted({32, ref(a)}), sorted({32, ref(b)})]
    return pg.Game(P, O, S)
def write(g, p):
    with open(p, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
