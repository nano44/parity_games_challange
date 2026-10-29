#!/usr/bin/env python3
"""L-SI box 30 (N5-TORD-box30.md §10): W-silent transitions (σ changes, W does not) inside frozen W-phases. Per frozen W-phase: the
longest run of consecutive W-silent transitions (SILRUN), and for |D| = 1 with c1 = c2: TC (trap-changing transitions) against WCH.
Counters: SIL2 (frozen W-phases with two consecutive W-silent transitions), TCW_V (TC > WCH + 1), SILEXIT_V (a W-silent transition of a
|D| = 1, c1 = c2 frozen W-phase where S does not strictly shrink or a switched vertex does not exit: Lemma SIL-EXIT).
Usage: silent.py --list FILE | --one GAME [START]"""
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
            sil = [R[t]["W"] == R[t + 1]["W"] for t in range(a, b)]
            run = best = 0
            for x in sil:
                run = run + 1 if x else 0; best = max(best, run)
            C["fw"] += 1
            if best >= 2:
                C["SIL2"] += 1
                if len(EX) < 5: EX.append(("SIL2", name, a, b, best, len(D), n))
            if best > MX.get("silrun", (0,))[0]: MX["silrun"] = (best, name, a, b, len(D), n)
            if len(D) == 1:
                o = next(iter(D))
                if R[a]["vs"][o][0] == R[a]["W"][o][0]:
                    Sp = [set(range(n)) - avoid(R[t]["wn"], D, n) for t in range(a, b + 1)]
                    tc = sum(1 for q in range(1, len(Sp)) if Sp[q] != Sp[q - 1]); wch = sum(1 for x in sil if not x)
                    if tc > wch + 1: C["TCW_V"] += 1; EX.append(("TCW", name, a, b, tc, wch, n))
                    for q in range(len(sil)):              # Lemma SIL-EXIT: a W-silent transition only shrinks S
                        if sil[q]:
                            C["sil_same"] += 1; t = a + q
                            sw = [v for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]]
                            if not (Sp[q + 1] < Sp[q] and all(v in Sp[q] and v not in Sp[q + 1] for v in sw)):
                                C["SILEXIT_V"] += 1; EX.append(("SILEXIT", name, a, b, t, sw[:4], n))
                    r = tc / max(wch, 1)
                    if r > MX.get("tc/wch", (0,))[0]: MX["tc/wch"] = (r, tc, wch, name, a, b, n)

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
    for z in EX[:8]: print("EXAMPLE", z)

if __name__ == "__main__": main()
