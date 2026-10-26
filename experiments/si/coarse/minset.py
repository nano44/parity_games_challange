#!/usr/bin/env python3
"""L-SI box 9 §13: DATA for Lemma MINSET / CONJECTURE NJB (docs/si/N5-C-box9.md §10). For every interval (f_i, f_{i+1}) of a level-M
block (M >= 0) of a scope run (reltrace.py), track Mn_t := {exits x ∈ F_t : COARSE_M(o ⊕ Ξ_t x) = COARSE_M(θ_t)}:
|Mn| at the interval start, its minimum inside, #members absorbed (x ∈ Mn_t, x ∈ R_{t+1}), and (MINSET-c) "COARSE_M(θ) changes iff
Mn empties". NJB violation = Mn empty at some state strictly inside a block. Usage: minset.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reltrace import *

def mn(g, a, o, exits, M):
    th = coarse(a["Xi"][o], M); E = n5.Engine(g)
    return {x for x in exits if x != o and x not in a["R"] and coarse(E.extend(o, a["Xi"][x]), M) == th}

def scan_m(g, name):
    runs, d_o, exits, out = runs_of(g, name); o = odd_choice(g); C = Counter(); ex = []
    for S in runs:
        fbs = [t for t, e in enumerate(S) if e["k"] == "F"]
        for t1, t2 in zip(fbs, fbs[1:]):
            M = S[t1]["M"]
            if M < 0 or S[t2]["M"] != M: continue
            C["intervals"] += 1; k1, k2 = S[t1]["i"], S[t2]["i"]
            sizes = [len(mn(g, out[k], o, exits, M)) for k in range(k1 + 1, k2 + 1)]
            C["start_sum"] += sizes[0]; C["min_le1"] += min(sizes) <= 1
            if min(sizes) == 0: C["njb_viol"] += 1; ex.append((name, "NJB", M, k1, k2, sizes))
            for k in range(k1 + 1, k2):
                A = mn(g, out[k], o, exits, M); C["absorbed"] += sum(1 for x in A if x in out[k + 1]["R"])
                ch = coarse(out[k + 1]["Xi"][o], M) != coarse(out[k]["Xi"][o], M)
                if ch != (len(mn(g, out[k + 1], o, exits, M) & A) == 0 and len(A) > 0 and all(x in out[k + 1]["R"] for x in A)):
                    C["minset_c_mismatch"] += 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan_m(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
