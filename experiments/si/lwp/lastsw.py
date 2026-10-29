#!/usr/bin/env python3
"""L-SI box 26: DATA for the candidate LAST-SWITCH (docs/si/N5-LWP-box26.md): in an L-WAVE' gap [x, y] (reference b = y - 1 if the gap
closes at an event (the run end included), else y), every transition t -> t+1 (x <= t < b) contains the LAST switch in [x, b] of some Even vertex (sigma_{t+1}(v)
!= sigma_t(v) and sigma constant at v on [t+1, b]). LAST-SWITCH gives b - x <= number of Even vertices that switch in the gap <= n - 1.
Also: SWL_V counts gaps longer than (switching Even vertices + L-cuts in the gap); NEVEN_V gaps longer than the number of Even vertices.
MODE=run: the same on whole fallback-free runs (control; RUN-LIN is dead, so it must fail somewhere). Usage: lastsw.py --list F | --one G [S]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gaps import _pts, LCUTS, EVENTS
from common import rows, load, readstart
C = Counter(); EX = []; MODE = os.environ.get("MODE", "gap")

def run(g, name, start=None):
    E, R = rows(g, start)
    G = sorted({(s, e, s, e) for s, e, x, y in _pts(g, R)}) if MODE == "run" else _pts(g, R)
    for s, e, x, y in G:
        b = y - 1 if (y in EVENTS and MODE != "run") else y
        if b <= x: continue
        C["gaps"] += 1; C["trans"] += b - x
        last = {}                                   # Even v -> time of its last switch in [x, b]
        for t in range(x, b):
            for v in range(g.n):
                if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: last[v] = t
        lt = set(last.values())
        for t in range(x, b):
            if t not in lt: C["LS_V"] += 1; EX.append((name, s, e, x, y, t))
        C["excess_max_plus1000"] = max(C["excess_max_plus1000"], 1000 + (b - x) - len(last))
        nE = sum(1 for v in range(g.n) if g.owner[v] == 0); nl = sum(1 for a in LCUTS if x < a <= b)
        C["gap_minus_nEven_max_plus1000"] = max(C["gap_minus_nEven_max_plus1000"], 1000 + (b - x) - nE)
        if b - x > len(last) + nl: C["SWL_V"] += 1; EX.append(("SWL", name, x, y, b - x, len(last), nl))   # gap <= switchers + L-cuts?
        if b - x > nE: C["NEVEN_V"] += 1; EX.append(("NEVEN", name, x, y, b - x, nE))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in [z for z in EX if z[0] in ("SWL", "NEVEN")][:8] + [z for z in EX if z[0] not in ("SWL", "NEVEN")][:4]: print("EXAMPLE", z)
    print("LASTSW PASS" if "LS_V" not in C else "LASTSW FAIL")

if __name__ == "__main__":
    main()
