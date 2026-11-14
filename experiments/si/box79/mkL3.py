#!/usr/bin/env python3
"""L-SI P-IDEAL-DBL fix round 2 (CHECKER C133 E-1..E-6): line L-3 = L-2 with C133 §5's R1-R6 applied in order. Every string is copied
by script from c133_8f6d03bc.md (byte copy of docs/checker/C133.md at claude/checker 8f6d03bc; wrapped lines joined with one space,
as C133 §5 says). Each old string occurs once in the current text when it is applied (R4's once, inside R3's new text) and each new
string once in L-3. Prints L-3; MAP=1 prints the map to stderr."""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
L2 = open("../../../docs/si/P-IDEAL-DBL-line-L2.txt", encoding="utf-8").read()
C = open("c133_8f6d03bc.md", encoding="utf-8").read()
sec = C[C.index("## 5. The L-3 (exact wording)"):C.index("## DONE / FINDINGS / NEEDS")]
sec = re.sub(r"\n\s+", " ", sec)          # join wrapped lines with one space
R = []
items = sec.split("\n- ")
for k in range(1, 7):
    it = [x for x in items if x.startswith("R%d (E-" % k)]; assert len(it) == 1, k
    m = re.fullmatch(r"R%d \(E-\d\): «(.*)» → «(.*)»" % k, it[0].rstrip("\n")); assert m, k
    R.append(("R%d" % k, m.group(1), m.group(2)))
t = L2
for tag, old, new in R:
    assert t.count(old) == 1, tag + " old not once"
    t = t.replace(old, new)
for tag, old, new in R:
    assert t.count(new) == 1 or (tag == "R3" and t.count(new.replace("; G-N5-TIME stays OPEN; not M3", R[3][2])) == 1), tag + " new not once"
assert t.count("(") == t.count(")") and "|" not in t and t.count(" — ") == 1 and "[" not in t and t.count("\n") == 1
dep = 0
for ch in t:
    dep += (ch == "(") - (ch == ")"); assert dep >= 0
sys.stdout.write(t)
if os.environ.get("MAP"):
    for tag, old, new in R: sys.stderr.write("%s\n  OLD «%s»\n  NEW «%s»\n" % (tag, old, new))
