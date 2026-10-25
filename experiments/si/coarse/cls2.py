#!/usr/bin/env python3
"""L-SI box 8: DATA for the (CL-S) proof route (docs/si/N5-C-box8.md). On 𝒞^1O inside phases:
  MF_k := max level of gate edges (y, z) with z ∉ R̄_k ("off-R̄ gates"); MR_k := the same for z ∈ R̄_k.
Checks:
  (OG)  every gate (y, z) at k+1 with z ∉ R̄_{k+1} has level <= M_k (Lemma OFFGATE), at every in-phase transition;
  (OG') the same with MF_k in place of M_k (stronger; needed for the potential);
  (CN)  every in-phase switch at a cycle node (λ_k(y) = y) has gate level -1;
  (FBR) at every in-phase S4c fallback with (h): every gate with target in R̄_k has level <= -1; split by state kind
        (THR u*≠none / THR u*=none / EQ) and by tail membership;
  (MF-mono) MF non-increasing along scope runs (all transitions, jumps included).
Usage: cls2.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dpot import *
from collections import Counter

def scan2(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g)); C = Counter(); ex = []
    for a in out:
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o); a["Rb"] = a["R"] | {o}
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
        a["gl"] = [(y, z, lev(a["Xi"][a["s"][y]], a["Xi"][z])) for y, z in a["Is"]]
        a["M"] = max([l for _, _, l in a["gl"]] or [-3])
        a["MF"] = max([l for y, z, l in a["gl"] if z not in a["Rb"]] or [-3])
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != b["key"]: continue
        for y, z, l in b["gl"]:
            if z not in b["Rb"]:
                C["OG"] += 1
                if l > a["M"]: C["OG_viol"] += 1; ex.append((name, "OG", i, y, z, l, a["M"]))
                if l > a["MF"]: C["OGp_viol"] += 1; ex.append((name, "OG'", i, y, z, l, a["MF"]))
        for y in range(n):
            if g.owner[y] == 0 and b["s"][y] != a["s"][y] and a["Xi"][y][0] == y:
                C["CN"] += 1; l = lev(a["Xi"][a["s"][y]], a["Xi"][b["s"][y]])
                if l != -1: C["CN_viol"] += 1; ex.append((name, "CN", i, y, l))
        if a["fb"] and a["h"]:
            thr = a["Xi"][o] != a["W"][o]; us = (a["Xi"][o][1] ^ a["W"][o][1]) != 0
            kind = "THRu" if thr and us else ("THR0" if thr else "EQ")
            for y, z, l in a["gl"]:
                if z in a["Rb"]:
                    C["FBR_" + kind] += 1
                    if l > -1: C["FBR_viol_" + kind + ("_RR" if y in a["R"] else "_FR")] += 1; ex.append((name, "FBR", i, kind, y, z, l))
    # MF monotone along scope runs
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] == b["key"] and a["h"] and b["h"] and a["W"][o] == b["W"][o]:
            C["MFchk"] += 1
            if b["MF"] > a["MF"]: C["MF_up"] += 1; ex.append((name, "MFup", i, a["MF"], b["MF"]))
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan2(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:25]: print("  ", e)
