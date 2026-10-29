#!/usr/bin/env python3
"""L-SI box 29: the BLOCKED set B_t = {(x, z): x Even, z a successor, (x, z) not in the arena sigma_t + I_t, W_t(z) strictly better than
W_t(sigma_t x)} inside frozen W-phases (fwphase.py). Counters: BUP_V (an edge enters B, t > a), BDOWN_V (an edge leaves B), BDOWN_UNBLOCK
(an edge leaves B by entering I_t), BUSED_V (an edge of B_t is used by sigma at a later state of the same frozen W-phase).
Usage: blocked.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases, Engine
from fwphase import fwphases
C = Counter(); EX = []

def Bset(E, EN, g, A):
    I = set(EN.improving(tuple(A["s"]), A["vs"])); out = set()
    for x in range(g.n):
        if g.owner[x] != 0: continue
        for z in set(g.succ[x]):
            if z != A["s"][x] and (x, z) not in I and E.key(A["W"][z]) > E.key(A["W"][A["s"][x]]): out.add((x, z))
    return out, I

def _run(E, g, R, name):
    EN = Engine(g)
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            Bs = [Bset(E, EN, g, R[t]) for t in range(a, b + 1)]
            for k in range(1, len(Bs)):
                up = Bs[k][0] - Bs[k - 1][0]; down = Bs[k - 1][0] - Bs[k][0]
                if up: C["BUP_V"] += 1; C["bup_edges"] += len(up)
                if down:
                    C["BDOWN_V"] += 1; C["bdown_edges"] += len(down); C["bdown_into_I"] += len(down & Bs[k][1])
                    if len(EX) < 5: EX.append(("DOWN", name, a, b, a + k, sorted(down)[:4], sorted(down & Bs[k][1])[:4]))
            for k in range(len(Bs)):
                for (x, z) in Bs[k][0]:
                    if any(R[a + l]["s"][x] == z for l in range(k + 1, len(Bs))): C["BUSED_V"] += 1
            C["fw"] += 1; C["fw_with_B"] += any(B for B, _ in Bs)

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
    for z in EX: print("EXAMPLE", z)

if __name__ == "__main__":
    main()
