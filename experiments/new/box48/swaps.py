#!/usr/bin/env python3
"""Box 48 DATA (N5-KPOLY §4): pairwise order swaps between the options of an Odd choice vertex inside a phase (lower-envelope view of
sigma-bar(q) = the kappa-argmin over Y^q_t, RESULTS R56 (d)). Per phase, class c, q in Q with q != c and q on no honest cycle at t: for every
pair y, y' in succ(q) cap U_c whose honest plays at t avoid q, the sign of (M_t(y), len) - (M_t(y'), len') in the class order (M first; then
the length with the class's sign, as L-SI common's kappa; ties = 0). SWAPS(y, y') := sign changes between nonzero signs over the states where
both are options. Reports: max swaps of one pair in a phase, max sigma-bar(q) changes of one q in a phase (CH), and max d_q, and per phase
whether CH <= lambda-bound for the observed max swap order s (s = 1: CH <= d - 1; s = 2: CH <= 2d - 2) (DS_V counts violations of the
elementary s = 1, 2 forms; the general Davenport-Schinzel bound is NOT used or claimed here).
Usage: swaps.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, M, load, readstart
C = {}; TOP = []
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def avoids(A, y, q):
    nx, c = A["nxt"], A["vs"][y][0]; x, seen = y, set()
    while x not in seen:
        if x == q: return False
        if x == c: return True
        seen.add(x); x = nx[x]
    return True
def key(E, A, y):
    v = A["vs"][y]; c = v[0]; s = 1 if E.par[c] == 0 else -1
    return (M(E, v), -s * v[2])          # larger = better for Even; Odd minimises (as kappa: M first, then length with the cycle's sign)
def run(g, start, nm):
    E, R = rows(g, start)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases")
        for q in Q:
            c = R[i]["vs"][q][0]
            if c == q: continue
            ys = [y for y in g.succ[q] if R[i]["vs"][y][0] == c]
            if len(ys) < 2: continue
            last = {}; sw = {}; ch = 0; prev = None
            for t in range(i, j + 1):
                A = R[t]
                nxt = A["sb"][q]
                if prev is not None and nxt != prev: ch += 1
                prev = nxt
                opts = [y for y in ys if avoids(A, y, q)]
                ks = {y: key(E, A, y) for y in opts}
                for a in range(len(opts)):
                    for b in range(a + 1, len(opts)):
                        y, z = opts[a], opts[b]; d = (ks[y] > ks[z]) - (ks[y] < ks[z])
                        if d == 0: continue
                        if (y, z) in last and last[(y, z)] != d: sw[(y, z)] = sw.get((y, z), 0) + 1
                        last[(y, z)] = d
            s = max(sw.values(), default=0); d = len(ys)
            inc("q_phases"); mx("max_pair_swaps", s); mx("max_CH", ch); mx("max_d", d)
            C.setdefault("swap_hist", {}); C["swap_hist"][s] = C["swap_hist"].get(s, 0) + 1
            if s <= 1 and ch > d - 1: inc("DS1_V")
            if s == 2 and ch > 2 * d - 2: inc("DS2_V")
            TOP.append((ch, s, d, j - i, g.n, q, nm))
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
    h = C.pop("swap_hist", {})
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())), "| swap histogram", dict(sorted(h.items())))
    for w in sorted(TOP, reverse=True)[:8]: print("  top (CH swaps d len n q name):", *w)
