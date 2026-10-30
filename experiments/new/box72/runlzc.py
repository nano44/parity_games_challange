#!/usr/bin/env python3
"""L-NEW box 72: run any n5x-based script unchanged on N5-LZC (n5x.step replaced by box72/n5lz.step with --lzc).
Usage: runlzc.py SCRIPT.py GAME.pg [START]"""
import sys, os, runpy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
sys.argv.append("--lzc")
import n5x, n5lz
n5x.step = n5lz.step
script = os.path.abspath(sys.argv[1]); sys.argv = [script] + [a for a in sys.argv[2:] if a != "--lzc"]
sys.path.insert(0, os.path.dirname(script))
runpy.run_path(script, run_name="__main__")
