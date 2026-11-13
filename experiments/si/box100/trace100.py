#!/usr/bin/env python3
"""L-SI box 100 (SCC-LIN, trace first): HOW3 on Gamma3(G) with L-RED 65's own engine (claude/l-red 59daaef2, experiments/red/r232/how3_232.py,
read-only, extracted at run time; env RED = that archive's root). Per state t >= 1: movers that switch (all, and those in the largest SCC C
of D(G)); gates whose Odd choice sigma-bar flips, split into: ext (a target of the option outside C or -1: ONE-CROSS3 says <= 1 flip after
t0(C)) and int (both targets in C). Prints a per-state line and a per-gate flip summary.
Usage: trace100.py G.json [quiet]"""
import sys, os, json
R = os.environ["RED"]; sys.path.insert(0, os.path.join(R, "experiments/red/r232"))
import how3_232 as H
def trace(G):
    full = []; seq = H.how3(G, full=full); N = G["N"]; T = len(seq) - 1
    cs, comp, succ = H.sccs(G); big = max(range(len(cs)), key=lambda c: len(cs[c])); C = set(cs[big])
    V = full[0][2]; gates = []
    for x in range(N):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            kind = "int" if (x in C and wt in C and xt in C) else ("ext" if x in C else "out")
            gates.append(((x, k), V[("g", (x, k))], V[("pe", (x, k))], V[("pbeta", (x, k))], kind, wt, xt))
    rows = []
    for t in range(1, T + 1):
        sw = [x for x in range(N) if seq[t][x] != seq[t - 1][x]]
        fl = [(q, kind, full[t][1][g] == pe) for (q, g, pe, pb, kind, wt, xt) in gates if full[t][1][g] != full[t - 1][1][g]]
        rows.append((t, sw, fl))
    return seq, full, cs, comp, C, gates, rows
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); G = G.get("genome", G); G.pop("_evals", None)
    seq, full, cs, comp, C, gates, rows = trace(G); q = len(sys.argv) > 2
    MC = sum(len(G["opts"][x]) for x in C)
    print("N", G["N"], "T3", len(seq) - 1, "bigC", len(C), "M_C", MC, "int gates", sum(1 for g in gates if g[4] == "int"))
    cnt = {}
    for t, sw, fl in rows:
        for (qq, kind, toe) in fl: cnt[qq] = cnt.get(qq, 0) + 1
        if not q:
            print("t%d sw%d [%s] | flips ext %d int %d: %s" % (t, len(sw), " ".join("%d:%d>%d" % (x, seq[t-1][x], seq[t][x]) for x in sw),
                  sum(1 for f in fl if f[1] == "ext"), sum(1 for f in fl if f[1] == "int"),
                  " ".join("%d.%d%s%s" % (f[0][0], f[0][1], "e" if f[2] else "b", "*" if f[1] == "int" else "") for f in fl)))
    kinds = {g[0]: g[4] for g in gates}
    print("gate flip counts (>=2):", sorted(((k, v, kinds[k]) for k, v in cnt.items() if v >= 2), key=lambda z: -z[1]))
    print("ext gates flipping:", sum(1 for k in cnt if kinds[k] == "ext"), "max ext flips", max([cnt[k] for k in cnt if kinds[k] == "ext"] or [0]))
    sws = {}
    for t, sw, fl in rows:
        for x in sw: sws[x] = sws.get(x, 0) + 1
    print("mover switch counts:", sorted(sws.items(), key=lambda z: -z[1])[:20], "total", sum(sws.values()))
