#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): the synthetic counter to fixed-context monotonicity (M) of DTL's pruning
(docs/alg/GAP-A-M.md §4). Injects two stored Even tangles into a 9-vertex game and runs one best_vertices call on R = all
vertices with T = {t} and with T' = {t, t'}. Expected: v in V* under T, v pruned under T'. Exit 1 if not reproduced."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D
import dtl_ideal as I

names = "o w2 k m v w x tau2 tau".split()          # index order = non-decreasing priority, tau after tau2
pr = [1, 1, 2, 2, 2, 2, 3, 4, 4]
ow = [1, 1, 0, 0, 0, 0, 0, 0, 0]
N = {s: i for i, s in enumerate(names)}
E = {"o": ["k", "m", "tau2"], "w2": ["w", "tau"], "k": ["o", "w"], "m": ["o"], "v": ["x"], "w": ["w2"], "x": ["o"],
     "tau2": ["tau2"], "tau": ["tau"]}
succ = [[N[t] for t in E[s]] for s in names]
t1 = ([("k", "o"), ("m", "o"), ("o", None)], ["tau2"])
t2 = ([("w", "w2"), ("w2", None)], ["tau"])


def run(tangles):
    d = D.DTL(pr, ow, succ); d.tkeys = []
    for vs, esc in tangles:
        t = len(d.tv)
        d.tv.append([(N[a], N[b] if b else -1) for a, b in vs]); d.tout.append([N[e] for e in esc]); d.tpr.append(2)
        for e in esc:
            d.tin[N[e]].append(t)
    R = set(range(len(names))); V = set()
    tl = list(range(len(d.tv)))
    P = {v for v in R if pr[v] % 2 == 0}
    Ua, regs = I.actual_union(d, 0, P, R, tl)
    Uh = I.ideal_union(d, 0, P, R, tl)
    res = d.best_vertices(V, set(R), 0)
    return res, {names[v] for v in V}, [(names[a], sorted(names[x] for x in z)) for a, z in regs], {names[x] for x in Uh - Ua}


ok = True
for label, T in (("T = {t}", [t1]), ("T' = {t, t'}", [t1, t2])):
    res, Vstar, regs, deficit = run(T)
    print(f"{label}: result {res}, V* = {sorted(Vstar)}; round-1 regions {regs}; U_hat minus U = {sorted(deficit)}")
r1, V1, _, _ = run([t1]); r2, V2, _, _ = run([t1, t2])
if not ("v" in V1 and "v" not in V2 and V2 <= V1):
    ok = False
print("M-COUNTER", "REPRODUCED (v in V*(T), v not in V*(T'))" if ok else "NOT REPRODUCED")
sys.exit(0 if ok else 1)
