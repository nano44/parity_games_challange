"""REFEREE s31: P-N5-GATE L-4 = L-3 + LT-1 (Lead's landing-order form, typed from fixes entry 4 / the Lead's 05:09Z message) + GL-1..GL-3
(parsed from MY §J in R-P-N5-GATE.md) + «fixes entries 1-3» -> «1-4». Usage: gate_l4.py REPORT.md L3 OUT"""
import sys, re, hashlib
rep = open(sys.argv[1], encoding="utf-8").read(); L = open(sys.argv[2], encoding="utf-8").read()
J = rep[rep.index("## §J."):]
def grab(tag):
    m = re.search(r"- " + tag + r": Old «(.*?)»\s*→\s*New «(.*?)»", J, re.S)
    return re.sub(r"\s*\n\s*", " ", m.group(1)), re.sub(r"\s*\n\s*", " ", m.group(2))
gl = [grab("GL-1"), grab("GL-2"), grab("GL-3")]
lt = [("C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3);",
       "C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry);"),
      ("PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV", "PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV")]
for name, (o, n) in zip(["LT-1a", "LT-1b", "GL-1", "GL-2", "GL-3"], lt + gl):
    print(name, "old count", L.count(o)); L = L.replace(o, n)
print("src note old count", L.count("fixes entries 1-3")); L = L.replace("fixes entries 1-3", "fixes entries 1-4")
open(sys.argv[3], "w", encoding="utf-8").write(L)
print("sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B; lines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
for s in ["RA-MULT", "K1-FLIP(c)", "a polynomial bound on the RA path count", "pending"]: print("count", s, L.count(s))
