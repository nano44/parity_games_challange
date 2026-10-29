#!/usr/bin/env python3
"""L-SI box 26: DATA for the candidate PS-STEP (KEY=V: VS-STEP) (docs/si/N5-LWP-box26.md): inside an L-WAVE' gap [x, y], every transition t -> t+1 makes
at least one vertex P-SETTLED ((c, P) of Xi_{t+1}(v) = that of Xi_y(v), not of Xi_t(v); KEY=V: the whole valuation, VS-STEP). The settled set only grows (Xi is monotone, R15 (a), and the order is lexicographic in (c, P, l)), so PS-STEP gives
y - x <= n - |settled at x| <= n - 1. MODE=run tests the same on whole fallback-free runs (must fail on runfam_K10, RUN-LIN dead) and
MODE=seg on REL segments. Counts VS_V (transitions with no new settled vertex) and NEV (the same counting Even vertices only).
REF=pre (default): when the gap ends at an event y (run end included), the reference state is y - 1 (the event transition itself is
not asked to settle anything: at most 1 per gap). Usage: vstep.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gaps import _pts, EVENTS
for p in (os.path.join(HERE, "..", "root"),): sys.path.insert(0, p)
from common import rows, load, readstart
C = Counter(); EX = []; EXPV = []; MODE = os.environ.get("MODE", "gap")
K = (lambda x: x[:2]) if os.environ.get("KEY", "P") == "P" else (lambda x: x)   # KEY=P (default): settled = (c, P) final; KEY=V: whole Xi

def run(g, name, start=None):
    E, R = rows(g, start)
    if MODE == "run": G = sorted({(s, e, s, e) for s, e, x, y in _pts(g, R)})
    else: G = _pts(g, R)
    for s, e, x, y in G:
        C["gaps"] += 1; C["trans"] += y - x
        if y in EVENTS and os.environ.get("REF", "pre") == "pre": y -= 1   # REF=pre (default): settle against the state before the closing event
        for t in range(x, y):
            new = [v for v in range(g.n) if K(R[t + 1]["vs"][v]) == K(R[y]["vs"][v]) != K(R[t]["vs"][v])]
            newv = [v for v in range(g.n) if R[t + 1]["vs"][v] == R[y]["vs"][v] != R[t]["vs"][v]]
            if not new: C["VS_V"] += 1; EX.append((name, s, e, x, y, t))
            if not new and not newv: C["PV_V"] += 1; EXPV.append((name, s, e, x, y, t))
            if not [v for v in new if g.owner[v] == 0]: C["NEV"] += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:4]: print("EXAMPLE", x)
    for x in EXPV[:6]: print("EXAMPLE_PV", x)
    print("PVSTEP PASS" if "PV_V" not in C else "PVSTEP FAIL")   # PV-STEP: P-settled or value-settled grows at every transition
    print("VSTEP PASS" if "VS_V" not in C else "VSTEP FAIL")

if __name__ == "__main__":
    main()
