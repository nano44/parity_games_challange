#!/usr/bin/env python3
"""Box 48 DATA (N5-KPOLY §7): Lemma OFFSET-MONO' (no region hypothesis). At an in-phase transition t -> t+1, for q in Q, q != c, q on no honest
cycle at t, p := par_{t+1}(q) (the first vertex of Q - {q} on q's honest play at t+1 before c; c if none), y2 := sigma-bar_{t+1}(q):
claim Delta_{t+1}(q) >= Delta_t(q), Delta_s(x) := K_s(x) - K_s(p), unless LOOP (y2's honest play at t passes q).
K is checked in two forms: M only (path weight), and the pair (M, sgn*len) in lexicographic order for both signs sgn = +1, -1 (one of them is
the class order of RESULTS R56 (M1kappa); the claim must hold for that one). Violations: V_M, V_K+ , V_K- (split by LOOP / not LOOP).
K's length sign is set per class from the parity of c (V_Kc), with the opposite sign as a control (V_Kx). (A farther Odd choice vertex on the
chain is NOT a control: offsets telescope along the chain.) MUT=1: p := a vertex of U_c NOT on q's (t+1)-play (must bite).
Usage: offmono2.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, M, load, readstart
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
MUT = os.environ.get("MUT") == "1"
def play(A, z):
    nx, c = A["nxt"], A["vs"][z][0]; out, x, seen = [], z, set()
    while x not in seen and x != c: seen.add(x); out.append(x); x = nx[x]
    return out, x == c
def oncycle(A, q):
    nx = A["nxt"]; x, seen = nx[q], set()
    while x not in seen:
        if x == q: return True
        seen.add(x); x = nx[x]
    return False
def run(g, start, nm):
    E, R = rows(g, start)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases")
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            for q in Q:
                c = A["vs"][q][0]
                if c == q or oncycle(A, q): continue
                pl, ok = play(B, q)
                qs = [x for x in pl[1:] if x in Q]
                p = qs[0] if qs else c
                if MUT:
                    off = [x for x in range(g.n) if A["vs"][x][0] == c and B["vs"][x][0] == c and x not in pl and x != c]
                    if not off: continue
                    p = off[0]
                y2 = B["nxt"][q]; loop = q in play(A, y2)[0]
                inc("checks"); tag = "_LOOP" if loop else ""
                if loop: inc("LOOP")
                if q != B["sb"][q] and False: pass
                ka = lambda S, x, sg: (M(E, S["vs"][x]), sg * S["vs"][x][2])
                dM = (M(E, B["vs"][q]) - M(E, B["vs"][p])) - (M(E, A["vs"][q]) - M(E, A["vs"][p]))
                if dM < 0: inc("V_M" + tag)
                sc = 1 if E.par[c] == 1 else -1     # per-class sign; "V_Kc" uses it, "V_Kx" the opposite (control for the sign)
                for sg, nmK in ((sc, "V_Kc"), (-sc, "V_Kx")):
                    a1, a2 = ka(B, q, sg), ka(B, p, sg); b1, b2 = ka(A, q, sg), ka(A, p, sg)
                    d = (a1[0] - a2[0] - b1[0] + b2[0], a1[1] - a2[1] - b1[1] + b2[1])
                    if d < (0, 0): inc(nmK + tag)
                if p != c and qs and A["vs"][q][0] == c:
                    pa, _ = play(A, q); pt = [x for x in pa[1:] if x in Q]
                    if (pt[0] if pt else c) != p: inc("parent_changed_checks")
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
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
