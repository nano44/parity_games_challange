#!/usr/bin/env python3
"""L-RED R145 (c): per-Odd-vertex sigma-bar flips per W-run (L-NEW box 90 SBV_F(o); L-SI box 52 HEAD-RED's SB_F(o)), on n5b SPEC.
W-run: maximal run of transitions with tau fixed, lambda_W map constant, no fallback, sigma moving (as L-SI heads.py). Prints the number of
W-runs, the longest |F|, max_o SB_F(o) with o's label and out-degree, and the flips at o that are returns (back to a target o held
earlier in the run). Usage: sbv.py GAME.pg START"""
import sys, os, re
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
lab = {}
for l in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"([^"]*)"', l)
    if m: lab[int(m.group(1))] = m.group(2)
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb); SG = n5b.SpecSI(g); Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]))
    return Wc[t].evaluate(list(s))
SB = [SG.evaluate_choice(list(s))[1] for s, t in tr]
runs, cur = [], None
for k in range(len(tr) - 1):
    (s, t), (s2, t2) = tr[k], tr[k + 1]
    ok = t == t2 and not fb[k] and s != s2 and [x[0] for x in W(s, t)] == [x[0] for x in W(s2, t)]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k + 1]; runs.append(cur)
    else: cur[1] = k + 1
best = (0, None, 0, 0, 0)
for p, q in runs:
    for o in range(g.n):
        if g.owner[o] != 1: continue
        held, f, ret = {SB[p][o]}, 0, 0
        for k in range(p, q):
            a, b = SB[k][o], SB[k + 1][o]
            if a != b:
                f += 1; ret += b in held; held.add(b)
        if f > best[0]: best = (f, o, len(g.succ[o]), ret, q - p)
print(f"SBV {os.path.basename(sys.argv[1])} n {g.n} iterations {len(tr) - 1} W-runs {len(runs)} longest {max([q - p for p, q in runs], default=0)} "
      f"maxSB {best[0]} at {lab.get(best[1], best[1])} (out-degree {best[2]}, returns {best[3]}, its W-run length {best[4]})")
