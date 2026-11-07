#!/usr/bin/env python3
"""L-RED 54 R217: switchallexp G_n re-prioritised to satisfy E-DOM (every CycleLeaver m_i above every other priority except the
sink p), keeping the relative order inside each band; Howard (switch-all VJ, best-reward start) on the modified ORIGINAL game.
Modes: 'drop' = move every non-m priority above min(m) down below min(m), keeping order. Usage: edom.py mode n..."""
import sys
from fried import game, howard
def remap(V, mode):
    m = sorted(v[1] for v in V if v[4][0] == "m"); top = max(v[1] for v in V)
    others = sorted((v[1], v[0]) for v in V if v[4][0] != "m" and v[4] != "p")
    # new priority list: others (in order) then m's then p, re-numbered keeping parity: assign increasing values with given parity
    order = [v for _, v in others] + [v for _, v in sorted((v[1], v[0]) for v in V if v[4][0] == "m")] + [v[0] for v in V if v[4] == "p"]
    newp = {}; cur = -1
    for v in order:
        par = V[v][1] % 2; cur += 1
        if cur % 2 != par: cur += 1
        newp[v] = cur
    return [(v[0], newp[v[0]], v[2], v[3], v[4]) for v in V]
if __name__ == "__main__":
    mode = sys.argv[1]
    for n in map(int, sys.argv[2:]):
        V = remap(game(n), mode); T, _ = howard(V); print(f"E-DOM {mode} switchallexp {n}: Howard T {T}", flush=True)
