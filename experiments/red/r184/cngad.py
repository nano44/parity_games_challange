#!/usr/bin/env python3
"""L-RED R184 CN gadget: a W-cycle node c (Even, even priority pc) with options = Odd gates A, B whose tau-faces return to c and whose
other edges go to targets (core vertices of odxi_n37's core 0..31, or other gadgets' c). k gadgets; genome per gadget:
(pc, (ta, pa), (tb, pb)), target t < 32 = core vertex, t >= 32 = gadget c_(t - 32). Core = odxi_n37 vertices 0..31 (+ its sink 32 kept
so core edges into 32 stay valid). Usage (library): build(G) -> pg.Game"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r183"), os.path.join(H, "..", "..", "new", "box21")]
import chain, pg
from n5x import load
core = load(chain.CORE)
def build(G):
    k = len(G); P, O, S = list(core.prio[:33]), list(core.owner[:33]), [list(x) for x in core.succ[:33]]
    C = [33 + 3 * i for i in range(k)]; ref = lambda t: t if t < 32 else C[(t - 32) % k]
    for i, (pc, (ta, pa), (tb, pb)) in enumerate(G):
        c = C[i]; P += [pc, pa, pb]; O += [0, 1, 1]
        S += [[c + 1, c + 2], sorted({c, ref(ta)}), sorted({c, ref(tb)})]
    return pg.Game(P, O, S)
