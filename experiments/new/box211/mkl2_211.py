#!/usr/bin/env python3
"""P-N5-LEVEL line L-2 generator (L-NEW successor 74). From the repo root: python3 experiments/new/box211/mkl2_211.py
(needs the git objects of claude/referee 4c8d6c4f and claude/referee-2 43824abc).
L-2 = L-1 + the items the Lead ruled in (Lead, 2026-11-12 21:43Z): REQUIRED REFEREE 34 LT-1, LT-2, LT-3 (claude/referee 4c8d6c4f,
docs/referee/R-P-N5-LEVEL.md §5) and REFEREE-2 39 R-1 (claude/referee-2 43824abc, docs/referee-2/R2-P-N5-LEVEL.md §5.4; the same point
as REFEREE 34's LO-2, R-1's string used); ADOPTED optional REFEREE-2 39 R-2 and REFEREE 34 LO-1. Every old / new string is EXTRACTED
from the reports at those commits (never retyped): a bullet's wrapped lines are joined with one space (both reports: «one space
wherever this file wraps a line inside a string»), then its «…» strings are taken in order.
Asserts: the frozen packet's sha1 (7c956df4…), L-1's sha1 (28565b3c…), each report file's sha1 at its commit, each old string exactly
once; prints the sha1 after LT-1..LT-3 and asserts REFEREE 34's reported L-1′ sha1 389645a2…; then applies R-1, R-2, LO-1 (in this
order) and checks: one line, no «|», balanced parentheses, each new string exactly once. Writes docs/new/P-N5-LEVEL-line-L2.txt."""
import hashlib, re, subprocess, os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(ROOT)
sha = lambda b: hashlib.sha1(b).hexdigest()
pk = open("docs/new/P-N5-LEVEL.md", "rb").read()
assert sha(pk) == "7c956df443cfddbf23bfbaa18a26a98369b176ec", "frozen packet changed"
L1 = open("docs/new/P-N5-LEVEL-line-L1.txt", "rb").read()
assert sha(L1) == "28565b3c60fe8167f4b660c83fa27c00cd7b4fe9", "L-1 changed"
def show(commit, path, want):
    b = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, check=True).stdout
    assert sha(b) == want, (commit, path, sha(b)); return b.decode("utf-8")
R34 = show("4c8d6c4f", "docs/referee/R-P-N5-LEVEL.md", "374a1ba06f845ab9376f78b5ef82d24a3e4d2fc5")
R2 = show("43824abc", "docs/referee-2/R2-P-N5-LEVEL.md", "77a38f1ae36c32aed245fdd0a1bb0777ec9690fb")
print("REFEREE 34 report 4c8d6c4f sha1 374a1ba06f845ab9376f78b5ef82d24a3e4d2fc5; REFEREE-2 39 report 43824abc sha1 77a38f1ae36c32aed245fdd0a1bb0777ec9690fb")
def bullet(text, start):
    """the bullet whose first line starts with `start` (after indentation), wrapped lines joined with one space"""
    lines = text.split("\n"); i = next(k for k, l in enumerate(lines) if l.lstrip().startswith(start))
    ind = len(lines[i]) - len(lines[i].lstrip()); out = [lines[i].strip()]
    for l in lines[i + 1:]:
        if not l.strip() or (len(l) - len(l.lstrip()) <= ind and l.lstrip().startswith("- ")) or l.startswith("#"): break
        out.append(l.strip())
    return " ".join(out)
q = lambda b: re.findall(r"«([^«»]*)»", b)
lt1, lt2, lt3 = (q(bullet(R34, k)) for k in ("- LT-1 (", "- LT-2 (", "- LT-3 ("))
lo = q(bullet(R34, "- OPTIONAL (the Lead's call): LO-1"))
r1, r2 = q(bullet(R2, "- R-1 (")), q(bullet(R2, "- R-2 ("))
ITEMS1 = [("LT-1", lt1[0], lt1[1]), ("LT-2", lt2[0], lt2[1]), ("LT-3", lt3[0], lt3[1])]
ITEMS2 = [("R-1", r1[0], r1[1]), ("R-2", r2[0], r2[1]), ("LO-1", lo[0], lo[0] + " " + lo[1])]
L = L1.decode("utf-8")
def apply(items, L):
    for k, o, n in items:
        assert L.count(o) == 1, (k, L.count(o), o[:60])
        L = L.replace(o, n)
        print(k, "applied; sha1", sha(L.encode())[:8], len(L.encode()), "B")
    return L
L = apply(ITEMS1, L); h1 = sha(L.encode())
print("L-1 + LT-1..LT-3: sha1", h1, len(L.encode()), "B (REFEREE 34 reports 389645a2a646522a8fb57f05dba4458695ac74f2)")
assert h1 == "389645a2a646522a8fb57f05dba4458695ac74f2", "does not reproduce REFEREE 34's L-1′"
L = apply(ITEMS2, L)
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
for k, o, n in ITEMS1 + ITEMS2: assert L.count(n) == 1, k
b = L.encode(); open("docs/new/P-N5-LEVEL-line-L2.txt", "wb").write(b)
print("L-2 written: sha1", sha(b), len(b), "B;", L.count("("), "( =", L.count(")"), ")")
