#!/usr/bin/env python3
"""L-SI box 9: DATA for Lemma ABS-O (docs/si/N5-C-box9.md §3b). At every in-phase non-fallback transition j with H1 at j at which
σ̄(o) changes from x0 and x0 ∈ F_j ∩ R_{j+1} (an absorption), with c = λ(o): if rank o > rank c, then the max gate level g of the
Even switches on x0's H_{j+1}-path to o is >= rank o. Also splits the level-M blocks of scope runs (reltrace.py) by whether
rank o > max(M, rank c) (Corollary NJ-HI: such blocks have no COARSE_M change inside). Usage: abso.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reltrace import *

def scan_o(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    rank = E.rank; C = Counter(); ex = []
    for a in out:
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"]); a["R"] = reach(g, a["s"], a["t"], o)
        a["h1"] = not oncycle(g, a["s"], a["sb"], o)
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != b["key"] or not a["h1"] or a["fb"]: continue
        x0, x1 = a["sb"][o], b["sb"][o]
        if x0 == x1 or x0 in a["R"] or x0 not in b["R"]: continue
        c = a["Xi"][o][0]; C["abs"] += 1
        if rank[o] <= rank[c]: continue
        C["counted"] += 1
        nxt = lambda v: b["s"][v] if g.owner[v] == 0 else (b["t"][v] if v != o else None)
        v, gmax = x0, -3
        while v != o:
            if g.owner[v] == 0 and b["s"][v] != a["s"][v]: gmax = max(gmax, lev(a["Xi"][a["s"][v]], a["Xi"][b["s"][v]]))
            v = nxt(v)
        if gmax < rank[o]: C["viol"] += 1; ex.append((name, "ABS-O", i, gmax, rank[o]))
    runs, d_o, exits, out2 = runs_of(g, name)
    for S in runs:
        for e in S:
            if e["k"] == "F" and e["M"] >= 0:
                k = e["i"]; c = out2[k]["Xi"][o][0]
                C["fb_hi" if rank[o] > max(e["M"], rank[c]) else "fb_lo"] += 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan_o(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
