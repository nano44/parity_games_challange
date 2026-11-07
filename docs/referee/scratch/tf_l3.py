"""REFEREE successor 27: byte test L-2 + C134 §5 R1-R4 (in order) == L-3. Pairs written here from C134 §5 (wrapped lines joined
by one space). Usage: tf_l3.py L2.txt L3.txt"""
import sys, hashlib
L2, L3 = (open(p, encoding="utf-8").read() for p in sys.argv[1:3])
P = [
 ("R1", " (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md; L-LOWER successor 5)",
  " (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)"),
 ("R2", "; G-N5-TIME stays OPEN; not M3, not a gauntlet step",
  "; the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees; G-N5-TIME stays OPEN; not M3, not a gauntlet step"),
 ("R3", "not a gauntlet step", "not a step-4 pass"),
 ("R4", "meets PULSE, GAP ≥ 7 − j at levels 1-5 while",
  "meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while"),
]
t = L2
for tag, o, n in P:
    c = t.count(o); assert c == 1, (tag, c); t = t.replace(o, n); print(tag, "old once in the text it is applied to: yes")
print("L-2 + R1-R4 == L-3:", t == L3, "| L-3 sha1", hashlib.sha1(L3.encode()).hexdigest(), len(L3.encode()), "bytes;",
      L3.count("("), "(", L3.count(")"), ")", "| «|»", L3.count("|"), "| « — »", L3.count(" — "), "| gauntlet", L3.count("gauntlet"),
      "| lines", L3.count("\n"))
