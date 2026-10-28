#!/usr/bin/env python3
"""L-RED successor 23: topology for a fallback-clocked two-way chain (R96 §2 / R97). Gate o (the only Odd choice vertex, k = 1):
o -> {X, Z, l_1..l_m}? no: o -> {X, Z}; ladder rungs l_j (Even) -> {mo_j -> o (current: W via tau(o) = X), r_j -> l_{j-1}}, l_0 = B -> sinkB;
tops tL, tR (Even): tL -> odd rungs' r? (via the rung vertices l_j, j odd), tR -> even rungs; two-way chain v_1..v_L between tL and tR.
Z (Even) -> {zl -> sinkZ, zm -> l_m} (Even's best reply from Z reads the finished ladder). X -> sinkX.
Priorities come from a vector p (one per vertex) so that a climb can search them; owners fixed.
Usage (module): build(L, m) -> (names, owner, succ); write(names, owner, succ, prio, sigma, tau, out)."""
import sys

def build(L, m):
    names = []; succ = {}; own = {}
    def add(nm, ow, s): names.append(nm); own[nm] = ow; succ[nm] = s
    ch = lambda i: "tL" if i == 0 else ("tR" if i == L + 1 else "v%d" % i)
    for i in range(1, L + 1): add("v%d" % i, 0, [ch(i - 1), ch(i + 1)])
    add("tL", 0, ["l%d" % j for j in range(0, m + 1, 2)]); add("tR", 0, ["l%d" % j for j in range(1, m + 1, 2)] or ["l0"])
    add("o", 1, ["X", "Z"]); add("X", 0, ["sX"]); add("sX", 0, ["sX"])
    add("Z", 0, ["zl", "zm"]); add("zl", 0, ["sZ"]); add("sZ", 0, ["sZ"]); add("zm", 0, ["l%d" % m])
    add("l0", 0, ["B"]); add("B", 0, ["sB"]); add("sB", 0, ["sB"])
    for j in range(1, m + 1):
        add("l%d" % j, 0, ["mo%d" % j, "r%d" % j]); add("mo%d" % j, 0, ["o"]); add("r%d" % j, 0, ["l%d" % (j - 1)])
    return names, own, succ

def start(names, own, succ, L, m):
    sigma = {nm: succ[nm][0] for nm in names if own[nm] == 0}
    for i in range(1, L + 1): sigma["v%d" % i] = "tR" if i == L else "v%d" % (i + 1)
    sigma.update({"tL": "l0", "tR": "l1" if m >= 1 else "l0", "Z": "zl"})
    for j in range(1, m + 1): sigma["l%d" % j] = "mo%d" % j
    tau = {"o": "X"}
    return sigma, tau

def write(names, own, succ, prio, sigma, tau, out):
    idx = {nm: i for i, nm in enumerate(names)}
    with open(out, "w") as f:
        f.write("parity %d;\n" % (len(names) - 1))
        for nm in names: f.write('%d %d %d %s "%s";\n' % (idx[nm], prio[nm], own[nm], ",".join(str(idx[x]) for x in succ[nm]), nm))
    with open(out[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (idx[a], idx[sigma[a]]) for a in names if own[a] == 0) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (idx[a], idx[tau[a]]) for a in names if own[a] == 1) + "\n")
