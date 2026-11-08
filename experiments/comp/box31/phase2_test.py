#!/usr/bin/env python3
"""L-COMP 12 box 31 (Lead 03:28Z): phase-2 one-edit test. Base genome B; for option m in {24 (12:0), 25 (12:1)} and target y in
{18, 19} (level 9): xt[m] = y. Per edit: cyclic?, sim6 (T, caps, F(0..8), first broken level), q6 = roles(6)[1], npaths(12 -> {14,15}),
npaths(y -> {14,15}) (y's own paths), and replay30 (box27/sim.py) + fenc (L-LOWER 9, ENC) T/F agreement. Usage: phase2_test.py B OUTDIR"""
import sys, os, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "l-lower"))
from sim6 import rd, wr, run, Fprof, caps, topo
from guard_l6 import roles, npaths, windows
B, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True); D0 = rd(B)
def meas(D, tag):
    if topo(D) is None: return f"{tag}: CYCLIC"
    S, O = run(D, cap=5000); T = len(S) - 1; F = Fprof(D, O); c = caps(F); r = roles(D, S, O, 6)
    n1 = sum(1 for a, e, _ in windows(S, O, 7) if e == a)
    p = os.path.join(od, tag + ".txt"); wr(D, p)
    rp = subprocess.run([sys.executable, os.path.join(H, "..", "box30", "replay30.py"), p], capture_output=True, text=True).stdout.split(" F ")[-1].split()
    fe = subprocess.run([os.path.join(H, "bin", "fenc"), p], capture_output=True, text=True).stdout.split()
    fT, fF = int(fe[1]), list(map(int, fe[3:3 + D['d']]))
    agree = (list(map(int, rp)) == F) and fT == T and fF == F
    exp = [2 ** (l + 2) - 2 for l in range(9)]
    return (f"{tag}: T {T} caps {c} F(0..8) {F[:9]} (cap values {exp}) first-broken-level {c if c < len(F) else None} "
            f"q6 {r[1] if r else None} npaths(12->14,15) {npaths(D, 12, {14, 15})} n1_7 {n1} | replay30+fenc agree {agree}")
print(meas(D0, "base"))
for m in (24, 25):
    for y in (18, 19):
        D = {k: (list(v) if isinstance(v, list) else v) for k, v in D0.items()}; old = D['xt'][m]; D['xt'][m] = y
        own = npaths(D, y, {14, 15}) if topo(D) is not None else None
        print(meas(D, f"opt{m}_{old}to{y}"), f"| npaths({y}->14,15) {own}")
