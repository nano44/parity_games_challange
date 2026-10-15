#!/usr/bin/env python3
"""Families for the DTL box (L-RED). `chain n`: one-player (all Odd-owned) game with even priorities 2..2n, vertex i has
edges to every j <= i+1 (dense downward, one step up): DTL's sptl loop learns a chain of tangles, one more top per pass.
Usage: gens_dtl.py chain|counter_dftl|counter_odftl n"""
import sys


def chain(n):
    out = [f"parity {n - 1};"]
    for i in range(n):
        succ = sorted(set(range(0, min(n, i + 2))))
        out.append(f"{i} {2 * i + 2} 1 {','.join(map(str, succ))};")
    return "\n".join(out) + "\n"




def counter_dftl(n, two=False):
    """Transcription of van Dijk's src/tools/counter_dftl.cpp (oink branch dftl @ a028e62, 8 + 4N vertices) and, with
    two=True, counter_odftl.cpp (@ d54dfad, 8 + 6N vertices: a 2-cycle of priority 1 in front of each dominant)."""
    piv = 2 + 2 * n; k = 6 if two else 4; V = 8 + k * n
    pr = [0] * V; ow = [0] * V; E = []
    def init(v, p, o): pr[v] = p; ow[v] = o
    init(0, piv + 6, 1); init(1, 0, 1); init(2, piv + 5, 1); init(3, 2, 1); init(4, 2, 1)
    E += [(0, 3), (1, 0), (2, 1), (3, 2), (3, 4), (4, 3)]
    init(5, piv + 2, 0); init(6, piv + 4, 0); init(7, piv + 5, 0)
    E += [(1, 5), (5, 1), (5, 6), (6, 7), (7, 5)]
    for i in range(n):
        c = 8 + k * i; d = piv + 8 + 2 * i; e = piv - 2 * i
        init(c, e, 0); init(c + 1, e, 0); init(c + 2, d, 0); init(c + 3, d + 1, 0)
        E += [(1, c), (c, 1), (3, c + 1), (c + 1, 3), (c, c + 2), (c + 1, c + 2), (c + 3, c + 1)]
        if two:
            init(c + 4, 1, 0); init(c + 5, 1, 0); E += [(c + 2, c + 4), (c + 4, c + 5), (c + 5, c + 4), (c + 4, c + 3)]
        else:
            E += [(c + 2, c + 3)]
    succ = [[] for _ in range(V)]
    for a, b in E: succ[a].append(b)
    return f"parity {V - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n" for v in range(V))


def counter_odftl(n): return counter_dftl(n, True)


if __name__ == "__main__":
    sys.stdout.write({"chain": chain, "counter_dftl": counter_dftl, "counter_odftl": counter_odftl}[sys.argv[1]](int(sys.argv[2])))
