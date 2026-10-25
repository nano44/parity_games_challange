#!/usr/bin/env python3
"""L-SI box 8: DATA for the invariants behind (CL-S) (docs/si/N5-C-box8.md §5). Inside a scope run, after an S4c fallback, let L := the
least fallback level M so far in the run. Checks at every later in-scope state j / transition j -> j+1:
  (RF-INV) every gate R_j -> F_j has level <= L;   (FF-INV) every gate F_j -> F_j has level <= L;
  (F-FREEZE) z ∈ F_j ∩ F_{j+1} keeps COARSE_L(Ξ);   (R-ROUTE) z ∈ R_j ∩ R_{j+1} changes above L only at θ's change level;
  (LEAVE) leavers change only at levels <= L;   (B1) no gate of level > L into a vertex that leaves R at that transition.
Also counts in-scope fallbacks by state kind (THR with u* ≠ none / THR with u* = none / EQ).
Counts the preconditions of the open case: gates INTO R̄_j of level > L ("highRbar"), and arena-step leaves, after a fallback.
Usage: rfinv.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cls2 import *
from collections import Counter

def scan_r(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g)); C = Counter(); ex = []
    for a in out:
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o); a["Rb"] = a["R"] | {o}
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
        a["gl"] = [(y, z, lev(a["Xi"][a["s"][y]], a["Xi"][z])) for y, z in a["Is"]]
        a["M"] = max([l for *_, l in a["gl"]] or [-3])
    L = None
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        scope = a["key"] == b["key"] and a["h"] and b["h"] and a["W"][o] == b["W"][o]
        if not scope: L = None; continue
        if L is not None:
            for y, z, l in a["gl"]:
                if l <= L: continue
                if z in a["Rb"]: C["highRbar"] += 1
                elif y in a["R"]: C["RF_viol"] += 1; ex.append((name, "RF", i, y, z, l, L))
                else: C["FF_viol"] += 1; ex.append((name, "FF", i, y, z, l, L))
            lt = lev(a["Xi"][o], b["Xi"][o])
            for z in range(n):
                if z == o: continue
                inA, inB = z in a["R"], z in b["R"]; lz = lev(a["Xi"][z], b["Xi"][z])
                if not inA and not inB:
                    C["F_chk"] += 1
                    if lz > L: C["F_viol"] += 1; ex.append((name, "F", i, z, lz, L))
                elif inA and inB:
                    C["R_chk"] += 1
                    if lz > L and lz != lt: C["R_viol"] += 1; ex.append((name, "R", i, z, lz, lt, L))
                elif inA:
                    C["leave_" + ("fb" if a["fb"] else "ar")] += 1
                    hi = [l for y, zz, l in a["gl"] if zz == z and l > L]       # (B1): no gate of level > L into a leaving vertex
                    C["B1_chk"] += 1
                    if hi: C["B1_viol"] += 1; ex.append((name, "B1", i, z, max(hi), L))
                    if lz > L: C["LEAVE_viol"] += 1; ex.append((name, "LEAVE", i, z, lz, L))
        if a["fb"]:
            thr = a["Xi"][o] != a["W"][o]; us = (a["Xi"][o][1] ^ a["W"][o][1]) != 0
            C["fb_" + ("THRu" if thr and us else ("THR0" if thr else "EQ"))] += 1
            L = a["M"] if L is None else min(L, a["M"])
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan_r(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
