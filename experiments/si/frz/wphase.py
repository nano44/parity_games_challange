#!/usr/bin/env python3
"""L-SI box 29 (docs/si/N5-FRZ-box29.md): the W FRAME. Inside an N5 phase (lambda_Xi, tau constant) cut at S4c fallback transitions and at
transitions that change the W cycle-node map lambda_W (W = val(sigma_t, tau), the one-player game G_tau). A W-PHASE is a maximal run of
transitions with no fallback and lambda_W constant at both ends. Per W-phase: L, WCH (W-changing), NMw (most W-carries of one vertex),
PCHw (most W P-changes of one vertex), LONw (most length-only W rises of one vertex), |D| (Odd u with sigma-bar != tau at some state),
SBCH (sigma-bar-changing transitions), n, m. Per phase: L, fallbacks FB, lambda_W-changing non-fb transitions LWCH, W-silent non-fb
transitions WSIL, W-phases count. Checks: WMON_V (W falls at a non-fb transition), CNW_V (a vertex's W cycle node changes to a worse
reward at a non-fb transition), R17W_V (a W-phase with >= n + m transitions: R17 (c)'s bound read in the W frame).
Usage: wphase.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "chg"))
from common import rows, load, readstart, phases
from compose import matched, bits
C = Counter(); TOP = []; PTOP = []; EX = []; ETOP = []

def wphases(R, i, j):
    out, a = [], i
    for t in range(i, j):
        cut = R[t]["fb"] or tuple(x[0] for x in R[t]["W"]) != tuple(x[0] for x in R[t + 1]["W"])
        if cut:
            if t > a: out.append((a, t))
            a = t + 1
    if j > a: out.append((a, j))
    return out

def _run(E, g, R, name):
    n = g.n; m = sum(len(set(g.succ[v])) for v in range(n)); rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
    rew = lambda c: (E.rank[c] if E.par[c] == 0 else -E.rank[c])
    for i, j in phases(R):
        fb = sum(R[t]["fb"] for t in range(i, j)); lw = wsil = 0
        for t in range(i, j):
            A, B = R[t], R[t + 1]
            if A["fb"]: continue
            if A["W"] == B["W"]: wsil += 1
            for v in range(n):
                if E.key(B["W"][v]) < E.key(A["W"][v]): C["WMON_V"] += 1; EX.append(("WMON", name, t, v))
                if A["W"][v][0] != B["W"][v][0] and rew(B["W"][v][0]) < rew(A["W"][v][0]): C["CNW_V"] += 1
            lw += tuple(x[0] for x in A["W"]) != tuple(x[0] for x in B["W"])
        WP = wphases(R, i, j); C["phases"] += 1; C["wphases"] += len(WP); C["WSIL"] += wsil
        PTOP.append((j - i, name, i, j, fb, lw, wsil, len(WP), n))
        for a, b in WP:
            nm = Counter(); pc = Counter(); lo = Counter(); wch = 0; ent = Counter(); esw = 0
            for t in range(a, b):
                for v in range(n):
                    if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: ent[(v, R[t + 1]["s"][v])] += 1; esw += 1
                wch += R[t]["W"] != R[t + 1]["W"]
                for x in range(n):
                    p, q = R[t]["W"][x], R[t + 1]["W"][x]
                    if p == q: continue
                    if p[1] == q[1]: lo[x] += 1; continue
                    pc[x] += 1; rc = E.rank[p[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
                    if not matched(bits(p[1]), bits(q[1]), w, odd): nm[x] += 1
            D = {u for u in range(n) if g.owner[u] == 1 and any(R[t]["sb"][u] != R[t]["t"][u] for t in range(a, b + 1))}
            sbch = sum(1 for t in range(a, b) if R[t]["sb"] != R[t + 1]["sb"])
            L = b - a; mE = sum(len(set(g.succ[v])) for v in range(n) if g.owner[v] == 0)
            if max(ent.values(), default=0) > 1: C["ENT1_V"] += 1
            if esw > mE: C["ESWM_V"] += 1
            if L > mE: C["LME_V"] += 1
            ETOP.append((max(ent.values(), default=0), esw, mE, L, name, a, b, n))
            if L >= n + m: C["R17W_V"] += 1; EX.append(("R17W", name, a, b, L, n, m))
            TOP.append((L, name, a, b, wch, max(nm.values(), default=0), max(pc.values(), default=0), max(lo.values(), default=0), len(D), sbch, n, m))

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
    print("W-phase columns: L, game, a, b, WCH, NMw, PCHw, LONw, |D|, SBCH, n, m")
    for z in sorted(TOP, key=lambda z: -z[0])[:5]: print("TOP", z)
    if TOP:
        for k, lab in ((0, "L"), (4, "WCH"), (5, "NMw"), (6, "PCHw"), (7, "LONw")):
            z = max(TOP, key=lambda z: (z[k] / z[10], z[1])); print("max %s/n = %.3f" % (lab, z[k] / z[10]), z)
        z = max(TOP, key=lambda z: (z[0] / (z[10] + z[11]), z[1])); print("max L/(n+m) = %.3f" % (z[0] / (z[10] + z[11])), z)
    print("phase columns: L, game, i, j, FB, LWCH (lambda_W-changing non-fb), WSIL (W-silent non-fb), #W-phases, n")
    for z in sorted(PTOP, key=lambda z: -z[0])[:4]: print("PTOP", z)
    if PTOP:
        z = max(PTOP, key=lambda z: (z[5] / z[8], z[1])); print("max LWCH/n = %.3f" % (z[5] / z[8]), z)
    for z in EX[:4]: print("EXAMPLE", z)
    print("ENT columns: max entries of one Even edge, Even switches, m_E, L, game, a, b, n")
    for z in sorted(ETOP, key=lambda z: (-z[0], -z[1]))[:3]: print("ETOP", z)
    if ETOP: z = max(ETOP, key=lambda z: (z[1] / z[2], z[4])); print("max ESW/m_E = %.3f" % (z[1] / z[2]), z); z = max(ETOP, key=lambda z: (z[3] / z[2], z[4])); print("max L/m_E = %.3f" % (z[3] / z[2]), z)
    for k in ("WMON", "CNW", "R17W", "ENT1", "ESWM", "LME"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
