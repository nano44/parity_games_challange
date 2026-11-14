#!/usr/bin/env python3
"""REFEREE successor 24: independent exact re-check of a P-IDEAL-RISE §5 certificate (l-new 2f4d96de), written from the packet's §5
text; L-NEW's risecheck.py feature code was NOT read (only its output line format).
- Every transition (G_i, s_i -> next_i) is recomputed with MY simulator t3r_sim.py (R104 text) and must equal the stored «next».
- Every genome must be in L^R_d (R110 wiring) and Xi-acyclic (t3r_sim.in_LR).
- Features of class PHX = BASE + P + H + X, from §5's definitions:
    z_s(x) = [Xi_s(x, 1 - s(x)) |> Xi_s(x, s(x))] (R104 set order), k_s(x) = [s(x) != KP_s(x)], u = z k;
    P: per level l, indicator of each (k(2l), k(2l+1), z(2l), z(2l+1)) in {0,1}^4, and ord_l(s) = [key(2l) < key(2l+1)];
    H: per level l and height eta, #{x of level l: h(x) = eta, z = 1} and #{...: u = 1}; h(x) = number of movers on the longest Xi-path
       from x (1 + max h of a mover Xi-target of x; X counts 0);
    X: for l <= d - 2, a in {2l, 2l+1}, b in {2l+2, 2l+3}: z(a) k(b) and k(a) z(b).
- Linear system (exact Fractions): for every feature f: sum_i y_i (f(s_i) - f(next_i)) + sum_j a_j f(lo_j) - sum_j b_j f(hi_j) = 0;
  sum a = 1; sum b = 1. Solved by exact Gaussian elimination over ALL rows of the certificate. Reports the rank / free variables, the
  exact solution if unique, nonnegativity, and the bound sum y.
PBG (CLASS argument PBG) = BASE + P + B + G: positions ic, io of cv_s(x) and v_s(x, 1 - s(x)) in the list of the beta-sets of all
maximal Xi-paths from x, sorted by the R104 set order (no ENC; positions 0-based, a constant shift cancels since sum a = sum b).
Usage: python3 -I cert_check.py cert.json [PHX|PBG]"""
import json, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def kp(G, s, x): return min(range(2), key=lambda k: R.key(G, s, x, k, {}))
def ck(G, s, x): return R.key(G, s, x, s[x], {})

def heights(G):
    memo = {}
    def h(x):
        if x not in memo:
            memo[x] = 1 + max((h(o[1]) for o in G["opts"][x] if o[1] >= 0), default=0)
        return memo[x]
    return [h(x) for x in range(G["N"])]

CLS = sys.argv[2] if len(sys.argv) > 2 else "PHX"
import functools
def pathsets(G, x):
    """beta-sets of all maximal Xi-paths from x (one option chosen at every mover on the way, ending at X)."""
    out = []
    for o in G["opts"][x]:
        if o[1] < 0: out.append(frozenset([o[2]]))
        else: out += [frozenset([o[2]]) | t for t in pathsets(G, o[1])]
    return out
def pos(G, lst, v):
    return lst.index(v)
def feats(G, s):
    N = G["N"]; d = N // 2; F = {}
    z = [int(R.better(G, R.value(G, s, x, 1 - s[x]), R.value(G, s, x, s[x]))) for x in range(N)]
    k = [int(s[x] != kp(G, s, x)) for x in range(N)]
    u = [z[x] * k[x] for x in range(N)]
    for x in range(N):
        F[("z", x)] = z[x]; F[("k", x)] = k[x]; F[("u", x)] = u[x]
    for l in range(d):
        p, q = 2 * l, 2 * l + 1
        for bits in [(a, b, c, e) for a in (0, 1) for b in (0, 1) for c in (0, 1) for e in (0, 1)]:
            F[("P", l, bits)] = int((k[p], k[q], z[p], z[q]) == bits)
        F[("ord", l)] = int(ck(G, s, p) < ck(G, s, q))
    if CLS == "PBG":
        cmpf = lambda A, B: 0 if A == B else (1 if R.better(G, A, B) else -1)
        PV = []; IC = []; IO = []
        for x in range(N):
            lst = sorted(set(pathsets(G, x)), key=functools.cmp_to_key(cmpf))
            PV.append(len(lst)); IC.append(pos(G, lst, R.value(G, s, x, s[x]))); IO.append(pos(G, lst, R.value(G, s, x, 1 - s[x])))
        for x in range(N):
            P = PV[x]; b = P - 1 - IC[x]; gdiff = IO[x] - IC[x]; gp = max(0, gdiff)
            F[("B1", x)] = Fr(b); F[("B2", x)] = Fr(b, max(1, P - 1))
            F[("G1", x)] = Fr(gdiff); F[("G2", x)] = Fr(gp); F[("G3", x)] = Fr(gp, max(1, P - 1)); F[("G4", x)] = Fr(k[x] * gp)
        for l in range(d):
            F[("B3", l)] = Fr(sum(PV[x] - 1 - IC[x] for x in (2 * l, 2 * l + 1)))
        return F
    hx = heights(G)
    for l in range(d):
        for eta in range(1, N + 1):
            F[("Hz", l, eta)] = sum(1 for x in (2 * l, 2 * l + 1) if hx[x] == eta and z[x] == 1)
            F[("Hu", l, eta)] = sum(1 for x in (2 * l, 2 * l + 1) if hx[x] == eta and u[x] == 1)
    for l in range(d - 1):
        for a in (2 * l, 2 * l + 1):
            for b in (2 * l + 2, 2 * l + 3):
                F[("Xzk", a, b)] = z[a] * k[b]; F[("Xkz", a, b)] = k[a] * z[b]
    return F

def main():
    c = json.load(open(sys.argv[1])); d = c["d"]
    rows = []; bad = 0
    for e in c["dec"]:
        G = e["genome"]; s = tuple(e["s"])
        if not R.in_LR(G, d): bad += 1
        nxt = R.step(G, s)
        if nxt is None or list(nxt) != list(e["next"]): bad += 1; continue
        f0, f1 = feats(G, s), feats(G, nxt)
        rows.append(("y", {f: Fr(f0[f] - f1[f]) for f in f0}))
    for kind, sign in (("lo", 1), ("hi", -1)):
        for e in c[kind]:
            G = e["genome"]; s = tuple(e["s"])
            if not R.in_LR(G, d): bad += 1
            f = feats(G, s); rows.append((kind, {g: Fr(sign * f[g]) for g in f}))
    names = sorted({f for _, r in rows for f in r}, key=str)
    n = len(rows)
    A = [[r.get(f, Fr(0)) for _, r in rows] + [Fr(0)] for f in names]
    A.append([Fr(1) if kd == "lo" else Fr(0) for kd, _ in rows] + [Fr(1)])
    A.append([Fr(1) if kd == "hi" else Fr(0) for kd, _ in rows] + [Fr(1)])
    # exact RREF
    piv = []; r = 0
    for col in range(n):
        pr = next((i for i in range(r, len(A)) if A[i][col] != 0), None)
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]
        pv = A[r][col]; A[r] = [v / pv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][col] != 0:
                fct = A[i][col]; A[i] = [a - fct * b for a, b in zip(A[i], A[r])]
        piv.append(col); r += 1
    incons = any(all(v == 0 for v in row[:n]) and row[n] != 0 for row in A)
    free = n - len(piv)
    sol = [Fr(0)] * n
    for i, col in enumerate(piv): sol[col] = A[i][n]
    neg = sum(1 for v in sol if v < 0)
    bound = sum(sol[i] for i in range(n) if rows[i][0] == "y")
    # independent residual check of the found solution
    resid = 0
    for f in names:
        if sum(sol[i] * rows[i][1].get(f, 0) for i in range(n)) != 0: resid += 1
    sa = sum(sol[i] for i in range(n) if rows[i][0] == "lo"); sb = sum(sol[i] for i in range(n) if rows[i][0] == "hi")
    print(f"{os.path.basename(sys.argv[1])} d {d} rows {n} features {len(names)} bad {bad} inconsistent {incons} rank {len(piv)} free {free} "
          f"negative {neg} residual-features {resid} sum_a {sa} sum_b {sb} bound {float(bound):.6f} = {bound}")

main()
