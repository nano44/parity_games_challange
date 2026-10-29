#!/usr/bin/env python3
"""L-SI box 30 (docs/si/N5-TORD-box30.md): |D| = 1 trap epochs in the PREFIX frame. Inside a frozen W-phase (frz/fwphase.py) with
D = {o}, an epoch = maximal run with S = S^p (vertices whose (σ, τ)-play meets o) constant (frz/epoch.py). For trapped x ≠ o, pre(x) := the
(σ, τ)-play from x up to (excluding) o; c1 := cycle node of Ξ(o), c2 := cycle node of W(o) (both constant in a frozen W-phase).
Prefix orders: ≤1 (Ξ frame) / ≤2 (W frame): mask of pre above rank(c_i), signed weight, then length (c_i odd: longer better).
θ_hi := max(rank c1, rank c2); H(x) := pre(x) above θ_hi. Checks (V = violation count):
  TD     : τ(o) ∈ U and σ̄(o) ∈ U at every state of the epoch (tail-disjoint), counted (not a violation).
  PMON1/2: prefix keys ≤1 / ≤2 non-decreasing at every trapped x ≠ o through the epoch (Lemma PMON) [on TD epochs].
  HLP    : H constant from step s = |S| − 1 after the epoch start (Lemma H-P) [on TD epochs].
  LMON   : after H is constant, ℓ = |pre| moves only in the case direction: c2 even and rank c1 < rank c2 -> ℓ non-increasing;
           rank c2 < rank c1 -> ℓ non-decreasing (Theorem TORD (ii)).
  CNT    : prefix-W-changing transitions (some trapped x ≠ o changes its ≤2 prefix key) ≤ s²  (Theorem TORD (iii)).
  TRAPFIX: c1 ≠ c2 ⇒ the frozen W-phase is ONE epoch (Theorem TRAP-FIX).
  FWD1   : c1 ≠ c2 ⇒ WCH (W-changing transitions of the frozen W-phase) ≤ |U| − 1 + s² (Corollary FW-D1).
  DATA   : max prefix-W-changing transitions per epoch / s (CONJECTURE TORD-BF: ≤ s); max epochs per frozen W-phase (per case);
           max WCH / (n − 1) over frozen W-phases with c1 ≠ c2. MUT=lmon reverses LMON's direction; MUT=hlp0 demands H constant from step 1 (controls).
Usage: epoch2.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, avoid
from fwphase import fwphases
C = Counter(); EX = []; MX = {}; MUT = os.environ.get("MUT") == "lmon"; MUTH = os.environ.get("MUT") == "hlp0"

def prefix(wn, x, o):
    p, y = [], x
    while y != o: p.append(y); y = wn[y]
    return p

def pkey(E, p, c):
    mask = 0
    for v in p:
        if E.rank[v] > E.rank[c]: mask |= E.bit[v]
    return (E.weight(mask), len(p) if E.par[c] == 1 else -len(p))

def hkey(E, p, th):
    mask = 0
    for v in p:
        if E.rank[v] > th: mask |= E.bit[v]
    return E.weight(mask)

def note(k, z):
    if len(EX) < 12: EX.append((k,) + z)

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if len(D) != 1: continue
            o = next(iter(D)); c1, c2 = R[a]["vs"][o][0], R[a]["W"][o][0]
            C["fw1"] += 1
            Sp = [frozenset(set(range(n)) - avoid(R[t]["wn"], D, n)) for t in range(a, b + 1)]
            e = 0; ne = 0
            for k in range(1, len(Sp) + 1):
                if k < len(Sp) and Sp[k] == Sp[e]: continue
                f = k - 1; ne += 1; S = Sp[e]; U = set(range(n)) - S; T = sorted(S - {o}); s = len(T)
                ep = (name, a, b, a + e, a + f, s, n)
                case = "same" if c1 == c2 else ("W>" if E.rank[c2] < E.rank[c1] else "X>")
                C["ep_" + case] += 1
                td = all(R[t]["t"][o] not in S and R[t]["sb"][o] not in S for t in range(a + e, a + f + 1))
                C["ep_TD" if td else "ep_notTD"] += 1
                pre = [{x: prefix(R[t]["wn"], x, o) for x in T} for t in range(a + e, a + f + 1)]
                k1 = [{x: pkey(E, P[x], c1) for x in T} for P in pre]
                k2 = [{x: pkey(E, P[x], c2) for x in T} for P in pre]
                th = max(E.rank[c1], E.rank[c2])
                hk = [{x: hkey(E, P[x], th) for x in T} for P in pre]
                pw = sum(1 for q in range(1, len(pre)) if k2[q] != k2[q - 1])
                if td:
                    for q in range(1, len(pre)):
                        for x in T:
                            if k1[q][x] < k1[q - 1][x]: C["PMON1_V"] += 1; note("PMON1", ep + (a + e + q, x))
                            if k2[q][x] < k2[q - 1][x]: C["PMON2_V"] += 1; note("PMON2", ep + (a + e + q, x))
                    for q in range((1 if MUTH else s + 1), len(pre)):
                        if hk[q] != hk[q - 1]: C["HLP_V"] += 1; note("HLP", ep + (a + e + q,))
                    for q in range(s + 1, len(pre)):
                        for x in T:
                            d = len(pre[q][x]) - len(pre[q - 1][x])
                            if MUT: d = -d                   # mutation: the wrong direction must be caught
                            if case == "X>" and E.par[c2] == 0 and d > 0: C["LMON_V"] += 1; note("LMON", ep + (a + e + q, x, d))
                            if case == "W>" and d < 0: C["LMON_V"] += 1; note("LMON", ep + (a + e + q, x, d))
                    if pw > s * s: C["CNT_V"] += 1; note("CNT", ep + (pw,))
                    C["checked_TD_epochs"] += 1
                r = pw / max(s, 1)
                if pw > s: C["TORDBF_V_" + ("TD" if td else "nTD")] += 1; note("TORDBF", ep + (pw, case, td))
                if r > MX.get("r", (0,))[0]: MX["r"] = (r, pw, case, td) + ep
                MX["pw"] = max(MX.get("pw", 0), pw)
                e = k
            MX["epochs"] = max(MX.get("epochs", 0), ne)
            cs = "same" if c1 == c2 else "diff"; MX["epochs_" + cs] = max(MX.get("epochs_" + cs, 0), ne)
            if c1 != c2:
                C["fw1_diff"] += 1
                if ne != 1: C["TRAPFIX_V"] += 1; note("TRAPFIX", (name, a, b, ne))
                wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"]); S = Sp[0]; s1 = len(S) - 1
                if wch > n - len(S) - 1 + s1 * s1: C["FWD1_V"] += 1; note("FWD1", (name, a, b, wch, s1, n))
                rr = wch / (n - 1)
                if rr > MX.get("diff_wch", (0,))[0]: MX["diff_wch"] = (rr, wch, name, a, b, s1, n)

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
    for z in EX[:12]: print("EXAMPLE", z)
    for k in ("PMON1", "PMON2", "HLP", "LMON", "CNT", "TRAPFIX", "FWD1"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__": main()
