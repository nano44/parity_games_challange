#!/usr/bin/env python3
"""L-SI box 29: inside each W-phase (wphase.py), REONLY = transitions whose Even switches all enter edges already entered earlier in the
same W-phase (no FRESH edge); FRESHE = transitions that enter some Even edge that was the sigma-value at the W-phase start or entered
before... (see note). CANDIDATE FRESH-EDGE: REONLY = 0 (would give L <= m_E per W-phase). Usage: fresh.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from wphase import wphases
C = Counter(); EX = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in wphases(R, i, j):
            seen = set((v, R[a]["s"][v]) for v in range(n) if g.owner[v] == 0); reonly = 0; reonly0 = 0; seen1 = set()
            for t in range(a, b):
                sw = [(v, R[t + 1]["s"][v]) for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]]
                if all(e in seen1 for e in sw): reonly += 1
                if all(e in seen for e in sw): reonly0 += 1
                seen |= set(sw); seen1 |= set(sw)
            C["wphases"] += 1
            if reonly: C["REONLY_V"] += 1; EX.append(("REONLY", name, a, b, reonly, n))
            if reonly0: C["REONLY0_V"] += 1; EX.append(("REONLY0 (start edges count as seen)", name, a, b, reonly0, n))

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
    for z in sorted(EX, key=lambda z: -z[4])[:5]: print("EXAMPLE", z)
    for k in ("REONLY", "REONLY0"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
