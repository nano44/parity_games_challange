#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §8 (Lead's GO (x), 14:40Z: FREEZE-A on A u {D-direct gates}). Per phase, class c, U := U_c,
A_t := F_D(t) cap U, DD_t := {u in D_t cap U : sigma-bar_t(u) in A_t and tau(u) in A_t} (the D-DIRECT GATES: both continuations direct),
B_t := A_t u {z in U : the first D_t-vertex of z's (sigma_t, tau)-play is in DD_t} (A plus the gate regions of D-direct gates).
  BFG: at an in-phase S4a transition t -> t+1, for Even z in (B_t \\ A_t) cap B_t+1, z != c, and x in succ(z) cap U: is
       M_t+1(z) >= wt(z) + M_t(x)?  (BF-F_D's inequality at gated vertices.)  BFG_fail counts failures (a CANDIDATE counterexample to the
       naive extension; printed with the two gates involved); bfg_checks the checks.
  Cuts: fallbacks and B-gains (B_t+1 not a subset of B_t), against fallbacks and A-gains; and on B-pieces longer than |B_s| - 1, FRZB_fail:
       z in B_t with M_t(z) != M at the piece's freeze index (the naive FREEZE-B).
  GATE-SHIFT checks: GS_A_V (M_t(z) = MW_t(z) - Delta_t(u), Delta >= 0, W cycle node c, at z in B_t \\ A_t; gs_a_checks) and GS_B_V
       (M_t+1(z) >= wt(z) + M_t(x) - Delta_t+1(u) for Even z in B_t+1 \\ A_t+1, x in succ(z) cap U whose play at t avoids z; gs_b_checks).
Usage: bfgate.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); EX = []; VERB = "-v" in sys.argv

def regions(g, A, U):
    D = Dset(g, A); F = avoid(A["wn"], D, g.n); Au = F & U
    DD = {u for u in D & U if A["sb"][u] in Au and A["t"][u] in Au}
    B = set(Au) | {z for z in U if first_D(A["wn"], z, D) in DD}
    return Au, DD, B, D

def run(g, name, start=None):
    E, R = rows(g, start)
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        for c, U in cls.items():
            if len(U) < 3: continue
            Rg = {k: regions(g, R[k], U) for k in range(i, j + 1)}
            cutsA = cutsB = 0; s = i
            for k in range(i, j):
                A0, DD0, B0, D0 = Rg[k]; A1, DD1, B1, D1 = Rg[k + 1]
                fb = R[k]["fb"]
                cutsA += fb or not A1 <= A0; cb = fb or not B1 <= B0; cutsB += cb
                for z in B0 - A0:                       # GATE-SHIFT (a) at t
                    u = first_D(R[k]["wn"], z, D0); dl = M(E, R[k]["vs"][R[k]["t"][u]]) - M(E, R[k]["vs"][R[k]["sb"][u]])
                    C["gs_a_checks"] += 1
                    if R[k]["W"][z][0] != c or M(E, R[k]["vs"][z]) != E.weight(R[k]["W"][z][1]) - dl or dl < 0: C["GS_A_V"] += 1
                if not fb:
                    for z in (B1 - A1):                     # GATE-SHIFT (b) at t -> t+1
                        if g.owner[z] != 0 or z == c: continue
                        u = first_D(R[k + 1]["wn"], z, D1); dl = M(E, R[k + 1]["vs"][R[k + 1]["t"][u]]) - M(E, R[k + 1]["vs"][R[k + 1]["sb"][u]])
                        for x in set(g.succ[z]):
                            if x not in U: continue
                            y, seen = x, set()
                            while y not in seen and y != z: seen.add(y); y = R[k]["wn"][y]
                            if y == z: continue
                            C["gs_b_checks"] += 1
                            if M(E, R[k + 1]["vs"][z]) < wt(E, z, c) + M(E, R[k]["vs"][x]) - dl: C["GS_B_V"] += 1
                    for z in (B0 - A0) & B1:
                        if g.owner[z] != 0 or z == c: continue
                        for x in set(g.succ[z]):
                            if x not in U: continue
                            C["bfg_checks"] += 1
                            if M(E, R[k + 1]["vs"][z]) < wt(E, z, c) + M(E, R[k]["vs"][x]):
                                C["BFG_fail"] += 1
                                gz = first_D(R[k]["wn"], z, D0); gx = first_D(R[k]["wn"], x, D0)
                                EX.append((name, i, k - i, z, x, gz, gx, R[k]["s"][z], R[k + 1]["s"][z]))
                                if VERB: print(f"  BFG_fail {name} phase@{i} t={k - i} z={z} x={x} gate(z)={gz} gate(x)={gx} sigma(z) {R[k]['s'][z]}->{R[k + 1]['s'][z]}")
                if cb or k == j - 1:
                    e = k if cb else j
                    L = max(len(Rg[s][2]) - 1, 0)
                    if e - s > L:
                        C["long_Bpieces"] += 1; base = s + L
                        for t in range(base, e + 1):
                            for z in Rg[t][2]:
                                if M(E, R[t]["vs"][z]) != M(E, R[base]["vs"][z]): C["FRZB_fail"] += 1
                    s = k + 1
            C["cutsA"] += cutsA; C["cutsB"] += cutsB
            if VERB and j - i > 40: print(f"  {name} phase@{i} c={c} len={j - i} cutsA={cutsA} cutsB={cutsB}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:6]: print("EXAMPLE (game, phase, t, z, x, gate(z), gate(x), sigma(z) t, t+1)", x)

if __name__ == "__main__":
    main()
