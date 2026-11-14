#!/usr/bin/env python3
"""REFEREE-2 succ. 33: P-N5-QUIET L-2 (claude/l-new 559cdffc) = L-1 (df0d2a25) + REFEREE 28's QT-L1..QT-L6 (CH read as DATA by ast from its
quiet_linefix.py at claude/referee 6ae1fc04). Usage: bt_l2.py   (run in the repository; reads git objects)"""
import subprocess, hashlib, ast
sh = lambda c, f: subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True).stdout
L1 = sh("df0d2a25", "docs/new/P-N5-QUIET-line-L1.txt").decode(); L2 = sh("559cdffcc46001c6a7e023522a8e5518448ddd7a", "docs/new/P-N5-QUIET-line-L2.txt")
src = sh("6ae1fc04", "docs/referee/scratch/quiet_linefix.py").decode(); a = src.index("CH = ["); b = src.index("\n]", a) + 2; QT = ast.literal_eval(src[a + 5:b])
X = L1
for k, o, n in QT:
    print(k, "old in L-1", L1.count(o), "| old in L-2", L2.decode().count(o), "| new in L-2", L2.decode().count(n)); X = X.replace(o, n)
print("L-2", hashlib.sha1(L2).hexdigest(), len(L2), "| L-1 + QT-L1..QT-L6 == L-2:", X.encode() == L2)
t = L2.decode(); d = 0; neg = False
for c in t: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-2 newlines", t.count("\n"), "parens", t.count("("), t.count(")"), "neg", neg, "pipes", t.count("|"), "guillemets", t.count("«"), t.count("»"))
