#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-4 = line L-3 (docs/si/P-N5-GATE-line-L3.txt, sha1 b60495b2…) with fixes entry 4 applied: (a) LT-1 in the Lead's
landing-order form (2026-11-12 02:57Z / 04:09Z: SPLIT-COUNT and C-EQUIV cited as «RESULTS R127 (P-N5-SPLIT)», A*-EQUIV (ii), (iii) CONDITIONAL
on it); (b) REFEREE 31's GL-1..GL-3, PARSED from the byte copy ref_R-P-N5-GATE_fbc4d865.md §J (sha1 asserted; wrapped lines joined by one
space), applied verbatim. Each Old asserted exactly once at the moment it is applied. Prints L-4. Usage: mkL4.py ROOT"""
import hashlib, os, re, sys
ROOT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p, sha):
    b = open(p, "rb").read(); assert hashlib.sha1(b).hexdigest() == sha, p; return b.decode("utf-8")
L3 = rd(os.path.join(ROOT, "docs/si/P-N5-GATE-line-L3.txt"), "b60495b2c607e8e6c1e145e40478717fa6ed15f4")
rep = rd(os.path.join(HERE, "ref_R-P-N5-GATE_fbc4d865.md"), "9aaf92a6e61e3d411297be6c45745a2b9b782b13")
J = re.sub(r"\s*\n\s*", " ", rep.split("\n## §J.")[1])
GL = re.findall(r"- (GL-[123]): Old «(.*?)» → New «(.*?)»", J)
assert [g[0] for g in GL] == ["GL-1", "GL-2", "GL-3"], GL
R = [
 ("LT-1a", "C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3);",
  "C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = "
  "P-N5-SPLIT, then this entry);"),
 ("LT-1b", "PROVED-CONDITIONAL on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV",
  "PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV"),
] + list(GL) + [
 ("lane", "with its fixes entries 1-3, docs/si/P-N5-GATE-fixes.md", "with its fixes entries 1-4, docs/si/P-N5-GATE-fixes.md"),
]
L = L3
for i, a, b in R:
    assert L.count(a) == 1, (i, L.count(a), a[:70])
    L = L.replace(a, b)
for bad in ("RA-MULT", "K1-FLIP(c)", "a polynomial bound on the RA path count"):
    assert bad not in L, bad
assert "|" not in L and L.count("\n") == 1 and L.endswith("\n") and L.count("(") == L.count(")")
sys.stdout.write(L)
