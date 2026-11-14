#!/usr/bin/env python3
# P-N5-SPLIT line L-2 generator (L-NEW successor 71). From the repo root: python3 experiments/new/box199/mkl2_199.py
# L-2 = L-1 + R-D7a (Lead ruling R-D7a 07:12Z 2026-11-12, L43; R127 first fill on trunk 07139249: D7's «RA-LOG» and «bounded
# multiplicity» enter as DATA with their numbers and sources, not as DEAD). Two edits, in this order: (R-D7a.1) D7 reduced to «fan-in 1 of
# RA» with its unit; (R-D7a.2) the RA-depth / multiplicity DATA inserted right after «max split pairs 5 (FW6_4, FW8_4);». Asserts the frozen
# packet's sha1, L-1's sha1 (634b2fdf…), each old string exactly once, one line, no «|», balanced parentheses, «RA-LOG» and «MW32_2,
# 445031d1» absent, each new source id exactly once.
import hashlib
pk = open("docs/new/P-N5-SPLIT.md", "rb").read()
assert hashlib.sha1(pk).hexdigest() == "5bc1b1f390ed81683fe5c93008c7ea0b338fe735", "frozen packet changed"
L1 = open("docs/new/P-N5-SPLIT-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L1.encode()).hexdigest() == "634b2fdfda31eda9e82e9f558ffebf3c89f5701c", "L-1 changed"
OLD1 = ("D7 fan-in 1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4; "
        "FW16_2, 94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)")
NEW1 = ("D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) "
        "of the number of letters of RA(y), box198/pair198.out maxRA)")
ANCH = "max split pairs 5 (FW6_4, FW8_4);"
INS = (" RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/referee-2 4948ce5d, own engine; "
       "L-SI 47 box 90, claude/l-si 4ded1e8d) and the per-pair multiplicity n on MW(n) (L-SI 47 box 90, claude/l-si 2d0344d3, not re-run by "
       "the lane or a referee), DATA only;")
L = L1
for k, o, n in (("R-D7a.1", OLD1, NEW1), ("R-D7a.2", ANCH, ANCH + INS)):
    # the line wraps nothing: the strings are matched in the one-line text exactly
    assert L.count(o) == 1, (k, L.count(o))
    L = L.replace(o, n)
    print(k, "applied; sha1", hashlib.sha1(L.encode()).hexdigest()[:8], len(L.encode()), "B")
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
assert "RA-LOG" not in L and "MW32_2, 445031d1" not in L
for s in ("da3308b5", "4948ce5d", "4ded1e8d", "2d0344d3"): assert L.count(s) == 1, s
b = L.encode(); h = hashlib.sha1(b).hexdigest()
open("docs/new/P-N5-SPLIT-line-L2.txt", "wb").write(b)
print("L-2 written: sha1", h, len(b), "B")
