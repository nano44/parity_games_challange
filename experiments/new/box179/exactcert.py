#!/usr/bin/env python3
"""L-NEW box 179: EXACT (rational) check of an LP lower-bound certificate written by lpot.py (out/cert_<cls>_d<d>_s<seed>.json).
The certificate is the dual of: min Mx s.t. w.(f(s) - f(s')) >= 1 (decrease rows), w.f(s) >= 0 (lo rows), Mx - w.f(s) >= 0 (hi rows).
Dual feasibility: sum_i y_i (f(s_i) - f(s_i')) + sum_j a_j f(s_j) - sum_j b_j f(s_j) = 0 for every feature and the constant, sum_j b_j = 1,
y, a, b >= 0. Then every potential w of the class has max Phi - 0 >= Mx >= sum_i y_i on these genomes (weak duality).
Features and transitions are RECOMPUTED here exactly (Fractions; the step by the box150 simulator), the multipliers are re-solved in
exact arithmetic on the certificate's support (free variables fixed at rationalised float values), and nonnegativity is checked.
Usage: exactcert.py cert.json"""
import os, sys, json
from fractions import Fraction as Fr
H = os.path.dirname(os.path.abspath(__file__))
L = {"__file__": os.path.join(H, "lpot.py"), "__name__": "lib"}; exec(open(L["__file__"]).read().split("\nif __name__")[0], L)
Gen, feats, xheight = L["Gen"], L["feats"], L["xheight"]
c = json.load(open(sys.argv[1])); cls = c["cls"]; cols = []; bad = 0
def F(G, s):
    g = Gen(G); return {k: Fr(v) for k, v in feats(cls, g, G, tuple(s), xheight(G)).items()}
for r in c["dec"]:
    g = Gen(r["genome"]); n, _ = g.step(tuple(r["s"]))
    if n is None or list(n) != r["next"]: bad += 1; continue
    a, b = F(r["genome"], r["s"]), F(r["genome"], n)
    v = {k: a.get(k, 0) - b.get(k, 0) for k in set(a) | set(b)}; v["__b"] = Fr(0); cols.append(("dec", r["y"], v))
for tag, sg in (("lo", 1), ("hi", -1)):
    for r in c[tag]:
        a = F(r["genome"], r["s"]); v = {k: sg * x for k, x in a.items()}; v["__const"] = Fr(sg); v["__b"] = Fr(1 if tag == "hi" else 0)
        cols.append((tag, r["y"], v))
rows = sorted(set(k for _, _, v in cols for k in v))
rhs = {k: Fr(0) for k in rows}; rhs["__b"] = Fr(1)
n = len(cols); A = [[cols[j][2].get(k, Fr(0)) for j in range(n)] + [rhs[k]] for k in rows]
# exact Gaussian elimination
piv, r0 = [], 0
for col in range(n):
    p = next((i for i in range(r0, len(A)) if A[i][col] != 0), None)
    if p is None: continue
    A[r0], A[p] = A[p], A[r0]; pv = A[r0][col]; A[r0] = [x / pv for x in A[r0]]
    for i in range(len(A)):
        if i != r0 and A[i][col] != 0:
            f = A[i][col]; A[i] = [x - f * y for x, y in zip(A[i], A[r0])]
    piv.append(col); r0 += 1
incons = any(all(x == 0 for x in row[:n]) and row[n] != 0 for row in A)
free = [j for j in range(n) if j not in piv]
val = [None] * n
for j in free: val[j] = Fr(cols[j][1]).limit_denominator(10 ** 6)
for i, col in enumerate(piv): val[col] = A[i][n] - sum(A[i][j] * val[j] for j in free)
neg = [j for j in range(n) if val[j] < 0]
bound = sum(val[j] for j in range(n) if cols[j][0] == "dec")
print("class %s d %d: support %d (dec %d, lo %d, hi %d), recompute mismatches %d, equations %d, free %d, inconsistent %s, negative %d" %
      (cls, c["d"], n, len(c["dec"]), len(c["lo"]), len(c["hi"]), bad, len(rows), len(free), incons, len(neg)))
ok = bad == 0 and not incons and not neg
print("EXACT bound %s = %.6f (float LP %.6f): %s" % (bound, float(bound), c["float_bound"], "CERTIFIED" if ok else "NOT CERTIFIED"))
