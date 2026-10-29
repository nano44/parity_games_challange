#!/usr/bin/env python3
"""L-SI box 31 (docs/si/N5-SPC-box31.md §5): anatomy of LATE ADOPTIONS in same-pair frozen W-phases. A late adoption (x, tau): Even x
switches to z = rho_{tau+1}(x) and (x, z) was not ALLOWED+ (gp.py) at some earlier state t of the phase. Per late adoption: class by the
basins of x at tau and tau+1 ("U>S" = x enters a basin, "S>S'" = x changes basin, "same" = no basin change of x), the number of earlier
refusal states, whether the transition tau -> tau+1 changes W. Per phase: R, per-vertex max, per-edge max, R_entry (U>S), TC.
Usage: late.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart, phases, avoid
from fwphase import fwphases
from gates import basins
C = Counter(); MX = {}; EX = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D or not all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D): continue
            F = [basins(R[t]["wn"], D, n) for t in range(a, b + 1)]
            REF = Counter(); perv = Counter(); pere = Counter(); r = 0; tc = sum(1 for q in range(b - a) if F[q] != F[q + 1])
            for k in range(a, b):
                Fk = F[k - a]; G3k = {d for d in D if Fk[R[k]["t"][d]] != d and Fk[R[k]["sb"][d]] != d}
                Is = {}
                for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): Is.setdefault(x, set()).add(z)
                for x in range(n):
                    if g.owner[x] != 0: continue
                    z = R[k + 1]["s"][x]
                    if z != R[k]["s"][x] and REF[(x, z)]:
                        r += 1; perv[x] += 1; pere[(x, z)] += 1
                        fx0, fx1 = Fk[x], F[k + 1 - a][x]
                        cl = "same" if fx0 == fx1 else ("U>S" if fx0 == -1 else ("S>U" if fx1 == -1 else "S>S'"))
                        C["cls_" + cl] += 1; C["wchg_at_adoption"] += R[k]["W"] != R[k + 1]["W"]
                        C["zS_at_tau"] += Fk[z] != -1
                    al = {R[k]["s"][x]} | Is.get(x, set()) | {w for w in g.succ[x] if Fk[w] == -1}
                    if Fk[x] != -1 and Fk[x] in G3k: al |= {w for w in g.succ[x] if Fk[w] == Fk[x]}
                    for w in g.succ[x]:
                        if w not in al: REF[(x, w)] += 1
            if not r: continue
            C["phases_R>0"] += 1
            pv, pe = max(perv.values()), max(pere.values())
            for key, v in (("R", r), ("R/(n-1)", r / (n - 1)), ("perv", pv), ("pere", pe), ("R-TC", r - tc)):
                if v > MX.get(key, (-99,))[0]: MX[key] = (v, r, tc, pv, pe, n, len(D), name, a, b)
            if r > tc: C["R>TC"] += 1
            if pv > 1: C["perv>1"] += 1
            if pe > 1: C["pere>1"] += 1

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
    print("columns: value, R, TC, per-vertex max, per-edge max, n, |D|, game, a, b")
    for k in sorted(MX): print("MAX", k, MX[k])

if __name__ == "__main__": main()
