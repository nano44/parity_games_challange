#!/usr/bin/env python3
"""L-COMP box 45: out/sum45_a.out, out/sum45_b.out := sum45.py a / b; README.md := README.src.md with @@A@@ / @@B@@ replaced by them.
Usage: mk45.py   (env LNEW209 as sum45.py)"""
import os, sys, subprocess
H = os.path.dirname(os.path.abspath(__file__)); s = open(os.path.join(H, "README.src.md")).read()
for k in ("a", "b"):
    t = subprocess.run([sys.executable, "-B", os.path.join(H, "sum45.py"), k], capture_output=True, text=True, check=True).stdout
    open(os.path.join(H, "out", "sum45_%s.out" % k), "w").write(t); s = s.replace("@@%s@@" % k.upper(), t.rstrip("\n"))
open(os.path.join(H, "README.md"), "w").write(s); print("README.md written,", s.count("\n"), "lines")
