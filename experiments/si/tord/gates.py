#!/usr/bin/env python3
"""L-SI box 30 (docs/si/N5-TORD-box30.md §11): frozen W-phases with |D| ≥ 1 by GATE CLASSES. For a gate d ∈ D: S_d := vertices whose
(σ, τ)-play meets D first at d; π(d) := (λ_Ξ(d), λ_W(d)). Conditions: G1 every gate has λ_Ξ(d) ≠ λ_W(d); G2 distinct gates have distinct
π; G3 at every state τ(d), σ̄(d) ∉ S_d. Checks: GTF_V (general TRAP-FIX: for every class π with π₁ ≠ π₂ the union of its basins is
constant on the frozen W-phase); GB_V (G1 ∧ G2 ⇒ every S_d constant); FWDG_V (G1 ∧ G2 ∧ G3 ⇒ WCH ≤ |U| − 1 + Σ_d s_d², s_d = |S_d| − 1,
Theorem FW-DG). DATA: counts per condition, max WCH/(n − 1) by |D|, FWD_V := WCH > (|D| + 1)(n − 1) (CONJECTURE FW-D).
Usage: gates.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from fwphase import fwphases
C = Counter(); MX = {}; EX = []

def basins(wn, D, n):
    first = [None] * n
    for v in range(n):
        x, seen, path = v, set(), []
        while first[x] is None and x not in D and x not in seen: seen.add(x); path.append(x); x = wn[x]
        f = x if x in D else (first[x] if first[x] is not None else -1)
        for u in path: first[u] = f
        if v in D: first[v] = v
    return first

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D: continue
            C["fw"] += 1; nd = len(D)
            pi = {d: (R[a]["vs"][d][0], R[a]["W"][d][0]) for d in D}
            F = [basins(R[t]["wn"], D, n) for t in range(a, b + 1)]
            g1 = all(p[0] != p[1] for p in pi.values()); g2 = len(set(pi.values())) == nd
            g3 = all(R[t]["t"][d] not in [v for v in range(n) if F[t - a][v] == d and v != d] and
                     R[t]["sb"][d] not in [v for v in range(n) if F[t - a][v] == d and v != d] for t in range(a, b + 1) for d in D)
            for cl in set(pi.values()):
                if cl[0] == cl[1]: continue
                gs = {d for d in D if pi[d] == cl}
                U0 = {v for v in range(n) if F[0][v] in gs}
                if any({v for v in range(n) if F[q][v] in gs} != U0 for q in range(len(F))): C["GTF_V"] += 1; EX.append(("GTF", name, a, b))
            wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            key = ("G1" if g1 else "") + ("G2" if g2 else "") + ("G3" if g3 else "")
            C[f"D{min(nd,4)}_{key or 'none'}"] += 1
            if g1 and g2:
                if any(F[q] != F[0] for q in range(len(F))): C["GB_V"] += 1; EX.append(("GB", name, a, b))
                if g3:
                    Us = sum(1 for v in range(n) if F[0][v] == -1); bound = Us - 1 + sum((sum(1 for v in range(n) if F[0][v] == d) - 1) ** 2 for d in D)
                    C["checked_FWDG"] += 1
                    if wch > bound: C["FWDG_V"] += 1; EX.append(("FWDG", name, a, b, wch, bound, nd, n))
            if wch > (nd + 1) * (n - 1): C["FWD_V"] += 1; EX.append(("FWD", name, a, b, wch, nd, n))
            k = f"wch_D{min(nd,4)}"; r = wch / (n - 1)
            if r > MX.get(k, (0,))[0]: MX[k] = (r, wch, name, a, b, nd, n, key)

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("maxima:", MX)
    for z in EX[:8]: print("EXAMPLE", z)
    for k in ("GTF", "GB", "FWDG", "FWD"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__": main()
