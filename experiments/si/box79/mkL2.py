#!/usr/bin/env python3
"""L-SI P-IDEAL-DBL fix round 1: make line L-2 from L-1 by scripted replacements (Lead 09:20Z rulings 1-5).
Sources (byte copies in this directory, sha1 pinned): ref_d7885be4.md = docs/referee/R-P-IDEAL-DBL.md at claude/referee d7885be4
(REFEREE 26: DB-L1, DB-L2), ref2_7891ba32.md = docs/referee-2/R2-P-IDEAL-DBL.md at claude/referee-2 7891ba32 (REFEREE-2 30: W-2 (a)-(d),
W-3, N-1..N-3). Every referee string is extracted from those files (markdown line breaks + indentation joined to one space); every
number of the DATA clause is read from dblcheck.out / dblcheck_neg2.out; the RE-ENTRY level sets from reentry_levels.out.
Each old string must occur exactly once in L-1 and each new string exactly once in L-2; parentheses balanced; no «|»."""
import re, sys, os
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
L1 = open("../../../docs/si/P-IDEAL-DBL-line-L1.txt", encoding="utf-8").read()
def flat(path):
    return re.sub(r"\n\s*", " ", open(path, encoding="utf-8").read())
R1 = flat("ref_d7885be4.md"); R2 = flat("ref2_7891ba32.md")
def guil(text, start):
    """the «…» string starting at index start (text[start] == '«'), nesting respected; returns the inside"""
    assert text[start] == "«"; dep = 0
    for i in range(start, len(text)):
        if text[i] == "«": dep += 1
        elif text[i] == "»":
            dep -= 1
            if dep == 0: return text[start + 1:i]
    raise SystemExit("unbalanced «» at %d" % start)
def after(text, marker, nth=0):
    i = -1
    for _ in range(nth + 1):
        i = text.index(marker, i + 1)
    return guil(text, text.index("«", i + len(marker) - 1))
# REFEREE 26 §5
i = R1.index("- DB-L1 (required).")
DBL1_old = after(R1[i:], "- Old: «"); DBL1_new = after(R1[i:], "- New: «")
i = R1.index("- DB-L2 (required).")
DBL2_old = after(R1[i:], "- Old: «"); DBL2_new = after(R1[i:], "- New: «")
# REFEREE-2 required line changes
def w2(label):
    i = R2.index(label); j = R2.index("«", i); old = guil(R2, j); k = R2.index("→ «", j + len(old)); new = guil(R2, k + 2)
    return old, new
W2a = w2("**W-2 (a)"); W2b = w2("**W-2 (b):**"); W2c = w2("**W-2 (c):**"); W2d = w2("**W-2 (d):**"); W3 = w2("**W-3 (DATA clause by clause):**")
assert W3[0] == DBL1_old, "W-3 and DB-L1 replace the same old string (Lead ruling 2)"
assert W2d[0] in DBL2_old, "W-2 (d)'s old string lies inside DB-L2's old string (Lead ruling 3)"
# numbers from dblcheck.out (DB-L1's New text must carry exactly these)
def units(fn, scope):
    for ln in open(fn):
        if ln.startswith(scope + " units:"): return ln
    raise SystemExit(scope)
def num(ln, key):
    m = re.search(re.escape(key) + r" (\d+)", ln); return int(m.group(1))
def ctl(fn, scope, key):
    for ln in open(fn):
        if ln.startswith(scope + " controls"): return num(ln, key)
def viol(fn, scope, key):
    for ln in open(fn):
        if ln.startswith(scope + " violations"): return num(ln, key)
C = units("dblcheck.out", "CORPUS"); L = units("dblcheck.out", "LOWER")
f = lambda n: "{:,}".format(n)
nums = {
  "runs": (num(C, "runs"), num(L, "runs")), "steps": num(C, "steps"),
  "WO": (num(C, "WO units (run, level, window, member)"), num(L, "WO units (run, level, window, member)")),
  "DBLa": (num(C, "DBLa units (run, level)"), num(L, "DBLa units (run, level)")),
  "dbl": (num(C, "doubling (run, level)"), num(L, "doubling (run, level)")),
  "DBLb": (num(C, "DBLb units (run, doubling level, window, member)"), num(L, "DBLb units (run, doubling level, window, member)")),
  "PF": num(C, "PF units (run, level) frozen split"),
  "HIT": (num(C, "HIT units (run, mover, step)"), num(L, "HIT units (run, mover, step)")),
  "FU2": (num(C, "FU2 units (run, level)"), num(L, "FU2 units (run, level)")),
  "ALT": (num(C, "ALT units (run, mover)"), num(L, "ALT units (run, mover)")),
  "TN": (num(C, "TN units (run, doubling level, member)"), num(L, "TN units (run, doubling level, member)")),
  "ALTb_T": (ctl("dblcheck.out", "CORPUS", "ALTb_T"), ctl("dblcheck.out", "LOWER", "ALTb_T")),
  "ALTc_T": (ctl("dblcheck.out", "CORPUS", "ALTc_T"), ctl("dblcheck.out", "LOWER", "ALTc_T")),
  "NEG_HIT": viol("dblcheck_neg2.out", "CORPUS", "HIT"),
}
assert "PF units" not in L   # «none in LOWER»
pair = lambda k: "%s / %s" % (f(nums[k][0]), f(nums[k][1]))
expect = ["the %s runs (%s steps)" % (f(nums["runs"][0]), f(nums["steps"])), "the %d runs of L-LOWER 3" % nums["runs"][1],
          "WINDOW-ONCE 0 violations on %s (run, level, window, member)" % pair("WO"),
          "(a) 0 on %s (run, level ≥ 1), both directions, with %s doubling (run, level)" % (pair("DBLa"), pair("dbl")),
          "(b) 0 on %s (run, doubling level, window, member)" % pair("DBLb"),
          "PASS-FREEZE 0 on the %s (run, level) of CORPUS" % f(nums["PF"]),
          "HIT 0 on %s (run, mover, step)" % pair("HIT"), "FUEL-EXACT 0 on %s (run, level)" % pair("FU2"),
          "ALT-MIN 0 on %s (run, mover)" % pair("ALT"), "0 on %s (run, doubling level, member)" % pair("TN"),
          "fail on %s and %s (run, mover)" % (pair("ALTb_T"), pair("ALTc_T")), "HIT fails on %s CORPUS (run, mover, step)" % f(nums["NEG_HIT"])]
for e in expect:
    assert DBL1_new.count(e) == 1, "DB-L1 number not equal to dblcheck.out: " + e
# Lead ruling 2: DB-L1's New + W-3's no-DATA entries and the dead79.py pointer
add_old = "MP-LIN no separate DATA;"
add_new = ("MP-LIN, the sufficient condition of PASS-FREEZE and DEAD-REENTRY (static Ξ-graph; its level sets measured by "
           "experiments/si/box79/reentry_levels.py): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py;")
assert DBL1_new.count(add_old) == 1
DATA_new = DBL1_new.replace(add_old, add_new)
# Lead ruling 3: RE-ENTRY with DB-L2's statement wording + the measured level sets + W-2 (d)'s paths
ro = open("reentry_levels.out", encoding="utf-8").read()
def lset(name):
    blk = ro[ro.index(name):]; m = re.search(r"reading A failing l: \{([0-9, ]*)\}", blk); return [int(v) for v in m.group(1).split(", ")]
lt, lk = lset("REC_d10_tower_mu30.json"), lset("KILL_M2D_d6_mu13.json")
assert lt == list(range(lt[0], lt[-1] + 1)) and lk == list(range(lk[0], lk[-1] + 1))
assert "path 1 -> 11 -> 3: PRESENT" in ro and "path 2 -> 5 -> 3: PRESENT" in ro
stmt = DBL2_new[:DBL2_new.index(" (static Ξ-graph;")]
assert stmt == "«the strict Ξ-descendants of the fuel targets U_l lie at levels > l»"
REENTRY_new = (stmt + " (static Ξ-graph; measured for every l in 0, …, d − 2 by experiments/si/box79/reentry_levels.py: false for l = %d, …, %d "
               "on experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, witness 1 → 11 → 3 (mover 11 of "
               "level 5 is the Ξ-target of mover 1's option 0, and 3 of level 1 is a Ξ-target of an option of 11), and for l = %d, …, %d on "
               "experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, a byte copy of L-LOWER's, 𝓛^R_6, witness 2 → 5 → 3 (mover 5 of level 2 "
               "is the Ξ-target of an option of mover 2 of level 1, and 3 of level 1 is a Ξ-target of an option of 5); true for l = 0 on both)") % (lt[0], lt[-1], lk[0], lk[-1])
# N-1 (and REFEREE 26's optional note): F0 dropped from the premise list; N-2: «higher» made explicit
N1 = ("R113's ALIGN, F0 and PATH-RISE", "R113's ALIGN and PATH-RISE")
N2 = ("whose Ξ-target has a higher level", "whose Ξ-target has a higher level than that mover")
REPL = [("W-2 (a)", W2a[0], W2a[1]), ("W-2 (b)", W2b[0], W2b[1]), ("W-2 (c)", W2c[0], W2c[1]),
        ("DB-L2 + W-2 (d) + N-3", DBL2_old, REENTRY_new), ("DB-L1 + W-3", DBL1_old, DATA_new), ("N-1", N1[0], N1[1]), ("N-2", N2[0], N2[1])]
L2 = L1
for tag, old, new in REPL:
    assert L1.count(old) == 1, "old string not once in L-1: " + tag
    L2 = L2.replace(old, new)
for tag, old, new in REPL:
    assert L2.count(new) == 1, "new string not once in L-2: " + tag
assert "|" not in L2 and L2.count("(") == L2.count(")") and L2.endswith("\n") and L2.count("\n") == 1
dep = 0
for ch in L2:
    dep += (ch == "(") - (ch == ")"); assert dep >= 0
sys.stdout.write(L2)
if os.environ.get("MAP"):
    for tag, old, new in REPL: sys.stderr.write("%s\n  OLD «%s»\n  NEW «%s»\n" % (tag, old, new))
