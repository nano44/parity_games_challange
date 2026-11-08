"""REFEREE successor 29: P-N5-ASC L-4 notes N-I / N-A (R121 second fill). Old strings once in L-4? sha1 of L-4 + R-I, L-4 + R-A,
L-4 + R-A + R-I. Usage: asc_l4na.py L4"""
import sys, hashlib
L4 = open(sys.argv[1], encoding="utf-8").read()
RI = ("(f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then", "(f, …), then")
RA = ("(items 1..M, a run of forests with every chain lex-nondecreasing)",
      "(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item)")
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()), t.count("("), t.count(")"))
for nm, (o, n) in (("R-I", RI), ("R-A", RA)): print(nm, "old in L-4:", L4.count(o), "new in L-4:", L4.count(n))
print("L-4        ", h(L4)); print("L-4 + R-I  ", h(L4.replace(*RI))); print("L-4 + R-A  ", h(L4.replace(*RA)))
print("L-4 + R-A + R-I", h(L4.replace(*RA).replace(*RI)))
