#!/usr/bin/env python3
"""L-COMP 12 box 31: summary of phase2b.sh. Per (y, variant): start and climbed genome measured by sim6 (T, caps, F(0..7)), npaths(12 -> 14,15),
{0..3} ∩ upstream(12) (before -> after), xt[24], xt[25], and replay30 + fenc agreement on T and F (climbed genome). Usage: phase2b_sum.py"""
import sys, os, subprocess, glob
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "l-lower"))
from sim6 import rd, run, Fprof, caps
from guard_l6 import npaths, upstream
def m(p):
    D = rd(p); S, O = run(D, cap=5000); F = Fprof(D, O); T = len(S) - 1
    return D, T, caps(F), F[:8], npaths(D, 12, {14, 15}), sorted({0, 1, 2, 3} & upstream(D, [12]))
for y in (-1, 18, 21, 26, 34, 38):
    s = os.path.join(H, "phase2b", f"start_{y}.txt")
    if not os.path.exists(s): continue
    _, T0, c0, F0, n0, u0 = m(s)
    for var in ("base", "NR"):
        p = os.path.join(H, "phase2b", f"{y}_{var}.txt")
        if not os.path.exists(p): continue
        D, T, c, F, n, u = m(p)
        rp = list(map(int, subprocess.run([sys.executable, os.path.join(H, "..", "box30", "replay30.py"), p], capture_output=True, text=True).stdout.split(" F ")[-1].split()))
        fe = subprocess.run([os.path.join(H, "bin", "fenc"), p], capture_output=True, text=True).stdout.split(); fT, fF = int(fe[1]), list(map(int, fe[3:3 + D['d']]))
        ag = rp[:8] == F and fT == T and fF[:8] == F
        print(f"y {y} {var}: start T {T0} caps {c0} npaths {n0} up(0..3)∋12 {u0} -> climbed T {T} caps {c} F(0..7) {F} npaths {n} up(0..3)∋12 {u} "
              f"xt24 {D['xt'][24]} xt25 {D['xt'][25]} | replay30+fenc agree {ag}")
