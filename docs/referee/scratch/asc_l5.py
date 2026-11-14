"""REFEREE successor 29: P-N5-ASC byte test L-4 -> L-5 (R-A then R-I, strings of R-P-N5-ASC §F addendum 1 / asc_l4na.py). Usage: asc_l5.py L4 L5"""
import sys, hashlib
L4 = open(sys.argv[1], encoding="utf-8").read(); L5 = open(sys.argv[2], encoding="utf-8").read()
R = [("R-A", "(items 1..M, a run of forests with every chain lex-nondecreasing)",
      "(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item)"),
     ("R-I", "(f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then", "(f, …), then")]
X = L4
for nm, o, n in R:
    print(nm, "old in L-4:", L4.count(o), "| new in L-4:", L4.count(n), "| new in L-5:", L5.count(n), "| old in L-5:", L5.count(o)); X = X.replace(o, n)
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()), t.count("("), t.count(")"), t.count("\n"))
print("L-4 + R-A + R-I == L-5:", X == L5, h(X), "| L-5", h(L5))
