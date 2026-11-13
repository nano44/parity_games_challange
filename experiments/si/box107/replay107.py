#!/usr/bin/env python3
"""Replay a syn107 model with L-NEW's one217.OneP (path of their box217 dir as argv[1]); assert the key run equals the SAT states
(as long as the SAT horizon goes) and report switch counts.  Usage: replay107.py LNEW_BOX217_DIR FILE.json ..."""
import sys, json
sys.path.insert(0, sys.argv[1])
import one217
for fn in sys.argv[2:]:
    D = json.load(open(fn)); G = D.get("genome", D); P = one217.OneP(G); S = [list(s) for s in P.run("key")]
    st = D.get("states"); N = G["N"]; T = len(S) - 1
    ok = True
    if st is not None:
        for t in range(min(len(st), len(S))):
            if st[t] != S[t]: ok = False; break
        if len(S) < len(st) and any(st[t] != S[-1] for t in range(len(S), len(st))): ok = False
    sw = [sum(S[t][x] != S[t + 1][x] for t in range(T)) for x in range(N)]
    full = [x for x in range(N) if sw[x] == 2 ** (G["lev"][x] + 1) - 1]
    print(f"{fn} N {N} T_key {T} replay_equals_model {int(ok)} sw {sw} full {full}")
