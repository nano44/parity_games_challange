#!/usr/bin/env python3
"""L-NEW box 152: value check of a wake-order witness (box151/xwake_anti.py output with states/KP). From the witness's full state
sequence and key-preferences KP, the C-ELEMENT requirements are: x moves at t => C_(t-1)(x) = s_t(x); x stays and KP_t(x) != s_(t-1)(x)
=> C_(t-1)(x) = s_(t-1)(x). They are solved by box151/req.py solve(): free acyclic Xi-targets, REL (distinct nonzero integer weights,
a relaxation of +-2^rank) or exact ranks. UNSAT (REL) => no IDEAL-ACYC genome runs this exact schedule. CORE=1 prints an unsat core
(minimal set of requirements (t-1, x, bit), deletion-minimised). Usage: valcheck.py witness.json   env: EXACT=1, CORE=1, TMO=s, FIXXT=1 (use the witness's per-option Xi-targets, box151 XT=1)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box151")]
import req as RQ
W = json.load(open(sys.argv[1])); S = [tuple(s) for s in W["states"]]; KP = W["KP"]; lev = W["lev"]; N = len(lev); L = len(S) - 1
WT = [m[1] for m in W["movers"]]
rq = {}
for t in range(1, L + 1):
    for x in range(N):
        if lev[x] == 0 and S[t][x] == S[t - 1][x]: continue  # level-0 KP is a constant chosen by the witness; keep only moves
        if S[t][x] != S[t - 1][x]: rq[(t - 1, x)] = S[t][x]
        elif KP[t][x] != S[t - 1][x]: rq[(t - 1, x)] = S[t - 1][x]
tmo = int(os.environ.get("TMO", "600")); rel = os.environ.get("EXACT") != "1"
xtfix = None
if os.environ.get("FIXXT") == "1" and "xt" in W:
    xtfix = {(int(a.split(",")[0]), int(a.split(",")[1])): v for a, v in W["xt"].items()}
r, out = RQ.solve(lev, WT, S, rq, xtfix=xtfix, rel=rel, tmo=tmo)
print("VALCHECK", os.path.basename(sys.argv[1]), "N", N, "L", L, "req", len(rq), "REL" if rel else "EXACT", "FIXXT" if xtfix else "freeXT", "->", r, flush=True)
if r == "unsat" and os.environ.get("CORE") == "1":
    core = dict(rq)
    for key in sorted(rq, key=lambda k: (-k[0], k[1])):
        trial = dict(core); trial.pop(key)
        if RQ.solve(lev, WT, S, trial, xtfix=xtfix, rel=rel, tmo=tmo)[0] == "unsat": core = trial
    print("CORE", len(core), sorted(core.items()))
if r == "sat": json.dump({str(k): v for k, v in out.items()}, open(sys.argv[1] + ".val.json", "w"))
