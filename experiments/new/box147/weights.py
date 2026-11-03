#!/usr/bin/env python3
"""L-NEW box 147: the LP weights of the linear UNST potential (allstart.py family UNST), printed against structure: pi position,
level, number of Xi-descendants (#movers Xi-reachable by any option), Xi-height (longest Xi-path below). Also tests fixed structural
weight rules (no LP): w_x = 1, pi+1, n-pi, #desc+1, height+1, 2^height, 2^#desc. Prints the violations of each on the all-start
graph. Usage: weights.py genome.json ..."""
import sys, os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "allstart.py"); ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns)
topo, feats, step, chained = ns["topo"], ns["feats"], ns["step"], ns["chained"]
import numpy as np
from scipy.optimize import linprog
def graph(G):
    n = G["N"]; pos = {v: i for i, v in enumerate(topo(G))}
    states = list(itertools.product((0, 1), repeat=n)); nxt = {s: step(G, s) for s in states}
    FS = {s: feats(G, list(s), pos) for s in states}; lab = {}
    for p in states:
        q = nxt[p]
        if q == p: continue
        r = nxt[q]
        if r == q: continue
        lab[(q, r)] = lab.get((q, r), False) or (not chained(G, p, q, r))
    return pos, FS, lab
def struct(G, pos):
    n, opts = G["N"], G["opts"]; desc = {}; ht = {}
    def D(x):
        if x not in desc:
            r = set()
            for o in opts[x]:
                if o[1] >= 0: r |= {o[1]} | D(o[1])
            desc[x] = r
        return desc[x]
    def H(x):
        if x not in ht: ht[x] = max((1 + H(o[1]) for o in opts[x] if o[1] >= 0), default=0)
        return ht[x]
    return [len(D(x)) for x in range(n)], [H(x) for x in range(n)]
def lp(G, pos, FS, lab, fam="UNST"):
    n = G["N"]; A = []; b = []
    for (q, r), u in lab.items():
        A.append(np.array(FS[r][fam], float) - np.array(FS[q][fam], float)); b.append(-1.0 if u else 0.0)
    A = np.array(A); sol = linprog(np.ones(2 * n), A_ub=np.hstack([A, -A]), b_ub=b, bounds=[(0, None)] * (2 * n), method="highs")
    return None if sol.status else sol.x[:n] - sol.x[n:]
def check(w, FS, lab, fam="UNST"):
    bad = 0
    for (q, r), u in lab.items():
        dphi = sum(w[x] * (FS[r][fam][x] - FS[q][fam][x]) for x in range(len(w)))
        if (u and not dphi < 0) or (not u and dphi > 0): bad += 1
    return bad
if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = json.load(open(p)); n = G["N"]
        if n > 14: continue
        pos, FS, lab = graph(G); nd, h = struct(G, pos); w = lp(G, pos, FS, lab)
        order = sorted(range(n), key=lambda x: pos[x])
        print(os.path.basename(p), "edges", len(lab), "unch", sum(lab.values()))
        if w is not None:
            print("  pi order :", order); print("  lev      :", [G["lev"][x] for x in order]); print("  #desc    :", [nd[x] for x in order])
            print("  height   :", [h[x] for x in order]); print("  LP w     :", [round(w[x], 2) for x in order])
        rules = {"one": [1] * n, "pi+1": [pos[x] + 1 for x in range(n)], "n-pi": [n - pos[x] for x in range(n)], "desc+1": [nd[x] + 1 for x in range(n)],
                 "ht+1": [h[x] + 1 for x in range(n)], "2^ht": [2 ** h[x] for x in range(n)], "2^desc": [2 ** nd[x] for x in range(n)],
                 "2^(n-pi)": [2 ** (n - pos[x]) for x in range(n)], "2^pi": [2 ** pos[x] for x in range(n)]}
        print("  rules viol:", " ".join(f"{k} {check(v, FS, lab)}" for k, v in rules.items()))
