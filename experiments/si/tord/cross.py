#!/usr/bin/env python3
"""L-SI box 30 (N5-TORD-box30.md §10): crossings in |D| = 1 frozen W-phases with c1 = c2. Per frozen W-phase: E := epochs, per vertex the
number of ENTRIES (U -> S) and EXITS (S -> U); TC := transitions that change S. Reports maxima of E, TC, entries/exits per vertex, and
CONJECTURE-style counters: EX2_V (some vertex exits twice), EN2_V (enters twice), RE_V (exits and later re-enters).
Usage: cross.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, avoid
from fwphase import fwphases
C = Counter(); MX = {}; EX = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if len(D) != 1: continue
            o = next(iter(D))
            if R[a]["vs"][o][0] != R[a]["W"][o][0]: continue
            C["fw_same"] += 1
            Sp = [set(range(n)) - avoid(R[t]["wn"], D, n) for t in range(a, b + 1)]
            ent, ext, tc = Counter(), Counter(), 0
            hist = {}
            for q in range(1, len(Sp)):
                if Sp[q] != Sp[q - 1]: tc += 1
                for v in Sp[q] - Sp[q - 1]: ent[v] += 1; hist.setdefault(v, []).append(("in", a + q))
                for v in Sp[q - 1] - Sp[q]: ext[v] += 1; hist.setdefault(v, []).append(("out", a + q))
            if any(c >= 2 for c in ext.values()): C["EX2_V"] += 1
            if any(c >= 2 for c in ent.values()): C["EN2_V"] += 1
            re = [v for v, h in hist.items() if any(h[k][0] == "out" and any(x[0] == "in" for x in h[k + 1:]) for k in range(len(h)))]
            if re:
                C["RE_V"] += 1
                if len(EX) < 6: EX.append(("RE", name, a, b, re[:4], hist[re[0]], n))
            for k, v in (("tc", tc), ("maxent", max(ent.values(), default=0)), ("maxext", max(ext.values(), default=0)),
                         ("totcross", sum(ent.values()) + sum(ext.values()))):
                if v > MX.get(k, (0,))[0]: MX[k] = (v, name, a, b, n)
            if tc > 0: C["fw_same_tc>0"] += 1

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
    print("maxima:", MX)
    for z in EX: print("EXAMPLE", z)

if __name__ == "__main__": main()
