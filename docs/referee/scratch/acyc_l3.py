"""REFEREE successor 28: P-ACYC byte test L-2 -> L-3 (REFEREE-2's D-5, one replacement); my AC-L1..AC-L5 strings re-counted on L-3
(AC-L5 with REFEREE-2's D-3 insertion, as at §C). Usage: acyc_l3.py L2 L3"""
import sys, os, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "acyc_linefix.py"), encoding="utf-8").read()
ns = {}; exec(src[src.index("CH = ["):src.index("pos = []")], ns); CH = ns["CH"]
L2 = open(sys.argv[1], encoding="utf-8").read(); L3 = open(sys.argv[2], encoding="utf-8").read()
o, n = "(pacyc81.py),", "(pacyc81.py; τ by fix1/pacyc81t.py),"
print("D-5 old in L-2:", L2.count(o), "| new in L-3:", L3.count(n), "| old in L-3:", L3.count(o))
X = L2.replace(o, n); h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()))
print("L-2 + D-5 == L-3:", X == L3, h(X), "| L-3", h(L3))
d3 = "; e-priorities ordered by (lev, gate index), as in ref gamma3.build"
for nm, old, new in CH:
    if nm == "AC-L5": i = new.index(")"); new = new[:i] + d3 + new[i:]
    print(nm, "new in L-3:", L3.count(new), "| old in L-3:", L3.count(old))
print("parens L-3", L3.count("("), L3.count(")"))
