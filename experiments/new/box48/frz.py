#!/usr/bin/env python3
"""Box 49 DATA (successor 29, N5-KPOLY §12): a general-game analogue of RESULTS R50 (c) FRZ-U (routes freeze after r - 1 transitions of a
fallback-free run on C^1O). Per phase and class c (U := lambda^-1(c), w := |U| - 1): the RUNS are the maximal runs of in-phase transitions
with no fallback (the transition fb flag). For z in U and a run S with first state s0, a transition k -> k+1 of S with k - s0 >= w that
changes M(kappa(z)) (the path-weight component) is a late M-change:
  FRZ_D_V  late M-changes at Odd choice vertices z in Q_c that are DIRECT at k and k+1 (honest play meets c before any other vertex of Q_c);
  FRZ_A_V  late M-changes at any z in U - {c}.
Also: per run and z, the number of kappa(z)-changes (KCH) and of M-changes (MCH); maxima; the largest k - s0 of an M-change (LASTM) against w.
Usage: frz.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart, M
C = {}; TOP = []
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def direct(A, x, Q, c):
    nx, y, seen = A["nxt"], A["nxt"][x], {x}
    while y != c and y not in seen:
        if y in Q: return False
        seen.add(y); y = nx[y]
    return True
def run(g, start, nm):
    E, R = rows(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases")
        runs, cur = [], [i]
        for k in range(i, j):
            if R[k]["fb"]: runs.append(cur); cur = [k + 1]
            else: cur.append(k + 1)
        runs.append(cur)
        for c in {R[i]["vs"][v][0] for v in range(n)}:
            U = [v for v in range(n) if R[i]["vs"][v][0] == c]; w = len(U) - 1
            for S in runs:
                if len(S) < 2: continue
                inc("runs"); s0 = S[0]
                for z in U:
                    if z == c: continue
                    kch = mch = 0
                    for k in S[:-1]:
                        a, b = R[k]["vs"][z], R[k + 1]["vs"][z]
                        if a != b: kch += 1
                        if M(E, a) != M(E, b):
                            mch += 1; mx("LASTM_minus_w", k - s0 - w)
                            if k - s0 >= w:
                                inc("FRZ_A_V")
                                if os.environ.get("VERB") == "1": print("   late", nm, "w", w, "pos", k - s0, "z", z, "inQ", z in Q, "mc", len([q for q in Q if q in U and q != c]), "runlen", len(S) - 1, "M", M(E, a), "->", M(E, b), "len", a[2], "->", b[2], "c", c, "par_c", E.par[c])
                                if z in Q and direct(R[k], z, Q, c) and direct(R[k + 1], z, Q, c): inc("FRZ_D_V")
                    mx("max_KCH", kch); mx("max_MCH", mch); inc("KCH", kch); inc("MCH", mch)
                    if z in Q: mx("max_KCH_Q", kch); mx("max_MCH_Q", mch)
                    TOP.append((mch, kch, len(S) - 1, w, z in Q, g.n, nm))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        gs = [(l.split()[0], load(os.path.join(ROOT, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    for k in ("FRZ_A_V", "FRZ_D_V"): C.setdefault(k, 0)
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for t in sorted(TOP, reverse=True)[:6]: print("  top (MCH KCH runlen w inQ n name):", *t)
