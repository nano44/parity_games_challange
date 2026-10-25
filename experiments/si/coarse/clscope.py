#!/usr/bin/env python3
"""L-SI box 7: DATA for CONJECTURE (CL-S) (docs/si/N5-C-box7.md §13). Inside a maximal scope run (in-phase transitions with (h) at k,
H2 at k+1, w constant; dpot.py), list the max gate level M_k at each S4c fallback. (CL-S): this sequence is non-increasing across the
whole scope run (non-tame jumps included), and each level occurs at most n_E times (M >= 0). Usage: clscope.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dpot import *
from collections import Counter

def scan_c(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g)); nE = sum(1 for v in range(n) if g.owner[v] == 0); runs = []; cur = None
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W
        a["h1"] = not oncycle(g, a["s"], a["sb"], o); a["h2"] = not oncycle(g, a["s"], a["t"], o); a["h3"] = a["Xi"][o][0] == W[o][0]
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        scope = a["key"] == b["key"] and a["h1"] and a["h2"] and a["h3"] and b["h2"] and a["W"][o] == b["W"][o]
        if not scope: cur = None; continue
        if cur is None: cur = dict(fbM=[], J=0); runs.append(cur)
        M = a["M"]
        if any(coarse(b["Xi"][v], M) != coarse(a["Xi"][v], M) for v in range(n)): cur["J"] += 1; cur["fbM"].append("J")
        if a["fb"]: cur["fbM"].append(M)
    c = dict(runs=len(runs), fb=0, mono_viol=0, perlevel_viol=0, maxfb_run=0, maxJ_run=0, maxgap=-100); ex = []
    for r in runs:
        seq = [x for x in r["fbM"] if x != "J"]; c["fb"] += len(seq); c["maxfb_run"] = max(c["maxfb_run"], len(seq))
        c["maxJ_run"] = max(c["maxJ_run"], r["J"])
        for i1 in range(len(seq)):          # largest rise of the fallback level between two fallbacks of the run (> 0 = violation)
            for i2 in range(i1 + 1, len(seq)): c["maxgap"] = max(c["maxgap"], seq[i2] - seq[i1])
        if any(y > x for x, y in zip(seq, seq[1:])): c["mono_viol"] += 1; ex.append((name, "mono", r["fbM"]))
        if any(m >= 0 and k > nE for m, k in Counter(seq).items()): c["perlevel_viol"] += 1; ex.append((name, "perlevel", r["fbM"]))
    return c, ex

if __name__ == "__main__":
    T = {}; X = []
    for p in sys.argv[1:]:
        c, ex = scan_c(load(p), os.path.basename(p)); X += ex
        for k, v in c.items(): T[k] = max(T.get(k, 0), v) if k.startswith("max") else T.get(k, 0) + v
    print("TOTAL", T)
    for e in X[:12]: print("  ", e)
