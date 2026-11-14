"""REFEREE s34: P-N5-GATE L-5 = L-4 + C142 §4's pairs (parsed by THIS script from C142.md as given, not from the lane's byte copy)
+ the Lead's tenth pair «fixes entries 1-4,» -> «fixes entries 1-5,». Usage: gate_l5.py C142.md L4 OUT"""
import sys, re, hashlib
c = open(sys.argv[1], encoding="utf-8").read(); L = open(sys.argv[2], encoding="utf-8").read()
s4 = c[c.index("## 4. Line L-5"):c.index("- Whitespace:")]
pairs = [(re.sub(r"\s*\n\s*", " ", o), re.sub(r"\s*\n\s*", " ", n)) for o, n in re.findall(r"«([^«»]*)»\s*→\s*«([^«»]*)»", s4)]
print("pairs parsed", len(pairs))
def h(x): return hashlib.sha1(x.encode()).hexdigest()
for i, (o, n) in enumerate(pairs):
    k = L.count(o); print("pair", i + 1, "old count", k, "| old", len(o), "ch | new", len(n), "ch")
    assert k == 1; L = L.replace(o, n)
print("after nine: sha1", h(L), len(L.encode()), "B")
o, n = "fixes entries 1-4,", "fixes entries 1-5,"
print("tenth old count", L.count(o)); assert L.count(o) == 1; L = L.replace(o, n)
open(sys.argv[3], "w", encoding="utf-8").write(L)
print("L-5 sha1", h(L), len(L.encode()), "B; newlines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
