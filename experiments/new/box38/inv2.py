#!/usr/bin/env python3
"""Box 38 (c): τ(o) ≠ o checks (docs/new/N5-NEB-box38.md §8). At every HN in-phase Even fallback a (any τ(o)), c_w(a) := top of o's
W-cycle at a; case A: rank(o) > rank(c_θ). Follow the θ-constant HN run from a.
- c_w(a) = o, case A: INV (i), (ii) of NO-ENTRY-A at every state (FAIL_A_i / FAIL_A_ii); case B: (ii_B) up to the first (i) failure,
  and a LOW rise at it (FAIL_B_LR).
- any c_w, case A: at the first state t+1 with a gate F -> R̄, some z ∈ R̄_t ∩ R̄_{t+1} has Ξ_t(z) ◁ Ξ_{t+1}(z) with
  lev ≥ rank(o) (a HIGH rise; FAIL_HR otherwise). Records the band level of high rises against rank(c_w).
- any case, any c_w: at that state a strict rise Ξ_t(z) ◁ Ξ_{t+1}(z) of some z ∈ R̄_t ∩ R̄_{t+1} (Lemma RISE; FAIL_RISE).
- NO-ENTRY violations by (case, c_w = o or not, τ(o) = o or not).
One Odd choice vertex asserted. Usage: inv2.py game.pg [game.state] ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from neb_run import *
from mono import lev

def run(g, s0, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; HN = [r["h1"] and not r["h2"] for r in rows]; ro = E.rank[o]
    def Rb(k): return set(rows[k]["R"]) | {o}
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"]): continue
        s, t = r["s"], r["t"]; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        C = [o]; x = nx[o]
        while x != o: C.append(x); x = nx[x]
        cw = max(C, key=lambda v: E.rank[v]); case = "A" if ro > E.rank[r["Xi"][o][0]] else "B"
        key = f"{case}_cw{'=o' if cw == o else '!=o'}_tauo{'=o' if t[o] == o else '!=o'}"; bump(acc, key + "_bases")
        k = a; failed = False
        while k + 1 < N and HN[k + 1] and rows[k + 1]["ph"] == r["ph"] and rows[k + 1]["th"] == r["th"]:
            if set(rows[k + 1]["R"]) > set(rows[k]["R"]): bump(acc, key + "_VIOLATION")
            if not failed:
                Xi, sk = rows[k]["Xi"], rows[k]["s"]; R1 = Rb(k)
                for y, z in E.improving(tuple(sk), Xi):
                    if y in R1 and z in R1 and y != o:
                        L = lev(Xi[sk[y]], Xi[z])
                        if cw == o and case == "A" and L >= ro: bump(acc, "FAIL_A_ii"); print("Aii", name, a, k)
                        if cw == o and case == "B" and L != -1: bump(acc, "FAIL_B_iiB"); print("BiiB", name, a, k)
                b = k + 1; Xb = rows[b]["Xi"]; Rb1 = Rb(b)
                if any(y not in Rb1 and z in Rb1 for y, z in E.improving(tuple(rows[b]["s"]), Xb)):
                    failed = True; bump(acc, key + "_INVi_fail")
                    if cw == o and case == "A": bump(acc, "FAIL_A_i"); print("Ai", name, a, b)
                    zs = [z for z in (Rb(k) & Rb1) - {o} if Xi[z] != Xb[z]]
                    if not [z for z in zs if E.key(Xi[z]) < E.key(Xb[z])]: bump(acc, "FAIL_RISE"); print("RISE", name, a, k)
                    if case == "A":
                        hr = [z for z in zs if lev(Xi[z], Xb[z]) >= ro]
                        if not hr: bump(acc, "FAIL_HR"); print("HR", name, a, k)
                        else: mx(acc, "ex_" + key + "_highrise", 1, n, name, a, k, hr[0], lev(Xi[hr[0]], Xb[hr[0]]), ro, E.rank[cw])
                    else:
                        lr = [z for z in zs if Xi[z][:2] == (Xi[o][0], Xi[o][1]) and Xb[z][:2] == (Xi[o][0], Xi[o][1])]
                        if cw == o and not lr: bump(acc, "FAIL_B_LR"); print("BLR", name, a, k)
                        if cw != o: bump(acc, key + ("_lowrise" if lr else "_NO_lowrise"))
            k += 1

if __name__ == "__main__":
    acc = {}; args = sys.argv[1:]; i = 0
    while i < len(args):
        f = args[i]; s0 = None
        if i + 1 < len(args) and args[i + 1].endswith(".state"): s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: run(g, s0, acc, f)
        else: bump(acc, "skipped_not_C1O")
        i += 1
    for key in sorted(acc): print(key, acc[key])
