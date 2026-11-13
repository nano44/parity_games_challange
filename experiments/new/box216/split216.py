#!/usr/bin/env python3
"""Box 216 V1 (L-NEW successor 76): box 199's split199.py (Lemma SPLIT / TRANSFER, REWIN, REWIN-HI, PAIR-SPLIT, SPLIT-COUNT, RW-1 counters)
run UNCHANGED on N5's key run: n5v.step is wrapped at import so that split199's call n5v.step(..., "xi") runs mode S216_MODE (default
spec = N5, SPEC S4a); no file of box 199 or box 190 is edited. split199 stops at the first fallback, so the run is N5's key run.
Usage: split216.py G.json ...   (same output format as split199.py, each line prefixed by «mode M»)"""
import os, sys, runpy, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
os.environ.setdefault("EG195_ROOT", ROOT)
import n5v
MODE = os.environ.get("S216_MODE", "spec"); _orig = n5v.step
n5v.step = lambda g, E, Ed, sigma, tau, mode: _orig(g, E, Ed, sigma, tau, MODE)
SPLIT = os.path.join(ROOT, "experiments/new/box199/split199.py")
for fn in sys.argv[1:]:
    sys.argv = [SPLIT, fn]; buf = io.StringIO()
    with contextlib.redirect_stdout(buf): runpy.run_path(SPLIT, run_name="__main__")
    for line in buf.getvalue().splitlines(): print("mode", MODE, line, flush=True)
