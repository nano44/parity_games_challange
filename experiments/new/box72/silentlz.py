#!/usr/bin/env python3
"""L-NEW box 72: box70/silent.py (L-SI's re-entry classes, P-N5-CUT §4) run on N5-LZC instead of N5: n5x.step is replaced by
box72/n5lz.step (with --lzc) before silent.py is executed unchanged. Usage: silentlz.py GAME.pg [START]"""
import sys, os, runpy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
if "--lzc" not in sys.argv: sys.argv.append("--lzc")
import n5x, n5lz
n5x.step = n5lz.step
sys.argv = [os.path.join(HERE, "..", "box70", "silent.py")] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
