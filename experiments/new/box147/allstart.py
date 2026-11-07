#!/usr/bin/env python3
"""L-NEW box 147: ALL-START test. For a deg-2 IDEAL-ACYC genome with n movers, enumerate all 2^n start states (each is a valid
IDEAL-ACYC genome: the start is part of the genome), apply the R178 §1 step map (box139/paths.py run, one step at a time), and label
every step q -> r that has a predecessor p -> q (p != q) as CHAINED / UNCHAINED (box 144 ALL form on the triple p, q, r). An edge is
UNCH if some predecessor makes it unchained.
(1) For each feature map F (functions of the state only): the quotient digraph on F-values; SOME g(F) with g non-increasing on every
    labelled edge and strictly decreasing on every UNCH edge exists iff no UNCH edge has both ends in one SCC (BAD = number of such
    edges); if none, LEVELS = the most UNCH edges on a path of the condensation (the levels g needs). For F = the state itself this
    is max U over all starts (the step map is acyclic: every run stops).
(2) LP: a LINEAR potential sum_x w_x f_x(s) over the 0/1 feature family FAM (per-mover features), real weights, with
    PHI(r) <= PHI(q) - 1 on UNCH edges and PHI(r) <= PHI(q) on chained edges: feasible or not (scipy linprog); if feasible, the minimal
    sum |w| (an upper bound on the levels the potential spans is n * max|w|).
Usage: allstart.py genome.json ... (n <= 14)"""
import sys, os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "stat.py"); ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns)
fc, topo, feats, scc_test = ns["fc"], ns["topo"], ns["feats"], ns["scc_test"]
import numpy as np
from scipy.optimize import linprog
def step(G, s):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]; order = sorted(range(N), key=lambda v: lev[v])
    val, idx, _, M = fc.values(G, s); face = lambda v, k: val(N + idx[(v, k)])
    cur = [face(v, s[v]) for v in range(N)]
    avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > cur[v]] for v in range(N)]
    if all(len(a) == 1 for a in avail): return s
    key = [None] * N; ns_ = list(s)
    for v in order:
        best = None
        for k in avail[v]:
            wt = opts[v][k][0]; kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
            if best is None or kk < best[0]: best = (kk, k)
        key[v] = best[0]; ns_[v] = best[1]
    return tuple(ns_)
def chained(G, p, q, r):
    N, opts, lev = G["N"], G["opts"], G["lev"]
    m1 = [x for x in range(N) if q[x] != p[x]]; m2 = [x for x in range(N) if r[x] != q[x]]
    h1 = min(m1, key=lambda x: (lev[x], x)); h2 = min(m2, key=lambda x: (lev[x], x))
    out = []; y = opts[h2][r[h2]][1]
    while y >= 0: out.append(y); y = opts[y][p[y]][1]
    return h1 in [y for y in out if q[y] != p[y]]
FEATS = {
  "STATE": lambda F, s: tuple(s), "UNST": lambda F, s: tuple(F["UNST"]), "B": lambda F, s: tuple(F["B"]),
  "AGR": lambda F, s: tuple(F["AGR"]), "KP": lambda F, s: tuple(F["KP"]), "B+UNST": lambda F, s: (tuple(F["B"]), tuple(F["UNST"])),
  "UNST+KP": lambda F, s: (tuple(F["UNST"]), tuple(F["KP"])), "WANT": lambda F, s: tuple(int(F["UNST"][x] and F["KP"][x] == F["B"][x]) for x in range(len(s))),
  "NUNST": lambda F, s: sum(F["UNST"]),
}
def _top(F, s, k):
    return tuple(sorted((F["_pos"][x] for x in range(len(s)) if F["UNST"][x]), reverse=True)[:k])
FEATS.update({"TOP1": lambda F, s: _top(F, s, 1), "TOP2": lambda F, s: _top(F, s, 2), "TOP3": lambda F, s: _top(F, s, 3),
  "LVCNT": lambda F, s: tuple(sum(F["UNST"][x] for x in range(len(s)) if F["_lev"][x] == l) for l in range(max(F["_lev"]) + 1)),
  "WANT+FROZEN_N": lambda F, s: (tuple(int(F["UNST"][x] and F["KP"][x] == F["B"][x]) for x in range(len(s))), sum(F["UNST"])),
  "UNST_UPPERHALF": lambda F, s: tuple(F["UNST"][x] for x in range(len(s)) if F["_pos"][x] >= len(s) // 2),
  "UNST_LOWERHALF": lambda F, s: tuple(F["UNST"][x] for x in range(len(s)) if F["_pos"][x] < len(s) // 2)})
FAMS = {"UNST": ["UNST"], "S": ["S"], "S+UNST": ["S", "UNST"], "S+UNST+AGR": ["S", "UNST", "AGR"], "S+UNST+AGR+B+KP": ["S", "UNST", "AGR", "B", "KP"]}
def vec(F, s, fam):
    v = []
    for f in fam:
        v += list(s) if f == "S" else list(F[f])
    return v
def analyse(G):
    n = G["N"]; pos = {v: i for i, v in enumerate(topo(G))}
    states = list(itertools.product((0, 1), repeat=n)); nxt = {s: step(G, s) for s in states}
    FS = {s: feats(G, list(s), pos) for s in states}
    for F in FS.values(): F["_pos"] = pos; F["_lev"] = G["lev"]
    lab = {}
    for p in states:
        q = nxt[p]
        if q == p: continue
        r = nxt[q]
        if r == q: continue
        u = not chained(G, p, q, r); lab[(q, r)] = lab.get((q, r), False) or u
    maxU = 0; memo = {}
    def Ulen(s, prev):  # unchained steps along the run from s (prev = predecessor or None)
        tot = 0
        while True:
            q = nxt[s]
            if q == s: return tot
            if prev is not None: tot += not chained(G, prev, s, q)
            prev, s = s, q
    maxU = max(Ulen(s, None) for s in states)
    res = {"states": len(states), "edges": len(lab), "unch": sum(lab.values()), "maxU": maxU}
    for k, f in FEATS.items():
        edges = [(f(FS[q], q), f(FS[r], r), u) for (q, r), u in lab.items()]
        res["Q_" + k] = scc_test(None, edges)
    for k, fam in FAMS.items():
        A = []; b = []
        for (q, r), u in lab.items():
            d_ = np.array(vec(FS[r], r, fam), float) - np.array(vec(FS[q], q, fam), float)
            A.append(d_); b.append(-1.0 if u else 0.0)
        m = len(A[0]) if A else 0
        if not A: res["LP_" + k] = "noedges"; continue
        A = np.array(A); c = np.ones(2 * m); Aub = np.hstack([A, -A])
        sol = linprog(c, A_ub=Aub, b_ub=np.array(b), bounds=[(0, None)] * (2 * m), method="highs")
        if sol.status == 0:
            w = sol.x[:m] - sol.x[m:]; res["LP_" + k] = f"FEAS(sum|w| {sum(abs(w)):.1f}, max|w| {max(abs(w)):.1f})"
        else: res["LP_" + k] = "INFEAS"
    return res
if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = json.load(open(p))
        if G["N"] > 14: print("SKIP", p, G["N"]); continue
        R = analyse(G)
        print(f"ALL {os.path.basename(p)} N {G['N']} STATES {R['states']} LAB_EDGES {R['edges']} UNCH {R['unch']} maxU {R['maxU']} | "
              + " ".join(f"{k[2:]}:{('BAD' + str(v[0])) if v[0] else ('lv' + str(v[1]))}" for k, v in R.items() if k.startswith("Q_")) + " | "
              + " ".join(f"{k[3:]}:{v}" for k, v in R.items() if k.startswith("LP_")), flush=True)
