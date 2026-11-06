#!/usr/bin/env python3
"""L-NEW box 184: Xi-channel cost of a switch on L^R_d runs (any Xi). For each run (every start for d <= 4): U (steps changing levels >= 1),
C (b_0 changes), Z (switch steps: moving 0 or 1), and per switch step t (switched movers zs): P := #upper options (x, k), lev(x) >= 1,
whose chain under s_(t-1) contains a switched mover; REN := #upper movers whose A-set grows from {s(x)} at s_(t-1) to both options
at s_t while their other option's chain under s_(t-1) contains a switched mover (renewed through the switch). Excess := U - T_C(d - 1)
with the EXACT T_C(2) = 4, 5, 7 (C = 0, 1, 2; SAT, L-COMP 27 / box 160) at d = 3; at d = 4 against the LOWER bounds T_C(3) >= 8, 10, 12
(proxy only: a positive proxy is not a violation). Hypotheses: H-Z excess <= Z; H-REN excess <= sum REN; H-P excess <= sum P.
Usage: switchcost.py files..."""
import os, sys, json, itertools
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
TC = {3: {0: 4, 1: 5, 2: 7}, 4: {0: 8, 1: 10, 2: 12}}
st = Counter(); worst = {}; hist = Counter()
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert fl["is_lr"](G)
    except Exception: continue
    d = G["N"] // 2
    if d not in TC: continue
    g = Gen(G); N = G["N"]; iso = fl["is_iso"](G)
    for s0 in itertools.product((0, 1), repeat=N):
        S, _ = g.run(s0); T = len(S) - 1
        U = sum(1 for t in range(1, T + 1) if S[t][2:] != S[t - 1][2:])
        b = [int(G["gate"][0][s[0]] < G["gate"][1][s[1]]) for s in S]; C = sum(1 for t in range(1, T + 1) if b[t] != b[t - 1])
        Psum = REN = Z = 0
        for t in range(1, T + 1):
            zs = [z for z in (0, 1) if S[t][z] != S[t - 1][z]]
            if not zs: continue
            Z += 1
            for x in range(2, N):
                for k in (0, 1):
                    if set(g.play(S[t - 1], x, k)) & set(zs): Psum += 1
                if len(g.avail(S[t - 1], x)) == 1 and len(g.avail(S[t], x)) == 2 and set(g.play(S[t - 1], x, 1 - S[t - 1][x])) & set(zs): REN += 1
        if C not in TC[d]: continue
        ex = U - TC[d][C]; key = (d, "ISO" if iso else "non")
        st[key + ("runs",)] += 1; hist[(d, ex)] += 1
        if d == 3:
            st[key + ("HZ_viol",)] += ex > Z; st[key + ("HREN_viol",)] += ex > REN; st[key + ("HP_viol",)] += ex > Psum
        if ex > worst.get(key, (-99,))[0]: worst[key] = (ex, os.path.basename(f), "".join(map(str, s0)), "U", U, "C", C, "Z", Z, "P", Psum, "REN", REN)
for k in sorted(st): print(k, st[k])
print("excess histogram (d, excess): count", dict(sorted(hist.items())))
for k in sorted(worst): print("max excess", k, worst[k])
