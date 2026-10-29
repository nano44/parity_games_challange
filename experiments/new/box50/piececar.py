#!/usr/bin/env python3
"""L-NEW box 50 (successor 31): CARRIES PER VERTEX PER PHASE against sigma-bar changes (Lead 12:01Z). A PIECE of a phase is a maximal stretch
of its transitions with sigma-bar unchanged (sb_t = sb_{t+1}); the sigma-bar-changing transitions are the CUTS, G(P) of them. Per vertex v:
NM_P(v) = carries of v's path set in P (fbcarry.kind == CAR); CPIECE = max over pieces of v's carries inside one piece; CCUT = v's carries at
cuts. Prints the maxima of CPIECE, NM_P(v) / (G(P) + 1), and the phases with the largest NM. Usage: piececar.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
for p in ("root", "runlin"): sys.path.insert(0, os.path.join(ROOT, "experiments", "si", p))
from common import rows, load, readstart, phases
from fbcarry import kind
C = Counter(); TOP = []

def one(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for i, j in phases(R):
        if j <= i: continue
        G = sum(R[t]["sb"] != R[t + 1]["sb"] for t in range(i, j)); C["phases"] += 1
        nm = Counter(); cut = Counter(); piece = Counter(); best_piece = Counter(); plen = 0; maxplen = 0
        for t in range(i, j):
            isc = R[t]["sb"] != R[t + 1]["sb"]
            if isc: piece = Counter(); plen = 0
            else: plen += 1; maxplen = max(maxplen, plen)
            for v in range(n):
                if kind(E, R[t]["vs"][v], R[t + 1]["vs"][v]) == "CAR":
                    nm[v] += 1
                    if isc: cut[v] += 1
                    else:
                        piece[v] += 1; best_piece[v] = max(best_piece[v], piece[v])
        mx_nm = max(nm.values(), default=0); mx_pc = max(best_piece.values(), default=0)
        C["NM_max"] = max(C["NM_max"], mx_nm); C["CPIECE_max"] = max(C["CPIECE_max"], mx_pc)
        C["piece_len_max"] = max(C["piece_len_max"], maxplen); C["G_max"] = max(C["G_max"], G)
        C["NM_over_G1_x100_max"] = max(C["NM_over_G1_x100_max"], 100 * mx_nm // (G + 1))
        TOP.append((mx_nm, mx_pc, G, j - i, maxplen, n, name, i, j))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": one(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                X = lambda q: os.path.join(ROOT, "experiments", q)
                try: one(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
                except Exception as ex: C["ERR"] += 1; print("ERR", p[0], repr(ex)[:80])
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: -x[1])[:6]: print("TOP-CPIECE NM %d CPIECE %d G %d len %d maxpiece %d n %d %s [%d,%d]" % x)
    for x in sorted(TOP, key=lambda x: -x[0] / (x[2] + 1))[:6]: print("TOP-NM/(G+1) NM %d CPIECE %d G %d len %d maxpiece %d n %d %s [%d,%d]" % x)

if __name__ == "__main__":
    main()
