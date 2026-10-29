#!/usr/bin/env python3
"""L-SI box 29 (N5-FRZ-box29.md §7): TRAP EPOCHS inside frozen W-phases [a, b] (fwphase.py). S^p_t := vertices whose (sigma_t, tau)-play
meets D (the PLAY form), S^v_t := {x : W_t(x) strictly better than Xi_t(x)} (the VALUE form). Checks: TMONO_P_V / TMONO_V_V (a vertex leaves
S^p / S^v: CONJECTURE TRAP-MONO says never). EPOCHS: maximal runs [e, f] of states with S^p constant. Per epoch: WCU (transitions changing
W at some vertex outside S^p), WCS (changing W at some vertex of S^p), |U|; R17U_V: WCU > |U| - 1 (the R17 count on the untrapped part);
EPS_V: WCS > n - 1. Usage: epoch.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, avoid
from fwphase import fwphases
C = Counter(); EX = []; MX = Counter(); MXA = {}

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            Sp = [set(range(n)) - avoid(R[t]["wn"], D, n) for t in range(a, b + 1)]
            Sv = [{x for x in range(n) if E.key(R[t]["W"][x]) > E.key(R[t]["vs"][x])} for t in range(a, b + 1)]
            for k in range(1, len(Sp)):
                if Sp[k - 1] - Sp[k]:
                    C["TMONO_P_V"] += 1
                    if len(EX) < 4: EX.append(("TMONO_P", name, a, b, a + k, sorted(Sp[k - 1] - Sp[k])[:5]))
                if Sv[k - 1] - Sv[k]: C["TMONO_V_V"] += 1
                if not Sv[k] <= Sp[k]: C["SV_NOT_IN_SP"] += 1
            e = 0; C["fw"] += 1; ne = 0
            for k in range(1, len(Sp) + 1):
                if k == len(Sp) or Sp[k] != Sp[e]:
                    f = k - 1; U = set(range(n)) - Sp[e]; wcu = wcs = 0
                    for t in range(a + e, a + f):
                        ch = {x for x in range(n) if R[t]["W"][x] != R[t + 1]["W"][x]}
                        wcu += bool(ch & U); wcs += bool(ch - U)
                    if wcu > max(len(U) - 1, 0): C["R17U_V"] += 1; EX.append(("R17U", name, a, b, a + e, a + f, wcu, len(U)))
                    if wcs > n - 1: C["EPS_V"] += 1
                    MX["wcu"] = max(MX["wcu"], wcu); MX["wcs"] = max(MX["wcs"], wcs); ne += 1
                    if wcs > MXA.get("wcs", (0,))[0]: MXA["wcs"] = (wcs, name, a, b, a + e, a + f, len(Sp[e]), n)
                    e = k
            MX["epochs"] = max(MX["epochs"], ne)

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
    print("maxima:", dict(MX), "largest WCS epoch (WCS, game, a, b, e, f, |S|, n):", MXA.get("wcs"))
    for z in EX[:6]: print("EXAMPLE", z)
    for k in ("TMONO_P", "TMONO_V", "R17U", "EPS"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
