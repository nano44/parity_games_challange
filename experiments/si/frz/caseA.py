#!/usr/bin/env python3
"""L-SI box 29: R17 Lemma P's Case A read in the W frame, inside frozen W-phases (fwphase.py): CASEA_V counts (t, x, z), x Even, z a
successor of x with (x, z) NOT in I_t (Xi-improving set) and z != sigma_t(x), but W_t(z) strictly better than W_t(sigma_t x) (comparison of
the successors' W-values, as in R17's Case A). Also CASEA_ALL over all non-fb in-phase transitions (unfrozen). Usage: caseA.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, Engine
from fwphase import fwphases
C = Counter(); EX = []; EXB = []

def _run(E, g, R, name):
    n = g.n; EN = Engine(g)
    for i, j in phases(R):
        inside = set()
        for a, b in fwphases(R, i, j): inside |= set(range(a, b + 1))
        for t in range(i, j + 1):
            A = R[t]; I = set(EN.improving(tuple(A["s"]), A["vs"]))
            for x in range(n):
                if g.owner[x] != 0: continue
                for z in set(g.succ[x]):
                    if z == A["s"][x] or (x, z) in I: continue
                    if E.key(A["W"][z]) > E.key(A["W"][A["s"][x]]):
                        C["CASEA_ALL"] += 1
                        if t in inside:
                            C["CASEA_V"] += 1
                            if len(EX) < 6: EX.append((name, t, x, z, A["s"][x], A["W"][z], A["W"][A["s"][x]], A["vs"][z], A["vs"][A["s"][x]]))
            C["states"] += 1; C["states_inside"] += t in inside
            if t < j and not A["fb"]:
                B = R[t + 1]
                for (x, z) in I:                       # Case B in the Xi frame (r17.py STALL): the honest switch x -> z beats the choice
                    if B["s"][x] == z or A["vs"][z][0] == x: continue
                    if E.key(E.extend(x, A["vs"][z])) > E.key(B["vs"][x]):
                        C["CASEB_ALL"] += 1
                        if t in inside and t + 1 in inside:
                            C["CASEB_V"] += 1
                            if len(EXB) < 4: EXB.append((name, t, x, z, A["s"][x], B["s"][x]))

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
    for z in EX: print("EXAMPLE (game, t, x, z, sigma x, W(z), W(sigma x), Xi(z), Xi(sigma x))", z)
    for z in EXB: print("EXAMPLE B (game, t, x, z, sigma_t x, sigma_t+1 x)", z)
    print("CASEA", "PASS" if "CASEA_V" not in C else "FAIL"); print("CASEB", "PASS" if "CASEB_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
