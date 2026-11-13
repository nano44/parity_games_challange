#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-5 = line L-4 (docs/si/P-N5-GATE-line-L4.txt, sha1 asserted) with CHECKER C142's strings applied (fixes entry 5):
R-E1, R-E2 and the seven insertions of R-E3, PARSED from the byte copy chk_C142_269effb3.md §4 (claude/checker 269effb3,
docs/checker/C142.md; sha1 asserted; wrapped lines joined by one space, as §4's «Whitespace» bullet says), applied in §4's order, each
old string asserted exactly once at the moment it is applied. Never retyped. The result of these nine pairs is CHECKER's target
(sha1 7ebcf7355be9838473f05a7defe913940b6fd723, 12,923 B; asserted here). Then a TENTH pair, the Lead's ruling of 2026-11-12 17:58Z
(precedent: L-4 changed «1-3» to «1-4» when entry 4 was added): the source note names fixes entries 1-5. Prints L-5; with --nine prints
the nine-pair line (CHECKER's target) instead; the two sha1s and byte counts go to stderr. Usage: mkL5.py ROOT [--nine]"""
import hashlib, os, re, sys
ROOT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p, sha):
    b = open(p, "rb").read(); assert hashlib.sha1(b).hexdigest() == sha, p; return b.decode("utf-8")
L4 = rd(os.path.join(ROOT, "docs/si/P-N5-GATE-line-L4.txt"), "6bfde78ef050b47f43527875256c65a205869e77")
rep = rd(os.path.join(HERE, "chk_C142_269effb3.md"), "8b005c61e217f0b3601d57a8d69a29e798fd1403")
sec = rep.split("\n## 4. Line L-5 and its UPDATE")[1].split("\n## 5. ")[0]
body = sec.split("\n- Whitespace:")[0]
J = re.sub(r"\s*\n\s*", " ", body)
P = re.findall(r"«(.*?)» → «(.*?)»", J)
assert len(P) == 9, len(P)
assert J.count("- R-E1: «") == 1 and J.count("- R-E2: «") == 1 and J.count("- R-E3 (seven insertions):") == 1
L = L4
for i, (a, b) in enumerate(P):
    assert L.count(a) == 1, (i, L.count(a), a[:70])
    L = L.replace(a, b)
def ok(L): assert "|" not in L and L.count("\n") == 1 and L.endswith("\n") and L.count("(") == L.count(")") == 238
ok(L); L9 = L; h9 = hashlib.sha1(L9.encode("utf-8")).hexdigest()
assert h9 == "7ebcf7355be9838473f05a7defe913940b6fd723" and len(L9.encode("utf-8")) == 12923, (h9, len(L9.encode("utf-8")))
T10 = ("docs/si/P-N5-GATE.md with its fixes entries 1-4,", "docs/si/P-N5-GATE.md with its fixes entries 1-5,")
assert L9.count(T10[0]) == 1 and L9.count("fixes entries 1-") == 1
L = L9.replace(T10[0], T10[1]); ok(L); assert "L-SI successors 48-50" in L
sys.stderr.write("L-5 after CHECKER's nine pairs: sha1 %s, %d bytes (= C142's target)\nL-5 (tenth pair applied): sha1 %s, %d bytes\n"
                 % (h9, len(L9.encode("utf-8")), hashlib.sha1(L.encode("utf-8")).hexdigest(), len(L.encode("utf-8"))))
sys.stdout.write(L9 if "--nine" in sys.argv[2:] else L)
