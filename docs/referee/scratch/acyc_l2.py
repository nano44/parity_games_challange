"""REFEREE successor 28: P-ACYC fix round 1 byte test. My AC-L1..AC-L5 are read from acyc_linefix.py (the strings of R-P-ACYC §5).
(1) L-1 + my five changes = my predicted c8ed32a8 (sanity). (2) L-2 is rebuilt here from L-1 with: AC-L1, AC-L2, AC-L3 verbatim; ONE
replacement of REFEREE-2's longer old string (which contains my AC-L4 old string) by the combined string = REFEREE-2 W-3 (a) part +
my AC-L4 new string's tail; my AC-L5 new string with REFEREE-2's D-3 insertion before its first «)». Each old string must occur once
in L-1; the result must be byte-equal to L-2. (3) For each of my strings: new present in L-2 (whole, or AC-L4's own text as a
substring), old absent. Usage: acyc_l2.py L1 L2"""
import sys, os, hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "acyc_linefix.py"), encoding="utf-8").read()
ns = {}; exec(src[src.index("CH = ["):src.index("pos = []")], ns); CH = ns["CH"]
L1 = open(sys.argv[1], encoding="utf-8").read(); L2 = open(sys.argv[2], encoding="utf-8").read()
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()))
X = L1
for nm, o, n in CH: X = X.replace(o, n)
print("(1) L-1 + AC-L1..AC-L5 =", h(X), "(predicted c8ed32a8…, 2638)")
D = dict((nm, (o, n)) for nm, o, n in CH)
r2old = "σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;"
assert D["AC-L4"][0] in r2old
r2new = "σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, " + D["AC-L4"][1]
d3 = "; e-priorities ordered by (lev, gate index), as in ref gamma3.build"
o5, n5 = D["AC-L5"]; i = n5.index(")"); n5d3 = n5[:i] + d3 + n5[i:]
REP = [D["AC-L1"], D["AC-L2"], D["AC-L3"], (r2old, r2new), (o5, n5d3)]
Y = L1
for o, n in REP:
    print("old once in L-1:", L1.count(o), "| new in L-2:", L2.count(n), "|", o[:60]); assert L1.count(o) == 1; Y = Y.replace(o, n)
print("(2) rebuilt == L-2:", Y == L2, h(Y), "| L-2", h(L2))
for nm, o, n in CH:
    print("(3)", nm, "new (whole) in L-2:", L2.count(n), "| old in L-2:", L2.count(o))
print("parens L-2", L2.count("("), L2.count(")"))
