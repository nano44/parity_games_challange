#!/usr/bin/env python3
"""REFEREE-2 succ. 33: REFEREE 28's QT-L1..QT-L6 (list CH read as DATA, by ast, from its quiet_linefix.py at claude/referee 6ae1fc04)
against my W-1..W-3, D-1 (b), D-2 (bt_strings.py's list S): span overlaps in L-1, then the combined line L-1 + QT-L1..QT-L6 + D-1 (b) + D-2
(and with D-1 by tool fix). Usage: bt_overlap.py L1.txt quiet_linefix.py"""
import sys, ast, hashlib, os
L = open(sys.argv[1], encoding='utf-8').read(); src = open(sys.argv[2], encoding='utf-8').read()
a = src.index("CH = ["); b = src.index("\n]", a) + 2; QT = ast.literal_eval(src[a + 5:b])
ns = {}; t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bt_strings.py"), encoding='utf-8').read()
a2 = t.index("S = ["); b2 = t.index("\n]", a2) + 2; MY = ast.literal_eval(t[a2 + 4:b2])
span = lambda o: (L.find(o), L.find(o) + len(o))
for q in QT:
    qs = span(q[1])
    for m in MY:
        ms = span(m[1])
        if qs[0] < ms[1] and ms[0] < qs[1]: print("OVERLAP", q[0], m[0])
    print(q[0], "old once in L-1:", L.count(q[1]) == 1)
for tag, extra in (("L-1 + QT-L1..QT-L6 + D-1 (b) + D-2", ["D-1b-i", "D-1b-ii", "D-2"]), ("L-1 + QT-L1..QT-L6 + D-2 (D-1 by tool fix)", ["D-2"]),
                   ("L-1 + QT-L1..QT-L6 (check = REFEREE's fed89346)", [])):
    X = L
    for q in QT: X = X.replace(q[1], q[2])
    for m in MY:
        if m[0] in extra: assert X.count(m[1]) == 1; X = X.replace(m[1], m[2])
    B = X.encode(); print(tag, ": sha1", hashlib.sha1(B).hexdigest(), len(B), "B,", X.count("("), "( =", X.count(")"), ")")
