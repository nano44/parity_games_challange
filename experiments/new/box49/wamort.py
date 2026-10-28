#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §6: the SW-AMORT potential in the W order, on FALLBACK-FREE runs.
A fallback-free run is a maximal stretch of consecutive transitions of one phase with fallback flag 0 (S4a steps only, τ fixed). W_t is the
valuation of the (σ_t, τ)-play (common.py wplay), compared in SPEC S1's order (E.key). Per run:
- WMONO: transitions with W_{t+1}(v) ◁ W_t(v) at some v (W falls somewhere);   WFLAT: transitions with W unchanged at every vertex.
- for every Even switch a -> b at t: W_t(b) vs W_t(a) (cnt sw_Wt_gt / eq / lt) and W_{t+1}(b) vs W_{t+1}(a) (sw_Wt1_gt / eq / lt).
- PASSW(w): (t, y), y ∈ succ(w), W_t(y) ⊴ W_t(σ_{t+1} w) and W_{t+1}(y) ▷ W_{t+1}(σ_{t+1} w). PHIW0(w): options W-above σ(w) at the run's start.
  If every switch is W-strict at t, the potential argument of SW-AMORT gives SW(w) <= PHIW0(w) + PASSW(w); WAMORT_viol counts failures.
Usage: wamort.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter
C = Counter(); MAX = {}
def mx(k, v, tag):
    if v > MAX.get(k, (-1,))[0]: MAX[k] = (v, tag)

def runs_of(R, i, j):
    k = i
    while k < j:
        a = k
        while k < j and R[k]["fb"] == 0: k += 1
        if k > a: yield a, k          # transitions a..k-1, states a..k
        k += 1

def run(g, st, nm):
    E, R = rows(g, st); n = g.n
    for i, j in phases(R):
        for a, b in runs_of(R, i, j):
            L = b - a; C["runs_ff"] += 1; C["L"] += L
            W = [[E.key(R[k]["W"][v]) for v in range(n)] for k in range(a, b + 1)]
            sw, pw = Counter(), Counter()
            for k in range(L):
                A, B = R[a + k], R[a + k + 1]; x, y = W[k], W[k + 1]
                if any(y[v] < x[v] for v in range(n)): C["WMONO"] += 1
                if x == y: C["WFLAT"] += 1
                for w in range(n):
                    if g.owner[w] != 0: continue
                    s0, s1 = A["s"][w], B["s"][w]
                    if s0 != s1:
                        sw[w] += 1
                        C["sw"] += 1
                        C["sw_Wt_" + ("gt" if x[s1] > x[s0] else "eq" if x[s1] == x[s0] else "lt")] += 1
                        C["sw_Wt1_" + ("gt" if y[s1] > y[s0] else "eq" if y[s1] == y[s0] else "lt")] += 1
                    for z in g.succ[w]:
                        if x[z] <= x[s1] and y[z] > y[s1]: pw[w] += 1
            for w in range(n):
                if g.owner[w] != 0: continue
                phi = sum(1 for z in g.succ[w] if W[0][z] > W[0][R[a]["s"][w]])
                if sw[w] > phi + pw[w]: C["WAMORT_viol"] += 1
            C["PASSW"] += sum(pw.values())
            tag = (nm, (a, b), n)
            mx("L_over_n", L / n, tag + (L,)); mx("PASSW_over_L", sum(pw.values()) / L, tag + (sum(pw.values()), L))
            mx("maxSW_run", max(sw.values(), default=0), tag)

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    for f in files:
        g = load(f)
        if g.n > nmax: continue
        sf = f[:-3] + ".start"
        sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                  {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, os.path.relpath(f, ROOT)); C["games_runs"] += 1
            except RecursionError: C["RECERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for k, v in sorted(MAX.items()): print("max", k, v)
