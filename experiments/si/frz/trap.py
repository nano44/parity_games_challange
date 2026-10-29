#!/usr/bin/env python3
"""L-SI box 29: the OPTIMISM-TRAPPED set S_t = {x : W_t(x) strictly better than Xi_t(x)} (equivalently x's (sigma_t, tau)-play enters D and
the two frames differ) inside frozen W-phases (fwphase.py). Counters: TIN (a vertex enters S), TOUT_V (a vertex leaves S: candidate TRAP-MONO
says never), TOUT_SW (leaves while switching itself), TRAPSW_V (a vertex of S_t switches at t, Even only). Usage: trap.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from fwphase import fwphases
C = Counter(); EX = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            S = lambda t: {x for x in range(n) if E.key(R[t]["W"][x]) > E.key(R[t]["vs"][x])}
            prev = S(a)
            for t in range(a + 1, b + 1):
                cur = S(t); C["TIN"] += len(cur - prev)
                out = prev - cur
                if out:
                    C["TOUT_V"] += len(out); C["TOUT_SW"] += sum(1 for x in out if g.owner[x] == 0 and R[t - 1]["s"][x] != R[t]["s"][x])
                    if len(EX) < 5: EX.append((name, a, b, t, sorted(out)[:6]))
                C["TRAPSW_V"] += sum(1 for x in prev if g.owner[x] == 0 and R[t - 1]["s"][x] != R[t]["s"][x])
                prev = cur
            C["fw"] += 1

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
    for z in EX: print("EXAMPLE (game, a, b, t, leaving)", z)

if __name__ == "__main__":
    main()
