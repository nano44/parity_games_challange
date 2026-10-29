#!/usr/bin/env python3
"""L-SI box 29 (docs/si/N5-FRZ-box29.md): FROZEN W-PHASES. Inside an N5 phase (lambda_Xi, tau constant), cut at S4c fallback transitions,
at transitions changing lambda_W (W's cycle-node map) and at transitions changing sigma-bar. A frozen W-phase is a maximal run of the
remaining transitions (tau, sigma-bar, D, lambda_Xi, lambda_W constant; no fallback). Per frozen W-phase: L, WCH (W-changing), XCH (Xi-changing),
|D|, n, m. CONJECTURE FW-BF: WCH <= n - 1 (R17 (b) in the W frame) [FWBF_V]; FW-LEN: L < n + m [FWLEN_V]; FW-WSIL: L = WCH [FWSIL_V].
Also per phase: number of sigma-bar-changing transitions SBCH. Usage: fwphase.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
C = Counter(); TOP = []; EX = []

def fwphases(R, i, j):
    out, a = [], i
    for t in range(i, j):
        cut = R[t]["fb"] or tuple(x[0] for x in R[t]["W"]) != tuple(x[0] for x in R[t + 1]["W"]) or R[t]["sb"] != R[t + 1]["sb"]
        if cut:
            if t > a: out.append((a, t))
            a = t + 1
    if j > a: out.append((a, j))
    return out

def _run(E, g, R, name):
    n = g.n; m = sum(len(set(g.succ[v])) for v in range(n))
    for i, j in phases(R):
        C["phases"] += 1; C["sbch"] += sum(1 for t in range(i, j) if R[t]["sb"] != R[t + 1]["sb"])
        for a, b in fwphases(R, i, j):
            L = b - a; wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"]); xch = sum(1 for t in range(a, b) if R[t]["vs"] != R[t + 1]["vs"])
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            C["fwphases"] += 1
            if wch > n - 1: C["FWBF_V"] += 1; EX.append(("FWBF", name, a, b, wch, len(D), n))
            if L >= n + m: C["FWLEN_V"] += 1; EX.append(("FWLEN", name, a, b, L, n, m))
            if L != wch: C["FWSIL_V"] += 1
            TOP.append((wch, name, a, b, L, xch, len(D), n, m))

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
    print("columns: WCH, game, a, b, L, XCH, |D|, n, m")
    for z in sorted(TOP, key=lambda z: -z[0])[:4]: print("TOP", z)
    if TOP:
        z = max(TOP, key=lambda z: (z[0] / (z[7] - 1), z[1])); print("max WCH/(n-1) = %.3f" % (z[0] / (z[7] - 1)), z)
        z = max(TOP, key=lambda z: (z[4] / (z[7] + z[8]), z[1])); print("max L/(n+m) = %.3f" % (z[4] / (z[7] + z[8])), z)
    for z in EX[:5]: print("EXAMPLE", z)
    for k in ("FWBF", "FWLEN", "FWSIL"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
