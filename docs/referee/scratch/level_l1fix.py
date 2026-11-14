#!/usr/bin/env python3
"""REFEREE s34: P-N5-LEVEL line L-1 (claude/l-new 1e6df499, sha1 28565b3c…) + the required strings LT-1..LT-3 of R-P-N5-LEVEL.md §5
(each old string asserted to occur exactly once; applied in this order). usage: level_l1fix.py L1.txt OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest() == "28565b3c60fe8167f4b660c83fa27c00cd7b4fe9"
FIX = [
 ("LT-1",
  "no run tests the constants: at most 199 values of Φ in a run, where P = 2,120,796, and no plateau longer than 26 steps",
  "no run tests the constants: at most 199 values of Φ in a run (unit: values of Φ with reference b = T; level208.py's phivals, largest "
  "over the level208.py sets above; 199 on MW32_2, out/level208_corpus.out, where P = 2,120,796) and no plateau longer than 26 steps "
  "(unit: steps; level208.py's platmax and rv208.py's platmax, largest over the sets above; 26 on mutants of MWR4_2, "
  "out/mut208_MWR4_2_s2086.out, and of CW4_n, out/rv208_mut_s2094.out)"),
 ("LT-2",
  "the counter of (K5) is 0 on G_1 and first fires on G_2 at the step 5 → 6",
  "L-COMP's counter k5 of (K5) (experiments/comp/box43/README.md item 1 (b), column k5) is 0 on G_1 and first fires on G_2 at the step 5 → 6"),
 ("LT-3",
  "L-FORMAL's lane-level Lean theorems Genome.k1, Genome.k2, Genome.k3, Genome.k5, level_count, plateau and brsegG (claude/l-formal f74d38a4)",
  "L-FORMAL's theorems PG.Genome.k1, PG.Genome.k2, PG.Genome.k3, PG.Genome.k5, PG.level_count, PG.plateau and PG.brsegG, Lean-checked "
  "(lane) on L-FORMAL's transcription, not through CHECKER (claude/l-formal f74d38a4)"),
]
for name, o, n in FIX:
    k = L.count(o); print(name, "old count", k); assert k == 1; L = L.replace(o, n)
open(sys.argv[2], "w", encoding="utf-8").write(L)
print("L-1' sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B; newlines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
