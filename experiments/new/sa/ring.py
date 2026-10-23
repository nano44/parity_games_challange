#!/usr/bin/env python3
"""Ring family R_L (N9-screen.md §1(c)): Even v_i (i < L) with successors a_i, b_i; a_i, b_i (Odd, one successor) -> v_{i+1 mod L};
pr(v_0) = 1, all others 0. Every play is the ring cycle through v_0: Odd wins every vertex. n = 3L, Even choices L."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg


def ring(L):
    prio, owner, succ = [], [], []
    for i in range(L):  # v_i = 3i, a_i = 3i+1, b_i = 3i+2
        prio += [1 if i == 0 else 0, 0, 0]; owner += [0, 1, 1]
        nxt = 3 * ((i + 1) % L)
        succ += [[3 * i + 1, 3 * i + 2], [nxt], [nxt]]
    return pg.Game(prio, owner, succ)


if __name__ == "__main__":
    pg.write(ring(int(sys.argv[1])), sys.argv[2])
