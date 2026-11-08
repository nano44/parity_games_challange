"""REFEREE successor 28: P-N5-ASC byte test L-1 -> L-2 (fixes entry 2): L-1 with exactly the two replacements (each old string once in
L-1, each new string once in L-2) must be byte-equal to L-2; AS-2 / AS-3 strings re-counted on L-2. Usage: asc_l2.py L1 L2"""
import sys, hashlib
L1 = open(sys.argv[1], encoding="utf-8").read(); L2 = open(sys.argv[2], encoding="utf-8").read()
CH = [("«(consecutive state pair, W-target with Λ fixed) pairs»"[1:-1], "(consecutive state pair, W-target or c_W with Λ fixed) pairs"),
      ("with fixes entry 1", "with fixes entries 1-2")]
X = L1
for o, n in CH:
    print("old in L-1:", L1.count(o), "| new in L-2:", L2.count(n), "| old in L-2:", L2.count(o), "|", o, "->", n); X = X.replace(o, n)
print("L-1 + 2 changes == L-2:", X == L2, hashlib.sha1(X.encode()).hexdigest(), len(X.encode()), "| L-2", hashlib.sha1(L2.encode()).hexdigest(), len(L2.encode()))
for s in ("UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]", "(only for §6 UP-JUMP, UP-B and NOUP)", "UP-JUMP and UP-B under HYPOTHESIS [E-LEV]",
          "(only for §6 UP-JUMP and UP-B)", "under [E-LEV]"):
    print("L-1", L1.count(s), "L-2", L2.count(s), "|", s)
print("parens L-2", L2.count("("), L2.count(")"), "| lines", L2.count("\n"))
