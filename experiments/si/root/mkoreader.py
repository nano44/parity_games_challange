#!/usr/bin/env python3
"""L-SI box 23 (successor 19): append an Odd READER vertex o (index n, priority PRIO, no predecessors) with edges to a set S of one class, to a
game and its start file (TAU0 o:Y). Nobody's play passes o, so the run on the old vertices must be unchanged (checked by orcheck.py); then
Xi(o) = o (+) min over S of Xi, and XR(o) counts the changes of that minimum (docs/si/N5-ALT-box23.md §8).
OWNER=0 appends an Even reader instead (SIGMA0 o:Y).
Usage: mkoreader.py GAME START OUT_PREFIX PRIO Y S1,S2,..."""
import sys
g, st, out, prio, y, S = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), [int(x) for x in sys.argv[6].split(",")]
L = [l.rstrip("\n") for l in open(g) if l.strip()]
n = len(L) - 1; assert L[0].startswith("parity")
assert y in S
L[0] = f"parity {n};"
own = int(__import__("os").environ.get("OWNER", "1"))       # OWNER=0: an EVEN reader (start SIGMA0 o:Y); passive only where no fallback fires
L.append(f"{n} {prio} {own} {','.join(map(str, sorted(S)))};")
open(out + ".pg", "w").write("\n".join(L) + "\n")
ls = [l.rstrip("\n") for l in open(st) if l.strip()]
ls[own ^ 1] = ls[own ^ 1] + f" {n}:{y}"
open(out + ".start", "w").write("\n".join(ls) + "\n")
print("wrote", out + ".pg", out + ".start", "n =", n + 1)
