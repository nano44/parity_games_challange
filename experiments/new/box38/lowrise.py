#!/usr/bin/env python3
"""Box 38 (c): checks Lemma LOW-RISE and Theorem BRK-B (docs/new/N5-NEB-box38.md) on N5 runs (canonical start, or a start pair
via a .state file). Phase with τ(o) = o; HN stretches S; C_θ := {(c_θ, P(θ), ℓ)} (the LOW class).
(LR) at an HN fallback state a, follow the θ-constant HN run from a; at the first state t+1 > a with an honest gate F_{t+1} -> R̄_{t+1}
     (INV (i) fails), some z ∈ R̄_t ∩ R̄_{t+1} has Ξ_t(z) ◁ Ξ_{t+1}(z), both in C_θ. Also checks INV (ii_B)/(ii) up to t (case B: every
     R -> R̄ gate length-only).
(BRK) every break (entry after an eviction in S, no entry between) has a θ-change or a LOW-RISE transition in [a, k) (a its first
     eviction after the previous entry, k its entry): case B and case A both counted.
(CNT) per θ-constant run: LOW-RISE transitions ≤ n(n − 1); breaks per stretch ≤ θ_S + n(n − 1)(θ_S + 1).
One Odd choice vertex asserted. Usage: lowrise.py game.pg [game.state] ... """
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from neb_run import *
from mono import lev

def run(g, s0, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; HN = [r["h1"] and not r["h2"] for r in rows]
    def Rb(k): return set(rows[k]["R"]) | {o}
    def lowrise(t):   # transition t -> t+1, θ constant: some z with a strict rise inside C_θ
        th = rows[t]["Xi"][o]; c, P = th[0], th[1]
        return [z for z in (Rb(t) & Rb(t + 1)) - {o} if rows[t]["Xi"][z][:2] == (c, P) and rows[t + 1]["Xi"][z][:2] == (c, P)
                and rows[t]["Xi"][z] != rows[t + 1]["Xi"][z]]
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"] and r["t"][o] == o): continue
        case = "A" if E.rank[o] > E.rank[r["Xi"][o][0]] else "B"; bump(acc, case + "_fallback_bases")
        t = a
        while t + 1 < N and HN[t + 1] and rows[t + 1]["ph"] == r["ph"] and rows[t + 1]["th"] == r["th"]:
            Xi, s = rows[t]["Xi"], rows[t]["s"]; R1 = Rb(t)
            for y, z in E.improving(tuple(s), Xi):
                if y in R1 and z in R1 and y != o:
                    L = lev(Xi[s[y]], Xi[z])
                    if case == "B" and L != -1: bump(acc, "FAIL_iiB"); print("iiB", name, a, t)
            b = t + 1; Xb, sbb = rows[b]["Xi"], rows[b]["s"]; Rb1 = Rb(b)
            if any(y not in Rb1 and z in Rb1 for y, z in E.improving(tuple(sbb), Xb)):
                bump(acc, case + "_INVi_fail")
                zs = [z for z in Rb(t) & Rb(b) if z != o and Xi[z][:2] == (Xi[o][0], Xi[o][1]) and Xb[z][:2] == (Xi[o][0], Xi[o][1]) and Xi[z] != Xb[z]]
                if not zs: bump(acc, case + "_FAIL_LR"); print("LR", name, a, t)
                break
            t += 1
    k = 0
    while k < N:
        if not (HN[k] and rows[k]["t"][o] == o): k += 1; continue
        j = k
        while j + 1 < N and HN[j + 1] and rows[j + 1]["ph"] == rows[k]["ph"]: j += 1
        case = "A" if E.rank[o] > E.rank[rows[k]["Xi"][o][0]] else "B"
        th = sum(rows[i]["th"] != rows[i + 1]["th"] for i in range(k, j)); lr = 0; B = 0; first_ev = None
        for i in range(k, j):
            R0, R1 = set(rows[i]["R"]), set(rows[i + 1]["R"])
            if rows[i]["th"] == rows[i + 1]["th"] and lowrise(i): lr += 1
            if R0 - R1 and first_ev is None: first_ev = i
            if R1 - R0 and not (R0 - R1):
                if first_ev is not None:
                    B += 1; a = first_ev
                    sep = any(rows[x]["th"] != rows[x + 1]["th"] for x in range(a + 1, i + 1)) or \
                          any(rows[x]["th"] == rows[x + 1]["th"] and lowrise(x) for x in range(a, i))
                    bump(acc, f"breaks_{case}_" + ("charged" if sep else "UNCHARGED"))
                    if not sep: print("BRK", name, a, i)
                first_ev = None
        bump(acc, "stretches_tauo_o_" + case); mx(acc, "max_lowrise_per_stretch_" + case, lr, n, th, B, name, k)
        if B > th + n * (n - 1) * (th + 1): bump(acc, "FAIL_CNT"); print("CNT", name, k)
        k = j + 1

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
