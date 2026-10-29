#!/usr/bin/env python3
"""L-SI box 29: per phase, the parameters of Theorem W-SPLIT (docs/si/N5-FRZ-box29.md): L, FB (S4c fallbacks), LWCH (non-fb transitions
changing lambda_W), SBCH (sigma-bar-changing non-fb transitions that keep lambda_W), NFW (frozen W-phases), LFW (longest frozen W-phase),
and the check WSPLIT_V: L > FB + LWCH + SBCH' + sum of frozen W-phase lengths (an accounting error; must be 0), CNW_V: some vertex changes
its W cycle node more than n - 1 times in one fallback-free stretch (Lemma CN-W says never). Usage: phstat.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from fwphase import fwphases
C = Counter(); TOP = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        fb = lw = sb = 0; cn = Counter()
        for t in range(i, j):
            if R[t]["fb"]: fb += 1; cn = Counter(); continue
            ch = [x for x in range(n) if R[t]["W"][x][0] != R[t + 1]["W"][x][0]]
            for x in ch: cn[x] += 1
            if any(cn[x] > n - 1 for x in ch): C["CNW_V"] += 1
            if ch: lw += 1
            elif R[t]["sb"] != R[t + 1]["sb"]: sb += 1
        FW = list(fwphases(R, i, j)); tot = fb + lw + sb + sum(b - a for a, b in FW)
        if tot != j - i: C["WSPLIT_V"] += 1
        C["phases"] += 1
        TOP.append((j - i, name, i, j, fb, lw, sb, len(FW), max((b - a for a, b in FW), default=0), n))

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
    print("columns: L, game, i, j, FB, LWCH, SBCH', #frozen W-phases, longest frozen W-phase, n")
    for z in sorted(TOP, key=lambda z: -z[0])[:3]: print("TOP", z)
    for k, lab in ((4, "FB"), (5, "LWCH"), (6, "SBCH'"), (7, "NFW")):
        z = max(TOP, key=lambda z: (z[k] / z[9], z[1])); print("max %s/n = %.3f" % (lab, z[k] / z[9]), z)
    for k in ("WSPLIT", "CNW"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
