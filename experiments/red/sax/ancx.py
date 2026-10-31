#!/usr/bin/env python3
"""L-RED successor 38 (R164): L-SI box 58 anc.py (escape / PLAT fields) on a HYBRID run from sax/hyb.py instead of N5 or SI. anc.py's
text (path in env ANC, read-only; l-si 6370a35f) is executed with its trace block replaced by hyb.run(MODE)'s (sigma, tau) states,
fallback flags and improving sets; W-runs are anc.py's (tau constant, no fallback). Usage: ANC=.../anc.py ancx.py MODE G.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import hyb, pg as _pg
mode, path = sys.argv[1], sys.argv[2]
g0 = _pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); hyb.run(g0, mode)
src = open(os.environ["ANC"]).read()
a = src.index("if SI:   # classical"); b = src.index("K = len(S) - 1")
src = src[:a] + "S = [x[0] for x in HYB_TR]; TAU = [x[1] for x in HYB_TR]; FB = list(HYB_FB) + [0]; IS = list(HYB_IS) + [set()]\n" + src[b:]
src = src.replace('check_start(g, st, sys.argv[2] if len(sys.argv) > 2 else "")', "None")
sys.argv = [os.environ["ANC"], path]
glb = {"__file__": os.environ["ANC"], "__name__": "__main__", "HYB_TR": hyb.run.TR, "HYB_FB": hyb.run.FB, "HYB_IS": hyb.run.IS}
exec(compile(src, os.environ["ANC"], "exec"), glb)
