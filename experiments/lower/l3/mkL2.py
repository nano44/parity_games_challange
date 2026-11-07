#!/usr/bin/env python3
"""Build docs/lower/P-M2D-DEAD-line-L1.txt (§6 of the frozen packet, lines joined by single spaces) and
docs/lower/P-M2D-DEAD-line-L2.txt (L-1 with the fix-round-1 replacements; each old string must occur exactly once)."""
import os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
P = open(os.path.join(R, "docs/lower/P-M2D-DEAD.md"), encoding="utf-8").read().split("\n")
a = P.index("## 6. Line L-1 (RESULTS dead-end style; to be checked by the referees)"); b = P.index("## 7. What this does NOT claim")
L1 = " ".join(l.strip() for l in P[a + 1:b] if l.strip())
REPL = [
 ("PM-L1", "obstruction: a metronome reading a key order that flips at every step, fed by laps",
  "obstruction (a description, no separate DATA): a metronome reading the key order of the pair one level below it, which flips at steps 2-13 (d 6) and 1-13, 17-24 (d 8), fed by laps"),
 ("PM-L2", "(sha1 d96c2b36…; 𝓛^R_8;", "(sha1 d96c2b36…; 𝓛^R_8, Ξ-acyclic, not ISO;"),
 ("PM-L3", "movescheck counters 0)", "movescheck counters 0 on both stored-start runs and on all 4,096 starts of the d 6 genome)"),
 ("PM-L4+W-1", "and independently by L-NEW box 188 (6d043927) and L-SI 41;",
  "and independently by L-NEW box 188 (6d043927), L-SI 41 (0803d551, docs/si/N5-TROPICAL-box76.md) and L-RED 52 (55557951, experiments/red/r214/lower3/), and by both referees' own simulators;"),
]
L2 = L1
for name, old, new in REPL:
    n = L2.count(old); assert n == 1, (name, n)
    L2 = L2.replace(old, new)
open(os.path.join(R, "docs/lower/P-M2D-DEAD-line-L1.txt"), "w", encoding="utf-8").write(L1 + "\n")
open(os.path.join(R, "docs/lower/P-M2D-DEAD-line-L2.txt"), "w", encoding="utf-8").write(L2 + "\n")
print("L1", len((L1 + "\n").encode()), "B; L2", len((L2 + "\n").encode()), "B; parens", L2.count("("), L2.count(")"))
