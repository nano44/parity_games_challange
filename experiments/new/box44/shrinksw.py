#!/usr/bin/env python3
"""Box 44 greedy shrink (box43 shrink.cands moves) keeping DIFFSW >= 1 (crd.py: a cross-terminal gate edge switched by S4c at a
fallback inside a phase with (hD) and (h3D) at the fallback state; refutes CONJECTURE Delta-RT-F). The number of Odd choice
vertices may drop (it must stay >= 2, else the property is impossible). Usage: shrinksw.py in.pg out.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from shrink import cands
from climb import save
from n5x import load
import crd

def prop(g):
    for k in crd.C: crd.C[k] = 0 if k != "CRD_maxj" else -1
    try: crd.check(g, cap=4000)
    except RecursionError: return False
    return crd.C["DIFFSW"] > 0

if __name__ == "__main__":
    g = load(sys.argv[1]); assert prop(g), "property fails on the input"; changed = True
    while changed:
        changed = False
        for h in cands(g):
            if prop(h): g = h; changed = True; break
    save(sys.argv[2], g, None, None); print("n =", g.n, "m =", sum(map(len, g.succ)))
