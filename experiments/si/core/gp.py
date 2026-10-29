#!/usr/bin/env python3
"""L-SI box 31 (docs/si/N5-SPC-box31.md §2): Lemma GP (timely Lemma P) on frozen W-phases [a, b] with D != {} whose gates are all
same-pair (lambda_Xi(d) = lambda_W(d)); control D = {}. Timely BF: B_0(x) := (x, {}, 0) for the cycle nodes of state a; B_{j+1}(x) := max of
B_j(x) and x (+) B_j(z) over the ALLOWED successors z of x at state a + j: Odd x: tau(x); Even x: rho_{a+j}(x), every z with (x, z) in
I_sigma at a + j, and every z in U_{a+j} (z's (rho, tau)-play avoids D); simple paths only (x not on z's stored path).
GP: W_{a+j} >= B_j pointwise for every j <= b - a [GP_V]. PLUS=1: GP+ (also z in x's basin S_d when d satisfies G3 at a + j).
B0=W: B_0 := W_a with its play paths (base variant). MUT=all (every successor allowed) is the control that must bite (MUT=noU only weakens the statement).
LATE = W-changing transitions k -> k+1 with k - a >= n - 1;
R = adoptions (rho_{k+1}(x) = z != rho_k(x)) of an edge (x, z) that was NOT allowed (in the GP+ sense) at an earlier state of the phase;
RED_V := WCH > n - 1 + n R (Corollary FW-R, a proved reduction; a violation would be a bug); RLIN_V := R > n - 1 (CONJECTURE R-LIN,
DEAD: core/instances/rlin_cex_n40). R_T := transitions with at least one late adoption; RED_V also checks WCH > (n - 1)(R_T + 1). Usage: gp.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, avoid
from fwphase import fwphases
sys.path.insert(0, os.path.join(HERE, "..", "tord")); from gates import basins
STAR = os.environ.get("STAR") == "1"   # GP* (note §6): every successor except the BLOCKED ones (W_k(z) > W_k(rho_k x), (x, z) not in I_sigma); R then counts late adoptions*
PLUS = os.environ.get("PLUS") == "1"   # GP+: also every z in the same basin S_d as x at a + j, if d satisfies G3 then (core note §2)
C = Counter(); MX = {}; EX = []
MUT = os.environ.get("MUT", "")

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if D and not all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D): continue
            cls = "ctrl" if not D else ("D1" if len(D) == 1 else "D2+"); C[cls] += 1
            lam = [w[0] for w in R[a]["W"]]; t = R[a]["t"]
            if os.environ.get("B0") == "W":       # B_0 := W_a with the play path of x up to its cycle node (GP0 form)
                P = []
                for x in range(n):
                    y, msk = x, 0
                    while y != lam[x]: msk |= 1 << y; y = R[a]["wn"][y]
                    P.append((R[a]["W"][x], msk | (1 << y)))
            else: P = [((x, 0, 0), 1 << x) if lam[x] == x else None for x in range(n)]
            viol = 0; late = 0; REF = set(); radopt = 0; rT = 0
            for k in range(a, b):
                if k - a >= n - 1 and R[k]["W"] != R[k + 1]["W"]: late += 1
                U = avoid(R[k]["wn"], D, n) if D else set(range(n))
                if MUT == "noU": U = set()
                Fk = basins(R[k]["wn"], D, n) if D else [-1] * n
                G3k = {d for d in D if Fk[R[k]["t"][d]] != d and Fk[R[k]["sb"][d]] != d}   # G3 at state k: d's two tails leave S_d
                Is = {}
                for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): Is.setdefault(x, set()).add(z)
                Q = list(P)
                for x in range(n):
                    if g.owner[x] == 1: al = [t[x]]
                    else:
                        al = {R[k]["s"][x]} | Is.get(x, set()) | {z for z in g.succ[x] if z in U}
                        if PLUS and Fk[x] != -1 and Fk[x] in G3k: al |= {z for z in g.succ[x] if Fk[z] == Fk[x]}
                    if STAR and g.owner[x] == 1: pass
                    elif STAR:
                        kr = E.key(R[k]["W"][R[k]["s"][x]])
                        al = {z for z in g.succ[x] if z in Is.get(x, set()) or z == R[k]["s"][x] or E.key(R[k]["W"][z]) <= kr}
                    if MUT == "all" and g.owner[x] == 0: al = g.succ[x]
                    for z in al:
                        if P[z] is None or (P[z][1] >> x) & 1: continue
                        v = E.extend(x, P[z][0])
                        if Q[x] is None or E.key(v) > E.key(Q[x][0]): Q[x] = (v, P[z][1] | (1 << x))
                r0 = radopt
                for x in range(n):                       # R: adoptions of edges not ALLOWED+ at an earlier state (§4)
                    if g.owner[x] == 0 and R[k + 1]["s"][x] != R[k]["s"][x] and (x, R[k + 1]["s"][x]) in REF: radopt += 1
                    if g.owner[x] == 0 and D:
                        al = {R[k]["s"][x]} | Is.get(x, set()) | {z for z in g.succ[x] if z in U}
                        if Fk[x] != -1 and Fk[x] in G3k: al |= {z for z in g.succ[x] if Fk[z] == Fk[x]}
                        if STAR:
                            kr = E.key(R[k]["W"][R[k]["s"][x]])
                            al = {z for z in g.succ[x] if z in Is.get(x, set()) or z == R[k]["s"][x] or E.key(R[k]["W"][z]) <= kr}
                        REF |= {(x, z) for z in g.succ[x] if z not in al}
                rT += radopt > r0
                P = Q; W = R[k + 1]["W"]
                bad = [x for x in range(n) if P[x] is not None and E.key(W[x]) < E.key(P[x][0])]
                if bad:
                    viol += 1
                    if len(EX) < 8: EX.append(("GP", cls, name, a, b, k + 1, bad[:5]))
            wch = sum(1 for q in range(a, b) if R[q]["W"] != R[q + 1]["W"])
            if wch > n - 1 + n * radopt or wch > (n - 1) * (rT + 1): C["RED_V"] += 1
            if rT / (n - 1) > MX.get(cls + ":R_T/(n-1)", (-1,))[0]: MX[cls + ":R_T/(n-1)"] = (rT / (n - 1), rT, wch, n, len(D), name, a, b)
            C[cls + "_R>0"] += radopt > 0
            if radopt > n - 1: C["RLIN_V"] += 1; EX.append(("RLIN", cls, name, a, b, radopt, n))
            if radopt / (n - 1) > MX.get(cls + ":R/(n-1)", (-1,))[0]: MX[cls + ":R/(n-1)"] = (radopt / (n - 1), radopt, wch, n, len(D), name, a, b)
            if radopt > MX.get(cls, (-1,))[0]: MX[cls] = (radopt, wch, b - a, n, len(D), name, a, b)
            C[cls + "_GP_V"] += viol > 0; C[cls + "_late>0"] += late > 0
            if viol: C["GP_V"] += 1

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
    print("max R (R, WCH, L, n, |D|, game, a, b):", MX)
    for z in EX: print("EXAMPLE", z)
    print("GP", "PASS" if "GP_V" not in C else "FAIL")
    print("RED", "PASS" if "RED_V" not in C else "FAIL")
    print("RLIN", "PASS" if "RLIN_V" not in C else "FAIL")

if __name__ == "__main__": main()
