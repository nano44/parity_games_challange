#!/usr/bin/env python3
"""L-COMP box 46: out/sum46_{1,2,3}.out := sum46.py 1 / 2 / 3; README.md := README.src.md with @@T1@@ .. @@T3@@ replaced by them."""
import os, sys, subprocess
H = os.path.dirname(os.path.abspath(__file__)); s = open(os.path.join(H, "README.src.md")).read()
for k in ("1", "2", "3"):
    t = subprocess.run([sys.executable, "-B", os.path.join(H, "sum46.py"), k], capture_output=True, text=True, check=True).stdout
    open(os.path.join(H, "out", "sum46_%s.out" % k), "w").write(t); s = s.replace("@@T%s@@" % k, t.rstrip("\n"))
open(os.path.join(H, "README.md"), "w").write(s); print("README.md written,", s.count("\n"), "lines")
