#!/usr/bin/env python3
"""Box 49 DATA (successor 29, queue item 3 (b); N5-KPOLY §9 (a) / §12): offsets inside p-runs. Per phase, class c, level x in Q_c := Q n U_c - {c},
x-pieces cut at EXIT_x u ZC'' (ZC'' := CYC n ZCH n FT, N5-KPOLY §11). Inside a piece (p := par(x) fixed), the p-RUNS: maximal runs of the piece's
states with kappa(p) constant (R58's q-run, restricted to the piece). Per p-run: VR := distinct values of off(x; p), RR := strict rises of
off(x; p) between consecutive states of the run, FBR := in-phase fallbacks with source in the run, ER := rises before the run's w_c-th fallback
source (w_c := |U_c| - 1; EARLY, R61 (b)'s window), LR := the other rises (LATE), RFB := rises AT a fallback transition. _DIR / _REL: p = c (x direct) / p in Q. Per piece: OR := strict
rises over the piece, KP := kappa(p)-changes inside the piece. Prints totals, maxima, and the hypotheses' violation counts:
  HA  VR > d_x                  (off takes at most d_x values per p-run)
  HB  ER > FBR_early            (early rises at most one per early fallback)
  HC  RR > RFB + (d_x - 1)      (non-fallback rises at most d_x - 1 per p-run)
  HD  OR > d_x * (KP + 1)       (per piece, at most d_x values per p-run, summed)
  HE  LR > d_x - 1              (late values at most d_x, R61 (b)'s |S| <= d_q, per p-run; must be 0 if SAT-k's window applies)
Usage: orun.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
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
def par(A, x, Q, c):
    nx, y, seen = A["nxt"], A["nxt"][x], {x}
    while y != c and y not in seen:
        if y in Q: return y
        seen.add(y); y = nx[y]
    return c
def run(g, start, nm):
    E, R = rows(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases")
        for c in {R[i]["vs"][v][0] for v in range(n)}:
            U = [v for v in range(n) if R[i]["vs"][v][0] == c]; w = len(U) - 1
            sc = 1 if E.par[c] == 1 else -1
            kap = lambda S, v: (M(E, S["vs"][v]), sc * S["vs"][v][2])
            F = lambda kk: kk[0] == 0 and kk[1] != 0
            X = [x for x in U if x in Q and x != c]
            cut = set()
            for k in range(i, j):
                za, zb = cyc_seq(R[k], c), cyc_seq(R[k + 1], c)
                if za != zb and any(x in za for x in X) and any(kap(R[k], z) != kap(R[k + 1], z) and (F(kap(R[k], z)) or F(kap(R[k + 1], z))) for z in U if z != c):
                    cut.add(k)
            for x in X:
                dx = len([y for y in g.succ[x]])
                pr = [par(R[k], x, Q, c) for k in range(i, j + 1)]
                pieces, cur = [], [i]
                for k in range(i, j):
                    if pr[k - i] != pr[k + 1 - i] or k in cut: pieces.append(cur); cur = [k + 1]
                    else: cur.append(k + 1)
                pieces.append(cur)
                for pc in pieces:
                    if len(pc) < 2: continue
                    p = pr[pc[0] - i]
                    off = {k: tuple(a - b for a, b in zip(kap(R[k], x), kap(R[k], p))) for k in pc}
                    runs, cr = [], [pc[0]]
                    for k in pc[1:]:
                        if kap(R[k], p) != kap(R[k - 1], p): runs.append(cr); cr = [k]
                        else: cr.append(k)
                    runs.append(cr)
                    OR = sum(1 for k in pc[:-1] if off[k + 1] > off[k]); KP = len(runs) - 1
                    inc("pieces"); inc("OR", OR); inc("KP", KP); mx("max_OR", OR)
                    if OR > dx * (KP + 1): inc("HD")
                    for rn in runs:
                        inc("pruns")
                        VR = len({off[k] for k in rn}); fbs = [k for k in rn[:-1] if R[k]["fb"]]
                        wth = fbs[w - 1] if len(fbs) >= w and w >= 1 else (rn[0] - 1 if w == 0 else None)
                        RR = ER = LR = RFB = FBE = 0
                        for k in rn[:-1]:
                            early = wth is None or k < wth
                            if R[k]["fb"] and early: FBE += 1
                            if off[k + 1] > off[k]:
                                RR += 1; RFB += 1 if R[k]["fb"] else 0
                                if early: ER += 1
                                else: LR += 1
                        tag = "DIR" if p == c else "REL"
                        inc("RR_" + tag, RR); mx("max_RR_" + tag, RR); inc("pruns_" + tag)
                        if RR > RFB + dx - 1: inc("HC_" + tag)
                        inc("RR", RR); inc("ER", ER); inc("LR", LR); inc("RFB", RFB); mx("max_VR", VR); mx("max_RR", RR); mx("max_ER", ER)
                        if VR > dx: inc("HA")
                        if ER > FBE: inc("HB")
                        if RR > RFB + dx - 1: inc("HC")
                        if LR > dx - 1: inc("HE")
                        TOP.append((RR, ER, LR, RFB, VR, dx, len(rn), w, g.n, nm))
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
    for k in ("HA", "HB", "HC", "HD", "HE"): C.setdefault(k, 0)
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for t in sorted(TOP, reverse=True)[:8]: print("  top (RR ER LR RFB VR d_x len w n name):", *t)
