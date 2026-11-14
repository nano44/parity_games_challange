# REFEREE-2 successor 33: L-4 = L-3 + REFEREE 28 R5 (own script; reads files given as args)
import sys, hashlib
l3 = open(sys.argv[1], 'rb').read().decode(); l4 = open(sys.argv[2], 'rb').read().decode()
old = "(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then"
new = "(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then"
print("old in L-3:", l3.count(old), " new in L-3:", l3.count(new))
print("old in L-4:", l4.count(old), " new in L-4:", l4.count(new))
built = l3.replace(old, new)
b = built.encode()
print("built sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
print("L-4   sha1", hashlib.sha1(l4.encode()).hexdigest(), len(l4.encode()), "B")
print("L-4 == L-3 + R5:", built == l4)
