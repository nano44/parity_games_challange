#!/usr/bin/env python3
"""k*(R_L): least SA level that is exact (infeasible) on the ring R_L, for L = 1..Lmax, with a cap on k."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sa import sa_feasible, even_wins_all
from ring import ring
Lmax, kmax = int(sys.argv[1]), int(sys.argv[2])
for L in range(1, Lmax + 1):
    g = ring(L)
    assert not even_wins_all(g)
    out = []
    for k in range(0, kmax + 1):
        t = time.time(); f = sa_feasible(g, k)
        out.append(f"k={k}:{'FEAS(gap)' if f else 'infeas'}({time.time()-t:.1f}s)")
        if not f:
            break
    print(f"L={L} n={g.n} " + " ".join(out), flush=True)
