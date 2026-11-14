"""REFEREE s31: P-N5-SPLIT L-3 = L-1 + R-D7a + R-U127 (a)-(d), strings typed from docs/new/P-N5-SPLIT-fixes.md entries 3-4 at l-new 621e6b77.
Prints each old string's count, the result's sha1/size, mechanics, and a word diff L-1 -> result. Usage: split_l3.py L1 OUT"""
import sys, re, hashlib, difflib
L1 = open(sys.argv[1], encoding="utf-8").read(); L = L1
R = [("R-D7a-1", "D7 fan-in 1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4; "
      "FW16_2, 94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)",
      "D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) of the "
      "number of letters of RA(y), box198/pair198.out maxRA)"),
     ("R-D7a-2", "max split pairs 5 (FW6_4, FW8_4);",
      "max split pairs 5 (FW6_4, FW8_4); RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, "
      "claude/referee-2 4948ce5d, own engine; L-SI 47 box 90, claude/l-si 4ded1e8d) and the per-pair multiplicity n on MW(n) (L-SI 47 box 90, "
      "claude/l-si 2d0344d3, not re-run by the lane or a referee), DATA only;"),
     ("R-U127a", "max c_y ≤ 6", "max c_y (unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc) ≤ 6"),
     ("R-U127b", "max split pairs 5 (FW6_4, FW8_4)", "max split pairs (unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over "
      "(v, I, y); split199.out maxSPL) 5 (FW6_4, FW8_4)"),
     ("R-U127c", "every run is short (T3 ≤ 199)", "every run is short (T3 ≤ 199; unit: states of the HOW3 run, max over the 28 frozen instances, "
      "split199.out T3; 199 on MW32_2)"),
     ("R-U127d", "with fixes entries 1-2", "with fixes entries 1-4")]
for name, o, n in R:
    print(name, "old count", L.count(o)); L = L.replace(o, n, 1)
open(sys.argv[2], "w", encoding="utf-8").write(L)
print("sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B; lines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
for s in ["RA-LOG", "MW32_2, 445031d1", "bounded multiplicity"]: print("absent?", s, L.count(s))
a, b = re.split(r"(\s+)", L1), re.split(r"(\s+)", L)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal": print(f"--- {tag}\n  OLD: {''.join(a[i1:i2])}\n  NEW: {''.join(b[j1:j2])}")
