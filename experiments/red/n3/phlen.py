#!/usr/bin/env python3
"""Longest phase (maximal run with (lambda_Xi, tau) constant) of N5 on a game; prints n, iterations, phases, max phase length T, T/n,
|Q| (Odd choice vertices), fallbacks inside the longest phase. Usage: phlen.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
def main():
    g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    if st is None and os.path.exists(sys.argv[1][:-3] + ".start"): st = n3x.readstart(sys.argv[1][:-3] + ".start")
    E, rows = n3x.trace(g, st)
    keys = [(r["lam"], r["tau"]) for r in rows]; best = (0, 0); i = 0; ph = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
        ph += 1; best = max(best, (j - i, i)); i = j + 1
    T, i0 = best; fb = sum(rows[k]["fb"] for k in range(i0, i0 + T))
    Q = sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    print(f"n={g.n} it={len(rows)-1} phases={ph} T={T} T/n={T/g.n:.2f} Q={Q} fb_in_phase={fb}")
main()
