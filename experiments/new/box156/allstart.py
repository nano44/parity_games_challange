#!/usr/bin/env python3
"""box 156: max over ALL starts of T and of M2 (steps 1..T-1 with >= 2 movers) for deg <= 2 genomes with N <= NMAX (default 12)."""
import sys, json, itertools, os
from val import ns
Gen = ns["Gen"]; NMAX = int(os.environ.get("NMAX", "12"))
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]
    if max(len(o) for o in G["opts"]) > 2 or N > NMAX: continue
    g = Gen(G); bT = bM = (-1, None)
    for st in itertools.product(*[range(len(o)) for o in G["opts"]]):
        S, _ = g.run(list(st)); T = len(S) - 1
        mv = [sum(1 for v in range(N) if S[t][v] != S[t + 1][v]) for t in range(T)]; M2 = sum(1 for c in mv[:-1] if c >= 2)
        if T > bT[0]: bT = (T, M2)
        if M2 > bM[0]: bM = (M2, T)
    print(f"{f} N {N} maxT {bT[0]} (M2 {bT[1]}) maxM2 {bM[0]} (T {bM[1]}) T/N {bT[0]/N:.2f} M2-N {bM[0]-N}", flush=True)
