#!/usr/bin/env python3
"""L-SI box 31: S-monotone segments of same-pair frozen W-phases (S := vertices whose (rho, tau)-play meets D). Per transition: entries
(U -> S), exits (S -> U), moves (S_d -> S_d', d != d'). A segment is a maximal run of transitions whose S-changes go one way (entries only
or exits only; transitions without S-change join any segment). SEG := number of segments; MIX := transitions with both entries and exits.
Usage: mono.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart, phases
from fwphase import fwphases
from gates import basins
C = Counter(); MX = {}; HIST = Counter()

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
            if not D or not all(R[a]["vs"][d][0] == R[a]["W"][d][0] for d in D): continue
            cls = "D1" if len(D) == 1 else "D2+"; C[cls] += 1
            F = [basins(R[t]["wn"], D, n) for t in range(a, b + 1)]
            seg, cur, mix, mv = 0, 0, 0, 0
            for q in range(b - a):
                ent = sum(1 for v in range(n) if F[q][v] == -1 and F[q + 1][v] != -1)
                ext = sum(1 for v in range(n) if F[q][v] != -1 and F[q + 1][v] == -1)
                mv += sum(1 for v in range(n) if F[q][v] != -1 and F[q + 1][v] != -1 and F[q][v] != F[q + 1][v])
                if ent and ext: mix += 1; d = 2
                else: d = 1 if ent else (-1 if ext else 0)
                if d and d != cur: seg += 1; cur = d
            HIST[(cls, seg)] += 1; C[cls + "_mix>0"] += mix > 0; C[cls + "_move>0"] += mv > 0
            if seg > MX.get(cls, (-1,))[0]: MX[cls] = (seg, mix, mv, name, a, b, n, len(D))

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
    print("segments histogram:", sorted(HIST.items()))
    print("max segments (seg, mix, moves, game, a, b, n, |D|):", MX)

if __name__ == "__main__": main()
