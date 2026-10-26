#!/usr/bin/env python3
"""Box 49 DATA (N5-KPOLY §8): CYC_c per phase. For a phase and an honest cycle node c: Z_t(c) := the vertex set of c's honest cycle at t;
CYC_c := the in-phase transitions t -> t+1 at which some q in Q - {c} with lambda(q) = c lies on Z_t(c) or Z_{t+1}(c), or c in Q and
sigma-bar(c) changes. Also: ZCH := transitions at which c's honest cycle (as a sequence from c) changes, split into ZCH_STRICT (some vertex of the new cycle with
a new successor has a strictly larger kappa) and ZCH_TIE (every such vertex is Odd with kappa unchanged); ZCH_CN_ONLY = only c's own successor changed (c excluded from the strict/tie test: kappa(c) = (0, 0)); ZCH_OTHER_V must be 0; QON := max |Q cap Z(c)|; CYCQ := (q, t) pairs. Per phase reports
max over c of CYC_c, against len and n. Usage: cyc.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart, M
C = {}; TOP = []
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def cyc_seq(A, c):
    nx = A["nxt"]; out, x = [c], nx[c]
    while x != c and len(out) <= len(nx): out.append(x); x = nx[x]
    return tuple(out)
def cycle(A, c):
    nx = A["nxt"]; out, x = [c], nx[c]
    while x != c and len(out) <= len(nx): out.append(x); x = nx[x]
    return set(out)
def run(g, start, nm):
    E, R = rows(g, start)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases"); L = j - i; best = (0, 0, 0)
        cs = {R[i]["vs"][v][0] for v in range(g.n)}
        for c in cs:
            Z = [cycle(R[t], c) for t in range(i, j + 1)]
            qc = {q for q in Q if R[i]["vs"][q][0] == c and q != c}
            cyc = zch = 0
            for k in range(j - i):
                on = any(q in Z[k] or q in Z[k + 1] for q in qc)
                cc = c in Q and R[i + k]["sb"][c] != R[i + k + 1]["sb"][c]
                if on or cc: cyc += 1
                A, B = R[i + k], R[i + k + 1]
                if cyc_seq(A, c) != cyc_seq(B, c):
                    zch += 1; sq = cyc_seq(B, c); sc = 1 if E.par[c] == 1 else -1
                    kap = lambda S, v: (M(E, S["vs"][v]), sc * S["vs"][v][2])
                    chg = [v for v in sq if A["nxt"][v] != B["nxt"][v] and v != c]
                    if A["nxt"][c] != B["nxt"][c]: inc("ZCH_c_moved_" + ("Odd" if g.owner[c] == 1 else "Even"))
                    if not chg: inc("ZCH_CN_ONLY")
                    elif any(kap(B, v) > kap(A, v) for v in chg): inc("ZCH_STRICT")
                    elif all(g.owner[v] == 1 and kap(B, v) == kap(A, v) for v in chg): inc("ZCH_TIE")
                    else: inc("ZCH_OTHER_V")
                    if any(kap(B, v) < kap(A, v) for v in chg): inc("KAPPA_FALL_V")
            mx("max_QON", max(len(qc & z) for z in Z))
            best = max(best, (cyc, zch, len(qc)))
        inc("trans", L); inc("CYC_sum", best[0]); mx("max_CYC", best[0]); mx("max_ZCH", best[1])
        if L: TOP.append((best[0], best[1], best[2], L, g.n, nm))
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
    for w in sorted(TOP, reverse=True)[:8]: print("  top (CYC_c ZCH |Q_c| len n name):", *w)
