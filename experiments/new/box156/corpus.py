#!/usr/bin/env python3
"""box 156: T, M2 (steps 1..T-1 with >= 2 movers), U, N, max degree for corpus genomes (genome start). Usage: corpus.py files..."""
import sys, json
from val import stats
rows = []
for f in sys.argv[1:]:
    G = json.load(open(f)); D = max(len(o) for o in G["opts"])
    try: T, M2, U, mv = stats(G)
    except Exception as e: print("SKIP", f, e); continue
    rows.append((T / G["N"], f, G["N"], D, T, M2, U, max(mv) if mv else 0))
for r in sorted(rows, reverse=True): print(f"{r[1]} N {r[2]} D {r[3]} T {r[4]} M2 {r[5]} U {r[6]} maxMv {r[7]} T/N {r[0]:.2f} T/(N(1+M2)) {r[4]/(r[2]*(1+r[5])):.2f}")
