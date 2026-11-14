"""REFEREE successor 29: P-N5-ASC byte test L-3 -> L-4 (R5 of R-P-N5-ASC §E). Usage: asc_l4.py L3 L4"""
import sys, hashlib
L3 = open(sys.argv[1], encoding="utf-8").read(); L4 = open(sys.argv[2], encoding="utf-8").read()
o = "(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then"
n = "(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then"
print("R5 old in L-3:", L3.count(o), "| new in L-3:", L3.count(n), "| new in L-4:", L4.count(n), "| old in L-4:", L4.count(o))
X = L3.replace(o, n)
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()))
print("L-3 + R5 == L-4:", X == L4, h(X), "| L-4", h(L4))
print("parens L-4", L4.count("("), L4.count(")"), "| newlines L-4", L4.count("\n"))
for s in ("hence seq_t(v) = (f, seq_t(y_f))", "an ascent of seq_t(v) a step", "; L-NEW successors 61-62)", "UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]", "(only for §6 UP-JUMP, UP-B and NOUP)", "referee-originated"):
    print("L-4", L4.count(s), "|", s)
i = L4.index(n); print("CTX:", L4[i - 200:i + 260])
