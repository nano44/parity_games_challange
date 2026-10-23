#!/usr/bin/env python3
"""K_n family (N9-screen.md §1(c)): n Even vertices, priority 1 each, edges to every other vertex (no self-loops).
Every positional sigma is a functional graph, which has a cycle, of max priority 1: Odd wins every vertex.
Prints SA_k feasibility for k = 1..kmax (least infeasible k = k*)."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg
from sa import sa_feasible, even_wins_all


def kn(n):
    return pg.Game([1] * n, [0] * n, [[w for w in range(n) if w != v] for v in range(n)])


if __name__ == "__main__":
    nmax, kmax = int(sys.argv[1]), int(sys.argv[2])
    for n in range(2, nmax + 1):
        g = kn(n); assert not even_wins_all(g)
        out = []
        for k in range(1, kmax + 1):
            t = time.time(); f = sa_feasible(g, k); out.append(f"k={k}:{'FEAS(gap)' if f else 'infeas'}({time.time()-t:.1f}s)")
            if not f:
                break
        print(f"K_{n} n={n} " + " ".join(out), flush=True)
