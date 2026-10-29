#!/usr/bin/env python3
"""REFEREE-2 succ. 19: reproduce P-N5-TOPSHAPE §2 / §3 single instances: tops of (v, phase) and the Delta-tops at P-changes. Ranks are SPEC
S1 ranks. Usage: repro.py game.pg [game.start] v phase_first_state"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
gp = R.pg.read(sys.argv[1]); s, t = R.read_start(gp, sys.argv[2]) if sys.argv[2] != "-" else R.starts(gp, 0, None)
v, a = int(sys.argv[3]), int(sys.argv[4])
states, fbs = R.DC.Runner(gp).run(s, t); ctx = R.Ctx(gp); st = R.Stats()
I = [R.state_info(ctx, x, y, st, "x") for x, y in states]
key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
b = a
while b + 1 < len(I) and key[b + 1] == key[a]: b += 1
top = lambda m: m.bit_length() - 1 if m else None
tops, dts = [top(I[a]["xi"][v][1])], []
for k in range(a, b):
    A, B = I[k]["xi"][v][1], I[k + 1]["xi"][v][1]
    if A != B:
        dts.append(top(A ^ B))
        if top(B) != tops[-1]: tops.append(top(B))
print(f"phase [{a},{b}] v {v}: tops {tops}")
print(f"P-changes {len(dts)}, Delta-tops first 10 {dts[:10]}, Delta-top rises {sum(1 for i in range(len(dts) - 1) if dts[i + 1] > dts[i])}")
