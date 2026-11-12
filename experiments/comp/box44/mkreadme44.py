#!/usr/bin/env python3
"""L-COMP box 44: README.md := README.src.md with its markers filled: @@FAM@@, @@FREE@@, @@LEV@@, @@BIG@@ by tab44.py (from out/), and
@@CMPLSI@@, @@BOUND@@, @@CLIMB@@ from parts/<name>.md (hand-written; they say PENDING until their runs exist). Usage: mkreadme44.py"""
import os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
def tab(*a): return subprocess.run([sys.executable, os.path.join(H, "tab44.py")] + list(a), capture_output=True, text=True, check=True).stdout
s = open(os.path.join(H, "README.src.md")).read()
sets = [x for x in ("records", "corpus", "dead", "mine", "rand", "mut") if os.path.exists(os.path.join(H, "out", "lev44_%s.out" % x)) and (x != "mine" or os.path.exists(os.path.join(H, "parts", "MINE_DONE")))]
fill = {"FAM": tab("fam"), "FREE": tab("free"), "LEV": tab("lev", *sets),
        "BIG": tab("big") if os.path.exists(os.path.join(H, "parts", "BIG_DONE")) else "PENDING at this commit: the long runs (out/lev44_big.out) are not finished.\n"}
for k in ("CMPLSI", "BOUND", "CLIMB"): fill[k] = open(os.path.join(H, "parts", k + ".md")).read()
for k, v in fill.items():
    assert s.count("@@%s@@\n" % k) == 1, k; s = s.replace("@@%s@@\n" % k, v if v.endswith("\n") else v + "\n")
assert "@@" not in s
open(os.path.join(H, "README.md"), "w").write(s)
print("README.md written, %d lines" % s.count("\n"))
