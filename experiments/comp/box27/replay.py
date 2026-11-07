#!/usr/bin/env python3
"""Replay a cnf.py model: run sim.py (mine) and L-RED's r187/ideal.py (second simulator; path in argv[1]) from the stored start;
check that both give the same states and that the first L+1 states equal the SAT model's states. Usage: replay.py LREDR187 f.json.."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import sim
sys.path.insert(0, sys.argv[1]); import ideal
ok = True
for f in sys.argv[2:]:
    G = json.load(open(f)); S, why = sim.run(G); S2, why2 = ideal.traj(G)
    L = len(G["states"]) - 1
    pre = [tuple(x) for x in G["states"]] == [tuple(x) for x in S[:L + 1]]
    same = S == S2 and why == why2
    ok &= pre and same and len(S) - 1 >= L
    print(f"{f}: model L {L}; sim T {len(S) - 1} ({why}); ideal.py T {len(S2) - 1} ({why2}); prefix equal {pre}; simulators equal {same}")
print("REPLAY", "OK" if ok else "FAIL")
