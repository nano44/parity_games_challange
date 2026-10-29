#!/usr/bin/env python3
"""L-SI box 26: DATA for the candidate GAP-DEPTH (docs/si/N5-LWP-box26.md): an L-WAVE' gap [x, y] (closing at an event y, also at the run end:
reference state b := y - 1; else b := y) has b - x <= max_Q d, d the two-frame REL depth at b (grun/relseg.py: X_b, CW_b, CH_b, piece/sdprime.py depths).
That would be STATIC-DEPTH-REL with "sigma-bar constant on RO_b" weakened to "no L-WAVE' event" (L-cuts allowed). Counts GD_V (gaps longer
than max d), h4p_fail; MUT=1 uses max d - 1 (must bite). Usage: gapdepth.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gaps import _pts, EVENTS
from common import rows, load, readstart
from staticdepth import walk
from relseg import cycof
from sdprime import depths
C = Counter(); EX = []; MUT = 1 if os.environ.get("MUT") == "1" else 0

def excess(g, R):
    """max over the gaps of (b - x) - max d (> 0: the gap outlasts the end-state depth), and max (b - x) - (n - 1) (> 0: an L-WAVE' kill)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try: _run(g, R, "x"); return (1000 - C["slack_min_plus1000"]) if "slack_min_plus1000" in C else -10 ** 6, C["kill_max"]
    finally: C, EX = save

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def _run(g, R, name):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    for s, e, x, y in _pts(g, R):
        b = y - 1 if y in EVENTS else y
        if b <= x: continue
        B = R[b]; X, st = set(), list(Q)
        while st:
            z = st.pop()
            if z in X: continue
            X.add(z); st.extend(w for w in sum(walk(B["wn"], z), ()) + sum(walk(B["nxt"], z), ()) if g.owner[w] == 0)
        CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
        CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
        TW = {v for c in CW for v in c}; TH = {v for c in CH for v in c}; C["gaps"] += 1
        try: dW, dH = depths(g, B, TW, TH, Q)
        except (ValueError, RecursionError): C["h4p_fail"] += 1; continue
        dm = max([dW[v] for v in Q] + [dH[v] for v in Q], default=0)
        C["slack_min_plus1000"] = min(C.get("slack_min_plus1000", 10 ** 6), 1000 + dm - (b - x))
        C["kill_max"] = max(C.get("kill_max", -10 ** 6), (y - x) - (n - 1))
        if b - x > dm - MUT: C["GD_V"] += 1; EX.append((name, s, e, x, y, b - x, dm, n))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:8]: print("EXAMPLE", z)
    print("GAPDEPTH PASS" if "GD_V" not in C else "GAPDEPTH FAIL")

if __name__ == "__main__":
    main()
