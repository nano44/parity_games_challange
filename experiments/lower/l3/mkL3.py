#!/usr/bin/env python3
"""Build docs/lower/P-M2D-DEAD-line-L3.txt: L-2 (docs/lower/P-M2D-DEAD-line-L2.txt) with the fix-round-2 replacement (REFEREE PM-C1
and REFEREE-2 W-1', both resolved by L-RED's committed replay output, Lead 03:55Z); the old string must occur exactly once in L-2."""
import os, hashlib
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
L2 = open(os.path.join(R, "docs/lower/P-M2D-DEAD-line-L2.txt"), encoding="utf-8").read()
assert L2.endswith("\n") and L2.count("\n") == 1
L2 = L2[:-1]
REPL = [
 ("PM-C1+W-1'", "L-RED 52 (55557951, experiments/red/r214/lower3/)",
  "L-RED 52 (6e743ab1, experiments/red/r214/lower3/replay.out)"),
]
L3 = L2
for name, old, new in REPL:
    n = L3.count(old); assert n == 1, (name, n)
    L3 = L3.replace(old, new)
depth = 0
for ch in L3:
    depth += (ch == "(") - (ch == ")"); assert depth >= 0
assert depth == 0 and "|" not in L3
b = (L3 + "\n").encode()
open(os.path.join(R, "docs/lower/P-M2D-DEAD-line-L3.txt"), "wb").write(b)
print("L3", len(b), "B; parens", L3.count("("), L3.count(")"), "sha1", hashlib.sha1(b).hexdigest())
