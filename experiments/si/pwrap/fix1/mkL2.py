#!/usr/bin/env python3
"""L-SI P-N5-WRAP fixes entry 1: line L-2 from line L-1 by the referees' strings, COPIED BY SCRIPT from the byte copies
(claude/referee 99df2458 docs/referee/R-P-N5-WRAP.md = REFEREE 34; claude/referee-2 07fd5ae4 docs/referee-2/R2-P-N5-WRAP.md = REFEREE-2 39).
Order: LW-1 (prints the check sha1, REFEREE 34's be7da8f3...), R-1, R-2 (on LW-1's REFEREE 33 clause, see below), LW-2, LW-3; every old
string must occur exactly once. Usage: mkL2.py ROOT OUT.txt   (ROOT = repository top; needs the two commits)"""
import sys, re, subprocess, hashlib
ROOT, OUT = sys.argv[1], sys.argv[2]
def show(c, p): return subprocess.run(["git", "-C", ROOT, "show", c + ":" + p], capture_output=True, check=True).stdout.decode()
def norm(s): return re.sub(r"\n[ \t]*", " ", s)
R34 = norm(show("99df2458", "docs/referee/R-P-N5-WRAP.md")); R2 = norm(show("07fd5ae4", "docs/referee-2/R2-P-N5-WRAP.md"))
def between(text, a, b):
    i = text.index(a); j = text.index(b, i + len(a)); return text[i + len(a):j]
def once(s, old, new, tag):
    assert s.count(old) == 1, "%s: old string occurs %d times" % (tag, s.count(old)); return s.replace(old, new)
L1 = open(ROOT + "/docs/si/P-N5-WRAP-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L1.encode()).hexdigest() == "896f9e97394695f903131f832a67f31bcfc23c28", "L-1 sha1"
# LW-1: REFEREE 34's «old» → «new» pair (its §5 bullet «LW-1 (L43): «…» → «…»»)
blk = between(R34, "- LW-1 (L43): «", " - The numbers in it:")
o1, n1 = blk.split("» → «"); n1 = n1.rstrip().rstrip("»")
L = once(L1, o1, n1, "LW-1"); h = hashlib.sha1(L.encode()).hexdigest()
print("L-1 + LW-1 sha1", h, len(L.encode()), "B; REFEREE 34's be7da8f3a98e4c5a26158eae9aa2766c56531222:", h == "be7da8f3a98e4c5a26158eae9aa2766c56531222")
assert h == "be7da8f3a98e4c5a26158eae9aa2766c56531222"
# R-1: REFEREE-2's Old / New (exact strings)
o = between(R2, "Old (exactly once in L-1): «", "» New: «"); n = between(R2, "the READING below) from ι and that run»"[:0] + o + "» New: «", "» - R-2")
L = once(L, o, n, "R-1")
# R-2: its Old «REFEREE 33 e44ce56b / 90703a81: 18 counters 0 on 523,721 runs)» does not occur after LW-1 (LW-1 rewrote that clause into
# «REFEREE 33 (e44ce56b / 90703a81; 18 counters 0 on 523,721 runs);»); R-2's New text is applied to LW-1's clause: its counter wording
# and its sentence on WRAP's six counters, both copied from R-2's New.
o2 = between(R2, "- R-2 (REQUIRED, DATA rule: every DATA clause names its counter). Old (exactly once): «", "» New: «")
n2 = between(R2, o2 + "» New: «", "» (the counts are §9's;")
assert L1.count(o2) == 1 and L.count(o2) == 0
lw1_clause = "18 counters 0 on 523,721 runs);"
assert L.count(lw1_clause) == 1
ref33 = between(n2, "REFEREE 33 e44ce56b / 90703a81: ", "); WRAP's six")       # «its 18 must-be-0 counters, named in its report, 0 on 523,721 runs»
six = n2[n2.index("WRAP's six must-0 counters"):]
L = once(L, lw1_clause, ref33 + "); " + six + ";", "R-2 (on LW-1's clause)")
# LW-2 (adopted; REFEREE 34 gives the files, not a string): the lane's string, naming the files REFEREE 34 lists
lw2 = between(R34, "could name its files (out/ ", ") as LW-1 does")          # «wrap_fried_xi.out, wrap_long.out, free_xi.out»
L = once(L, "(33 … 2,489 iterations = Howard T + 3)", "(33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/" + lw2 + ")", "LW-2")
# LW-3 (adopted; REFEREE 34's string; R-3 makes the same point): «to R117's core» → LW-3's «to the core K0-K3 (with pads pA, s, q, r)»
o3 = between(R34, "LW-3, «", "»: W's core")                                    # «an Even valve with an exit to R117's core»
n3tail = between(R34, "with W's edges are not R117's text); «", "» would avoid")   # «to the core K0-K3 (with pads pA, s, q, r)»
assert o3.endswith("to R117's core")
L = once(L, o3, o3[:-len("to R117's core")] + n3tail, "LW-3")
open(OUT, "w", encoding="utf-8").write(L)
print("L-2 sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B")
