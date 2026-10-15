#!/usr/bin/env python3
"""Families for the DTL box (L-RED). `chain n`: one-player (all Odd-owned) game with even priorities 2..2n, vertex i has
edges to every j <= i+1 (dense downward, one step up): DTL's sptl loop learns a chain of tangles, one more top per pass.
Usage: gens_dtl.py FAMILY n"""
import sys


def chain(n):
    out = [f"parity {n - 1};"]
    for i in range(n):
        succ = sorted(set(range(0, min(n, i + 2))))
        out.append(f"{i} {2 * i + 2} 1 {','.join(map(str, succ))};")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    sys.stdout.write({"chain": chain}[sys.argv[1]](int(sys.argv[2])))
