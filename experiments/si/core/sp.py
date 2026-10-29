#!/usr/bin/env python3
"""L-SI box 31 (docs/si/N5-SPC-box31.md): the SAME-PAIR CORE. Frozen W-phases (frz/fwphase.py) with D != {} in which every gate d has
lambda_Xi(d) = lambda_W(d) (so lambda_Xi = lambda_W everywhere, Lemma SAME-NODE); control: D = {} (one frame, R17).
Per frozen W-phase [a, b]: L, WCH, TC (basin-changing transitions; basins as tord/gates.py), BLK (states with a blocked edge: W-improving in
G_tau but not in the arena I_sigma), BF depth: BF_0 := W_a, BF_{j+1}(x) := max(BF_j(x), x (+) BF_j(z)) over x's G_tau successors z whose
BF_j value has x's cycle node (x not its own cycle node). e_k := max j with W_k >= BF_j pointwise. DEF := max_k (min(k, J) - e_k), J := the
first j with BF_j = BF_inf. REACH := W_b = BF_inf. Checks: CTRL_V (D = {} and DEF > 0: the relative Lemma P fails in one frame).
Usage: sp.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart, phases
from fwphase import fwphases
from gates import basins
C = Counter(); MX = {}; EX = []; TOP = []

def bfseq(E, g, W0, t, lam, adm=None):
    """BF_j(x) := the best value found of a SIMPLE G_tau path of <= j edges from x to a cycle node c of the phase start (value (c, P, len),
    R17 (b)'s value(r)); simple: x not on the stored path of z. Every BF_j value is the value of a real simple path, so W_k < BF_j(x) with
    j <= k is a genuine failure of Lemma P's statement."""
    n = g.n; NEG = None
    P = [((x, 0, 0), 1 << x) if lam[x] == x else NEG for x in range(n)]; seq = [P]
    for _ in range(n):
        Q = list(P)
        for x in range(n):
            for z in ((g.succ[x] if adm is None else adm[x]) if g.owner[x] == 0 else [t[x]]):
                if P[z] is None or (P[z][1] >> x) & 1: continue
                v = E.extend(x, P[z][0])
                if Q[x] is None or E.key(v) > E.key(Q[x][0]): Q[x] = (v, P[z][1] | (1 << x))
        if [q and E.key(q[0]) for q in Q] == [p and E.key(p[0]) for p in P]: break
        seq.append(Q); P = Q
    return seq

def depth(E, W, seq):
    kw = [E.key(w) for w in W]; e = -1
    for j, B in enumerate(seq):
        if all(B[x] is None or kw[x] >= E.key(B[x][0]) for x in range(len(W))): e = j
        else: break
    return e

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            same = all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D)
            if D and not same: continue
            cls = "ctrl" if not D else ("D1" if len(D) == 1 else "D2+")
            C[cls] += 1
            lam = [w[0] for w in R[a]["W"]]
            seq = bfseq(E, g, R[a]["W"], R[a]["t"], lam); J = len(seq) - 1
            seqx = bfseq(E, g, R[a]["W"], R[a]["sb"], lam); JX = len(seqx) - 1
            adm = [set() for _ in range(n)]
            for k in range(a, b + 1):
                for x in range(n):
                    if g.owner[x] == 0: adm[x].add(R[k]["s"][x])
                if k < b:
                    for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): adm[x].add(z)
            seqa = bfseq(E, g, R[a]["W"], R[a]["t"], lam, adm); JA = len(seqa) - 1
            L = b - a; wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            F = [basins(R[t]["wn"], D, n) for t in range(a, b + 1)] if D else None
            tc = sum(1 for q in range(L) if F[q] != F[q + 1]) if D else 0
            blk = 0; dfc = 0; dfx = 0; dfm = 0; dfa = 0
            for k in range(a, b + 1):
                e = depth(E, R[k]["W"], seq); dfc = max(dfc, min(k - a, J) - e)
                dfa = max(dfa, min(k - a, JA) - depth(E, R[k]["W"], seqa))
                dfx = max(dfx, min(k - a, JX) - depth(E, R[k]["vs"], seqx)); dfm = max(dfm, min(k - a, JX) - depth(E, R[k]["W"], seqx))
                if D and k < b:
                    s = tuple(R[k]["s"]); Is = set(E.improving(s, R[k]["vs"])); Iw = set(E.improving(s, R[k]["W"]))
                    if Iw - Is: blk += 1
            reach = all(seq[-1][x] is not None and E.key(R[b]["W"][x]) == E.key(seq[-1][x][0]) for x in range(n))
            C[cls + "_reach"] += reach; C[cls + "_tc>0"] += tc > 0; C[cls + "_blk>0"] += blk > 0; C[cls + "_def>0"] += dfc > 0
            if cls == "ctrl" and dfc > 0: C["CTRL_V"] += 1; EX.append(("CTRL", name, a, b, dfc))
            C[cls + "_defX>0"] += dfx > 0; C[cls + "_defM>0"] += dfm > 0; C[cls + "_defA>0"] += dfa > 0
            if dfa > 0: C[cls + "_DEFA_V"] += 1; EX.append(("DEFA", cls, name, a, b, dfa, wch, n))
            TOP.append((cls, wch, n, len(D), L, tc, blk, dfc, J, reach, dfx, dfm, dfa, JA, name, a, b))
            for key, val in (("wch/(n-1)", wch / (n - 1)), ("def", dfc), ("tc", tc), ("defX", dfx), ("defM", dfm), ("defA", dfa)):
                k2 = cls + ":" + key
                if val > MX.get(k2, (-1,))[0]: MX[k2] = (val, name, a, b, n, len(D), wch, tc, blk, dfc, J, reach, dfx, dfm, dfa, JA)

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
    print("columns of maxima: value, game, a, b, n, |D|, WCH, TC, BLK, DEF, J, REACH, DEFX, DEFM, DEFA, JA")
    for k in sorted(MX): print("MAX", k, MX[k])
    if os.environ.get("ALL") == "1":
        for z in TOP: print("ROW", z)
    for z in EX[:8]: print("EXAMPLE", z)
    print("CTRL", "PASS" if "CTRL_V" not in C else "FAIL")

if __name__ == "__main__": main()
