#!/usr/bin/env python3
"""L-SI box 7: (JUMP-EQ) exactly as stated in docs/si/N5-C-box5.md §6.2: inside a phase with w constant, if an INR at k -> k+1 raises θ
at a level above the level L of the most recent carry (box 5 leaver level; w unchanged since that carry), then θ_{k+1} = w.
INR here = NC failure (mono.py), which on one-Odd-choice games inside a phase means the old exit σ̄_k(o) is captured.
Prints every case: instance, k, L, M_k, θ-change level, θ_{k+1} = w?, (h) at k+1, carries later in the phase with the same w.
Usage: jumpeq.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tame import *
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
from nhprof import oncycle

def scan_e(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None
    Ed = n5.Engine(n5.dual(g)); rows = []
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o)
        a["h"] = (not oncycle(g, a["s"], a["sb"], o), not oncycle(g, a["s"], a["t"], o), a["Xi"][o][0] == W[o][0])
    L = None; w0 = None; ph0 = None
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != ph0: ph0 = a["key"]; L = None; w0 = None
        if a["key"] != b["key"]: continue
        if a["W"][o] != w0: L, w0 = None, a["W"][o]
        lam = [a["Xi"][v][0] for v in range(n)]
        nc = all(lam[t] == t for t in (max(C, key=lambda v: E.rank[v]) for C in cycles(g, b["s"], a["sb"])))
        thl = lev(a["Xi"][o], b["Xi"][o])
        if not nc and L is not None and b["W"][o] == w0 and thl > L:
            later = sum(1 for j in range(i + 1, len(out) - 1) if out[j]["key"] == a["key"] and out[j + 1]["key"] == a["key"]
                        and out[j]["W"][o] == w0 and out[j]["fb"] and any(y in out[j]["R"] and out[j + 1]["s"][y] not in out[j]["R"]
                        and out[j + 1]["s"][y] != o for y in range(n) if g.owner[y] == 0))
            rows.append((name, i, L, a["M"], thl, b["Xi"][o] == b["W"][o], "".join("123"[q] for q in range(3) if not b["h"][q]) or "h",
                         later))
        if a["fb"]:
            lv = [lev(a["Xi"][y], b["Xi"][y]) for y in range(n) if g.owner[y] == 0 and b["s"][y] != a["s"][y]
                  and y in a["R"] and b["s"][y] not in a["R"] and b["s"][y] != o]
            if lv: L = max(lv)
    return rows

if __name__ == "__main__":
    allr = []
    for p in sys.argv[1:]:
        allr += scan_e(load(p), os.path.basename(p))
    print("cases (name, k, L, M_k, θ-level, θ'=w, (h) at k+1 or failing clauses, evicting fallbacks later at same w):")
    for r in allr: print("  ", r)
    print("total", len(allr), "θ'=w:", sum(r[5] for r in allr), "with later carries:", sum(1 for r in allr if r[7]))
