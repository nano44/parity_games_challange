#!/usr/bin/env python3
"""L-SI box 29: CANDIDATE SETTLE in frozen W-phases [a, b] (fwphase.py): W_(a+k)(x) = W_b(x) for every x with W_b(x).length <= k
(Bellman-Ford settling toward the END valuation; it implies FW-BF). SETTLE_V counts (phase, x) failures; also SETTLE2 with the length of
x's sigma_b-play in G_tau to its cycle node counted from the END state's play (same thing) and SETTLE_A with the Xi frame
(Xi_(a+k)(x) = Xi_b(x) when Xi_b(x).length <= k). Per |D| class: max WCH/(n-1). Usage: settle.py --one GAME [START] | --list FILE"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from fwphase import fwphases
C = Counter(); EX = []; MX = {}

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = sum(1 for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]); d = min(D, 3)
            wch = sum(1 for t in range(a, b) if R[t]["W"] != R[t + 1]["W"])
            if d not in MX or wch / (n - 1) > MX[d][0]: MX[d] = (round(wch / (n - 1), 3), name, a, b, wch, D, n)
            C["fw_D%d" % d] += 1
            for x in range(n):
                for key, tag in (("W", "SETTLE"), ("vs", "SETTLE_X")):
                    fin = R[b][key][x]; lx = fin[2]
                    bad = [k for k in range(lx, b - a + 1) if R[a + k][key][x] != fin]
                    if bad:
                        C[tag + "_V"] += 1; C[tag + "_V_D%d" % d] += 1
                        if len(EX) < 8 or (tag == "SETTLE_X" and len(EX) < 40): EX.append((tag, name, a, b, x, lx, bad[0], R[a + bad[0]][key][x], fin, D))

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
    for d in sorted(MX): print("max WCH/(n-1) at |D| class %d:" % d, MX[d])
    for z in EX: print("EXAMPLE (tag, game, a, b, x, final length, first k failing, value then, final value, |D|)", z)
    for k in ("SETTLE", "SETTLE_X"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
