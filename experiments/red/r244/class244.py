#!/usr/bin/env python3
"""L-RED 70 R244: membership check of a genome in R104's class IDEAL-ACYC, clause by clause (docs/red/P-N5-REALIZE.md §2, landed as RESULTS R104;
R117 Theorem REACH3 asks for «G with an ACYCLIC Ξ-graph» in that class). Clauses:
 c1 GRADED   every mover has a level in 0..d-1; wt(x, k) is a mover of level lev(x) - 1 if lev(x) >= 1 and none (-1) if lev(x) = 0
 c2 XT       xt(x, k) is a mover or the exit (-1)
 c3 BETA     the beta-ids b(x, k) are a bijection onto 0..M-1
 c4 GATE     the gate indices are a bijection onto 0..M-1
 c5 RANK     br is a bijection onto 0..M-1 and bp(b) in {0, 1}
 c6 START    the start is one option index per mover
 c7 ACYC     the Xi-graph (x -> xt(x, k), xt != exit) is acyclic, self-loops counting as cycles
Also printed (not clauses of R104): the degree histogram (REFEREE-2 41's note: k(G) is meaningful only with every degree >= 2), movers per level.
Usage: class244.py G.json ...   (exit code 1 if any clause fails on any file)"""
import sys, json
def check(G):
    N, lev, opts = G["N"], G["lev"], G["opts"]; M = sum(len(o) for o in opts); r = {}
    r["c1"] = len(lev) == N and len(opts) == N and all(isinstance(l, int) and l >= 0 for l in lev) and all(
        (o[0] == -1 if lev[x] == 0 else (isinstance(o[0], int) and 0 <= o[0] < N and lev[o[0]] == lev[x] - 1)) for x in range(N) for o in opts[x]) and all(len(opts[x]) >= 1 for x in range(N))
    r["c2"] = all(isinstance(o[1], int) and -1 <= o[1] < N for x in range(N) for o in opts[x])
    r["c3"] = sorted(o[2] for x in range(N) for o in opts[x]) == list(range(M))
    r["c4"] = len(G["gate"]) == N and all(len(G["gate"][x]) == len(opts[x]) for x in range(N)) and sorted(g for x in range(N) for g in G["gate"][x]) == list(range(M))
    r["c5"] = sorted(G["br"]) == list(range(M)) and len(G["bp"]) == M and all(p in (0, 1) for p in G["bp"])
    r["c6"] = len(G["start"]) == N and all(isinstance(G["start"][x], int) and 0 <= G["start"][x] < len(opts[x]) for x in range(N))
    col = [0] * N; ok = True
    for s in range(N):
        if col[s]: continue
        st = [(s, 0)]; col[s] = 1
        while st and ok:
            v, i = st[-1]; tg = [o[1] for o in opts[v] if o[1] >= 0]
            if i < len(tg):
                st[-1] = (v, i + 1); w = tg[i]
                if col[w] == 1: ok = False
                elif col[w] == 0: col[w] = 1; st.append((w, 0))
            else: col[v] = 2; st.pop()
    r["c7"] = ok
    deg = {}; per = {}
    for x in range(N): deg[len(opts[x])] = deg.get(len(opts[x]), 0) + 1; per[lev[x]] = per.get(lev[x], 0) + 1
    return r, M, deg, [per.get(l, 0) for l in range(max(lev) + 1)]
if __name__ == "__main__":
    bad = 0
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); r, M, deg, per = check(G); ok = all(r.values()); bad += not ok
        print(f"CLASS244 {f.split('/')[-1]}: N {G['N']} M {M} d {len(per)} " + " ".join(f"{c} {'PASS' if v else 'FAIL'}" for c, v in r.items()) + f" | degrees {sorted(deg.items())} movers/level {per} | {'IN IDEAL-ACYC' if ok else 'NOT in the class'}")
    sys.exit(1 if bad else 0)
