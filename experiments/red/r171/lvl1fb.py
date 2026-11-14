#!/usr/bin/env python3
"""R171: fbscore on R100's lvl1 template (fb/lvl1.py spec m, built with sel/dsl.py): FB inside one TWO-FIX window vs n. Usage: lvl1fb.py m...  (B = max(100, 2m + 10) keeps the chain below the gadget)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "fb")); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
from fbscore import windows_fb
from lvl1 import spec
from dsl import build
from n5x import start_pair, Engine, dual
for m in map(int, sys.argv[1:]):
    g, st, nm = build(spec(m, B=max(100, 2 * m + 10))); s, t = start_pair(g, Engine(g), Engine(dual(g)), st)
    W, K = windows_fb(g, s, t); w = max(W, key=lambda w: w["FB"])
    print(f"LVL1 m {m} n {g.n} K {K} FB {w['FB']} XO {w['XO']} L {w['L']} ODIFF {w['ODIFF']} FB/n {w['FB'] / g.n:.3f}")
