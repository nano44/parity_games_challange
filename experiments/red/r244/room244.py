#!/usr/bin/env python3
"""L-RED 70 R244: ROOM screen. Re-wire the two Xi-targets of the old second mover B over all pairs of exit + existing movers (no mover added).
INTACT: per-level best switch counts below F's level and sw(F) unchanged. For INTACT candidates: ROOM1 = min over B's switches (step t) of
t - (step of F's last arrival at A before t), ROOM2 = min over A's switches (step t') of t' - (step of F's last arrival at B before t');
a second full mover y at F's level can visit A after F and before B moves only if ROOM1 >= 2 (and likewise ROOM2 >= 2 on B's side).
Engine: sim244 (own). Usage: room244.py G.json FI AI BI"""
import sys, copy, sim244
G0 = sim244.load(sys.argv[1]); FI, AI, BI = (int(a) for a in sys.argv[2:5]); N = G0["N"]; LF = G0["lev"][FI]
def stats(G):
    try: T, sw, S = sim244.run(G, cap=100000, trace=True)
    except ValueError: return None
    best = [max(sw[x] for x in range(N) if G["lev"][x] == l) for l in range(LF)]
    arrA = arrB = None; r1 = r2 = 10 ** 9
    for t in range(1, T + 1):
        if S[t][BI] != S[t - 1][BI] and arrA is not None: r1 = min(r1, t - arrA)
        if S[t][AI] != S[t - 1][AI] and arrB is not None: r2 = min(r2, t - arrB)
        if S[t][FI] != S[t - 1][FI]:
            if G["opts"][FI][S[t][FI]][0] == AI: arrA = t
            else: arrB = t
    return T, sw, best, r1, r2
b = stats(G0); print(f"ROOM244 base: T {b[0]} sw(F) {b[1][FI]} sw(B) {b[1][BI]} best below {b[2]} ROOM1 {b[3]} ROOM2 {b[4]}")
tot = acyc = intact = 0; hist = {}; good = []
for u0 in range(-1, N):
    for u1 in range(-1, N):
        if u0 == BI or u1 == BI: continue
        tot += 1; G = copy.deepcopy(G0); G["opts"][BI][0][1] = u0; G["opts"][BI][1][1] = u1; s = stats(G)
        if s is None: continue
        acyc += 1
        if s[2] != b[2] or s[1][FI] != b[1][FI]: continue
        intact += 1; key = (min(s[3], 9), min(s[4], 9)); hist[key] = hist.get(key, 0) + 1
        if s[3] >= 2 and s[4] >= 2: good.append((u0, u1, s[0], s[3], s[4]))
print(f"ROOM244 candidates {tot} acyclic {acyc} INTACT {intact}; (ROOM1, ROOM2) histogram among INTACT: {sorted(hist.items())}")
print(f"ROOM244 INTACT with ROOM1 >= 2 and ROOM2 >= 2: {len(good)} {good[:12]}")
